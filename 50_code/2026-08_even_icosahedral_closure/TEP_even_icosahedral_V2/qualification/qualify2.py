#!/usr/bin/env python3
"""Planted-ladder qualification, TWIST-ENRICHED (pre-registered fallback per prereg §6, engaged after
base-only GATE-M attempt 1 failed: S1 8.1e-2 / S2 exact / S3 5.7e-7-spurious — logged, bars unchanged).
Arms: base FE + quadratic twists d in {5,8,12,13,-3,-4,-7,-8} (d<0 through the odd port).
Decoder-internal t-grid: 33-pt geomspace [0.5,2.0] (A3 precedent: internal only).
Certification metrics unchanged: pre-registered TGRID base arm, fresh-sieved at the solved state.
Usage: python3 qualify2.py <D> <S1|S2|S3|cert> [start-chunk info for S3]"""
import numpy as np, json, sys, time
sys.path.insert(0, '.')
import instr2
from instr2 import Arm, Problem, sieve, Xof, TGRID, S1_sc, S2_beam, S3_temper, sensitivity

TW = [5, 8, 12, 13, -3, -4, -7, -8]
TGRID_DEC = np.geomspace(0.5, 2.0, 33)
FACP = [1.0, -2.0, 1.0]; FACN = [1.0, 1.0, 1.0]; FACI = [1.0, 0.0, -1.0]; FACR = [1.0, -1.0]

def load_planted(D):
    cls = {}
    for line in open(f'classes_planted_{D}.txt'):
        p, c = line.strip().split(':')
        cls[int(p)] = c
    return cls

def load_kron(D):
    kr = {}
    for line in open(f'kron_{D}.txt'):
        parts = line.strip().split(':')
        kr[int(parts[0])] = {TW[i]: int(parts[i+1]) for i in range(len(TW))}
    return kr

def build(D):
    cls = load_planted(D); kr = load_kron(D)
    X0 = Xof(D)
    bitp = [p for p, c in cls.items() if p <= X0 and c in 'PN']
    truth = {p: (+1 if cls[p] == 'P' else -1) for p in bitp}
    arms = [Arm(float(D), 0, tgrid=TGRID_DEC, label='base')]
    cands = [{p: (FACP, FACN) for p in bitp}]
    def fixed_base(p):
        c = cls.get(p)
        if c is None or c in 'PN':
            return None
        return FACI if c == 'I' else FACR
    fixed = [fixed_base]
    for d in TW:
        Nd = float(D) * d * d
        port = 0 if d > 0 else 1
        arm = Arm(Nd, port, tgrid=TGRID_DEC, label=f'tw{d}')
        cn = {}
        def mk_fixed(d):
            def f(p):
                if p in (2, 3, 5, 7, 13) and (4*abs(d)) % p == 0 and kr.get(p, {}).get(d, 0) == 0:
                    return None
                c = cls.get(p)
                kd = kr.get(p, {}).get(d)
                if c is None or kd is None:
                    return None
                if kd == 0:
                    return None
                if c in 'PN':
                    return None   # bit prime: handled via cands
                if c == 'I':
                    return FACI
                return [1.0, -kd]   # ramified in D: (1 - kd*T)
            return f
        for p in bitp:
            kd = kr.get(p, {}).get(d)
            if kd is None or kd == 0 or p > arm.X:
                # beyond arm range or killed by twist: both candidates trivial
                cn[p] = ([1.0], [1.0]) if (kd == 0 or kd is None) else ([1.0], [1.0])
            else:
                cn[p] = ([1.0, -2.0*kd, 1.0], [1.0, 1.0*kd, 1.0])
        # bit primes between X0 and arm.X: not unknowns; use TRUE-class? NO — unknown region: treat marginalized?
        # Honest choice: primes p in (X0, arm.X] with class P/N are ALSO unknowns of the problem.
        arms.append(arm); cands.append(cn); fixed.append(mk_fixed(d))
    # extend bit set to the largest arm's range: unknowns exist wherever any arm sees them
    Xmax = max(a.X for a in arms)
    bitp_ext = [p for p, c in cls.items() if p <= Xmax and c in 'PN']
    for p in bitp_ext:
        if p not in bitp:
            truth[p] = +1 if cls[p] == 'P' else -1
    # rebuild cands with extended bit set
    cands = [{p: (FACP, FACN) for p in bitp_ext if p <= arms[0].X}]
    for ai, d in enumerate(TW):
        arm = arms[ai+1]; cn = {}
        for p in bitp_ext:
            if p > arm.X:
                continue
            kd = kr.get(p, {}).get(d)
            if kd is None or kd == 0:
                continue
            cn[p] = ([1.0, -2.0*kd, 1.0], [1.0, 1.0*kd, 1.0])
        cands.append(cn)
    # per-arm candidate presence: Problem assumes cands[ai][p] exists for all bit p — relax via wrapper
    return arms, bitp_ext, truth, cands, fixed, cls

class MultiProblem(Problem):
    """Problem variant where a bit prime may be absent from some arms (beyond X or twist-killed)."""
    def init_marginal(self):
        from instr2 import primes_upto, inv_series, _fold
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

    def peek_set(self, p, s_new):
        Jt = 0.0; ds = []
        for ai, arm in enumerate(self.arms):
            if p not in self.cands[ai]:
                z = np.zeros(0, dtype=int); zt = np.zeros(len(arm.t), dtype=complex)
                d = (z, np.zeros(0, dtype=complex), zt, zt.copy())
                Jt += arm.peek_J(d[2], d[3]); ds.append(d)
                continue
            q = self._q(ai, p, self.state[p], s_new)
            idx, val, dF, dFi = arm.delta_for(p, q)
            Jt += arm.peek_J(dF, dFi)
            ds.append((idx, val, dF, dFi))
        return Jt, ds

    def weights(self):
        w = {}
        for p in self.bp:
            tot = 0.0
            for ai, arm in enumerate(self.arms):
                if p not in self.cands[ai]:
                    continue
                s0 = self.state[p]
                qP = self._q(ai, p, s0, +1); qM = self._q(ai, p, s0, -1)
                _, _, dFP, dFiP = arm.delta_for(p, qP)
                _, _, dFM, dFiM = arm.delta_for(p, qM)
                tot += float(np.linalg.norm(dFP - dFM) + np.linalg.norm(dFiP - dFiM))
            w[p] = tot
        return w

    def resieve_gate(self, tol=1e-12):
        from instr2 import primes_upto, inv_series, _fold
        worst = 0.0
        for ai, arm in enumerate(self.arms):
            cn = self.cands[ai]; fx = self.fixed[ai]
            X = arm.X
            a = np.zeros(X + 1, dtype=complex); a[1] = 1.0
            for p in primes_upto(X):
                kmax = int(np.log(X) / np.log(p))
                if p in cn:
                    s = self.state.get(p, 0)
                    if s == 0:
                        inv = 0.5 * (inv_series(np.asarray(cn[p][0], dtype=complex), kmax)
                                   + inv_series(np.asarray(cn[p][1], dtype=complex), kmax))
                    else:
                        inv = inv_series(np.asarray(cn[p][0] if s == +1 else cn[p][1], dtype=complex), kmax)
                else:
                    poly = fx(p)
                    if poly is None:
                        continue
                    inv = inv_series(np.asarray(poly, dtype=complex), kmax)
                a = _fold(a, p, inv, X)
            drift = float(np.max(np.abs(a - arm.a)))
            worst = max(worst, drift)
            arm.a = a; arm.refresh()
        return worst

def true_locfac(cls):
    def f(p):
        c = cls.get(p)
        if c is None:
            return None
        return {'P': FACP, 'N': FACN, 'I': FACI, 'R': FACR}[c]
    return f

def cert_metrics(D, state, cls, floor):
    """certification on the pre-registered grid: fresh sieve at the solved state (UNDECIDED->marginal not allowed
    at cert: undecided bits (state 0) kept marginalized and reported)."""
    X = Xof(D)
    arm = Arm(float(D), 0, tgrid=TGRID, label='cert')
    def f(p):
        c = cls.get(p)
        if c is None:
            return None
        if c in 'PN' and p <= X:
            s = state.get(p, 0)
            if s == +1: return FACP
            if s == -1: return FACN
            return 'MARG'
        return {'P': FACP, 'N': FACN, 'I': FACI, 'R': FACR}[c] if c not in 'PN' else (FACP if cls[p] == 'P' else FACN)
    from instr2 import primes_upto, inv_series, _fold
    a = np.zeros(X + 1, dtype=complex); a[1] = 1.0
    for p in primes_upto(X):
        kmax = int(np.log(X) / np.log(p))
        pol = f(p)
        if pol is None:
            continue
        if isinstance(pol, str):
            inv = 0.5 * (inv_series(np.asarray(FACP, dtype=complex), kmax)
                       + inv_series(np.asarray(FACN, dtype=complex), kmax))
        else:
            inv = inv_series(np.asarray(pol, dtype=complex), kmax)
        a = _fold(a, p, inv, X)
    arm.set_a(a)
    r, eps = arm.residual()
    x, eta, gnew = arm.meter(eps)
    return arm, r, eps, float(np.max(np.abs(gnew - 2)))

def run(D, which):
    t0 = time.time()
    arms, bitp, truth, cands, fixed, cls = build(D)
    print(f"== D={D} twist-enriched: arms={len(arms)} (X: {[a.X for a in arms]}), bit-primes={len(bitp)} ==", flush=True)
    prob = MultiProblem(arms, bitp, cands, fixed)
    floor = 3.2e-15
    if which == 'S1':
        st, J = S1_sc(prob, log=lambda *a: print(' ', *a, flush=True))
    elif which == 'S2':
        st, J = S2_beam(prob, width=64, log=lambda *a: print(' ', *a, flush=True))
    elif which == 'S3':
        st, J = S3_temper(prob, sweeps=20000, log=lambda *a: print(' ', *a, flush=True))
    else:
        raise SystemExit('which?')
    carm, r, eps, gdev = cert_metrics(D, st, cls, floor)
    # sensitivity/visible on the certification arm
    certprob = Problem([carm], [p for p in bitp if p <= carm.X], [ {p: (FACP, FACN) for p in bitp if p <= carm.X} ], [lambda p: None])
    certprob.state = {p: st.get(p, 0) for p in bitp if p <= carm.X}
    s, vis = sensitivity(certprob, floor)
    vp = sorted(vis.keys())
    acc_all = sum(1 for p in bitp if st.get(p, 0) == truth[p]) / len(bitp)
    wrong_vis = [p for p in vp if st.get(p, 0) != truth[p]]
    acc_vis = (len(vp) - len(wrong_vis)) / len(vp) if vp else float('nan')
    dt = time.time() - t0
    print(f"{which}: cert-residual {r:.3e}  eps {eps:.6f}  meterdev {gdev:.3e}  acc(all incl. ext) {acc_all*100:.1f}%  "
          f"acc(visible) {acc_vis*100:.1f}% ({len(vp)} visible, wrong: {wrong_vis})  [{dt:.0f}s]", flush=True)
    out = {'D': D, 'which': which, 'cert_residual': r, 'eps': [eps.real, eps.imag], 'meterdev': gdev,
           'acc_all': acc_all, 'acc_vis': acc_vis, 'n_visible': len(vp), 'wrong_visible': wrong_vis,
           'bits': {str(p): int(st.get(p, 0)) for p in bitp}, 'time_s': dt}
    json.dump(out, open(f'qualify2_{D}_{which}.json', 'w'), indent=1)
    return out

if __name__ == '__main__':
    run(int(sys.argv[1]), sys.argv[2])
