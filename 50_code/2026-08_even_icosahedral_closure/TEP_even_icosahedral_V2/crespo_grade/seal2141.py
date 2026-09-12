#!/usr/bin/env python3
import numpy as np, json, sys
sys.path.insert(0, '.')
from instr2 import Arm, TGRID, inv_series, primes_upto, _fold
PHI = (1+np.sqrt(5))/2
MT = {0: 2.0, 1: 0.0, 2: 1.0, 3: 1/PHI, 4: PHI}   # orientation A (2141's winner)
sig = {}
for line in open('crespo_signs_2141.txt'):
    p, m, s = line.strip().split(':'); sig[int(p)] = (int(m), int(s))
cls = {}
for line in open('classesX_2141.txt'):
    p, c = line.strip().split(':'); cls[int(p)] = int(c)
jl = {}
for line in open('chilog_2141.txt'):
    p, j = line.strip().split(':'); jl[int(p)] = int(j)
comm = {int(p): v for p, v in json.load(open('summit2141_nu5_odd_A.json'))['bits'].items()}
def kron24(p):
    r = pow((-24) % p, (p-1)//2, p) if p not in (2, 3) else 0
    return 1 if r == 1 else -1
def constr_sign(p):
    m, sq = sig[p]; lab = cls[p]
    if lab == 0: return +1 if sq == 1 else -1
    if lab == 2: return -1 if sq == 1 else +1
    if lab == 3: return +1 if sq == 1 else -1
    if lab == 4: return -1 if sq == 1 else +1
    return None
Z10 = np.exp(1j*np.pi/5)
arm = Arm(2141.0, 1, tgrid=TGRID)
X = arm.X
def build(b2, b43):
    a = np.zeros(X+1, dtype=complex); a[1] = 1.0
    for p in primes_upto(X):
        c = cls.get(p); j5 = None if p not in jl else jl[p] % 5
        if c is None or j5 is None or p == 2141: continue
        kmax = int(np.log(X)/np.log(p))
        th = Z10**j5; ch = th*th
        if c == 1:
            poly = [1.0, 0.0, ch]
        else:
            if p == 2: bn = b2
            elif p == 43: bn = b43
            elif p in sig and constr_sign(p) is not None:
                bn = constr_sign(p) * kron24(p) * (-1)**(j5 % 2)
            else:
                return None
            poly = [1.0, -bn*th*MT[c], ch]
        a = _fold(a, p, inv_series(np.asarray(poly, dtype=complex), kmax), X)
    return a
print("FE certificate of CONSTRUCTED 2141 coefficients (4-way scan of p=2,43):")
for b2 in (+1, -1):
    for b43 in (+1, -1):
        arm.set_a(build(b2, b43))
        r, eps = arm.residual()
        mark = " <== committed values" if (b2 == comm[2] and b43 == comm[43]) else ""
        print(f"  b2={b2:+d} b43={b43:+d}: residual {r:.3e}{mark}")
