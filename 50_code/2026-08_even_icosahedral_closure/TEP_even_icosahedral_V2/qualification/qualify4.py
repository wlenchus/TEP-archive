#!/usr/bin/env python3
"""GATE-M under AMENDMENT R1 + whitened multi-arm objective (R1.w): each arm's FE defect is
whitened by its marginalization variance sigma^2_arm(t) = sum_{undecided p} v_p(t)/4,
v_p(t) = |dFi_p(t)|^2 + t^2 |dF_p(t)|^2  (candidate-gap deltas, answer-free), floored at the
control floor. Bands/staging per R1; passes >= 2 run at full sharpness (all bits decided).
Usage: python3 qualify4.py <D> <S1|S2|S3>"""
import numpy as np, json, sys, time
sys.path.insert(0, '.')
from qualify2 import build, MultiProblem, cert_metrics, TW, FACP, FACN
from instr2 import Arm, Problem, Xof, TGRID, sensitivity

class WProblem(MultiProblem):
    def build_sigma(self, floor=3.2e-15):
        self.vmap = []   # per arm: dict p -> v(t) rows
        self.sig2 = []
        for ai, arm in enumerate(self.arms):
            vm = {}
            s2 = np.zeros(len(arm.t))
            for p in self.cands[ai]:
                if p not in self.state:
                    continue
                qP = self._q(ai, p, 0, +1); qM = self._q(ai, p, 0, -1)
                _, _, dFP, dFiP = arm.delta_for(p, qP)
                _, _, dFM, dFiM = arm.delta_for(p, qM)
                v = (np.abs(dFiP - dFiM) ** 2 + arm.t ** 2 * np.abs(dFP - dFM) ** 2) / 4.0
                vm[p] = v
                if self.state[p] == 0:
                    s2 += v
            self.vmap.append(vm)
            scF = np.max(np.abs(arm.F)) if arm.F is not None else 1.0
            self.floor2 = (10 * floor * scF) ** 2
            self.sig2.append(s2)
        self._floor = floor

    def _Jarm(self, ai, dF, dFi):
        arm = self.arms[ai]
        F = arm.F + dF; Fi = arm.Fi + dFi
        sc = np.max(np.abs(F))
        if sc == 0:
            return 1e30
        num = np.sum(Fi * arm.t * F)
        eps = num / abs(num) if num != 0 else 1.0
        d = Fi - eps * arm.t * np.conj(F)
        w = np.maximum(self.sig2[ai], 0.0) + (10 * self._floor * sc) ** 2   # clamp: fp cancellation guard
        return float(np.sum(np.abs(d) ** 2 / w))

    def peek_set(self, p, s_new):
        Jt = 0.0; ds = []
        for ai, arm in enumerate(self.arms):
            if p not in self.cands[ai]:
                zt = np.zeros(len(arm.t), dtype=complex)
                d = (np.zeros(0, dtype=int), np.zeros(0, dtype=complex), zt, zt.copy())
                Jt += self._Jarm(ai, d[2], d[3]); ds.append(d)
                continue
            q = self._q(ai, p, self.state[p], s_new)
            idx, val, dF, dFi = arm.delta_for(p, q)
            # sigma adjustment if deciding a previously-undecided bit
            Jt_arm = None
            if self.state[p] == 0 and s_new != 0 and p in self.vmap[ai]:
                self.sig2[ai] -= self.vmap[ai][p]
                Jt_arm = self._Jarm(ai, dF, dFi)
                self.sig2[ai] += self.vmap[ai][p]
            else:
                Jt_arm = self._Jarm(ai, dF, dFi)
            Jt += Jt_arm
            ds.append((idx, val, dF, dFi))
        return Jt, ds

    def commit_set(self, p, s_new, ds):
        s_old = self.state[p]
        for ai, (arm, d) in enumerate(zip(self.arms, ds)):
            arm.commit(*d)
            if p in self.vmap[ai]:
                if s_old == 0 and s_new != 0:
                    self.sig2[ai] = self.sig2[ai] - self.vmap[ai][p]
                elif s_old != 0 and s_new == 0:
                    self.sig2[ai] = self.sig2[ai] + self.vmap[ai][p]
        self.state[p] = s_new

    def Jtot(self):
        z = np.zeros(0, dtype=complex)
        tot = 0.0
        for ai, arm in enumerate(self.arms):
            zt = np.zeros(len(arm.t), dtype=complex)
            tot += self._Jarm(ai, zt, zt)
        return float(tot)

    # snapshots must carry sigma
    def snap(self, copy=True):
        base = super().snap(copy)
        sig = [s.copy() for s in self.sig2] if copy else list(self.sig2)
        return (base[0], base[1], sig)

    def load(self, sn, copy=False):
        st, arrs, sig = sn
        super().load((st, arrs), copy)
        self.sig2 = [s.copy() for s in sig] if copy else list(sig)

def band_edges(arms):
    return sorted(set(a.X for a in arms))

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

ORDER_JITTER = None   # set to an int seed for perturbed-order replicate runs

def inband_S2(prob, band, log, width=64):
    w = prob.weights()
    if ORDER_JITTER is not None:
        rng = np.random.default_rng([ORDER_JITTER, len(band)])
        order = [p for p in sorted(band, key=lambda p: -w[p] * (1 + 0.15 * rng.standard_normal()))]
    else:
        order = [p for p in sorted(band, key=lambda p: -w[p])]
    beam = [prob.snap(copy=True) + (prob.Jtot(),)]
    for p in order:
        cand = []
        for (st, arrs, sig, J) in beam:
            prob.load((st, arrs, sig), copy=False)
            for ss in (+1, -1):
                Jc, ds = prob.peek_set(p, ss)
                cand.append((Jc, st, arrs, sig, ss, ds))
        cand.sort(key=lambda c: c[0])
        newbeam = []
        for (Jc, st, arrs, sig, ss, ds) in cand[:width]:
            prob.load((st, arrs, sig), copy=True)
            prob.commit_set(p, ss, ds)
            newbeam.append(prob.snap(copy=False) + (Jc,))
        beam = newbeam
    st, arrs, sig, J = min(beam, key=lambda b: b[3])
    prob.load((st, arrs, sig), copy=True)

def inband_S3(prob, band, log, seeds=(20260803, 1951, 2089, 5), nchains=6, sweeps=400):
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
            prob.set_bit(p, +1 if c == 0 else int(rng.choice([-1, 1])))   # chain 0 = structured all-plus (B §6 precedent)
        chains.append(list(prob.snap(copy=False)) + [prob.Jtot()])
    temps = np.geomspace(0.02, 2.0, nchains)      # ln-J units: scale-free acceptance
    best = None; last_gain = 0
    m = len(order)
    props = max(6, m // 3)
    for sw in range(sweeps):
        for c in range(nchains):
            st, arrs, sig, J = chains[c]
            prob.load((st, arrs, sig), copy=False)
            T = temps[c]
            L = np.log(J + 1e-300)
            for _ in range(props):
                p = order[int(rng.choice(m, p=wv))]
                s = prob.state[p]
                Jf, ds = prob.peek_set(p, -s)
                Lf = np.log(Jf + 1e-300)
                if Lf <= L or rng.random() < np.exp(-(Lf - L) / T):
                    prob.commit_set(p, -s, ds); J = Jf; L = Lf
            chains[c] = list(prob.snap(copy=False)) + [J]
            if best is None or J < best[1]:
                best = (dict(prob.state), J); last_gain = sw
        if sw - last_gain > 120:
            break
        if sw % 50 == 0 and sw > 0:
            for c in range(nchains - 1):
                L1, L2 = np.log(chains[c][3] + 1e-300), np.log(chains[c + 1][3] + 1e-300)
                d = (1.0 / temps[c] - 1.0 / temps[c + 1]) * (L1 - L2)
                if d > 0 or rng.random() < np.exp(d):
                    chains[c], chains[c + 1] = chains[c + 1], chains[c]
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
    prob = WProblem(arms, bitp, cands, fixed)
    prob.init_marginal()
    prob.build_sigma()
    edges = band_edges(arms)
    lo = 0; bands = []
    for hi in edges:
        band = [p for p in bitp if lo < p <= hi]
        if band:
            bands.append((lo, hi, band))
        lo = hi
    print(f"== R1.w staged {which} at D={D}: {len(arms)} arms, {len(bitp)} bits ==", flush=True)
    fn = {'S1': inband_S1, 'S2': inband_S2, 'S3': inband_S3}[which]
    if which == 'S3':
        npass = min(npass, 2)
    for ps in range(npass):
        for (lo, hi, band) in bands:
            fn(prob, band, log=print)
        print(f"  pass {ps+1}: J = {prob.Jtot():.3e}", flush=True)
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
    print(f"{which}/R1.w: J {prob.Jtot():.3e}  drift {drift:.1e}  cert-residual {r:.3e}  eps {eps:.4f}  "
          f"acc(all {len(bitp)}) {acc_all*100:.1f}%  acc(visible) {acc_vis*100:.1f}% "
          f"({len(vp)} visible, wrong: {wrong_vis})  undecided {und}  [{dt:.0f}s]", flush=True)
    out = {'D': D, 'which': which + '/R1.w', 'J': prob.Jtot(), 'cert_residual': r,
           'eps': [eps.real, eps.imag], 'meterdev': gdev, 'acc_all': acc_all, 'acc_vis': acc_vis,
           'n_visible': len(vp), 'wrong_visible': wrong_vis, 'undecided': und,
           'bits': {str(p): int(st.get(p, 0)) for p in bitp}, 'time_s': dt}
    json.dump(out, open(f'qualify4_{D}_{which}.json', 'w'), indent=1)
    return out

if __name__ == '__main__':
    staged(int(sys.argv[1]), sys.argv[2])
