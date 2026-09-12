#!/usr/bin/env python3
"""Consensus completion for 2141 winner: (1) hold-out re-decode on the disjoint grid; (2) S5b."""
import numpy as np, json, sys
sys.path.insert(0, '.')
import instr2
TG2 = np.sort(np.array([0.55, 1/0.55, 0.62, 1/0.62, 0.71, 1/0.71, 0.82, 1/0.82, 0.95, 1/0.95]))
import s2141lib as S
from qualify4 import WProblem
from instr2 import Arm

sol = {int(p): v for p, v in json.load(open('summit2141_nu5_odd_A.json'))['bits'].items()}

def beam_decode(tgrid, s5=False):
    arm, bitp, cands, fixed = S.build(5, 1, 'A')
    if tgrid is not None:
        arm = Arm(2141.0, 1, tgrid=tgrid)
    prob = WProblem([arm], bitp, [cands], [fixed])
    prob.init_marginal(); prob.build_sigma()
    w = prob.weights()
    order = sorted(bitp, key=lambda p: -w[p])
    if not s5:
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
    else:
        heavy, rest = order[:8], order[8:]
        base_sn = prob.snap(copy=True)
        leaves = []
        for leaf in range(256):
            prob.load(base_sn, copy=True)
            for i, p in enumerate(heavy):
                prob.set_bit(p, +1 if (leaf >> i) & 1 else -1)
            W = 16
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
            leaves.append((J, dict(st)))
        leaves.sort(key=lambda x: x[0])
        prob.load(base_sn, copy=True)
        for p in order:
            prob.set_bit(p, leaves[0][1][p])
        print(f"  S5b best/runner J: {leaves[0][0]:.3e} / {leaves[1][0]:.3e}")
    for _ in range(8):
        improved = False
        Jnow = prob.Jtot()
        for p in order:
            s = prob.state[p]
            Jf, dsf = prob.peek_set(p, -s)
            if Jf < Jnow:
                prob.commit_set(p, -s, dsf); Jnow = Jf; improved = True
        if not improved: break
    r, eps = prob.arms[0].residual()
    return dict(prob.state), r, eps

st_h, r_h, eps_h = beam_decode(TG2)
d_h = [p for p in sol if st_h[p] != sol[p]]
print(f"HOLD-OUT (disjoint grid): residual {r_h:.3e}  eps {eps_h.real:+.5f}{eps_h.imag:+.5f}i  disagreements: {len(d_h)} {d_h[:6]}")
st_5, r_5, eps_5 = beam_decode(None, s5=True)
d_5 = [p for p in sol if st_5[p] != sol[p]]
print(f"S5b: residual {r_5:.3e}  disagreements: {len(d_5)} {d_5[:6]}")
json.dump({'holdout_residual': r_h, 'holdout_disagr': d_h, 's5b_residual': r_5, 's5b_disagr': d_5},
          open('consensus2141.json', 'w'))
