"""P-t1 TEST — the rapidity-sampling design rule for shell tomography.
2026-08-11 (session B). PREREG (stated before run; same-session, unhashed):
  P-t1 (as filed in the ADDENDUM): the shell-suite Abel system is best
  conditioned when shells are equally spaced in the RAPIDITY chart
  (eta = artanh p), beating both uniform-radius and uniform-angle
  (= the natural equal-k suite, since p_k = cos(pi k/n)).
  Quantitative bar: kappa(rapidity) < 0.95 * kappa(angle) at all three
  suite sizes (16, 24, 32).
KILL K-t1: if angle-uniform matches or beats rapidity (ratio >= 0.95),
  P-t1 as filed is FALSIFIED and reported as such; the winning chart is
  reported regardless (a Chebyshev-style angle-optimum would itself be a
  budget chart, but NOT the one P-t1 named -- a kill is a kill).
Setup (fixed across designs; only shell placement varies):
  radial profiles on [0.3, 1.0], 24 piecewise-linear hat functions on
  uniform-r nodes; shell reads S(p) = 2 int_p^1 f(r) r dr/sqrt(r^2-p^2)
  (per-chord line integral of a radial function), computed via the exact
  flattening substitution r = p cosh(sigma), 400-pt Gauss-Legendre;
  square systems, kappa_2 reported.

OUTCOME (filed as RESULT_Pt1_FALSIFIED_rapidity_sampling_20260811B.md):
  K-t1 FIRED.  kappa(radius) ~ 1e1 while BOTH chart-clustered designs are
  numerically singular (~1e17).  Lesson extracted: G measures DWELL, not
  INFORMATION -- clustering probes where the gain diverges duplicates the
  same read (near-collinear rows), because the Abel read is dominated by
  the tangency neighbourhood.  The forward G-kernel identification is
  untouched; its naive design corollary is dead.
  Confound disclosed: the reconstruction basis (uniform-r hats) is not
  chart-neutral -- see qtest_matched_basis.py for the matched rerun."""
import numpy as np

A_IN, P_LO, P_HI = 0.3, 0.30, 0.98
NODES = np.linspace(A_IN, 1.0, 24)
def hat(i, r):
    x = np.zeros_like(r)
    lo = NODES[i-1] if i > 0 else NODES[0]
    hi = NODES[i+1] if i < len(NODES)-1 else NODES[-1]
    c = NODES[i]
    left = (r >= lo) & (r <= c); right = (r > c) & (r <= hi)
    if c > lo: x[left] = (r[left]-lo)/(c-lo)
    if hi > c: x[right] = (hi-r[right])/(hi-c)
    return x
xg, wg = np.polynomial.legendre.leggauss(400)
def shell_read_matrix(ps):
    M = np.zeros((len(ps), len(NODES)))
    for k, p in enumerate(ps):
        smax = np.arccosh(1.0/p)
        s = (xg+1)/2*smax; w = wg/2*smax
        r = p*np.cosh(s)
        for i in range(len(NODES)):
            M[k, i] = 2*np.sum(w * hat(i, r) * p*np.cosh(s))
    return M
def suite(rule, m):
    if rule == 'radius':   q = np.linspace(P_LO, P_HI, m)
    if rule == 'angle':    q = np.sin(np.linspace(np.arcsin(P_LO), np.arcsin(P_HI), m))
    if rule == 'rapidity': q = np.tanh(np.linspace(np.arctanh(P_LO), np.arctanh(P_HI), m))
    return q
print(f"{'m_s':>4s} {'kappa(radius)':>14s} {'kappa(angle)':>13s} {'kappa(rapidity)':>16s}")
verdicts = []
for m in (16, 24, 32):
    globals()['NODES'] = np.linspace(A_IN, 1.0, m)
    ks = {}
    for rule in ('radius', 'angle', 'rapidity'):
        M = shell_read_matrix(suite(rule, m))
        ks[rule] = np.linalg.cond(M)
    ratio = ks['rapidity']/ks['angle']
    verdicts.append(ratio < 0.95)
    print(f"{m:4d} {ks['radius']:14.3e} {ks['angle']:13.3e} {ks['rapidity']:16.3e}  {ratio:8.3f}")
print("\nP-t1 (rapidity beats angle by >=5% at all sizes):",
      "PASS" if all(verdicts) else "FALSIFIED (K-t1 fired)")
