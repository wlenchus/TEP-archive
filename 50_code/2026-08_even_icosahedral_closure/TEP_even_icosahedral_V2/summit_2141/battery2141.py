#!/usr/bin/env python3
"""Batteries on the 2141 winner (nu5_odd_A): N-scan, scrambles, hold-out re-decode on disjoint grid,
S5b consensus, and the Gauss-sum eps/u lock."""
import numpy as np, mpmath as mp, json, sys
sys.path.insert(0, '.')
import instr2
from instr2 import Arm, Xof, TGRID
from qualify4 import WProblem
import s2141lib as S

sol = {int(p): v for p, v in json.load(open('summit2141_nu5_odd_A.json'))['bits'].items()}
arm, bitp, cands, fixed = S.build(5, 1, 'A')
prob = WProblem([arm], bitp, [cands], [fixed])
prob.init_marginal(); prob.build_sigma()
for p in sorted(sol): prob.set_bit(p, sol[p])
r0, eps0 = arm.residual()
print(f"solution: residual {r0:.3e}  eps {eps0.real:+.6f}{eps0.imag:+.6f}i")
print("N-scan:", end="")
for mult in (0.9, 0.95, 1.0, 1.05, 1.1):
    aw = Arm(2141.0*mult, 1, X=arm.X); aw.set_a(arm.a)
    rw, _ = aw.residual()
    print(f"  {mult}: {rw:.3e}", end="")
print()
for seed in (1, 2, 3):
    rng = np.random.default_rng([2141, seed])
    stx = dict(sol)
    ks = sorted(sol)
    for p in rng.choice(ks, size=len(ks)//10, replace=False):
        stx[int(p)] = -stx[int(p)]
    p2 = WProblem([S.build(5, 1, 'A')[0]], bitp, [cands], [fixed])
    p2.init_marginal(); p2.build_sigma()
    for p in sorted(stx): p2.set_bit(p, stx[p])
    rs, _ = p2.arms[0].residual()
    print(f"NEG scramble10% s{seed}: {rs:.3e}", end="  ")
print()
# Gauss-sum lock: tau(nu) exact, nu = zeta5^{ind_2(a) mod 5} mod 2141
mp.mp.dps = 40
P = 2141
dlog = {}; x = 1
for k in range(P-1):
    dlog[x] = k % 5; x = (x*2) % P
Z5 = mp.e**(2j*mp.pi/5)
tau = sum((Z5**dlog[a]) * mp.e**(2j*mp.pi*a/P) for a in range(1, P))
print(f"|tau|/sqrt(P) = {mp.nstr(abs(tau)/mp.sqrt(P), 10)}")
eps = mp.mpc(eps0.real, eps0.imag); eps = eps/abs(eps)
Z10 = mp.e**(1j*mp.pi/5)
best = []
for s, tk in (('chi', tau), ('chibar', mp.conj(tau))):
    for c_lab, c in (('+1',1), ('-1',-1), ('+i',1j), ('-i',-1j)):
        u = eps*mp.sqrt(P)/(c*tk)
        d, k = min((abs(u - Z10**k), k) for k in range(10))
        best.append((float(d), s, c_lab, k))
best.sort()
for d, s, c_lab, k in best[:3]:
    print(f"lock: tau({s}), c={c_lab}: u -> zeta10^{k}  distance {d:.3e}")
