#!/usr/bin/env python3
"""Consensus on the winning cell (odd port, orientation B): S2ord7-base and S5-base (S2-base done).
Then sensitivity/visible set on the certification arm."""
import numpy as np, json, sys
sys.path.insert(0, '.')
import qualify4
from summit import build_summit, cert_arm_for
from qualify4 import WProblem, inband_S2
from instr2 import Problem, sensitivity

CELL, GS = 1, True
arms, bitp, cands, fixed, data = build_summit(CELL, goldenswap=GS)
arm0 = arms[0]
bp = [p for p in bitp if p <= arm0.X]

def mkprob():
    prob = WProblem([arm0], list(bp), [{p: cands[0][p] for p in bp}], [fixed[0]])
    prob.init_marginal(); prob.build_sigma()
    return prob

def beamsolve(prob, W=128, jitter=None):
    w = prob.weights()
    if jitter is not None:
        rng = np.random.default_rng(jitter)
        order = sorted(bp, key=lambda p: -w[p] * (1 + 0.15 * rng.standard_normal()))
    else:
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
        for (Jc, st, arrs, sig, ss, ds) in cand[:W]:
            prob.load((st, arrs, sig), copy=True)
            prob.commit_set(p, ss, ds)
            nb.append(prob.snap(copy=False) + (Jc,))
        beam = nb
    st, arrs, sig, J = min(beam, key=lambda b: b[3])
    prob.load((st, arrs, sig), copy=True)
    polish(prob, order)
    return dict(prob.state)

def polish(prob, order):
    for _ in range(8):
        improved = False
        Jnow = prob.Jtot()
        for p in order:
            s = prob.state[p]
            if s == 0: continue
            Jf, dsf = prob.peek_set(p, -s)
            if Jf < Jnow:
                prob.commit_set(p, -s, dsf); Jnow = Jf; improved = True
        if not improved: break

def s5solve(prob):
    w = prob.weights()
    order = sorted(bp, key=lambda p: -w[p])
    heavy, rest = order[:8], order[8:]
    base_sn = prob.snap(copy=True)
    leaves = []
    for leaf in range(256):
        prob.load(base_sn, copy=True)
        for i, p in enumerate(heavy):
            prob.set_bit(p, +1 if (leaf >> i) & 1 else -1)
        for p in rest:
            JP, dsP = prob.peek_set(p, +1)
            JM, dsM = prob.peek_set(p, -1)
            prob.commit_set(p, +1 if JP <= JM else -1, dsP if JP <= JM else dsM)
        polish(prob, rest)
        leaves.append((prob.Jtot(), dict(prob.state)))
    leaves.sort(key=lambda x: x[0])
    prob.load(base_sn, copy=True)
    for p in order:
        prob.set_bit(p, leaves[0][1][p])
    polish(prob, order)
    print(f"  S5 best/runner-up J: {leaves[0][0]:.3e} / {leaves[1][0]:.3e}")
    return dict(prob.state)

s2 = json.load(open('summit_base_oddGS.json'))['bits']
s2 = {int(p): v for p, v in s2.items()}
st_ord = beamsolve(mkprob(), jitter=7)
st_s5 = s5solve(mkprob())
runs = {'S2': s2, 'S2ord7': st_ord, 'S5': st_s5}
for name, st in runs.items():
    carm = cert_arm_for(CELL, st, data, goldenswap=GS)
    r, eps = carm.residual()
    print(f"{name}: cert-residual {r:.3e}  eps {eps.real:+.6f}{eps.imag:+.6f}i")
# sensitivity/visible on S2's solution
carm = cert_arm_for(CELL, s2, data, goldenswap=GS)
FACS = {p: cands[0][p] for p in bp}
class CP(Problem):
    pass
certprob = Problem([carm], list(bp), [FACS], [lambda p: None])
certprob.state = {p: s2.get(p, 0) for p in bp}
s, vis = sensitivity(certprob, 5e-15)
vp = sorted(vis.keys())
agree_vis = all(all(runs[a][p] == runs[b][p] for p in vp) for a in runs for b in runs)
agree_all = sum(1 for p in bp if len(set(r[p] for r in runs.values())) == 1)
print(f"visible bits: {len(vp)} / {len(bp)}   consensus on visible set: {agree_vis}   full-set agreement: {agree_all}/{len(bp)}")
json.dump({'visible': [int(p) for p in vp], 'sens': {str(p): s[p] for p in bp},
           'S2ord7': {str(p): st_ord[p] for p in bp}, 'S5': {str(p): st_s5[p] for p in bp},
           'consensus_visible': bool(agree_vis)}, open('summit_consensus.json', 'w'), indent=1)
