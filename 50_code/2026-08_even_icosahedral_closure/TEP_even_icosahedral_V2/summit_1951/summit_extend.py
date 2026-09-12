#!/usr/bin/env python3
"""Extended decode: freeze the 67 consensus base bits; decode mid-band (517 < p <= 6723) through the
whitened enriched arms band-by-band (S2); u-lock at p=1951; per-arm (twist-battery) residuals + eps_d."""
import numpy as np, json, sys
sys.path.insert(0, '.')
import qualify4
from summit import build_summit, cert_arm_for, add_u_sigma, u_lock, bands_of, TW
from qualify4 import WProblem, inband_S2
from instr2 import Problem

CELL, GS = 1, True
arms, bitp, cands, fixed, data = build_summit(CELL, goldenswap=GS)
sol = {int(p): v for p, v in json.load(open('summit_base_oddGS.json'))['bits'].items()}
prob = WProblem(arms, bitp, cands, fixed)
prob.init_marginal(); prob.build_sigma()
add_u_sigma(prob, data[2])
# freeze base bits at consensus
X0 = arms[0].X
for p in sorted(sol):
    prob.set_bit(p, sol[p])
bands = bands_of(arms, [p for p in bitp if p > X0])
print(f"extended decode: {sum(len(b) for b in bands)} mid-band bits in {len(bands)} bands", flush=True)
qualify4.ORDER_JITTER = None
for ps in range(3):
    for band in bands:
        inband_S2(prob, band, log=print)
    print(f"  pass {ps+1}: J = {prob.Jtot():.3e}", flush=True)
k10, uscores, usep = u_lock(prob, data[2])
# final polish over mid-band only (base bits stay frozen at committed consensus)
w = prob.weights()
mid = [p for p in bitp if p > X0]
order = sorted(mid, key=lambda p: -w[p])
for _ in range(6):
    improved = False
    Jnow = prob.Jtot()
    for p in order:
        s = prob.state[p]
        if s == 0: continue
        Jf, dsf = prob.peek_set(p, -s)
        if Jf < Jnow:
            prob.commit_set(p, -s, dsf); Jnow = Jf; improved = True
    if not improved: break
print(f"u-lock: u = zeta10^{k10}   scores: " + " ".join(f"{s:.2e}" for s in uscores))
print(f"separation: runner-up/best = {sorted(uscores)[1]/sorted(uscores)[0]:.2f}")
armtab = {}
for arm in prob.arms:
    r, e = arm.residual()
    armtab[arm.label] = [r, e.real, e.imag]
    print(f"  arm {arm.label:6s} N={int(arm.N):>7d} port {arm.port}: residual {r:.3e}  eps_d {e.real:+.5f}{e.imag:+.5f}i")
json.dump({'u_zeta10_pow': int(k10), 'u_scores': [float(s) for s in uscores], 'arm_residuals': armtab,
           'mid_bits': {str(p): int(prob.state[p]) for p in sorted(mid)}},
          open('summit_extended.json', 'w'), indent=1)
