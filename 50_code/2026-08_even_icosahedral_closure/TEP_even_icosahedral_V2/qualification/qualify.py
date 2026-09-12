#!/usr/bin/env python3
"""Planted-ladder solver qualification (GATE-M / GATE-B). Usage: python3 qualify.py <D> [solvers]"""
import numpy as np, json, sys, time
sys.path.insert(0, '.')
from instr2 import Arm, Problem, sieve, Xof, S1_sc, S2_beam, S3_temper, sensitivity

FACP = [1.0, -2.0, 1.0]   # split principal:    (1-T)^2
FACN = [1.0, 1.0, 1.0]    # split nonprincipal: 1+T+T^2
FACI = [1.0, 0.0, -1.0]   # inert:              1-T^2
FACR = [1.0, -1.0]        # ramified (h odd => principal => +1)

def load_planted(D):
    cls = {}
    for line in open(f'classes_planted_{D}.txt'):
        p, c = line.strip().split(':')
        cls[int(p)] = c
    return cls

def build(D, port=0):
    X = Xof(D)
    arm = Arm(float(D), port)
    cls = load_planted(D)
    bitp = [p for p, c in cls.items() if p <= X and c in 'PN']
    truth = {p: (+1 if cls[p] == 'P' else -1) for p in bitp}
    cands = {p: (FACP, FACN) for p in bitp}
    def fixed(p):
        c = cls.get(p)
        if c is None or c in 'PN':
            return None
        return FACI if c == 'I' else FACR
    return arm, bitp, truth, cands, fixed, cls

def true_locfac(cls):
    def f(p):
        c = cls.get(p)
        if c is None:
            return None
        return {'P': FACP, 'N': FACN, 'I': FACI, 'R': FACR}[c]
    return f

def run(D, solvers=('S1', 'S2', 'S3')):
    t0 = time.time()
    arm, bitp, truth, cands, fixed, cls = build(D)
    X = arm.X
    print(f"== planted rung D={D}: X={X}, bit-primes={len(bitp)} ==", flush=True)
    # true-bits certification
    arm.set_a(sieve(X, true_locfac(cls)))
    rT, eT = arm.residual()
    xT, etaT, gT = arm.meter(eT)
    gdev = float(np.max(np.abs(gT - 2)))
    print(f"TRUE-BITS certification: residual {rT:.3e}  eps {eT:.6f}  meter dev {gdev:.3e}  (bar 5e-12)", flush=True)
    res = {'D': D, 'X': X, 'nbits': len(bitp), 'true_residual': rT, 'true_meterdev': gdev, 'solvers': {}}
    if rT > 5e-12:
        print("*** TRUE-BITS CERTIFICATION FAILED — rung invalid ***")
        json.dump(res, open(f'qualify_{D}.json', 'w'), indent=1); return res
    floor = max(rT, 3.2e-15)

    prob = Problem([arm], bitp, [cands], [fixed])
    for sname in solvers:
        ts = time.time()
        if sname == 'S1':
            st, J = S1_sc(prob, log=lambda *a: print(' ', *a, flush=True))
        elif sname == 'S2':
            st, J = S2_beam(prob, width=64, log=lambda *a: print(' ', *a, flush=True))
        else:
            st, J = S3_temper(prob, log=lambda *a: print(' ', *a, flush=True))
        r, eps = prob.arms[0].residual()
        s, vis = sensitivity(prob, floor)
        nb = len(bitp)
        acc_all = sum(1 for p in bitp if st[p] == truth[p]) / nb
        vp = sorted(vis.keys())
        acc_vis = (sum(1 for p in vp if st[p] == truth[p]) / len(vp)) if vp else float('nan')
        wrong_vis = [p for p in vp if st[p] != truth[p]]
        dt = time.time() - ts
        print(f"{sname}: residual {r:.3e}  J {J:.3e}  acc(all) {acc_all*100:.1f}%  "
              f"acc(visible) {acc_vis*100:.1f}% ({len(vp)} visible, {len(wrong_vis)} wrong)  [{dt:.0f}s]", flush=True)
        res['solvers'][sname] = {'residual': r, 'J': J, 'acc_all': acc_all, 'acc_vis': acc_vis,
                                 'n_visible': len(vp), 'wrong_visible': wrong_vis,
                                 'bits': {str(p): int(st[p]) for p in bitp}, 'time_s': dt}
    # gate evaluation
    g = all(v['residual'] <= 1e-11 and v['n_visible'] > 0 and len(v['wrong_visible']) == 0
            for v in res['solvers'].values()) and len(res['solvers']) >= 3
    res['gate_pass'] = bool(g)
    print(f"GATE at D={D}: {'PASS' if g else 'FAIL'}   [{time.time()-t0:.0f}s total]", flush=True)
    json.dump(res, open(f'qualify_{D}.json', 'w'), indent=1)
    return res

if __name__ == '__main__':
    D = int(sys.argv[1])
    solvers = sys.argv[2].split(',') if len(sys.argv) > 2 else ('S1', 'S2', 'S3')
    run(D, solvers)
