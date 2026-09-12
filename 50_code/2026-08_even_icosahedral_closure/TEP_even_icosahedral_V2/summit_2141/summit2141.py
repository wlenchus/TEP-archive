#!/usr/bin/env python3
"""Second-summit decode, Doud-2141: 8 cells = nu-order {5,10} x port {even,odd} x orientation {A,B},
base-only S2 beam-128 per the qualified recipe. Usage: python3 summit2141.py <cellindex 0-7>"""
import numpy as np, json, sys
sys.path.insert(0, '.')
from instr2 import Arm, Xof, TGRID, inv_series, primes_upto, _fold
from qualify4 import WProblem

PHI = (1+np.sqrt(5))/2
N = 2141.0
cls = {}
for line in open('classesX_2141.txt'):
    p, c = line.strip().split(':'); cls[int(p)] = int(c)
jl = {}
for line in open('chilog_2141.txt'):
    p, j = line.strip().split(':'); jl[int(p)] = int(j)

def build(order, port, orient):
    """order in (5,10); orient 'A': m(3)=1/phi,m(4)=phi; 'B': swapped."""
    MT = {0: 2.0, 1: 0.0, 2: 1.0}
    MT[3], MT[4] = (1/PHI, PHI) if orient == 'A' else (PHI, 1/PHI)
    def theta_p(p):
        j = jl.get(p)
        if j is None: return None
        return np.exp(1j*np.pi*(j % 5)/5) if order == 5 else np.exp(1j*np.pi*j/10)
    arm = Arm(N, port)
    X = arm.X
    bitp = [p for p in sorted(cls) if p <= X and p != 2141 and cls[p] in (0, 2, 3, 4) and p in jl]
    cands = {}
    for p in bitp:
        th = theta_p(p); m = MT[cls[p]]; ch = th*th
        cands[p] = ([1.0, -th*m, ch], [1.0, th*m, ch])
    def fixed(p):
        c = cls.get(p); th = theta_p(p)
        if c is None or th is None or p == 2141: return None
        if c == 1: return [1.0, 0.0, th*th]
        return None
    return arm, bitp, cands, fixed

CELLS = [(o, pt, orn) for o in (5, 10) for pt in (0, 1) for orn in ('A', 'B')]
ci = int(sys.argv[1])
order, port, orient = CELLS[ci]
arm, bitp, cands, fixed = build(order, port, orient)
prob = WProblem([arm], bitp, [cands], [fixed])
prob.init_marginal(); prob.build_sigma()
w = prob.weights()
srt = sorted(bitp, key=lambda p: -w[p])
beam = [prob.snap(copy=True) + (prob.Jtot(),)]
for p in srt:
    cand = []
    for (st, arrs, sig, J) in beam:
        prob.load((st, arrs, sig), copy=False)
        for ss in (+1, -1):
            Jc, ds = prob.peek_set(p, ss)
            cand.append((Jc, st, arrs, sig, ss, ds))
    cand.sort(key=lambda c: c[0])
    nb = []
    for (Jc, st, arrs, sig, ss, ds) in cand[:128]:
        prob.load((st, arrs, sig), copy=True)
        prob.commit_set(p, ss, ds)
        nb.append(prob.snap(copy=False) + (Jc,))
    beam = nb
st, arrs, sig, J = min(beam, key=lambda b: b[3])
prob.load((st, arrs, sig), copy=True)
for _ in range(8):
    improved = False
    Jnow = prob.Jtot()
    for p in srt:
        s = prob.state[p]
        Jf, dsf = prob.peek_set(p, -s)
        if Jf < Jnow:
            prob.commit_set(p, -s, dsf); Jnow = Jf; improved = True
    if not improved: break
r, eps = arm.residual()
tag = f"nu{order}_{'even' if port==0 else 'odd'}_{orient}"
print(f"CELL {tag}: bits {len(bitp)}  residual {r:.3e}  eps {eps.real:+.5f}{eps.imag:+.5f}i")
json.dump({'cell': tag, 'residual': r, 'eps': [eps.real, eps.imag],
           'bits': {str(p): int(prob.state[p]) for p in bitp}}, open(f'summit2141_{tag}.json', 'w'))
