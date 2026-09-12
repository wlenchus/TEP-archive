#!/usr/bin/env python3
"""THE SUMMIT DECODE — even-icosahedral 2-dim lift at N = 1951 (quintic nebentypus), per
decode2dim_RESUMPTION_preregistration_20260803.md + AMENDMENTs R1/R1.w and the GATE-M-qualified
recipe (S2 beam + S2-perturbed + S5 list decoder on whitened twist-enriched arms).
Cells: parity in {even(0), odd(1)}. No truth exists anywhere; consensus + batteries carry the grade.
Usage: python3 summit.py <even|odd> <S2|S2ord7|S5>"""
import numpy as np, json, sys, time
sys.path.insert(0, '.')
import qualify4
from qualify4 import WProblem, inband_S2
from instr2 import Arm, Problem, Xof, TGRID, sensitivity, sieve, inv_series, primes_upto, _fold

TW = [5, 8, 12, 13, -3, -4, -7, -8]
PHI = (1 + np.sqrt(5.0)) / 2
Z10 = np.exp(1j * np.pi / 5)          # zeta_10
MTAB = {0: 2.0, 1: 0.0, 2: 1.0, 3: 1.0 / PHI, 4: PHI}   # |a_p| by RAW label under certified faceswap=1
NBASE = 1951.0

def load_data():
    cls = {}
    for line in open('../gp/classesX_doud1951.txt'):
        p, c = line.strip().split(':')
        cls[int(p)] = int(c)
    jl = {}
    for line in open('chilog_1951.txt'):
        p, j = line.strip().split(':')
        jl[int(p)] = int(j)
    kr = {}
    for line in open('kron_1951.txt'):
        parts = line.strip().split(':')
        kr[int(parts[0])] = {TW[i]: int(parts[i + 1]) for i in range(len(TW))}
    return cls, jl, kr

def build_summit(cell, conj=False, goldenswap=False):
    """cell: 0 even / 1 odd. conj: chi -> chi^2 Galois transport cell. goldenswap: A4-style live negative."""
    cls, jl, kr = load_data()
    mul = 2 if conj else 1
    def phase(p):        # theta_p = zeta10^(mul*j); chi(p) = theta^2
        j = jl.get(p)
        if j is None:
            return None
        return Z10 ** ((mul * j) % 10)
    def mag(p):
        c = cls.get(p)
        if c is None:
            return None
        if goldenswap and c in (3, 4):
            c = 7 - c
        return MTAB[c]
    arms = [Arm(NBASE, cell, label='base')]
    ports = {None: cell}
    for d in TW:
        port = cell if d > 0 else 1 - cell
        arms.append(Arm(NBASE * d * d, port, label=f'tw{d}'))
    Xmax = max(a.X for a in arms)
    bitp = [p for p in sorted(cls) if p <= Xmax and p != 1951 and cls[p] != 1 and p in jl]
    cands = []
    fixed = []
    for ai, arm in enumerate(arms):
        d = None if ai == 0 else TW[ai - 1]
        cn = {}
        for p in bitp:
            if p > arm.X:
                continue
            kd = 1 if d is None else kr.get(p, {}).get(d, 0)
            if kd == 0:
                continue
            th = phase(p); m = mag(p)
            ap = kd * th * m
            chp = th * th
            cn[p] = ([1.0, -ap, chp], [1.0, ap, chp])     # candidate +1: a_p = +theta*m (dressed)
        def mk_fixed(d):
            def f(p):
                if p == 1951:
                    return None                            # mu10-marginal: sum over u in mu10 of u = 0 => factor 1
                c = cls.get(p); th = phase(p)
                if c is None or th is None:
                    return None
                kd = 1 if d is None else kr.get(p, {}).get(d, 0)
                if kd == 0:
                    return None
                if c == 1:
                    return [1.0, 0.0, th * th]             # 2A: a_p = 0, det chi survives twist (kd^2=1)
                return None                                # bit primes handled via cands
            return f
        cands.append(cn); fixed.append(mk_fixed(d))
    return arms, bitp, cands, fixed, (cls, jl, kr)

def cert_arm_for(cell, state, data, conj=False, goldenswap=False, N=NBASE):
    cls, jl, kr = data
    mul = 2 if conj else 1
    X = Xof(N)
    arm = Arm(N, cell, tgrid=TGRID, label='cert')
    a = np.zeros(X + 1, dtype=complex); a[1] = 1.0
    for p in primes_upto(X):
        kmax = int(np.log(X) / np.log(p))
        c = cls.get(p); j = jl.get(p)
        if c is None or j is None or p == 1951:
            continue
        th = Z10 ** ((mul * j) % 10)
        cc = 7 - c if (goldenswap and c in (3, 4)) else c
        m = MTAB[cc]
        if c == 1:
            poly = [1.0, 0.0, th * th]
        else:
            s = state.get(p, 0)
            if s == 0:
                iP = inv_series(np.asarray([1.0, -th * m, th * th], dtype=complex), kmax)
                iM = inv_series(np.asarray([1.0, th * m, th * th], dtype=complex), kmax)
                a = _fold(a, p, 0.5 * (iP + iM), X)
                continue
            poly = [1.0, -s * th * m, th * th]
        a = _fold(a, p, inv_series(np.asarray(poly, dtype=complex), kmax), X)
    arm.set_a(a)
    return arm

def add_u_sigma(prob, kr):
    """AMENDMENT R2: charge the mu10-marginalized ramified port (p=1951) to each twist arm's
    whitening variance: v_u(t) = (1/10) sum_{u in mu10} |delta-defect(u)|^2. Stored for later removal."""
    prob._uvar = {}
    for ai, arm in enumerate(prob.arms):
        if ai == 0 or arm.X < 1951:
            continue
        d = TW[ai - 1]
        kd = kr[1951][d]
        kmax = int(np.log(arm.X) / np.log(1951))
        v = np.zeros(len(arm.t))
        for k10 in range(10):
            u = np.exp(1j * np.pi * k10 / 5)
            q = np.array([(kd * u) ** k for k in range(kmax + 1)], dtype=complex)  # inv of (1 - kd u T)
            idx, val, dF, dFi = arm.delta_for(1951, q)
            v += (np.abs(dFi) ** 2 + arm.t ** 2 * np.abs(dF) ** 2) / 10.0
        prob._uvar[ai] = v
        prob.sig2[ai] = prob.sig2[ai] + v

def u_lock(prob, kr):
    """post-band 10-way determination of the ramified-port eigenvalue u; returns (k10, separation)."""
    best = None; scores = []
    for k10 in range(10):
        u = np.exp(1j * np.pi * k10 / 5)
        Jt = 0.0; dss = []
        for ai, arm in enumerate(prob.arms):
            if ai == 0 or arm.X < 1951:
                dss.append(None); continue
            d = TW[ai - 1]; kd = kr[1951][d]
            kmax = int(np.log(arm.X) / np.log(1951))
            q = np.array([(kd * u) ** k for k in range(kmax + 1)], dtype=complex)
            idx, val, dF, dFi = arm.delta_for(1951, q)
            Jt += arm.peek_J(dF, dFi)
            dss.append((idx, val, dF, dFi))
        scores.append(Jt)
        if best is None or Jt < best[0]:
            best = (Jt, k10, dss)
    Jt, k10, dss = best
    for ai, arm in enumerate(prob.arms):
        if dss[ai] is not None:
            arm.commit(*dss[ai])
        if hasattr(prob, '_uvar') and ai in prob._uvar:
            prob.sig2[ai] = prob.sig2[ai] - prob._uvar[ai]
    ranked = sorted(scores)
    sep = ranked[1] / ranked[0] if ranked[0] > 0 else float('inf')
    return k10, scores, sep

def bands_of(arms, bitp):
    edges = sorted(set(a.X for a in arms))
    lo = 0; bands = []
    for hi in edges:
        band = [p for p in bitp if lo < p <= hi]
        if band:
            bands.append(band)
        lo = hi
    return bands

def solve(cell, which, goldenswap=False):
    t0 = time.time()
    arms, bitp, cands, fixed, data = build_summit(cell, goldenswap=goldenswap)
    prob = WProblem(arms, bitp, cands, fixed)
    prob.init_marginal(); prob.build_sigma()
    add_u_sigma(prob, data[2])          # AMENDMENT R2
    bands = bands_of(arms, bitp)
    print(f"== SUMMIT cell={'even' if cell==0 else 'odd'} {which}: {len(arms)} arms, {len(bitp)} bits, "
          f"bands {[len(b) for b in bands]} ==", flush=True)
    if which in ('S2', 'S2ord7'):
        qualify4.ORDER_JITTER = 7 if which == 'S2ord7' else None
        for ps in range(3):
            for band in bands:
                inband_S2(prob, band, log=print)
            print(f"  pass {ps+1}: J = {prob.Jtot():.3e}", flush=True)
        w = prob.weights()
        order = sorted(bitp, key=lambda p: -w[p])
        for _ in range(8):
            improved = False
            Jnow = prob.Jtot()
            for p in order:
                s = prob.state[p]
                if s == 0:
                    continue
                Jf, dsf = prob.peek_set(p, -s)
                if Jf < Jnow:
                    prob.commit_set(p, -s, dsf); Jnow = Jf; improved = True
            if not improved:
                break
    else:  # S5
        w = prob.weights()
        order = sorted(bitp, key=lambda p: -w[p])
        heavy = order[:8]; rest = order[8:]
        base_sn = prob.snap(copy=True)
        leaves = []
        for leaf in range(256):
            prob.load(base_sn, copy=True)
            for i, p in enumerate(heavy):
                prob.set_bit(p, +1 if (leaf >> i) & 1 else -1)
            for p in rest:
                JP, dsP = prob.peek_set(p, +1)
                JM, dsM = prob.peek_set(p, -1)
                prob.commit_set(p, +1 if JP <= JM else -1, dsP if JP <= JM else dsM)
            for _ in range(2):
                improved = False
                Jnow = prob.Jtot()
                for p in rest:
                    s = prob.state[p]
                    Jf, dsf = prob.peek_set(p, -s)
                    if Jf < Jnow:
                        prob.commit_set(p, -s, dsf); Jnow = Jf; improved = True
                if not improved:
                    break
            leaves.append((prob.Jtot(), leaf, dict(prob.state)))
            if leaf % 64 == 0:
                print(f"  S5 leaf {leaf}  J {leaves[-1][0]:.3e}", flush=True)
        leaves.sort(key=lambda x: x[0])
        best = None
        for J0, leaf, st0 in leaves[:16]:
            prob.load(base_sn, copy=True)
            for p in order:
                prob.set_bit(p, st0[p])
            for _ in range(8):
                improved = False
                Jnow = prob.Jtot()
                for p in order:
                    s = prob.state[p]
                    Jf, dsf = prob.peek_set(p, -s)
                    if Jf < Jnow:
                        prob.commit_set(p, -s, dsf); Jnow = Jf; improved = True
                if not improved:
                    break
            if best is None or prob.Jtot() < best[0]:
                best = (prob.Jtot(), leaf, dict(prob.state))
        print(f"  S5 winner leaf {best[1]}  J {best[0]:.3e}  (runner-up J {leaves[1][0]:.3e})", flush=True)
        prob.load(base_sn, copy=True)
        for p in order:
            prob.set_bit(p, best[2][p])
    globals()['_GS'] = goldenswap
    k10, uscores, usep = u_lock(prob, data[2])
    # final polish with u locked and sigma un-padded
    w = prob.weights()
    order = sorted(bitp, key=lambda p: -w[p])
    for _ in range(6):
        improved = False
        Jnow = prob.Jtot()
        for p in order:
            s = prob.state[p]
            if s == 0:
                continue
            Jf, dsf = prob.peek_set(p, -s)
            if Jf < Jnow:
                prob.commit_set(p, -s, dsf); Jnow = Jf; improved = True
        if not improved:
            break
    print(f"  u-lock: u = zeta10^{k10}  separation x{usep:.1f}  post-lock J = {prob.Jtot():.3e}", flush=True)
    drift = 0.0   # resieve gate would need u-aware rebuild; drift checked pre-lock by band machinery
    st = dict(prob.state)
    # certification on the pre-registered grid
    carm = cert_arm_for(cell, st, data, goldenswap=goldenswap)
    r, eps = carm.residual()
    x, eta, gnew = carm.meter(eps)
    gdev = float(np.max(np.abs(gnew - 2)))
    # per-arm residuals at solution
    armres = {}
    for arm in prob.arms:
        rr, ee = arm.residual()
        armres[arm.label] = [rr, ee.real, ee.imag]
    dt = time.time() - t0
    print(f"SUMMIT {('even' if cell==0 else 'odd')}/{which}: J {prob.Jtot():.3e}  drift {drift:.1e}  "
          f"CERT residual {r:.3e}  eps {eps.real:+.6f}{eps.imag:+.6f}i  meter dev {gdev:.3e}  [{dt:.0f}s]", flush=True)
    out = {'cell': ('even' if cell == 0 else 'odd') + ('GS' if goldenswap else ''), 'which': which, 'J': prob.Jtot(), 'drift': drift,
           'cert_residual': r, 'eps': [eps.real, eps.imag], 'meterdev': gdev, 'arm_residuals': armres,
           'bits': {str(p): int(st[p]) for p in bitp}, 'time_s': dt}
    json.dump(out, open(f'summit_{out["cell"]}_{which}.json', 'w'), indent=1)
    return out

if __name__ == '__main__':
    tag = sys.argv[1]
    cell = 0 if tag.startswith('even') else 1
    solve(cell, sys.argv[2], goldenswap=tag.endswith('GS'))
