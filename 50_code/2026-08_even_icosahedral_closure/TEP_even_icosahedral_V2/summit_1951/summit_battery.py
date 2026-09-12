#!/usr/bin/env python3
"""Full section-7 battery on the consensus solution (odd port, orientation B, N=1951)."""
import numpy as np, json, sys
sys.path.insert(0, '.')
from summit import build_summit, cert_arm_for, MTAB, Z10
from instr2 import Arm, Problem, Xof, TGRID, sensitivity, sieve, inv_series, primes_upto, _fold

CELL, GS = 1, True
arms, bitp, cands, fixed, data = build_summit(CELL, goldenswap=GS)
cls, jl, kr = data
arm0 = arms[0]
bp = [p for p in bitp if p <= arm0.X]
sol = {int(p): v for p, v in json.load(open('summit_base_oddGS.json'))['bits'].items()}
s5b = {int(p): v for p, v in json.load(open('summit_S5b.json'))['bits'].items()}
ord7 = {int(p): v for p, v in json.load(open('summit_consensus.json'))['S2ord7'].items()}

# 1. explicit agreement
sens = {int(p): v for p, v in json.load(open('summit_consensus.json'))['sens'].items()}
vis = sorted([p for p in bp if sens[p] > 100 * 5e-15])
ag_vis = [p for p in vis if not (sol[p] == s5b[p] == ord7[p])]
ag_full = [p for p in bp if not (sol[p] == s5b[p] == ord7[p])]
print(f"1. consensus: visible {len(vis)}: disagreements {ag_vis}; full-set disagreements: {len(ag_full)} {ag_full[:8]}")

# 2. blind N-scan on the certification coefficients
carm = cert_arm_for(CELL, sol, data, goldenswap=GS)
r0, eps0 = carm.residual()
print(f"2. N-scan (solution residual {r0:.3e}):")
for mult in (0.25, 0.5, 0.8, 0.9, 0.95, 1.0, 1.05, 1.1, 1.25, 2.0, 4.0):
    Nw = 1951.0 * mult
    aw = Arm(Nw, CELL, X=carm.X, tgrid=TGRID)
    aw.set_a(carm.a)
    rw, _ = aw.residual()
    print(f"   N = 1951*{mult}: {rw:.3e}")

# 3. negatives
rng = np.random.default_rng(20260803)
res_neg = {}
for seed in (1, 2, 3):
    r2 = np.random.default_rng([20260803, seed])
    stx = dict(sol)
    flips = r2.choice(vis, size=max(1, len(vis)//10), replace=False)
    for p in flips:
        stx[int(p)] = -stx[int(p)]
    cx = cert_arm_for(CELL, stx, data, goldenswap=GS)
    rx, _ = cx.residual()
    res_neg[f'scramble10%_s{seed}'] = rx
aE = Arm(1951.0, 0, X=carm.X, tgrid=TGRID); aE.set_a(carm.a); rE, _ = aE.residual()
res_neg['opposite_port'] = rE
num = np.sum(carm.Fi * carm.t * carm.F); epsf = num/abs(num)
d = carm.Fi - (epsf * np.exp(1j*np.pi/3)) * carm.t * np.conj(carm.F)
res_neg['eps_rot60'] = float(np.max(np.abs(d))/np.max(np.abs(carm.F)))
for k, v in res_neg.items():
    print(f"3. NEG {k}: {v:.3e}")

# 4. meter / eta jets on the winner
x, eta, gnew = carm.meter(eps0)
print(f"4. meter: max|G_new-2| = {np.max(np.abs(gnew-2)):.3e}   max|eta| = {np.max(np.abs(eta)):.3e}")

# 5. orientation/parity cell table (from earlier runs)
print("5. cell table: even 3.11e-3 / evenGS 2.76e-2 / odd 1.31e-3 / oddGS(WINNER) 8.96e-15 (base-only S2-128)")

json.dump({'visible': [int(p) for p in vis], 'disagreements_visible': [int(p) for p in ag_vis],
           'negatives': res_neg, 'N_scan_solution': r0,
           'eps': [eps0.real, eps0.imag]}, open('summit_battery.json', 'w'), indent=1)
