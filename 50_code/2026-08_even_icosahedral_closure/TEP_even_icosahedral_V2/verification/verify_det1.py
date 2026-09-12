#!/usr/bin/env python3
"""Verification avenue 3: the derived det-1 sibling rho0 = rho (x) chibar^3.
Traces a0_p = b_p * (-1)^{j(p)} * m_p are REAL; det = 1 (trivial nebentypus); N = 1951^2, a=0;
same parity (odd port). This FE at a different conductor was never used by any solver.
Coefficients: committed bits (p<=517) + provisional mid-band (517<p<=6723) + marginalized tail.
Prediction: real eps in {+1,-1}; residual at the marginal-tail floor (~1e-4); scrambles ~1e-1."""
import numpy as np, json, sys
sys.path.insert(0, '.')
from instr2 import Arm, Xof, TGRID, inv_series, primes_upto, _fold

PHI = (1 + np.sqrt(5)) / 2
MT = {0: 2.0, 1: 0.0, 2: 1.0, 3: PHI, 4: 1/PHI}
cls = {}
for line in open('../gp/classesX_doud1951.txt'):
    p, c = line.strip().split(':'); cls[int(p)] = int(c)
jl = {}
for line in open('chilog_1951.txt'):
    p, j = line.strip().split(':'); jl[int(p)] = int(j)
bits = {int(p): v for p, v in json.load(open('summit_base_oddGS.json'))['bits'].items()}
mid = {int(p): v for p, v in json.load(open('summit_extended.json'))['mid_bits'].items()}
allbits = dict(mid); allbits.update(bits)

N = 1951.0**2
X = Xof(N)
def build(state, scramble_seed=None):
    st = dict(state)
    if scramble_seed is not None:
        rng = np.random.default_rng(scramble_seed)
        ks = [p for p in st if p <= 517]
        for p in rng.choice(ks, size=len(ks)//10, replace=False):
            st[int(p)] = -st[int(p)]
    a = np.zeros(X+1, dtype=complex); a[1] = 1.0
    for p in primes_upto(X):
        c = cls.get(p); j = jl.get(p)
        if p == 1951 or c is None:
            continue   # 1951: local factor 1 (no fixed vector); beyond table: factor 1
        kmax = int(np.log(X)/np.log(p))
        if c == 1:
            inv = inv_series(np.asarray([1.0, 0.0, 1.0], dtype=complex), kmax)   # 2A: 1 + T^2
        elif p in st and st[p] != 0:
            a0 = st[p] * (-1)**(j % 2) * MT[c]
            inv = inv_series(np.asarray([1.0, -a0, 1.0], dtype=complex), kmax)
        else:
            iP = inv_series(np.asarray([1.0, -MT[c], 1.0], dtype=complex), kmax)
            iM = inv_series(np.asarray([1.0,  MT[c], 1.0], dtype=complex), kmax)
            inv = 0.5*(iP+iM)
        a = _fold(a, p, inv, X)
    return a

arm = Arm(N, 1, tgrid=TGRID)     # odd port, conductor 1951^2
arm.set_a(build(allbits))
r, eps = arm.residual()
print(f"DET-1 SIBLING FE (N=1951^2, real coefficients, odd port, never solver-touched):")
print(f"  residual {r:.3e}   fitted eps = {eps.real:+.6f}{eps.imag:+.6f}i   (prediction: real, +-1)")
arm.set_a(build(bits))           # committed-only variant (mid-band marginalized)
r2, eps2 = arm.residual()
print(f"  committed-only variant (mid-band marginalized): residual {r2:.3e}  eps {eps2.real:+.5f}{eps2.imag:+.5f}i")
for seed in (1, 2):
    arm.set_a(build(allbits, scramble_seed=seed))
    rs, _ = arm.residual()
    print(f"  NEG 10%-scramble of committed bits, seed {seed}: {rs:.3e}")
# wrong-conductor negative
armw = Arm(N*1.1, 1, X=X, tgrid=TGRID); armw.set_a(build(allbits)); rw, _ = armw.residual()
print(f"  NEG wrong-N*1.1: {rw:.3e}")
