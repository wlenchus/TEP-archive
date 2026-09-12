#!/usr/bin/env python3
"""S4 — soft coordinate relaxation (mean-field) decoder, added under AMENDMENT R1.w as a fourth
solver family (addition, no bar change). Bits carry lambda in [0,1] (P-weight); F is exactly
multilinear in the lambdas, so each coordinate has a closed-form whitened least-squares minimizer.
Sweeps in weight order to a fixed point; sigma^2 tracks residual softness sum lam(1-lam) v_p;
then round, hard greedy polish, resieve gate, certification.
Usage: python3 qualify5.py <D> [order_seed]"""
import numpy as np, json, sys, time
sys.path.insert(0, '.')
from qualify2 import build, MultiProblem, cert_metrics, TW, FACP, FACN
from instr2 import Arm, Problem, Xof, TGRID, sensitivity, inv_series

def mix_inv(P, M, lam, kmax):
    return lam * inv_series(np.asarray(P, dtype=complex), kmax) + (1 - lam) * inv_series(np.asarray(M, dtype=complex), kmax)

def q_between(P, M, lam_old, lam_new, kmax):
    io = mix_inv(P, M, lam_old, kmax); inw = mix_inv(P, M, lam_new, kmax)
    q = np.zeros(kmax + 1, dtype=complex); q[0] = 1.0
    for k in range(1, kmax + 1):
        s = inw[k]
        for j in range(1, k + 1):
            s -= io[j] * q[k - j]
        q[k] = s
    return q

def S4_soft(D, order_seed=0, max_sweeps=40):
    t0 = time.time()
    arms, bitp, truth, cands, fixed, cls = build(D)
    prob = MultiProblem(arms, bitp, cands, fixed)
    prob.init_marginal()
    lam = {p: 0.5 for p in bitp}
    # cache v_p rows per arm for sigma
    vmap = []
    for ai, arm in enumerate(prob.arms):
        vm = {}
        for p in prob.cands[ai]:
            kmax = int(np.log(arm.X) / np.log(p))
            qP = q_between(*prob.cands[ai][p], 0.5, 1.0, kmax)
            qM = q_between(*prob.cands[ai][p], 0.5, 0.0, kmax)
            _, _, dFP, dFiP = arm.delta_for(p, qP)
            _, _, dFM, dFiM = arm.delta_for(p, qM)
            vm[p] = (np.abs(dFiP - dFiM) ** 2 + arm.t ** 2 * np.abs(dFP - dFM) ** 2) / 4.0
        vmap.append(vm)
    floor = 3.2e-15
    def sig2(ai):
        s = np.zeros(len(prob.arms[ai].t))
        for p, v in vmap[ai].items():
            s += 4.0 * lam[p] * (1 - lam[p]) * v
        return s
    S2r = [sig2(ai) for ai in range(len(arms))]
    w0 = prob.weights()
    rng = np.random.default_rng(order_seed) if order_seed else None
    order = sorted(bitp, key=lambda p: -w0[p])
    if rng is not None:
        # perturbed order: jitter weights by ±15%
        order = sorted(bitp, key=lambda p: -w0[p] * (1 + 0.15 * rng.standard_normal()))
    for sw in range(max_sweeps):
        move = 0.0
        for p in order:
            l0 = lam[p]
            # per-arm: d(lam) = d0 + (lam - l0) * Delta; whitened LS over all arms jointly
            num = 0.0; den = 0.0
            deltas = []
            for ai, arm in enumerate(prob.arms):
                if p not in prob.cands[ai]:
                    deltas.append(None); continue
                kmax = int(np.log(arm.X) / np.log(p))
                q1 = q_between(*prob.cands[ai][p], l0, 1.0, kmax)
                q0 = q_between(*prob.cands[ai][p], l0, 0.0, kmax)
                _, _, dF1, dFi1 = arm.delta_for(p, q1)
                _, _, dF0, dFi0 = arm.delta_for(p, q0)
                DF = dF1 - dF0; DFi = dFi1 - dFi0            # per unit lambda
                F0 = arm.F + dF0 + l0 * DF * 0               # current F = at lam l0: arm.F itself
                eps = arm.eps_fit()
                d0 = arm.Fi - eps * arm.t * np.conj(arm.F)
                Dd = DFi - eps * arm.t * np.conj(DF)
                wgt = 1.0 / (np.maximum(S2r[ai] - 4.0 * l0 * (1 - l0) * vmap[ai].get(p, 0.0), 0.0)
                             + (10 * floor * np.max(np.abs(arm.F))) ** 2)
                num += -np.sum(np.real(np.conj(Dd) * d0) * wgt)
                den += np.sum(np.abs(Dd) ** 2 * wgt)
                deltas.append((q1, q0))
            if den == 0:
                continue
            lnew = float(np.clip(l0 + num / den, 0.0, 1.0))
            if abs(lnew - l0) < 1e-4:
                continue
            for ai, arm in enumerate(prob.arms):
                if p not in prob.cands[ai]:
                    continue
                kmax = int(np.log(arm.X) / np.log(p))
                q = q_between(*prob.cands[ai][p], l0, lnew, kmax)
                idx, val, dF, dFi = arm.delta_for(p, q)
                arm.commit(idx, val, dF, dFi)
            move = max(move, abs(lnew - l0))
            lam[p] = lnew
        S2r = [sig2(ai) for ai in range(len(arms))]
        Jw = 0.0
        for ai, arm in enumerate(prob.arms):
            eps = arm.eps_fit()
            d = arm.Fi - eps * arm.t * np.conj(arm.F)
            Jw += float(np.sum(np.abs(d) ** 2 / (np.maximum(S2r[ai], 0) + (10 * floor * np.max(np.abs(arm.F))) ** 2)))
        nhard = sum(1 for p in bitp if lam[p] < 0.05 or lam[p] > 0.95)
        print(f"  S4 sweep {sw+1}: max|dlam| {move:.3f}  Jw {Jw:.3e}  hard {nhard}/{len(bitp)}", flush=True)
        if move < 1e-3:
            break
    # round + hard polish on the ROUNDED state via fresh problem
    st = {p: (+1 if lam[p] >= 0.5 else -1) for p in bitp}
    prob2 = MultiProblem(arms, bitp, cands, fixed)
    prob2.init_marginal()
    for p in order:
        prob2.set_bit(p, st[p])
    for _ in range(8):
        improved = False
        Jnow = prob2.Jtot()
        for p in order:
            s = prob2.state[p]
            Jf, dsf = prob2.peek_set(p, -s)
            if Jf < Jnow:
                prob2.commit_set(p, -s, dsf); Jnow = Jf; improved = True
        if not improved:
            break
    drift = prob2.resieve_gate()
    st = dict(prob2.state)
    carm, r, eps, gdev = cert_metrics(D, st, cls, floor)
    certprob = Problem([carm], [p for p in bitp if p <= carm.X],
                       [{p: (FACP, FACN) for p in bitp if p <= carm.X}], [lambda p: None])
    certprob.state = {p: st.get(p, 0) for p in bitp if p <= carm.X}
    s, vis = sensitivity(certprob, floor)
    vp = sorted(vis.keys())
    acc_all = sum(1 for p in bitp if st.get(p, 0) == truth[p]) / len(bitp)
    wrong_vis = [p for p in vp if st.get(p, 0) != truth[p]]
    acc_vis = (len(vp) - len(wrong_vis)) / len(vp) if vp else float('nan')
    soft_conf = {p: abs(lam[p] - 0.5) * 2 for p in bitp}
    dt = time.time() - t0
    tag = f"S4/R1.w{'/ord' + str(order_seed) if order_seed else ''}"
    print(f"{tag}: drift {drift:.1e}  cert-residual {r:.3e}  eps {eps:.4f}  acc(all {len(bitp)}) {acc_all*100:.1f}%  "
          f"acc(visible) {acc_vis*100:.1f}% ({len(vp)} visible, wrong: {wrong_vis})  [{dt:.0f}s]", flush=True)
    out = {'D': D, 'which': tag, 'cert_residual': r, 'eps': [eps.real, eps.imag], 'meterdev': gdev,
           'acc_all': acc_all, 'acc_vis': acc_vis, 'n_visible': len(vp), 'wrong_visible': wrong_vis,
           'bits': {str(p): int(st.get(p, 0)) for p in bitp},
           'lambda_conf': {str(p): soft_conf[p] for p in bitp}, 'time_s': dt}
    json.dump(out, open(f'qualify5_{D}_S4_{order_seed}.json', 'w'), indent=1)
    return out

if __name__ == '__main__':
    D = int(sys.argv[1])
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    S4_soft(D, seed)
