#!/usr/bin/env python3
"""S5 with beam-16 tails (family: exhaustive heavy-8 prefix enumeration; tail solver strengthened
greedy->beam16 after summit golden-gap bits broke SC tails; logged, no bar change)."""
import numpy as np, json, sys, os
sys.path.insert(0, '.')
from summit import build_summit, cert_arm_for
from qualify4 import WProblem
from instr2 import Problem

CELL, GS = 1, True
arms, bitp, cands, fixed, data = build_summit(CELL, goldenswap=GS)
arm0 = arms[0]
bp = [p for p in bitp if p <= arm0.X]
prob = WProblem([arm0], list(bp), [{p: cands[0][p] for p in bp}], [fixed[0]])
prob.init_marginal(); prob.build_sigma()
w = prob.weights()
order = sorted(bp, key=lambda p: -w[p])
heavy, rest = order[:8], order[8:]
base_sn = prob.snap(copy=True)

def beamtail(W=16):
    beam = [prob.snap(copy=True) + (prob.Jtot(),)]
    for p in rest:
        cand = []
        for (st, arrs, sig, J) in beam:
            prob.load((st, arrs, sig), copy=False)
            for ss in (+1, -1):
                Jc, ds = prob.peek_set(p, ss)
                cand.append((Jc, st, arrs, sig, ss, ds))
        cand.sort(key=lambda c: c[0])
        nb = []
        for (Jc, st, arrs, sig, ss, ds) in cand[:W]:
            prob.load((st, arrs, sig), copy=True)
            prob.commit_set(p, ss, ds)
            nb.append(prob.snap(copy=False) + (Jc,))
        beam = nb
    st, arrs, sig, J = min(beam, key=lambda b: b[3])
    prob.load((st, arrs, sig), copy=True)
    return J

lo, hi = int(sys.argv[1]), int(sys.argv[2])
ck = 's5b_ckpt.json'
state = json.load(open(ck)) if os.path.exists(ck) else {}
for leaf in range(lo, hi):
    if str(leaf) in state:
        continue
    prob.load(base_sn, copy=True)
    for i, p in enumerate(heavy):
        prob.set_bit(p, +1 if (leaf >> i) & 1 else -1)
    J = beamtail()
    state[str(leaf)] = {'J': J, 'bits': {str(p): int(prob.state[p]) for p in bp}}
    if leaf % 32 == 0:
        json.dump(state, open(ck, 'w'))
        print(f"  leaf {leaf}: J {J:.3e}", flush=True)
json.dump(state, open(ck, 'w'))
if len(state) == 256:
    ranked = sorted(state.items(), key=lambda kv: kv[1]['J'])
    Jb = ranked[0][1]['J']; Jr = ranked[1][1]['J']
    stb = {int(p): v for p, v in ranked[0][1]['bits'].items()}
    # polish winner
    prob.load(base_sn, copy=True)
    for p in order:
        prob.set_bit(p, stb[p])
    for _ in range(8):
        improved = False
        Jnow = prob.Jtot()
        for p in order:
            s = prob.state[p]
            Jf, dsf = prob.peek_set(p, -s)
            if Jf < Jnow:
                prob.commit_set(p, -s, dsf); Jnow = Jf; improved = True
        if not improved:
            break
    st = dict(prob.state)
    carm = cert_arm_for(CELL, st, data, goldenswap=GS)
    r, eps = carm.residual()
    print(f"S5b winner leaf {ranked[0][0]}: J {prob.Jtot():.3e} (runner-up {Jr:.3e})  "
          f"cert-residual {r:.3e}  eps {eps.real:+.6f}{eps.imag:+.6f}i", flush=True)
    json.dump({'bits': {str(p): int(st[p]) for p in bp}, 'residual': r,
               'eps': [eps.real, eps.imag]}, open('summit_S5b.json', 'w'), indent=1)
