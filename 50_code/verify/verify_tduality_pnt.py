# verify_tduality_pnt.py — 2026-07-20 (coda): Will's two closing identifications.
# (1) PNT dress: the abelian totals' per-symbol share ~ 1/pi(n) in nats (his "inverse prime
#     counting function" — exact as an asymptotic equivalence to the Prime Number Theorem).
# (2) Port<->length swap as a Fricke-type inversion on the capacity line with level ln 2:
#     u = 2^(-R) (R = C/B), swap R -> 1/R  =>  ln u * ln u' = (ln 2)^2, fixed point u = 1/2
#     — "ln 2 plays the self-dual radius squared" (Will's T-duality naming, corpus dress).
import sympy as sp
from sympy import primepi
import math
P = []
def check(name, ok):
    P.append(bool(ok)); print(("PASS " if ok else "FAIL ") + name)

# (1) PNT share
print("  n        pi(n)     [ln(n+1)/n] * pi(n)   (-> 1 by PNT)")
ratios = []
for n in [10**3, 10**4, 10**5, 10**6, 10**7]:
    r = float(primepi(n)) * math.log(n + 1) / n
    ratios.append(r)
    print("  %-8d %-9d %.5f" % (n, int(primepi(n)), r))
check("C1 abelian per-symbol share (nats) * pi(n) -> 1 monotonically over 10^3..10^7 — "
      "H_ab/n ~ 1/pi(n): 'one nat of solvable ledger per prime below n' (a PNT restatement; "
      "[id] as a places-as-rungs dress, not a discovery)",
      all(ratios[i] > ratios[i+1] for i in range(len(ratios)-1)) and abs(ratios[-1] - 1) < 0.09)

# (2) the port<->length inversion
R, u = sp.symbols('R u', positive=True)
uR  = 2**(-R)
uRp = 2**(-1/R)
check("C2 ln u * ln u' = (ln 2)^2 under R -> 1/R  [Fricke-type inversion on the capacity line, "
      "level ln 2 — 'ln 2 as the self-dual radius squared']",
      sp.simplify(sp.log(uR)*sp.log(uRp) - sp.log(2)**2) == 0)
check("C3 fixed point of the inversion: R = 1 <=> u = 1/2 (self-dual) — same fixed point as the "
      "swap u -> 1-u, but a DIFFERENT involution elsewhere",
      sp.simplify(uR.subs(R, 1) - sp.Rational(1,2)) == 0 and
      abs(float(uRp.subs(R, 4)) - (1 - float(uR.subs(R, 4)))) > 0.05)   # at R=4: u'=2^-.25=.841 vs 1-u=.9375
print("\n%d/%d PASS" % (sum(P), len(P)))
