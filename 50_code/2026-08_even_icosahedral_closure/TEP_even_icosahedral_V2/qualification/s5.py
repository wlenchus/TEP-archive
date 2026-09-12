#!/usr/bin/env python3
"""S5 — exhaustive heavy-prefix list decoder (family addition under R1.w; no bar change).
Stage 1: enumerate all 2^8 assignments of the 8 heaviest bits; whitened SC tail (no polish) each;
Stage 2: full SC + polish on the 16 best by stage-1 J; winner = minimal final J. No truth used.
Usage: python3 s5.py <D> <lo> <hi>   (leaf range chunking; state in s5_ckpt_<D>.json)"""
import numpy as np, json, sys, os, time
sys.path.insert(0, '.')
from qualify2 import build, cert_metrics, FACP, FACN
from qualify4 import WProblem
from instr2 import Problem, Arm, TGRID, sensitivity

def sc_tail(prob, rest, polish_sweeps=2):
    for p in rest:
        JP, dsP = prob.peek_set(p, +1)
        JM, dsM = prob.peek_set(p, -1)
        prob.commit_set(p, +1 if JP <= JM else -1, dsP if JP <= JM else dsM)
    for _ in range(polish_sweeps):
        improved = False
        Jnow = prob.Jtot()
        for p in rest:
            s = prob.state[p]
            Jf, dsf = prob.peek_set(p, -s)
            if Jf < Jnow:
                prob.commit_set(p, -s, dsf); Jnow = Jf; improved = True
        if not improved:
            break
    return prob.Jtot()

def main(D, lo, hi):
    t0 = time.time()
    arms, bitp, truth, cands, fixed, cls = build(D)
    prob = WProblem(arms, bitp, cands, fixed)
    prob.init_marginal(); prob.build_sigma()
    w = prob.weights()
    order = sorted(bitp, key=lambda p: -w[p])
    heavy = order[:8]; rest = order[8:]
    base = prob.snap(copy=True)
    ck = f's5_ckpt_{D}.json'
    state = json.load(open(ck)) if os.path.exists(ck) else {'leaves': {}}
    for leaf in range(lo, hi):
        if str(leaf) in state['leaves']:
            continue
        prob.load(base, copy=True)
        for i, p in enumerate(heavy):
            prob.set_bit(p, +1 if (leaf >> i) & 1 else -1)
        J = sc_tail(prob, rest, polish_sweeps=2)
        state['leaves'][str(leaf)] = {'J': J, 'bits': {str(p): int(prob.state[p]) for p in bitp}}
        if leaf % 16 == 0:
            json.dump(state, open(ck, 'w'))
            print(f"  leaf {leaf}: J {J:.3e}  [{time.time()-t0:.0f}s]", flush=True)
    json.dump(state, open(ck, 'w'))
    if len(state['leaves']) == 256:
        ranked = sorted(state['leaves'].items(), key=lambda kv: kv[1]['J'])
        print("stage-1 complete. best 5 leaves:", [(k, f"{v['J']:.3e}") for k, v in ranked[:5]], flush=True)
        # stage 2: full SC+polish on best 16
        best = None
        for k, v in ranked[:16]:
            leaf = int(k)
            prob.load(base, copy=True)
            for i, p in enumerate(heavy):
                prob.set_bit(p, +1 if (leaf >> i) & 1 else -1)
            J = sc_tail(prob, rest, polish_sweeps=8)
            if best is None or J < best[1]:
                best = (dict(prob.state), J, leaf)
        st, J, leaf = best
        drift = prob.resieve_gate() if prob.state == st else 0.0
        carm, r, eps, gdev = cert_metrics(D, st, cls, 3.2e-15)
        certbits = [p for p in bitp if p <= carm.X]
        certprob = Problem([carm], certbits, [{p: (FACP, FACN) for p in certbits}], [lambda p: None])
        certprob.state = {p: st.get(p, 0) for p in certbits}
        s, vis = sensitivity(certprob, 3.2e-15)
        vp = sorted(vis.keys())
        wrong_vis = [p for p in vp if st.get(p, 0) != truth[p]]
        acc_all = sum(1 for p in bitp if st.get(p, 0) == truth[p]) / len(bitp)
        acc_vis = (len(vp) - len(wrong_vis)) / len(vp) if vp else float('nan')
        print(f"S5/R1.w: winning leaf {leaf}  J {J:.3e}  cert-residual {r:.3e}  eps {eps:.4f}  "
              f"acc(all) {acc_all*100:.1f}%  acc(visible) {acc_vis*100:.1f}% ({len(vp)} visible, wrong: {wrong_vis})", flush=True)
        out = {'D': D, 'which': 'S5/R1.w', 'leaf': leaf, 'J': J, 'cert_residual': r,
               'eps': [eps.real, eps.imag], 'acc_all': acc_all, 'acc_vis': acc_vis,
               'n_visible': len(vp), 'wrong_visible': wrong_vis,
               'bits': {str(p): int(st.get(p, 0)) for p in bitp}}
        json.dump(out, open(f'qualify5_{D}_S5.json', 'w'), indent=1)

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
