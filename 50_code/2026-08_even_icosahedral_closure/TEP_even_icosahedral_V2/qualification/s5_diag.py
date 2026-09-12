#!/usr/bin/env python3
"""Diagnostic: freeze top-k heavy bits at TRUE values, SC-decode the rest (whitened).
Purely a landscape probe — no qualifying run uses truth."""
import numpy as np, sys
sys.path.insert(0, '.')
from qualify2 import build, cert_metrics, FACP, FACN
from qualify4 import WProblem, inband_S1
from instr2 import Problem, Arm, TGRID, sensitivity

D = 2089
for K in (8, 12, 16):
    arms, bitp, truth, cands, fixed, cls = build(D)
    prob = WProblem(arms, bitp, cands, fixed)
    prob.init_marginal(); prob.build_sigma()
    w = prob.weights()
    order = sorted(bitp, key=lambda p: -w[p])
    heavy = order[:K]
    for p in heavy:
        prob.set_bit(p, truth[p])
    rest = order[K:]
    # SC over rest in weight order + polish
    for p in rest:
        JP, dsP = prob.peek_set(p, +1)
        JM, dsM = prob.peek_set(p, -1)
        prob.commit_set(p, +1 if JP <= JM else -1, dsP if JP <= JM else dsM)
    for _ in range(8):
        improved = False
        Jnow = prob.Jtot()
        for p in rest:
            s = prob.state[p]
            Jf, dsf = prob.peek_set(p, -s)
            if Jf < Jnow:
                prob.commit_set(p, -s, dsf); Jnow = Jf; improved = True
        if not improved:
            break
    st = dict(prob.state)
    carm, r, eps, gdev = cert_metrics(D, st, cls, 3.2e-15)
    certbits = [p for p in bitp if p <= carm.X]
    certprob = Problem([carm], certbits, [{p: (FACP, FACN) for p in certbits}], [lambda p: None])
    certprob.state = {p: st.get(p, 0) for p in certbits}
    s, vis = sensitivity(certprob, 3.2e-15)
    vp = sorted(vis.keys())
    wrong_vis = [p for p in vp if st.get(p, 0) != truth[p]]
    acc_all = sum(1 for p in bitp if st.get(p, 0) == truth[p]) / len(bitp)
    print(f"K={K}: cert-residual {r:.3e}  acc(all) {acc_all*100:.1f}%  visible wrong: {wrong_vis} of {len(vp)}")
