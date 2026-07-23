"""Verification: the affinity-distillation identity. 2026-07-19 (late tangent, self-directed).
Thread: R3.3 / Apr-20 never-run prediction "distillation rate ~ prod sech^2(Delta eta_i)"
vs this session's pair-budget (affinity of adjacent budget states).
Conventions: x = sin A = tanh eta, u = 1 - x^2, C_nats = ln cosh eta, A = gd(eta).
Two difference-budgets for a pair of budget states:
  boost chart:  sqrt(u_rel) = sech(eta1 - eta2)  (residual amplitude of the relative state)
  angle chart:  affinity = cos(A1 - A2) = x1 x2 + sqrt(u1 u2)  (Gram overlap of amplitude vectors)
Result: they differ by an EXACT side-bit-signed term. 12 checks. All symbolic unless noted.
"""
import sympy as sp
import numpy as np
e1, e2, t = sp.symbols('eta1 eta2 t', real=True)
x1s, x2s = sp.tanh(e1), sp.tanh(e2)
res = []
def ok(n, b): res.append(bool(b)); print(("PASS " if b else "FAIL ") + n)
f_ = lambda expr: sp.simplify(sp.expand(expr.rewrite(sp.exp)))

# X1 [numeric]: cos(gd e1 - gd e2) = tanh tanh + sech sech  — anchors the angle-chart affinity
dA = sp.atan(sp.sinh(e1)) - sp.atan(sp.sinh(e2))
aff_gd = sp.cos(dA)
aff = x1s*x2s + 1/(sp.cosh(e1)*sp.cosh(e2))     # = x1x2 + sqrt(u1u2), the working form
ok("X1 cos(A1-A2) = x1x2 + sqrt(u1u2) = tanh.tanh + sech.sech  [numeric 1e-12, mixed signs]",
   all(abs(float((aff_gd - aff).subs({e1: a, e2: b}))) < 1e-12
       for a,b in [(0.7,0.2),(1.5,-0.8),(-0.3,-2.1),(2.0,0.0)]))

sech_rel = 1/sp.cosh(e1-e2)
gap = aff - sech_rel

# X2: THE IDENTITY (exact, symbolic)
ok("X2 EXACT: cos(dA) - sech(d.eta) = x1*x2*(1 - sech(d.eta))",
   f_(gap - x1s*x2s*(1 - sech_rel)) == 0)

# X3 [numeric grid]: sign(gap) = side-bit product; zero iff x1x2 = 0 or coincidence
gf = sp.lambdify((e1, e2), gap, 'numpy')
oks = True
for a in np.linspace(-2.5, 2.5, 9):
    for b in np.linspace(-2.5, 2.5, 9):
        g = float(gf(a, b))
        if abs(a) < 1e-12 or abs(b) < 1e-12 or abs(a-b) < 1e-12: oks &= abs(g) < 1e-12
        else: oks &= np.sign(g) == np.sign(a)*np.sign(b)
ok("X3 sign(gap) = side-bit product s1*s2; gap = 0 iff x1x2 = 0 or eta1 = eta2  [9x9 grid]", oks)

# X4: convex-combination reading
ok("X4 cos(dA) = (1 - x1x2)*sech(d.eta) + x1x2  (affinity interpolates sech_rel -> 1 with weight x1x2)",
   f_(aff - ((1-x1s*x2s)*sech_rel + x1s*x2s)) == 0)

# X5: halving-map face: gap = x1x2 * sqrt(u_rel) * (G_rel - 1); via X2 and the one-variable
#     identity 1 - sech t = sech t (cosh t - 1)  (kept single-variable so simplify is instant)
ok("X5 1 - sech(t) = sech(t)(cosh(t)-1); with X2 => gap = x1*x2*sqrt(u_rel)*(G_rel - 1)",
   sp.simplify(1 - 1/sp.cosh(t) - (1/sp.cosh(t))*(sp.cosh(t)-1)) == 0)

# X6 [numeric]: small-step at a common anchor: gap -> (1/2)(Delta C_nats)^2
oks = True
for eta0 in [0.4, 1.0, 2.2]:
    d = 1e-4
    g = float(gf(eta0+d/2, eta0-d/2))
    dC = float(np.log(np.cosh(eta0+d/2)) - np.log(np.cosh(eta0-d/2)))
    oks &= abs(g/(0.5*dC**2) - 1) < 1e-2
ok("X6 small-step: gap -> (1/2)(Delta C_nats)^2  (half the squared capacity step)", oks)

# X7: N=2 Gram spectrum = amplitude coin of the difference angle; condition number = pair SWR
c = sp.Symbol('c', real=True)
lam = set(sp.Matrix([[1, c],[c, 1]]).eigenvals().keys())
ok("X7a Gram eigenvalues {1±cos dA}: normalized halves = the amplitude coin of dA",
   {sp.simplify(l - (1+c)) == 0 or sp.simplify(l - (1-c)) == 0 for l in lam} == {True})
ok("X7b det Gram = sin^2(dA) = pair-budget noise; cond# = (1+cos dA)/(1-cos dA) = cot^2(dA/2) = pair SWR",
   sp.simplify(sp.expand((1+c)*(1-c)) - (1-c**2)) == 0 and
   all(abs(float(((1+sp.cos(t))/(1-sp.cos(t)) - sp.cot(t/2)**2).subs(t, v))) < 1e-12 for v in [0.4, 1.2, 2.6]))

# X8: the pair is itself a budget state: x_pair = cos dA, u_pair = det Gram
ok("X8 x_pair^2 + u_pair = 1 with x_pair = cos(dA), u_pair = sin^2(dA)",
   sp.simplify(sp.cos(t)**2 + sp.sin(t)**2 - 1) == 0)

# X9: the false near-identity, killed properly (exact only at the origin-anchored case)
ok("X9 cos(dA) != sech(d.eta) generically; equality at eta2 = 0",
   abs(float(gf(1.3, 0.6))) > 1e-3 and abs(float(gf(1.3, 0.0))) < 1e-15)

# X10 [numeric]: N=3 same-side ordering for the recorded product form
etas = [0.9, 0.5, 0.2]
P_sech = float(np.prod([1/np.cosh(a-b)**2 for i,a in enumerate(etas) for b in etas[i+1:]]))
afff = sp.lambdify((e1, e2), aff, 'numpy')
P_aff = float(np.prod([afff(a,b)**2 for i,a in enumerate(etas) for b in etas[i+1:]]))
ok("X10 same-side ensemble: prod cos^2(dA) >= prod sech^2(d.eta) (the recorded distillation product is the lower bound)",
   P_aff >= P_sech)
print(f"   N=3 same-side example: prod sech^2 = {P_sech:.6f}  <=  prod cos^2(dA) = {P_aff:.6f}")

print(f"\n{sum(res)}/{len(res)} PASS")
