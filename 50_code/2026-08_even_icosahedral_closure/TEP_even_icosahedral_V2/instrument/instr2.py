#!/usr/bin/env python3
"""instr2.py — degree-2 seam instrument + qualified solvers. Resumption session 2026-08-03.
Exact Bessel kernels (both ports); complex two-arm theta; eps-phase fit; eps-folded signed port meter;
sparse flip machinery with float-drift resieve gate; solvers S1 (successive cancellation),
S2 (beam-64), S3 (parallel tempering, 8 chains, exchange every 50).
Pre-registered in decode2dim_RESUMPTION_preregistration_20260803.md (sha256 158da198...).
"""
import numpy as np
from scipy.special import k0 as _besk0

SQ5 = np.sqrt(5.0)
PHI = (1.0 + SQ5) / 2.0
TGRID = np.sort(np.array([0.50, 0.58, 1/0.58, 0.67, 1/0.67, 0.78, 1/0.78, 0.90, 1/0.90, 1.00, 1.11, 1.28, 1.72, 2.00]))
UGRID = np.concatenate([-np.linspace(0.02, 0.40, 15)[::-1], np.linspace(0.02, 0.40, 15)])
YCUT = 18.6   # kernel support cutoff: 4K0(2*18.6) ~ 4e-17

def ker(port, y):
    """port 0 (even): 4K0(2y) = Mellin^-1[Gamma(s/2)^2]; port 1 (odd): 4yK0(2y) = Mellin^-1[Gamma((s+1)/2)^2]."""
    y = np.asarray(y, dtype=float)
    out = np.zeros_like(y)
    m = (y > 0) & (y < YCUT)
    ym = y[m]
    v = 4.0 * _besk0(2.0 * ym)
    if port == 1:
        v = v * ym
    out[m] = v
    return out

def Xof(N):
    return int(np.ceil(11.71 * np.sqrt(N)))

# ---------------- sieve ----------------
def inv_series(poly, kmax):
    inv = np.zeros(kmax + 1, dtype=complex); inv[0] = 1.0
    d = len(poly) - 1
    for k in range(1, kmax + 1):
        s = 0.0 + 0.0j
        for j in range(1, min(k, d) + 1):
            s += poly[j] * inv[k - j]
        inv[k] = -s
    return inv

def primes_upto(X):
    isc = np.ones(X + 1, dtype=bool); isc[:2] = False
    for i in range(2, int(X ** 0.5) + 1):
        if isc[i]:
            isc[i*i::i] = False
    return [int(p) for p in np.nonzero(isc)[0]]

def _fold(a, p, inv, X):
    b = a.copy()
    kmax = len(inv) - 1
    for k in range(1, kmax + 1):
        if inv[k] == 0.0:
            continue
        pk = p ** k
        if pk > X:
            break
        b[pk::pk] += inv[k] * a[1:(X // pk) + 1]
    return b

def sieve(X, locfac):
    """a_n for n<=X. locfac(p) -> poly coeffs (c0=1), or None for factor 1."""
    a = np.zeros(X + 1, dtype=complex); a[1] = 1.0
    for p in primes_upto(X):
        kmax = int(np.log(X) / np.log(p))
        poly = locfac(p)
        if poly is None:
            continue
        a = _fold(a, p, inv_series(np.asarray(poly, dtype=complex), kmax), X)
    return a

# ---------------- arm ----------------
class Arm:
    def __init__(self, N, port, X=None, tgrid=TGRID, label=""):
        self.N = float(N); self.port = port; self.label = label
        self.X = X if X is not None else Xof(N)
        n = np.arange(1, self.X + 1)
        rN = np.sqrt(self.N)
        self.t = tgrid
        self.K  = np.stack([ker(port, np.pi * n * tt / rN) for tt in tgrid])
        self.Ki = np.stack([ker(port, np.pi * n / (tt * rN)) for tt in tgrid])
        eu = np.exp(UGRID)
        self.Ku  = np.stack([ker(port, np.pi * n * t0 / rN) for t0 in eu])
        self.Kiu = np.stack([ker(port, np.pi * n / (t0 * rN)) for t0 in eu])
        self.a = None; self.F = None; self.Fi = None

    def set_a(self, a):
        assert len(a) == self.X + 1
        self.a = a.astype(complex).copy()
        self.refresh()

    def refresh(self):
        self.F  = self.K  @ self.a[1:]
        self.Fi = self.Ki @ self.a[1:]

    def eps_fit(self, F=None, Fi=None):
        F = self.F if F is None else F; Fi = self.Fi if Fi is None else Fi
        num = np.sum(Fi * self.t * F)
        return num / abs(num) if num != 0 else 1.0 + 0j

    def residual(self, eps=None):
        if eps is None:
            eps = self.eps_fit()
        d = self.Fi - eps * self.t * np.conj(self.F)
        return float(np.max(np.abs(d)) / np.max(np.abs(self.F))), eps

    def meter(self, eps=None):
        if eps is None:
            eps = self.eps_fit()
        Fu  = self.Ku  @ self.a[1:]
        Fiu = self.Kiu @ self.a[1:]
        A   = np.exp(UGRID / 2) * Fu        # A(u)  = e^{u/2}  F(e^u)
        Am  = np.exp(-UGRID / 2) * Fiu      # A(-u) = e^{-u/2} F(e^{-u})   [sign fixed; caught by KD-1 controls]
        x = (Am - eps * np.conj(A)) / (Am + eps * np.conj(A))
        gnew = 2.0 / (1.0 - x)
        eta = np.arctanh(np.clip(np.real(x), -0.999999, 0.999999))
        return x, eta, gnew

    def delta_for(self, p, q):
        """da from multiplying in correction series q (q0=1) at prime p, given current a."""
        idx_all = []; val_all = []
        for k in range(1, len(q)):
            if q[k] == 0.0:
                continue
            pk = p ** k
            if pk > self.X:
                break
            j = np.arange(1, self.X // pk + 1)
            idx_all.append(j * pk)
            val_all.append(q[k] * self.a[j])
        if not idx_all:
            z = np.zeros(0, dtype=int); zt = np.zeros(len(self.t), dtype=complex)
            return z, np.zeros(0, dtype=complex), zt, zt.copy()
        idx = np.concatenate(idx_all); val = np.concatenate(val_all)
        # collapse duplicate indices (k-powers overlap at p^k multiples)
        dF  = self.K[:, idx - 1]  @ val
        dFi = self.Ki[:, idx - 1] @ val
        return idx, val, dF, dFi

    def peek_J(self, dF, dFi):
        F = self.F + dF; Fi = self.Fi + dFi
        sc = np.max(np.abs(F))
        if sc == 0:
            return 1e30
        num = np.sum(Fi * self.t * F)
        eps = num / abs(num) if num != 0 else 1.0
        d = Fi - eps * self.t * np.conj(F)
        return float(np.sum(np.abs(d) ** 2) / sc ** 2)

    def peek_residual(self, dF, dFi):
        F = self.F + dF; Fi = self.Fi + dFi
        sc = np.max(np.abs(F))
        if sc == 0:
            return 1e30
        num = np.sum(Fi * self.t * F)
        eps = num / abs(num) if num != 0 else 1.0
        d = Fi - eps * self.t * np.conj(F)
        return float(np.max(np.abs(d)) / sc)

    def commit(self, idx, val, dF, dFi):
        if len(idx):
            np.add.at(self.a, idx, val)
        self.F += dF; self.Fi += dFi

# ---------------- decode problem ----------------
class Problem:
    """Bit-primes with two candidate local factors per arm; state in {-1,0,+1} (0 = marginalized inverse-average)."""
    def __init__(self, arms, bitprimes, cands, fixedfac):
        self.arms = arms
        self.bp = list(bitprimes)
        self.cands = cands
        self.fixed = fixedfac
        self.state = {p: 0 for p in self.bp}
        self._qcache = {}

    def init_marginal(self):
        for ai, arm in enumerate(self.arms):
            cn = self.cands[ai]; fx = self.fixed[ai]
            X = arm.X
            a = np.zeros(X + 1, dtype=complex); a[1] = 1.0
            for p in primes_upto(X):
                kmax = int(np.log(X) / np.log(p))
                if p in cn:
                    inv = 0.5 * (inv_series(np.asarray(cn[p][0], dtype=complex), kmax)
                               + inv_series(np.asarray(cn[p][1], dtype=complex), kmax))
                else:
                    poly = fx(p)
                    if poly is None:
                        continue
                    inv = inv_series(np.asarray(poly, dtype=complex), kmax)
                a = _fold(a, p, inv, X)
            arm.set_a(a)
        for p in self.bp:
            self.state[p] = 0

    def _q(self, ai, p, s_old, s_new):
        key = (ai, p, s_old, s_new)
        if key in self._qcache:
            return self._qcache[key]
        arm = self.arms[ai]
        kmax = int(np.log(arm.X) / np.log(p))
        P, M = self.cands[ai][p]
        def invof(s):
            if s == 0:
                return 0.5 * (inv_series(np.asarray(P, dtype=complex), kmax)
                            + inv_series(np.asarray(M, dtype=complex), kmax))
            return inv_series(np.asarray(P if s == +1 else M, dtype=complex), kmax)
        io, inw = invof(s_old), invof(s_new)
        q = np.zeros(kmax + 1, dtype=complex); q[0] = 1.0
        for k in range(1, kmax + 1):
            s = inw[k]
            for j in range(1, k + 1):
                s -= io[j] * q[k - j]
            q[k] = s
        self._qcache[key] = q
        return q

    def peek_set(self, p, s_new):
        Jt = 0.0; ds = []
        for ai, arm in enumerate(self.arms):
            q = self._q(ai, p, self.state[p], s_new)
            idx, val, dF, dFi = arm.delta_for(p, q)
            Jt += arm.peek_J(dF, dFi)
            ds.append((idx, val, dF, dFi))
        return Jt, ds

    def commit_set(self, p, s_new, ds):
        for arm, d in zip(self.arms, ds):
            arm.commit(*d)
        self.state[p] = s_new

    def set_bit(self, p, s_new):
        J, ds = self.peek_set(p, s_new)
        self.commit_set(p, s_new, ds)
        return J

    def Jtot(self):
        z = [a.peek_J(np.zeros(len(a.t), dtype=complex), np.zeros(len(a.t), dtype=complex)) for a in self.arms]
        return float(sum(z))

    def weights(self):
        w = {}
        arm = self.arms[0]
        for p in self.bp:
            s0 = self.state[p]
            qP = self._q(0, p, s0, +1); qM = self._q(0, p, s0, -1)
            _, _, dFP, dFiP = arm.delta_for(p, qP)
            _, _, dFM, dFiM = arm.delta_for(p, qM)
            w[p] = float(np.linalg.norm(dFP - dFM) + np.linalg.norm(dFiP - dFiM))
        return w

    def resieve_gate(self, tol=1e-12):
        """float-drift gate: rebuild each arm from scratch at the current committed state; compare F."""
        worst = 0.0
        for ai, arm in enumerate(self.arms):
            cn = self.cands[ai]; fx = self.fixed[ai]
            st = self.state
            def f(p):
                if p in cn:
                    if st[p] == +1: return cn[p][0]
                    if st[p] == -1: return cn[p][1]
                    return ('MARG',)
                return fx(p)
            X = arm.X
            a = np.zeros(X + 1, dtype=complex); a[1] = 1.0
            for p in primes_upto(X):
                kmax = int(np.log(X) / np.log(p))
                pol = f(p)
                if isinstance(pol, tuple):
                    inv = 0.5 * (inv_series(np.asarray(cn[p][0], dtype=complex), kmax)
                               + inv_series(np.asarray(cn[p][1], dtype=complex), kmax))
                elif pol is None:
                    continue
                else:
                    inv = inv_series(np.asarray(pol, dtype=complex), kmax)
                a = _fold(a, p, inv, X)
            drift = float(np.max(np.abs(a - arm.a)))
            worst = max(worst, drift)
            arm.a = a; arm.refresh()
        return worst

    # ---- state snapshot / load by reference ----
    def snap(self, copy=True):
        if copy:
            return (dict(self.state), [(a.a.copy(), a.F.copy(), a.Fi.copy()) for a in self.arms])
        return (dict(self.state), [(a.a, a.F, a.Fi) for a in self.arms])

    def load(self, sn, copy=False):
        st, arrs = sn
        self.state = dict(st)
        for a, (aa, F, Fi) in zip(self.arms, arrs):
            if copy:
                a.a = aa.copy(); a.F = F.copy(); a.Fi = Fi.copy()
            else:
                a.a = aa; a.F = F; a.Fi = Fi

# ---------------- solvers ----------------
def S1_sc(prob, log=lambda *a: None):
    prob.init_marginal()
    w = prob.weights()
    order = sorted(prob.bp, key=lambda p: -w[p])
    for p in order:
        JP, dsP = prob.peek_set(p, +1)
        JM, dsM = prob.peek_set(p, -1)
        if JP <= JM:
            prob.commit_set(p, +1, dsP)
        else:
            prob.commit_set(p, -1, dsM)
    log("S1 SC pass done, J =", prob.Jtot())
    improved = True; sweeps = 0
    while improved and sweeps < 60:
        improved = False; sweeps += 1
        Jnow = prob.Jtot()
        for p in order:
            s = prob.state[p]
            Jf, dsf = prob.peek_set(p, -s)
            if Jf < Jnow * (1 - 1e-12) and Jf < Jnow:
                prob.commit_set(p, -s, dsf); Jnow = Jf; improved = True
    heavy = order[:min(40, len(order))]
    for i in range(len(heavy)):
        for j in range(i + 1, len(heavy)):
            J0 = prob.Jtot()
            p, q = heavy[i], heavy[j]
            sp, sq = prob.state[p], prob.state[q]
            prob.set_bit(p, -sp); Jpq = prob.set_bit(q, -sq)
            if Jpq >= J0 * (1 - 1e-12):
                prob.set_bit(q, sq); prob.set_bit(p, sp)
    drift = prob.resieve_gate()
    log("S1 done. J =", prob.Jtot(), " drift =", drift)
    return dict(prob.state), prob.Jtot()

def S2_beam(prob, width=64, log=lambda *a: None):
    prob.init_marginal()
    w = prob.weights()
    order = sorted(prob.bp, key=lambda p: -w[p])
    beam = [prob.snap(copy=True) + (prob.Jtot(),)]   # (state, arrs, J)
    for li, p in enumerate(order):
        cand = []
        for (st, arrs, J) in beam:
            prob.load((st, arrs), copy=False)     # reference load; peeks don't mutate
            for ss in (+1, -1):
                Jc, ds = prob.peek_set(p, ss)
                cand.append((Jc, st, arrs, ss, ds))
        cand.sort(key=lambda c: c[0])
        newbeam = []
        for (Jc, st, arrs, ss, ds) in cand[:width]:
            prob.load((st, arrs), copy=True)      # copy-on-select
            prob.commit_set(p, ss, ds)
            newbeam.append(prob.snap(copy=False) + (Jc,))
        beam = newbeam
        if li % 25 == 0:
            log(f"S2 level {li}/{len(order)} bestJ={beam[0][2]:.3e}")
    st, arrs, J = min(beam, key=lambda b: b[2])
    prob.load((st, arrs), copy=True)
    drift = prob.resieve_gate()
    log("S2 done. J =", prob.Jtot(), " drift =", drift)
    return dict(prob.state), prob.Jtot()

def S3_temper(prob, seeds=(20260803, 1951, 2089, 5), nchains=8, sweeps=20000,
              exchange_every=50, log=lambda *a: None):
    rng = np.random.default_rng(list(seeds))
    prob.init_marginal()
    w = prob.weights()
    order = sorted(prob.bp, key=lambda p: -w[p])
    wv = np.array([np.sqrt(w[p]) for p in order]); wv = wv / wv.sum()
    base = prob.snap(copy=True)
    chains = []
    for c in range(nchains):
        prob.load(base, copy=True)
        for p in order:
            prob.set_bit(p, int(rng.choice([-1, 1])))
        chains.append(list(prob.snap(copy=False)) + [prob.Jtot()])
    temps = np.geomspace(3e-2, 30.0, nchains)
    Jscale = np.median([c[2] for c in chains]) + 1e-30
    temps = temps * Jscale
    best = None
    m = len(order)
    props = max(8, m // 4)
    for sw in range(sweeps):
        for c in range(nchains):
            st, arrs, J = chains[c]
            prob.load((st, arrs), copy=False)
            T = temps[c]
            for _ in range(props):
                p = order[int(rng.choice(m, p=wv))]
                s = prob.state[p]
                Jf, ds = prob.peek_set(p, -s)
                if Jf <= J or rng.random() < np.exp(-(Jf - J) / T):
                    prob.commit_set(p, -s, ds); J = Jf
            chains[c] = list(prob.snap(copy=False)) + [J]
            if best is None or J < best[1]:
                best = (dict(prob.state), J)
        if sw % exchange_every == 0 and sw > 0:
            for c in range(nchains - 1):
                J1, J2 = chains[c][2], chains[c + 1][2]
                d = (1.0 / temps[c] - 1.0 / temps[c + 1]) * (J1 - J2)
                if d > 0 or rng.random() < np.exp(d):
                    chains[c], chains[c + 1] = chains[c + 1], chains[c]
        if sw % 500 == 0:
            log(f"S3 sweep {sw}: bestJ={best[1]:.3e} coldJ={chains[0][2]:.3e}")
        if best[1] < 1e-24:
            log(f"S3 early stop at sweep {sw}: bestJ={best[1]:.3e}")
            break
    # polish best with greedy
    prob.load(base, copy=True)
    for p in order:
        prob.set_bit(p, best[0][p])
    improved = True; guard = 0
    while improved and guard < 40:
        improved = False; guard += 1
        Jnow = prob.Jtot()
        for p in order:
            s = prob.state[p]
            Jf, dsf = prob.peek_set(p, -s)
            if Jf < Jnow:
                prob.commit_set(p, -s, dsf); Jnow = Jf; improved = True
    drift = prob.resieve_gate()
    log("S3 done. J =", prob.Jtot(), " drift =", drift)
    return dict(prob.state), prob.Jtot()

def sensitivity(prob, floor):
    """single-flip residual displacement per bit prime at current solution (arm 0 theta residual)."""
    arm = prob.arms[0]
    r0, _ = arm.residual()
    s = {}
    for p in prob.bp:
        q = prob._q(0, p, prob.state[p], -prob.state[p])
        idx, val, dF, dFi = arm.delta_for(p, q)
        s[p] = abs(arm.peek_residual(dF, dFi) - r0)
    vis = {p: v for p, v in s.items() if v > 100 * floor}
    return s, vis
