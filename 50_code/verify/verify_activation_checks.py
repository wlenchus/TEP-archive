# verify_activation_checks.py — 2026-07-20, countersign turn
# Checks Will's proposed identities (with two corrections) + the exponential-family reading
# + the corrected pair-expansion + Gram/triangle content + the Mercator naming.
import sympy as sp
import mpmath as mp
mp.mp.dps = 30
P = []
def check(name, ok):
    P.append(bool(ok)); print(("PASS " if ok else "FAIL ") + name)

et, th, x = sp.symbols('eta theta x', positive=True)
A1, A2 = sp.symbols('A1 A2', positive=True)

# (1) cosh as sinh/tanh (division, not multiplication)
check("W1 sinh(2e)/tanh(2e) = cosh(2e)   [the intended identity]",
      sp.simplify(sp.sinh(2*et)/sp.tanh(2*et) - sp.cosh(2*et)) == 0)
# (2) the multiplied version holds only at sinh(2e)=1, i.e. 2e = silver rapidity
sol = mp.findroot(lambda e: 1/(mp.sinh(2*e)*mp.tanh(2*e)) - mp.cosh(2*e), mp.mpf('0.4'))
check("W2 1/(sinh*tanh)=cosh only at sinh(2e)=1: root 2e = ln(1+sqrt2) (half-silver eta)",
      mp.almosteq(2*sol, mp.log(1+mp.sqrt(2)), 1e-24))
# (3) the x-antiderivative of the foil: d/dx[2 artanh x - x] = cosh(2 eta_b) = 2G^2-1
check("W3 d/dx[2 artanh x - x] = (1+x^2)/(1-x^2) = cosh(2 artanh x)  [foil's ledger = 2eta - x]",
      sp.simplify(sp.diff(2*sp.atanh(x) - x, x) - sp.cosh(2*sp.atanh(x))) == 0)
# (4) exponential-family reading: psi = ln cosh; mean^2 + Fisher = 1 at EVERY natural parameter
psi = sp.log(sp.cosh(th))
check("W4 psi=ln cosh: psi'=tanh (mean), psi''=sech^2 (Fisher/Var), mean^2+Fisher=1",
      sp.simplify(sp.diff(psi, th) - sp.tanh(th)) == 0 and
      sp.simplify(sp.diff(psi, th, 2) - sp.sech(th)**2) == 0 and
      sp.simplify(sp.tanh(th)**2 + sp.sech(th)**2 - 1) == 0)
# hence: standard budget = the identity at theta = eta_b; inverted budget = at theta = lambda = 2 eta_c
# (5) G is the fair coin's MGF at eta_b: E[e^{eta s}] = cosh eta
check("W5 (e^t + e^-t)/2 = cosh t  [G = MGF of the sign bit]",
      sp.simplify((sp.exp(et) + sp.exp(-et))/2 - sp.cosh(et)) == 0)
# (6) corrected expansion of u_rel = cos^2(A2-A1): cross term is the product of Sigma-diagonal legs
u_rel = sp.cos(A2-A1)**2
expand_ok = sp.simplify(sp.expand_trig(
    u_rel - (sp.sin(A1)**2*sp.sin(A2)**2 + sp.cos(A1)**2*sp.cos(A2)**2
             + sp.Rational(1,2)*sp.sin(2*A1)*sp.sin(2*A2)))) == 0
check("W6 u_rel = x1^2 x2^2 + u1 u2 + (1/2) sin(2A1) sin(2A2)   [corrected expansion]", expand_ok)
# (7) the four-term form is NOT u_rel (counterexample at A1=A2=A: LHS=1, RHS=2 sin 2A)
a = mp.mpf('0.6')
four_term = (mp.sin(a)+mp.sin(a))*(mp.cos(a)+mp.cos(a))  # (sqrt x1^2 + sqrt x2^2)(sqrt u1 + sqrt u2)
check("W7 four-term product != cos^2(Delta) (at A1=A2=0.6: %.4f vs 1)" % float(four_term),
      abs(four_term - 1) > 0.5)
# (8) affinity = inner product of unit coin vectors; d-outcome Bhattacharyya generalization
v1 = mp.matrix([mp.sin(a), mp.cos(a)]); b = mp.mpf('1.1'); v2 = mp.matrix([mp.sin(b), mp.cos(b)])
inner = v1[0]*v2[0] + v1[1]*v2[1]
check("W8 cos(Delta) = <v1, v2> on the sqrt-coin sphere  [Gram entry]",
      mp.almosteq(inner, mp.cos(b-a), 1e-24))
# 3-outcome Bhattacharyya: sum sqrt(p_i q_i) <= 1, equality iff p=q  (spot)
p3 = [mp.mpf('0.5'), mp.mpf('0.3'), mp.mpf('0.2')]; q3 = [mp.mpf('0.2'), mp.mpf('0.5'), mp.mpf('0.3')]
aff3 = sum(mp.sqrt(pi*qi) for pi, qi in zip(p3, q3))
check("W9 d=3 Bhattacharyya affinity < 1 for p != q (%.6f)" % float(aff3), aff3 < 1)
# (9) triangle inequality of arcs (the Gram/PSD content statement, flat at d=2)
c = mp.mpf('2.1')
arc = lambda s, t: mp.acos(mp.cos(t-s))
check("W10 arc(1,3) <= arc(1,2)+arc(2,3)  [coin-circle triangle inequality]",
      arc(a, c) <= arc(a, b) + arc(b, c) + mp.mpf('1e-25'))
# (10) Mercator naming: lambda = ln tan A = isometric latitude of the centered double angle
phi = 2*mp.asin(mp.tanh(mp.mpf('1.3'))) - mp.pi/2      # centered double angle = geographic latitude
lam = mp.log(mp.sinh(mp.mpf('1.3')))                    # = ln tan A
check("W11 lambda = ln tan(pi/4 + phi/2)  [isometric/Mercator latitude of the centered angle]",
      mp.almosteq(lam, mp.log(mp.tan(mp.pi/4 + phi/2)), 1e-24))

print("\n%d/%d PASS" % (sum(P), len(P)))
