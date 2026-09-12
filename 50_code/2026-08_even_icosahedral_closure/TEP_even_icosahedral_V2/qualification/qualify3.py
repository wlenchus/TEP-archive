#!/usr/bin/env python3
"""GATE-M under AMENDMENT R1: staged band decoding, all three families, twist-enriched arms.
Usage: python3 qualify3.py <D> <S1|S2|S3>"""
import numpy as np, json, sys, time
sys.path.insert(0, '.')
from qualify2 import build, MultiProblem, cert_metrics, TW, FACP, FACN
from instr2 import Arm, Problem, Xof, TGRID, sensitivity

def band_edges(arms):
    xs = sorted(set(a.X for a in arms))
    return xs

def inband_S1(prob, band, log):
    w = prob.weights()
    order = [p for p in sorted(band, key=lambda p: -w[p])]
    for p in order:
        JP, dsP = prob.peek_set(p, +1)
        JM, dsM = prob.peek_set(p, -1)
        if JP <= JM:
            prob.commit_set(p, +1, dsP)
        else:
            prob.commit_set(p, -1, dsM)
    # in-band greedy polish
    for _ in range(6):
        improved = False
        Jnow = prob.Jtot()
        for p in order:
            s = prob.state[p]
            Jf, dsf = prob.peek_set(p, -s)
            if Jf < Jnow:
                prob.commit_set(p, -s, dsf); Jnow = Jf; improved = True
        if not improved:
            break

def inband_S2(prob, band, log, width=64):
    w = prob.weights()
    order = [p for p in sorted(band, key=lambda p: -w[p])]
    beam = [prob.snap(copy=True) + (prob.Jtot(),)]
    for p in order:
        cand = []
        for (st, arrs, J) in beam:
            prob.load((st, arrs), copy=False)
            for ss in (+1, -1):
                Jc, ds = prob.peek_set(p, ss)
                cand.append((Jc, st, arrs, ss, ds))
        cand.sort(key=lambda c: c[0])
        newbeam = []
        for (Jc, st, arrs, ss, ds) in cand[:width]:
            prob.load((st, arrs), copy=True)
            prob.commit_set(p, ss, ds)
            newbeam.append(prob.snap(copy=False) + (Jc,))
        beam = newbeam
    st, arrs, J = min(beam, key=lambda b: b[2])
    prob.load((st, arrs), copy=True)

def inband_S3(prob, band, log, seeds=(20260803, 1951, 2089, 5), nchains=8, sweeps=2500):
    rng = np.random.default_rng(list(seeds) + [len(band)])
    w = prob.weights()
    order = [p for p in sorted(band, key=lambda p: -w[p])]
    if not order:
        return
    wv = np.array([np.sqrt(w[p]) + 1e-30 for p in order]); wv = wv / wv.sum()
    base = prob.snap(copy=True)
    chains = []
    for c in range(nchains):
        prob.load(base, copy=True)
        for p in order:
            prob.set_bit(p, int(rng.choice([-1, 1])))
        chains.append(list(prob.snap(copy=False)) + [prob.Jtot()])
    Jscale = np.median([c[2] for c in chains]) + 1e-30
    temps = np.geomspace(3e-2, 30.0, nchains) * Jscale
    best = None
    m = len(order)
    props = max(6, m // 3)
    for sw in range(sweeps):
        for c in range(nchains):
            st, arrs, J = chains[c]
            prob.load((st, arrs), copy=False)
            T = temps[c]
            for _ in range(props):
                p = order[int(rng.choice(m, p=wv))]
                s = prob.state[p]
                Jf, ds = prob.peek_set(p, -s)
                if Jf <= J or rng.random() < np.exp(-(Jf - J) / T):
                    prob.commit_set(p, -s, ds); J = Jf
            chains[c] = list(prob.snap(copy=False)) + [J]
            if best is None or J < best[1]:
                best = (dict(prob.state), J)
        if sw % 50 == 0 and sw > 0:
            for c in range(nchains - 1):
                J1, J2 = chains[c][2], chains[c + 1][2]
                d = (1.0 / temps[c] - 1.0 / temps[c + 1]) * (J1 - J2)
                if d > 0 or rng.random() < np.exp(d):
                    chains[c], chains[c + 1] = chains[c + 1], chains[c]
        if best[1] < prob.Jtot() * 0 + 1e-26:
            break
    # adopt best, greedy in-band polish
    prob.load(base, copy=True)
    for p in order:
        prob.set_bit(p, best[0][p])
    for _ in range(6):
        improved = False
        Jnow = prob.Jtot()
        for p in order:
            s = prob.state[p]
            Jf, dsf = prob.peek_set(p, -s)
            if Jf < Jnow:
                prob.commit_set(p, -s, dsf); Jnow = Jf; improved = True
        if not improved:
            break

def staged(D, which, npass=3):
    t0 = time.time()
    arms, bitp, truth, cands, fixed, cls = build(D)
    prob = MultiProblem(arms, bitp, cands, fixed)
    prob.init_marginal()
    edges = band_edges(arms)
    lo = 0
    bands = []
    for hi in edges:
        band = [p for p in bitp if lo < p <= hi]
        if band:
            bands.append((lo, hi, band))
        lo = hi
    print(f"== R1 staged {which} at D={D}: {len(arms)} arms, {len(bitp)} bits, bands: " +
          ", ".join(f"({a},{b}]:{len(c)}" for a, b, c in bands), flush=True)
    fn = {'S1': inband_S1, 'S2': inband_S2, 'S3': inband_S3}[which]
    for ps in range(npass):
        for (lo, hi, band) in bands:
            fn(prob, band, log=print)
        print(f"  pass {ps+1}: J = {prob.Jtot():.3e}", flush=True)
        if prob.Jtot() < 1e-24:
            break
    # global polish
    w = prob.weights()
    order = sorted(bitp, key=lambda p: -w[p])
    for _ in range(8):
        improved = False
        Jnow = prob.Jtot()
        for p in order:
            s = prob.state[p]
            if s == 0:
                continue
            Jf, dsf = prob.peek_set(p, -s)
            if Jf < Jnow:
                prob.commit_set(p, -s, dsf); Jnow = Jf; improved = True
        if not improved:
            break
    drift = prob.resieve_gate()
    st = dict(prob.state)
    carm, r, eps, gdev = cert_metrics(D, st, cls, 3.2e-15)
    certprob = Problem([carm], [p for p in bitp if p <= carm.X],
                       [{p: (FACP, FACN) for p in bitp if p <= carm.X}], [lambda p: None])
    certprob.state = {p: st.get(p, 0) for p in bitp if p <= carm.X}
    s, vis = sensitivity(certprob, 3.2e-15)
    vp = sorted(vis.keys())
    acc_all = sum(1 for p in bitp if st.get(p, 0) == truth[p]) / len(bitp)
    wrong_vis = [p for p in vp if st.get(p, 0) != truth[p]]
    acc_vis = (len(vp) - len(wrong_vis)) / len(vp) if vp else float('nan')
    und = sum(1 for p in bitp if st.get(p, 0) == 0)
    dt = time.time() - t0
    print(f"{which}/R1: J {prob.Jtot():.3e}  drift {drift:.1e}  cert-residual {r:.3e}  eps {eps:.4f}  "
          f"acc(all {len(bitp)}) {acc_all*100:.1f}%  acc(visible) {acc_vis*100:.1f}% "
          f"({len(vp)} visible, wrong: {wrong_vis})  undecided {und}  [{dt:.0f}s]", flush=True)
    out = {'D': D, 'which': which + '/R1', 'J': prob.Jtot(), 'cert_residual': r,
           'eps': [eps.real, eps.imag], 'meterdev': gdev, 'acc_all': acc_all, 'acc_vis': acc_vis,
           'n_visible': len(vp), 'wrong_visible': wrong_vis, 'undecided': und,
           'bits': {str(p): int(st.get(p, 0)) for p in bitp}, 'time_s': dt}
    json.dump(out, open(f'qualify3_{D}_{which}.json', 'w'), indent=1)
    return out

if __name__ == '__main__':
    staged(int(sys.argv[1]), sys.argv[2])
