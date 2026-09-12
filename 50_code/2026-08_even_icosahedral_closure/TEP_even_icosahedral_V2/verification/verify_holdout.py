#!/usr/bin/env python3
"""Verification avenue 2: hold-out re-decode. Fresh S2-base beam-128 decode of the winning cell
using a DISJOINT involution-closed t-grid (no point shared with the pre-registered TGRID).
If the 67 bits are constraint-driven (not grid artifacts), the identical vector must emerge."""
import numpy as np, json, sys
sys.path.insert(0, '.')
import instr2
# disjoint grid, involution-closed: pairs (t, 1/t), no 1.0, nothing from TGRID
TG2 = np.sort(np.array([0.55, 1/0.55, 0.62, 1/0.62, 0.71, 1/0.71, 0.82, 1/0.82, 0.95, 1/0.95]))
instr2.TGRID = TG2   # decoder + certification both on the held-out grid
from summit import build_summit, cert_arm_for
from qualify4 import WProblem

CELL, GS = 1, True
arms, bitp, cands, fixed, data = build_summit(CELL, goldenswap=GS)
arm0 = arms[0]
bp = [p for p in bitp if p <= arm0.X]
prob = WProblem([arm0], list(bp), [{p: cands[0][p] for p in bp}], [fixed[0]])
prob.init_marginal(); prob.build_sigma()
w = prob.weights()
order = sorted(bp, key=lambda p: -w[p])
beam = [prob.snap(copy=True) + (prob.Jtot(),)]
for p in order:
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
    for p in order:
        s = prob.state[p]
        Jf, dsf = prob.peek_set(p, -s)
        if Jf < Jnow:
            prob.commit_set(p, -s, dsf); Jnow = Jf; improved = True
    if not improved: break
carm = cert_arm_for(CELL, dict(prob.state), data, goldenswap=GS)
r, eps = carm.residual()
committed = {int(p): v for p, v in json.load(open('summit_base_oddGS.json'))['bits'].items()}
diff = [p for p in bp if prob.state[p] != committed[p]]
sens = {int(p): v for p, v in json.load(open('summit_consensus.json'))['sens'].items()}
vis = [p for p in bp if sens[p] > 100*5e-15]
dvis = [p for p in diff if p in vis]
print(f"HOLD-OUT RE-DECODE (disjoint 10-pt grid [0.55..1.82]):")
print(f"  residual on held-out grid: {r:.3e}   eps {eps.real:+.6f}{eps.imag:+.6f}i")
print(f"  bit agreement with committed vector: {len(bp)-len(diff)}/{len(bp)} all, visible disagreements: {dvis}")
print(f"  (committed eps was +0.885096-0.465408i)")
