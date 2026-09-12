#!/usr/bin/env python3
"""Bounded mid-band push: band-2 (517 < p <= 1552) with beam-128 through the whitened enriched arms,
committed base frozen; measure whether tw-3 (whose range this is) dives toward its floor."""
import numpy as np, json, sys
sys.path.insert(0, '.')
import qualify4
from summit import build_summit, add_u_sigma
from qualify4 import WProblem, inband_S2

CELL, GS = 1, True
arms, bitp, cands, fixed, data = build_summit(CELL, goldenswap=GS)
sol = {int(p): v for p, v in json.load(open('summit_base_oddGS.json'))['bits'].items()}
prob = WProblem(arms, bitp, cands, fixed)
prob.init_marginal(); prob.build_sigma()
add_u_sigma(prob, data[2])
for p in sorted(sol):
    prob.set_bit(p, sol[p])
band2 = [p for p in bitp if 517 < p <= 1552]
print(f"band-2 push: {len(band2)} bits, beam-128, 4 passes")
for ps in range(4):
    inband_S2(prob, band2, log=print, width=128)
    rt = {}
    for arm in prob.arms:
        r, e = arm.residual()
        rt[arm.label] = r
    print(f"  pass {ps+1}: tw-3 {rt['tw-3']:.3e}  tw-4 {rt['tw-4']:.3e}  tw5 {rt['tw5']:.3e}  base {rt['base']:.3e}", flush=True)
json.dump({str(p): int(prob.state[p]) for p in band2}, open('midband_band2.json', 'w'))
