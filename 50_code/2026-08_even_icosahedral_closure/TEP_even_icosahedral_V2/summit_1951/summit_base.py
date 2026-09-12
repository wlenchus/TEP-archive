#!/usr/bin/env python3
"""Base-only S2 beam triage on the summit: single clean arm (N=1951), no twist coupling.
All four cells: even/odd x goldenswap. Beam width 128 (single-arm affordable)."""
import numpy as np, json, sys
sys.path.insert(0, '.')
from summit import build_summit, cert_arm_for
from qualify4 import WProblem
from instr2 import Xof, TGRID

def run(cell, gs):
    arms, bitp, cands, fixed, data = build_summit(cell, goldenswap=gs)
    arm = arms[0]
    bp = [p for p in bitp if p <= arm.X]
    prob = WProblem([arm], [p for p in bp], [ {p: cands[0][p] for p in bp} ], [fixed[0]])
    prob.init_marginal(); prob.build_sigma()
    w = prob.weights()
    order = sorted(bp, key=lambda p: -w[p])
    beam = [prob.snap(copy=True) + (prob.Jtot(),)]
    W = 128
    for p in order:
        cand = []
        for (st, arrs, sig, J) in beam:
            prob.load((st, arrs, sig), copy=False)
            for ss in (+1, -1):
                Jc, ds = prob.peek_set(p, ss)
                cand.append((Jc, st, arrs, sig, ss, ds))
        cand.sort(key=lambda c: c[0])
        newbeam = []
        for (Jc, st, arrs, sig, ss, ds) in cand[:W]:
            prob.load((st, arrs, sig), copy=True)
            prob.commit_set(p, ss, ds)
            newbeam.append(prob.snap(copy=False) + (Jc,))
        beam = newbeam
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
        if not improved:
            break
    carm = cert_arm_for(cell, dict(prob.state), data, goldenswap=gs)
    r, eps = carm.residual()
    tag = ('even' if cell == 0 else 'odd') + ('GS' if gs else '')
    print(f"BASE-ONLY {tag}: bits {len(bp)}  cert-residual {r:.3e}  eps {eps.real:+.5f}{eps.imag:+.5f}i")
    json.dump({'cell': tag, 'residual': r, 'bits': {str(p): int(prob.state[p]) for p in bp}},
              open(f'summit_base_{tag}.json', 'w'))
    return r

for cell in (0, 1):
    for gs in (False, True):
        run(cell, gs)
