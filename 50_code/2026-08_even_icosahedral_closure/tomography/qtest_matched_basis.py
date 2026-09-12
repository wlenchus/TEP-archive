"""Q-t2 — the matched-basis rerun, deciding the even/odd-rung question.
2026-08-11 (session B). PREREG (stated before run; same-session, unhashed):
Each chart c in {r (rung 0), A=arcsin (rung 1, Fisher/odd), eta=artanh (rung 2)}
gets BOTH its shells AND its reconstruction basis (piecewise-linear hats in the
chart variable) uniformly spaced in c — removing the P-t1 basis confound.
Competing hypotheses, priors declared:
  H-r  (prior 0.6): conditioning is support-geometric (edge-overlap), metric-
       blind: rung 0 wins again.
  H-A  (prior 0.4): Petz/Chentsov reading — with fair bases the unique radial
       Fisher chart (rung 1, the ODD rung) wins.
Kill for the Petz-refined design rule: kappa(A-matched) >= kappa(r-matched).
Domain note (reported as data): the eta-chart cannot grid the closed annulus
(artanh(1) = inf) — nodes capped at r = 0.999 for ALL charts, same domain.

OUTCOME (filed as RESULT_Qt2_matched_basis_rung_law_20260811B.md):
  H-r survives, H-A dies.  Matched bases rescue the chart designs by ~11 orders,
  but rung 0 still wins by ~4 at every size: kappa ASCENDS MONOTONICALLY WITH RUNG
  (r < A < eta) -- each chart ascent (each factor of G) costs conditioning.
  Parity is nonetheless present, as DOMAIN TOPOLOGY: the odd rung compactifies
  (A holds the closed annulus in [.,pi/2]) while the even rungs diverge at
  saturation (artanh(1)=inf).  Petz/Chentsov uniqueness on the radial line is what
  makes the design question invariant at all; the invariant answer is that Abel
  conditioning is a SUPPORT-GEOMETRY functional, blind to the distinguishability
  metric.  Two ledgers: distinguishability prices the PROBE, support geometry
  prices the INVERSION."""
import numpy as np
A_IN, R_HI, P_LO, P_HI = 0.3, 0.999, 0.30, 0.98
xg, wg = np.polynomial.legendre.leggauss(400)
CH = {'r':   (lambda r: r,            lambda u: u),
      'A':   (np.arcsin,              np.sin),
      'eta': (np.arctanh,             np.tanh)}
def kappa(chart, m):
    fwd, inv = CH[chart]
    un = np.linspace(fwd(A_IN), fwd(R_HI), m)      # node grid in chart var
    up = np.linspace(fwd(P_LO), fwd(P_HI), m)      # shell grid in chart var
    ps = inv(up)
    def hat(i, r):
        u = fwd(np.clip(r, A_IN, R_HI))
        x = np.zeros_like(u)
        lo = un[i-1] if i > 0 else un[0]
        hi = un[i+1] if i < m-1 else un[-1]
        c = un[i]
        L = (u >= lo) & (u <= c); R = (u > c) & (u <= hi)
        if c > lo: x[L] = (u[L]-lo)/(c-lo)
        if hi > c: x[R] = (hi-u[R])/(hi-c)
        return x
    M = np.zeros((m, m))
    for k, p in enumerate(ps):
        smax = np.arccosh(R_HI/p)
        s = (xg+1)/2*smax; w = wg/2*smax
        r = p*np.cosh(s)
        for i in range(m):
            M[k, i] = 2*np.sum(w*hat(i, r)*p*np.cosh(s))
    return np.linalg.cond(M)
print(f"{'m':>4s} {'rung0 r-matched':>16s} {'rung1 A-matched':>16s} {'rung2 eta-matched':>18s}")
res = {}
for m in (16, 24, 32):
    row = [kappa(c, m) for c in ('r', 'A', 'eta')]
    res[m] = row
    print(f"{m:4d} {row[0]:16.3e} {row[1]:16.3e} {row[2]:18.3e}")
win = {m: ['r','A','eta'][int(np.argmin(v))] for m, v in res.items()}
print("winners:", win)
print("verdict:", "H-A (Fisher/odd rung) survives" if all(w == 'A' for w in win.values())
      else ("H-r (support-geometry) survives" if all(w == 'r' for w in win.values())
      else "MIXED — report as-is"))
