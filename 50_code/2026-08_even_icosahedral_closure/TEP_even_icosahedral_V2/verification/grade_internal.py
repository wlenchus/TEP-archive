#!/usr/bin/env python3
"""Post-commit internal graders: (a) chi->chi^2 Galois-transport coherence; (b) Chebotarev tallies."""
import numpy as np, json, sys
sys.path.insert(0, '.')
from summit import build_summit, cert_arm_for, MTAB, Z10
from qualify4 import WProblem
from instr2 import Problem

sol = {int(p): v for p, v in json.load(open('summit_base_oddGS.json'))['bits'].items()}

# (a) transport: decode the conjugate cell (chi -> chi^2, i.e. j -> 2j) same port/orientation... the
# conjugate object rho^sigma: sigma(sqrt5) = -sqrt5 => golden magnitudes swap => orientation flips too.
# Predicted transport: a_p^sigma = sigma(a_p). We decode the conjugate cell blind (S2-128) and compare.
CELL = 1
arms, bitp, cands, fixed, data = build_summit(CELL, conj=True, goldenswap=False)
# NOTE orientation: sigma swaps phi <-> -1/phi ... |a| swaps phi <-> 1/phi: orientation-B conjugates to orientation-A
arm0 = arms[0]
bp = [p for p in bitp if p <= arm0.X]
prob = WProblem([arm0], list(bp), [{p: cands[0][p] for p in bp}], [fixed[0]])
prob.init_marginal(); prob.build_sigma()
w = prob.weights()
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
    for (Jc, st, arrs, sig, ss, ds) in cand[:128]:
        prob.load((st, arrs, sig), copy=True)
        prob.commit_set(p, ss, ds)
        nb.append(prob.snap(copy=False) + (Jc,))
    beam = nb
stc, arrs, sig, J = min(beam, key=lambda b: b[3])
prob.load((stc, arrs, sig), copy=True)
for _ in range(8):
    improved = False
    Jnow = prob.Jtot()
    for p in order:
        s = prob.state[p]
        Jf, dsf = prob.peek_set(p, -s)
        if Jf < Jnow:
            prob.commit_set(p, -s, dsf); Jnow = Jf; improved = True
    if not improved: break
carm = cert_arm_for(CELL, dict(prob.state), data, conj=True, goldenswap=False)
r, eps = carm.residual()
print(f"(a) conjugate cell (chi^2, orientation-A, odd port): cert-residual {r:.3e}  eps {eps.real:+.6f}{eps.imag:+.6f}i")
# transport map: sigma: zeta5 -> zeta5^2 (so zeta10^j -> zeta10^{2j} up to sign*), phi -> -1/phi.
# a_p = b ph m: sigma(a_p) = b * sigma(ph) * sigma(m). conjugate-cell dictionary: a'_p = b' * zeta10^{2j} * m'
# with m' = MTAB[label] (orientation A: label3->1/phi wait MTAB is orientation-B map applied when goldenswap=...)
cls, jl, kr = data
PHI = (1+np.sqrt(5))/2
mism = []; tested = 0
for p in bp:
    lab = cls[p]; j = jl[p]
    if lab == 1: continue
    # committed: a_p = sol[p] * zeta10^j * mB(lab); mB: {0:2, 2:1, 3:phi, 4:1/phi}
    mB = {0: 2.0, 2: 1.0, 3: PHI, 4: 1/PHI}[lab]
    ap = sol[p] * Z10**(j % 10) * mB
    # sigma(a_p): conjugate golden part: sigma(phi) = 1-phi = -1/phi; sigma(1/phi) = ... sigma(sqrt5) = -sqrt5:
    sig_m = {0: 2.0, 2: 1.0, 3: -1/PHI, 4: -PHI}[lab]      # sigma(phi) = -1/phi, sigma(1/phi) = -phi
    sig_ap = sol[p] * Z10**((2*j) % 10) * ... if False else sol[p] * (np.exp(1j*np.pi*(2*j)/5)) * sig_m
    # conjugate-cell convention: a'_p = b'_p * zeta10^{2j mod 10} * mA(lab); mA (orientation A): {3: 1/phi, 4: phi}
    mA = {0: 2.0, 2: 1.0, 3: 1/PHI, 4: PHI}[lab]
    conv = np.exp(1j*np.pi*((2*j) % 10)/5) * mA
    pred_b = sig_ap / conv
    pb = int(np.sign(pred_b.real)) if abs(pred_b.imag) < 1e-9 and abs(abs(pred_b.real)-1) < 1e-9 else None
    if pb is None:
        continue
    tested += 1
    if prob.state[p] != pb:
        mism.append(p)
print(f"(a) transport grade: {tested} comparable bits, mismatches: {len(mism)} {mism[:10]}")

# (b) Chebotarev tallies of (class, bit): in <2.A5, zeta5 I> the lift classes of a given projective class
# split evenly between the two sign-lifts => bits should be ~50/50 per class.
import collections
tal = collections.Counter((cls[p], sol[p]) for p in sol)
print("(b) Chebotarev (class, bit) tallies:", dict(tal))
json.dump({'conj_residual': r, 'conj_eps': [eps.real, eps.imag], 'transport_tested': tested,
           'transport_mismatch': [int(m) for m in mism],
           'cheb': {f"{k[0]}:{k[1]:+d}": v for k, v in tal.items()}}, open('grade_internal.json', 'w'), indent=1)
