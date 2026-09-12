#!/usr/bin/env python3
"""Verification avenue 4: no-1-flip-repair certificate. For each visible bit: flip it, freeze it,
greedy re-optimize ALL other bits, record the best achievable residual. If any flipped-bit state
can be repaired back to floor, the solution is not locally unique."""
import numpy as np, json, sys
sys.path.insert(0, '.')
from summit import build_summit, cert_arm_for
from qualify4 import WProblem

CELL, GS = 1, True
arms, bitp, cands, fixed, data = build_summit(CELL, goldenswap=GS)
arm0 = arms[0]
bp = [p for p in bitp if p <= arm0.X]
sol = {int(p): v for p, v in json.load(open('summit_base_oddGS.json'))['bits'].items()}
sens = {int(p): v for p, v in json.load(open('summit_consensus.json'))['sens'].items()}
vis = sorted([p for p in bp if sens[p] > 100*5e-15])

prob = WProblem([arm0], list(bp), [{p: cands[0][p] for p in bp}], [fixed[0]])
prob.init_marginal(); prob.build_sigma()
for p in sorted(sol):
    prob.set_bit(p, sol[p])
base_sn = prob.snap(copy=True)
J0 = prob.Jtot()
worst = None; repaired = []
for pf in vis:
    prob.load(base_sn, copy=True)
    prob.set_bit(pf, -sol[pf])
    # greedy repair over all OTHER bits to convergence
    for _ in range(12):
        improved = False
        Jnow = prob.Jtot()
        for p in bp:
            if p == pf:
                continue
            s = prob.state[p]
            Jf, dsf = prob.peek_set(p, -s)
            if Jf < Jnow:
                prob.commit_set(p, -s, dsf); Jnow = Jf; improved = True
        if not improved:
            break
    carm = cert_arm_for(CELL, dict(prob.state), data, goldenswap=GS)
    r, _ = carm.residual()
    if r < 1e-11:
        repaired.append((pf, r))
    if worst is None or r < worst[1]:
        worst = (pf, r)
print(f"NO-1-FLIP-REPAIR: {len(vis)} visible bits each flipped+frozen, all others re-optimized:")
print(f"  states repaired back to <=1e-11: {len(repaired)} {repaired}")
print(f"  best repair achieved (i.e. the most dangerous flip): p={worst[0]}, residual {worst[1]:.3e}")
print(f"  solution residual for reference: 8.957e-15  => minimum gap {worst[1]/8.957e-15:.1e}x")
