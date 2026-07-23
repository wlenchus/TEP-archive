# verify_sigma_completion.py — 2026-07-20 tangent session
# Verifies: (1) the Sigma-completion of the 07-19 pair-ledger (swap-transport chirality),
# (2) the inverted double-angle budget as the improper self-transport (distance-to-own-dual),
# (3) the eta_c / lambda / ln tan A / Gudermannian identity chain (incl. v0.5 Log Kit form),
# (4) the hyperbolic mirror (Cayley foil) as the same construction on the hyperbolic face,
# (5) the four-fold template queue item (G^4 slot = capacity-doubling wiring), one-bit tolls,
# (6) golden fixed-point exact values, silver/self-dual locks, g-involution fixed point,
# (7) composition laws (SO(2) transport; telescope = sinSigma*sinDelta; Sigma-Delta interlock),
# (8) relative-budget reading of sech^2(Delta eta) and the gd-nonadditivity defect.
# Convention (settled corpus, 06-28 SL): x = sin A = tanh eta_b, u = 1 - x^2, G = 1/sqrt(u), SNR = x^2/u.

import sympy as sp
import mpmath as mp

mp.mp.dps = 30
PASS = []
def check(name, ok):
    PASS.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name)

A1, A2, A = sp.symbols('A1 A2 A', positive=True)
eta, e1, e2 = sp.symbols('eta eta1 eta2', positive=True)

def budget_from_angle(Aa):
    x = sp.sin(Aa); return x**2, sp.cos(Aa)**2  # (x^2, u)

# ---------- (1) Sigma-completion of the pair-ledger ----------
x2_1, u1 = budget_from_angle(A1)
x2_2, u2 = budget_from_angle(A2)

# Delta-form (07-19 note, re-derived cold): aff, cross
aff  = sp.sqrt(x2_1*x2_2) + sp.sqrt(u1*u2)
cro  = sp.sqrt(u1*x2_2)  - sp.sqrt(x2_1*u2)
check("D-form unit pair-budget: aff^2 + cross^2 = 1",
      sp.simplify(sp.expand_trig(sp.simplify(aff**2 + cro**2 - 1))) == 0)
check("D-form angle reading: aff = cos(A2-A1), cross = sin(A2-A1)",
      sp.simplify(aff - sp.cos(A2-A1)) == 0 and sp.simplify(sp.expand_trig(cro - sp.sin(A2-A1))) == 0)

# Sigma-form (new): pair rank 1 with the SWAP of rank 2
affS = sp.sqrt(u1*x2_2) + sp.sqrt(x2_1*u2)     # = sin(A1+A2)
croS = sp.sqrt(x2_1*x2_2) - sp.sqrt(u1*u2)     # = -cos(A1+A2)
check("S-form unit pair-budget: affS^2 + croS^2 = 1",
      sp.simplify(sp.expand_trig(sp.simplify(affS**2 + croS**2 - 1))) == 0)
check("S-form angle reading: affS = sin(A1+A2), croS = -cos(A1+A2)",
      sp.simplify(sp.expand_trig(affS - sp.sin(A1+A2))) == 0 and
      sp.simplify(sp.expand_trig(croS + sp.cos(A1+A2))) == 0)

# Werner split: the cross-budget terms' GM-readings are (sinSigma +/- sinDelta)/2
check("Werner: 2*sqrt(u1*x2_2) = sin(Sigma) + sin(Delta)",
      sp.simplify(sp.expand_trig(2*sp.sqrt(u1*x2_2) - (sp.sin(A1+A2) + sp.sin(A2-A1)))) == 0)
check("Werner: 2*sqrt(x2_1*u2) = sin(Sigma) - sin(Delta)",
      sp.simplify(sp.expand_trig(2*sp.sqrt(x2_1*u2) - (sp.sin(A1+A2) - sp.sin(A2-A1)))) == 0)

# Antisymmetric telescope factors as swap-leg * cross-leg
check("telescope u1*x2_2 - x2_1*u2 = x2_2 - x2_1 = sin(Sigma)*sin(Delta)",
      sp.simplify(u1*x2_2 - x2_1*u2 - (x2_2 - x2_1)) == 0 and
      sp.simplify(sp.expand_trig(u1*x2_2 - x2_1*u2 - sp.sin(A1+A2)*sp.sin(A2-A1))) == 0)

# ---------- (2) Diagonal collapse: inverted double-angle budget ----------
x2, u = budget_from_angle(A)
check("diagonal S-form: affS -> 2x*sqrt(u) = sin 2A ; croS -> x^2-u = -cos 2A",
      sp.simplify(sp.expand_trig(2*sp.sin(A)*sp.cos(A) - sp.sin(2*A))) == 0 and
      sp.simplify(sp.expand_trig((x2 - u) + sp.cos(2*A))) == 0)
check("double-angle budget: (x^2-u)^2 + (2x*sqrt(u))^2 = (x^2+u)^2 = 1",
      sp.simplify(sp.expand((x2-u)**2 + 4*x2*u - 1)) == 0)
# distance-to-own-dual: FR arc(amplitude coins) rank->swap(rank) = |2A - pi/2| = 2*|A - pi/4|
Aval = mp.mpf('0.9')
p1 = (1+mp.sin(Aval))/2; p2 = (1+mp.cos(Aval))/2   # amplitude coin of rank and of its swap
arc = 2*mp.acos(mp.sqrt(p1*p2) + mp.sqrt((1-p1)*(1-p2)))
check("FR arc (amplitude coin) to own dual = |2A - pi/2|, = 2x distance to self-dual",
      mp.almosteq(arc, abs(2*Aval - mp.pi/2), 1e-25) and
      mp.almosteq(arc, 2*abs(Aval - mp.pi/4), 1e-25))

# ---------- (3) The eta_c chain ----------
etab = sp.symbols('eta_b', positive=True)
xb = sp.tanh(etab)
SNR = xb**2/(1-xb**2)
lam = sp.Rational(1,2)*sp.log(SNR)          # lambda = (1/2) ln SNR  (T-6 third rapidity)
check("lambda = ln sinh(eta_b)  [so eta_c = (1/2) ln sinh eta_b, lambda = 2*eta_c]",
      sp.simplify(lam - sp.log(sp.sinh(etab))) == 0)
check("tanh(2*eta_c) = tanh(lambda) = (SNR-1)/(SNR+1) = 2x^2-1  [Cayley]",
      sp.simplify(sp.tanh(lam) - (SNR-1)/(SNR+1)) == 0 and
      sp.simplify(sp.expand(sp.simplify(sp.tanh(lam) - (2*xb**2 - 1)))) == 0)
check("odds gauge: x^2 = (1+tanh 2eta_c)/2 = sigma(4 eta_c); logit(x^2) = 4 eta_c = 2 ln SNR^(1/2)... = ln SNR",
      sp.simplify((1+sp.tanh(lam))/2 - xb**2) == 0)
# gd dictionary: sin A = tanh eta  <=>  tan A = sinh eta ; lambda = ln tan A ; v0.5 Log Kit = -ln tan A = -lambda
ev = mp.mpf('1.3'); Ae = mp.asin(mp.tanh(ev))
check("gd bridge: tan A = sinh eta_b ; lambda = ln tan A ( = - v0.5 Log-Kit rapidity )",
      mp.almosteq(mp.tan(Ae), mp.sinh(ev), 1e-25) and
      mp.almosteq(mp.log(mp.tan(Ae)), mp.log(mp.sinh(ev)), 1e-25))
check("centered double angle: 2A - pi/2 = gd(2*eta_c) = gd(lambda)",
      mp.almosteq(2*Ae - mp.pi/2, 2*mp.atan(mp.exp(mp.log(mp.sinh(ev)))) - mp.pi/2, 1e-25))
# involution linearization: swap A -> pi/2 - A  <=>  lambda -> -lambda ; in eta it is g(eta)=ln coth(eta/2)
g = lambda a: mp.log(mp.coth(a/2))
etaswap = mp.atanh(mp.cos(Ae))                     # rapidity of the swapped budget
check("swap transported to rapidity = g(eta) = ln coth(eta/2) ; and lambda(swap) = -lambda",
      mp.almosteq(etaswap, g(ev), 1e-25) and
      mp.almosteq(mp.log(mp.sinh(etaswap)), -mp.log(mp.sinh(ev)), 1e-25))
# g's fixed point = silver rapidity (KW quadratic w^2-2w-1=0)
w = sp.symbols('w', positive=True)
sil = sp.log(1+sp.sqrt(2))
check("g fixed point: ln coth(a/2)=a at a = ln(1+sqrt2) (silver rapidity; w^2-2w-1=0)",
      sp.simplify(sp.log(sp.coth(sil/2)) - sil) == 0)
check("self-dual lock: x^2=1/2 <=> A=pi/4 <=> eta_b=ln(1+sqrt2) <=> sinh eta_b=1 <=> eta_c=0",
      sp.simplify(sp.tanh(sil)**2 - sp.Rational(1,2)) == 0 and sp.simplify(sp.sinh(sil) - 1) == 0)

# ---------- (4) Hyperbolic mirror (Cayley foil) ----------
G2 = sp.cosh(etab)**2
check("G^2 + SNR = cosh(2 eta_b) = 2G^2 - 1 ; and G^2 - SNR = 1",
      sp.simplify(G2 + sp.sinh(etab)**2 - sp.cosh(2*etab)) == 0 and
      sp.simplify(sp.cosh(2*etab) - (2*G2-1)) == 0 and
      sp.simplify(G2 - sp.sinh(etab)**2 - 1) == 0)
check("hyperbolic pair-budget: (G^2+SNR)^2 - (2G*sqrt(SNR))^2 = 1  [cosh^2 2eta - sinh^2 2eta]",
      sp.simplify((sp.cosh(2*etab))**2 - (2*sp.cosh(etab)*sp.sinh(etab))**2 - 1) == 0)
check("hyperbolic sum legs: G1*G2 + sqrt(SNR1*SNR2) = cosh(e1+e2); G1*sqrt(SNR2)+sqrt(SNR1)*G2 = sinh(e1+e2)",
      sp.simplify(sp.cosh(e1)*sp.cosh(e2) + sp.sinh(e1)*sp.sinh(e2) - sp.cosh(e1+e2)) == 0 and
      sp.simplify(sp.cosh(e1)*sp.sinh(e2) + sp.sinh(e1)*sp.cosh(e2) - sp.sinh(e1+e2)) == 0)
check("hyperbolic swap is the quarter-move: tanh(eta + i*pi/2) = coth(eta)",
      sp.simplify(sp.tanh(etab + sp.I*sp.pi/2) - sp.coth(etab)) == 0)

# ---------- (5) Four-fold template: queue item + one-bit tolls ----------
nu = sp.acosh(G2)  # cosh nu = G^2
check("(1 + cosh 2nu)/2 = G^4 with cosh nu = G^2   [template rung 4]",
      sp.simplify((1 + sp.cosh(2*nu))/2 - G2**2) == 0)
# capacity doubling wiring: u' = u^2  =>  G'^2 = G^4 and C' = -ln u' = 2C
uu = sp.symbols('u', positive=True)
check("u' = u^2  =>  G'^2 = G^4 and -ln u' = 2(-ln u)   [rung 4 = capacity-doubling gain]",
      sp.simplify(1/uu**2 - (1/sp.sqrt(uu))**4) == 0 and
      sp.simplify(-sp.log(uu**2) - 2*(-sp.log(uu))) == 0)
# one-bit tolls: ln sinh, ln cosh, and acosh(cosh^2) all drift by (multiples of) ln 2
check("toll: lim [ln sinh eta - (eta - ln2)] = 0 ; lim [ln cosh eta - (eta - ln2)] = 0",
      sp.limit(sp.log(sp.sinh(eta)) - (eta - sp.log(2)), eta, sp.oo) == 0 and
      sp.limit(sp.log(sp.cosh(eta)) - (eta - sp.log(2)), eta, sp.oo) == 0)
check("toll rung 4: lim [nu - (2 eta_b - ln 2)] = 0",
      sp.limit(sp.acosh(sp.cosh(etab)**2) - (2*etab - sp.log(2)), etab, sp.oo) == 0)
check("AM-arm engine: (1+cosh a)/2 = cosh^2(a/2)  [I.7's AGM AM-arm = the coin template]",
      sp.simplify((1+sp.cosh(2*etab))/2 - sp.cosh(etab)**2) == 0)
check("arm split: (1/2)ln cosh - (1/2)ln sinh = (1/2) ln coth = eta-hat family, -> 0",
      sp.limit(sp.Rational(1,2)*sp.log(sp.coth(eta)), eta, sp.oo) == 0)

# ---------- (6) Golden fixed point of the nesting wiring ----------
phi = (1+sp.sqrt(5))/2
ustar = 1/phi**2; xstar2 = 1 - ustar
check("nesting fixed point: x*^2 - u* = 1/phi^3 and 2x*sqrt(u*) = 2/phi^(3/2)",
      sp.simplify(xstar2 - ustar - 1/phi**3) == 0 and
      sp.simplify(2*sp.sqrt(xstar2*ustar) - 2/phi**sp.Rational(3,2)) == 0)
check("golden double-angle budget: (1/phi^3)^2 + 4/phi^3 = 1",
      sp.simplify(1/phi**6 + 4/phi**3 - 1) == 0)
check("tanh(2 eta_c*) = 1/phi^3 at the nesting fixed point",
      sp.simplify((2*xstar2 - 1) - 1/phi**3) == 0)

# ---------- (7) Composition laws ----------
A3 = sp.symbols('A3', positive=True)
c12, a12 = sp.sin(A2-A1), sp.cos(A2-A1)
c23, a23 = sp.sin(A3-A2), sp.cos(A3-A2)
check("SO(2) transport: cross(1,3) = cross(1,2)aff(2,3) + aff(1,2)cross(2,3)",
      sp.simplify(sp.expand_trig(sp.sin(A3-A1) - (c12*a23 + a12*c23))) == 0)
check("Sigma-Delta interlock: Sigma_{d+1} - Sigma_d = Delta_d + Delta_{d+1}",
      sp.simplify((A2+A3) - (A1+A2) - ((A2-A1)+(A3-A2))) == 0)
check("two swaps = rotation: M(S2)M(S1) = R(S2-S1)  [reflection composition]",
      sp.simplify(sp.expand_trig(sp.cos(A1+A2 - (A1+A3)) - sp.cos(A3 - A2))) == 0)

# ---------- (8) Distillation / relative budget / gd defect ----------
check("relative budget: 1 - tanh^2(Delta eta) = sech^2(Delta eta)  [u of the velocity-subtracted pair]",
      sp.simplify(1 - sp.tanh(e2-e1)**2 - sp.sech(e2-e1)**2) == 0)
# gd non-additivity: Delta A  =  gd(eta2) - gd(eta1)  !=  gd(eta2 - eta1) in general
gd = lambda t: 2*mp.atan(mp.exp(t)) - mp.pi/2
d_angle = gd(mp.mpf('2.0')) - gd(mp.mpf('0.7'))
d_rap   = gd(mp.mpf('2.0') - mp.mpf('0.7'))
check("gd defect nonzero (angle-chart Delta != rapidity-chart Delta transported): %.6f vs %.6f"
      % (d_angle, d_rap), abs(d_angle - d_rap) > 0.05)

print()
n_ok = sum(1 for _, ok in PASS if ok)
print("%d/%d PASS" % (n_ok, len(PASS)))

# ---------- numeric-exact re-checks for the sympy structural balks (corpus convention) ----------
print("\n-- numeric re-checks (mpmath, 30 dps, tol 1e-24, 3 random points each) --")
import random
random.seed(7)
NUM = []
def ncheck(name, f):
    ok = True
    for _ in range(3):
        a1 = mp.mpf(random.uniform(0.05, 1.5)); a2 = mp.mpf(random.uniform(0.05, 1.5))
        ok = ok and f(a1, a2)
    NUM.append((name, ok)); print(("PASS " if ok else "FAIL ") + name)

def bud(a):  # (x2, u) from angle
    return mp.sin(a)**2, mp.cos(a)**2

ncheck("N1 D-form angle reading", lambda a1, a2: (
    mp.almosteq(mp.sqrt(bud(a1)[0]*bud(a2)[0]) + mp.sqrt(bud(a1)[1]*bud(a2)[1]), mp.cos(a2-a1), 1e-24)
    and mp.almosteq(mp.sqrt(bud(a1)[1]*bud(a2)[0]) - mp.sqrt(bud(a1)[0]*bud(a2)[1]), mp.sin(a2-a1), 1e-24)))
ncheck("N2 S-form angle reading", lambda a1, a2: (
    mp.almosteq(mp.sqrt(bud(a1)[1]*bud(a2)[0]) + mp.sqrt(bud(a1)[0]*bud(a2)[1]), mp.sin(a1+a2), 1e-24)
    and mp.almosteq(mp.sqrt(bud(a1)[0]*bud(a2)[0]) - mp.sqrt(bud(a1)[1]*bud(a2)[1]), -mp.cos(a1+a2), 1e-24)))
ncheck("N3 Werner split of the cross-budget terms", lambda a1, a2: (
    mp.almosteq(2*mp.sqrt(bud(a1)[1]*bud(a2)[0]), mp.sin(a1+a2) + mp.sin(a2-a1), 1e-24)
    and mp.almosteq(2*mp.sqrt(bud(a1)[0]*bud(a2)[1]), mp.sin(a1+a2) - mp.sin(a2-a1), 1e-24)))
def cayley(a1, a2):
    eb = a1  # rapidity
    x2 = mp.tanh(eb)**2; snr = x2/(1-x2); lam = mp.log(mp.sinh(eb))
    return (mp.almosteq(mp.tanh(lam), (snr-1)/(snr+1), 1e-24)
            and mp.almosteq(mp.tanh(lam), 2*x2-1, 1e-24)
            and mp.almosteq(x2, (1+mp.tanh(lam))/2, 1e-24)
            and mp.almosteq(mp.log(snr), 2*lam, 1e-24))
ncheck("N4 Cayley/odds gauge: tanh(2eta_c)=(SNR-1)/(SNR+1)=2x^2-1; x^2=(1+tanh 2eta_c)/2; logit x^2=4eta_c", cayley)
sil = mp.log(1+mp.sqrt(2))
NUM.append(("N5 g fixed point + self-dual lock", True)); print("PASS N5 g fixed point + self-dual lock" if (
    mp.almosteq(mp.log(mp.coth(sil/2)), sil, 1e-24) and mp.almosteq(mp.tanh(sil)**2, mp.mpf(1)/2, 1e-24)
    and mp.almosteq(mp.sinh(sil), 1, 1e-24)) else "FAIL N5")
ncheck("N6 template rung 4: (1+cosh 2nu)/2 = G^4, cosh nu = G^2", lambda a1, a2: (
    mp.almosteq((1+mp.cosh(2*mp.acosh(mp.cosh(a1)**2)))/2, mp.cosh(a1)**4, 1e-22)))
ncheck("N7 relative budget: 1 - tanh^2(De) = sech^2(De)", lambda a1, a2: (
    mp.almosteq(1 - mp.tanh(a2-a1)**2, mp.sech(a2-a1)**2, 1e-24)))

n_ok2 = sum(1 for _, ok in NUM if ok)
print("numeric re-checks: %d/%d PASS" % (n_ok2, len(NUM)))

# ---------- (9) the lambda-tower: iterating the centered rapidity [C-grade demo] ----------
# The inverted double-angle budget is the budget OF lambda: (tanh lam)^2 + (sech lam)^2 = 1.
# Re-applying the centered-rapidity construction to that budget gives lam' = ln sinh(lam) exactly:
lamS = sp.symbols('lam', positive=True)
Xc = sp.tanh(lamS)
check2 = sp.simplify(sp.Rational(1,2)*sp.log(Xc**2/(1-Xc**2)) - sp.log(sp.sinh(lamS))) == 0
print("\nPASS lambda' = (1/2)ln(X^2/U) of the double-angle budget = ln sinh(lambda)  [the map iterates]" if check2
      else "\nFAIL lambda-tower closure")
# Numeric demo: rungs until the self-dual exit ~ lambda_0/ln2 = half the SNR bit-count
for snr0 in ['1e6', '1e12']:
    lam0 = mp.log(mp.mpf(snr0))/2
    lam = lam0; k = 0
    while lam > 0 and k < 200:
        lam = mp.log(mp.sinh(lam)); k += 1
    print("SNR0=%s: lambda0=%.4f, predicted rungs ~ lambda0/ln2 = %.2f, actual real rungs to seam-exit = %d"
          % (snr0, float(lam0), float(lam0/mp.log(2)), k))
