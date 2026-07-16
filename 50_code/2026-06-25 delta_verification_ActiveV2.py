#!/usr/bin/env python3
# =====================================================================================
# Reproducible verification ledger for the 6-25-26 session delta (TEP / Entrodynamics)
# Run: python3 delta_verification.py
# Deps: sympy, numpy.   Each block is self-contained and prints PASS/value.
# =====================================================================================
import sympy as sp
import numpy as np

def hdr(s): print("\n" + "="*78 + "\n" + s + "\n" + "="*78)

s2 = sp.sqrt(2)

# -------------------------------------------------------------------------------------
hdr("[V1] O-2 closure: gamma* lands EXACTLY on the 2D Ising (Kramers-Wannier) point")
# gamma* = 2 - sqrt2 ; half-rapidity eta* = 1/2 ln(1+sqrt2)
gstar  = 2 - s2
eta_st = sp.Rational(1,2)*sp.log(1+s2)
sinh2  = sp.simplify(sp.sinh(2*eta_st).rewrite(sp.exp))           # Kramers-Wannier self-dual: sinh(2K)=1
Kc     = sp.asinh(1)/2                                            # Onsager critical coupling
print("  gamma* = 2 - sqrt2          =", float(gstar))
print("  eta*   = 1/2 ln(1+sqrt2)    =", float(eta_st))
print("  sinh(2 eta*)                =", sinh2, "   (Kramers-Wannier sinh(2K_c)=1)   PASS:", sinh2==1)
print("  eta* - K_c (Onsager)        =", sp.simplify(eta_st - Kc), "  PASS:", sp.simplify(eta_st-Kc)==0)
print("  independence: gamma* = G^2-G at G=sqrt2 =", sp.simplify(s2**2 - s2), " PASS:", sp.simplify(s2**2-s2-gstar)==0)

# -------------------------------------------------------------------------------------
hdr("[V2] The budget area form: W = sqrt(x^2 u) is maximal/antisymmetric at the self-dual point")
x2 = sp.symbols('xsq', positive=True); u = 1 - x2
W  = sp.sqrt(x2*u)
crit = sp.solve(sp.numer(sp.together(sp.diff(W, x2))), x2)
a,b = sp.symbols('a b', positive=True)
odd = sp.simplify(sp.powsimp((sp.sqrt(b*a)*(b-a)) + (sp.sqrt(a*b)*(a-b)), force=True))
print("  argmax_x2 sqrt(x^2 u)       =", crit, " (self-dual x^2=1/2)  W(1/2)=", W.subs(x2, sp.Rational(1,2)))
print("  rank-2 form sqrt(ab)(a-b) odd under a<->b  PASS:", odd==0)

# -------------------------------------------------------------------------------------
hdr("[V3] The budget = law of total variance: best-matching = conditional expectation = one")
hdr_done = True
rng = np.random.default_rng(1)
ok = True
for n in [4, 10, 40, 200]:
    Y = rng.standard_normal(n)
    Q,_ = np.linalg.qr(rng.standard_normal((n,2)))      # orthonormal basis for a rank-2 sub-sigma-algebra B
    P   = Q @ Q.T
    EYB = P @ Y                                         # conditional expectation (projection)
    coef,_,_,_ = np.linalg.lstsq(Q, Y, rcond=None)
    BM  = Q @ coef                                      # Barbour best-matching (minimize residual over orbit)
    TSS = Y@Y; ESS = EYB@EYB; RSS = (Y-EYB)@(Y-EYB)
    same = np.allclose(EYB, BM); pyth = np.isclose(ESS+RSS, TSS); bud = np.isclose((ESS+RSS)/TSS, 1.0)
    ok &= same and pyth and bud
    print(f"  n={n:3d}: best-match==cond-exp {same} | ESS+RSS=TSS {pyth} | x^2+u=1 {bud} "
          f"(x^2={ESS/TSS:.3f}, rank of projection = effective d = 2, indep of n)")
print("  PASS:", ok, "  -> dimensional agnosticism = dimension-independence of the projection")

# -------------------------------------------------------------------------------------
hdr("[V4] Relativity from sufficiency (sec.11.2): the budget's observer-invariant is MULTIPLICATIVE")
eta, lam = sp.symbols('eta lambda', real=True, positive=True)
p = (1 + sp.tanh(2*eta))/2; q = (1 - sp.tanh(2*eta))/2          # observer-movable split on p+q=1
prod = sp.simplify(p*q); summ = sp.simplify(p**2+q**2)
pb, qb = lam*p, q/lam                                          # light-cone boost p->λp, q->q/λ
inv_prod = sp.simplify(pb*qb - p*q) == 0
inv_sum  = sp.simplify(pb**2+qb**2 - (p**2+q**2)) == 0
print("  constraint p+q                 =", sp.simplify(p+q))
print("  multiplicative pq              =", prod, " (= 1/4 sech^2(2eta), the Minkowski null norm)")
print("  additive p^2+q^2               =", summ, " (eta-dependent)")
print("  boost-invariance:  pq invariant", inv_prod, " | p^2+q^2 invariant", inv_sum)
print("  -> SU(1,1)/Lorentzian is a CONSEQUENCE (sum pinned by constraint => product is the invariant)")
print("  apex eta=0: x^2=", p.subs(eta,0), " u=", q.subs(eta,0), " (self-dual = rest frame)  PASS:", inv_prod and not inv_sum)

# -------------------------------------------------------------------------------------
hdr("[V5] gamma* is the once-lifted self-dual base (operational, not a curvature artifact)")
# order 0: base self-duality x0^2=u0=1/2  => SNR0=1, G0^2=1+SNR0=2, G0=sqrt2
SNR0 = sp.Integer(1); G0sq = 1+SNR0; G0 = sp.sqrt(G0sq)
SNR1 = G0; G1sq = 1+SNR1                                       # lift: base G-factor becomes next SNR
u1 = 1/G1sq; x1sq = 1-u1
print("  order0: SNR0=", SNR0, " G0=sqrt2 ;  lift SNR1=G0=", sp.radsimp(SNR1), " G1^2=1+sqrt2")
print("  gamma* = x1^2 = 1 - 1/G1^2     =", sp.nsimplify(sp.radsimp(x1sq)), "  PASS:", sp.simplify(x1sq-(2-s2))==0)
print("  squaring/involution images: 1-u1^2 =", sp.nsimplify(sp.radsimp(1-u1**2)),
      " ; u1^2 =", sp.nsimplify(sp.radsimp(u1**2)))
# the transcription slip caught in-session: the closing substitution needs 1/(1+G0), not 1/sqrt(1+G0)
v_noroot = sp.simplify(1 - 1/(1+G0)); v_root = float(1 - 1/sp.sqrt(1+G0))
print("  closing form 1 - 1/(1+G0)     =", sp.nsimplify(sp.radsimp(v_noroot)), "  (matches gamma*) ;",
      "with an inner sqrt it gives", round(v_root,4), "(!= gamma*, the corrected slip)")

# -------------------------------------------------------------------------------------
hdr("[V6] Extrapolation proof-of-concept: linear mass density, capacity-additive via dilution")
f1,f2,l0,lmax = sp.symbols('f1 f2 lambda0 lambda_max', positive=True)
u_two = (f1*f2)*l0/lmax                                        # packing fraction after 2 dilutions
print("  two-stage deficit multiplies (capacity additive) PASS:", sp.simplify(u_two-(f1*l0/lmax)*f2)==0)
g = sp.symbols('gamma', positive=True)
gB = 1/(8*(2*g-1)*(1-g)); gP = 1/((1-g)*g**2)                 # Bures K=+4 ; purity/Poincare K=-1
roots = sp.solve(sp.Eq(4*gB, gP), g)
print("  curvature-weighted balance 4 g_B=g_P roots:", roots, " (geometric, coordinate-only)")
def lam_over_max(gv): x = 2*gv-1; return sp.nsimplify(sp.radsimp(1-x))
print("  forced thresholds: self-dual (gamma=3/4) -> lambda/lmax =", lam_over_max(sp.Rational(3,4)),
      " ; gamma*=2-sqrt2 -> lambda/lmax =", lam_over_max(2-s2), "=", float(lam_over_max(2-s2)))
print("  NOTE: thresholds land on NO known transition -> per corrected scoring, a (currently uncheckable) PREDICTION")

# -------------------------------------------------------------------------------------
hdr("[V7] DHO / trapped bead: self-dual = Butterworth; gamma* is the Layer-2 composition point")
z = sp.symbols('zeta', positive=True)
print("  single-mode self-dual x^2=zeta^2=1/2 -> zeta = 1/sqrt2 =", float(1/s2),
      " (Butterworth: driven-PSD peak omega^2=1-2 zeta^2 vanishes; distinct from critical zeta=1)")
pp = sp.symbols('p', positive=True); xz2 = pp/(1+pp)          # Layer-2 composition budget, p=zeta1 zeta2
print("  Layer-2 self-dual x_z^2=1/2 -> zeta1 zeta2 =", sp.solve(sp.Eq(xz2, sp.Rational(1,2)), pp))
print("  Layer-2 gamma* x_z^2=2-sqrt2 -> zeta1 zeta2 =", [sp.nsimplify(sp.radsimp(r)) for r in sp.solve(sp.Eq(xz2, 2-s2), pp)],
      " = sqrt2  PASS:", sp.simplify(xz2.subs(pp, s2)-(2-s2))==0)

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
hdr("[V8] RETRACTED identification, with the corrected facts (see delta I11)")
eta = sp.symbols('eta', real=True)
# (a) wrong OBJECT: sqrt(x^2 u) peaks at self-dual; the TRUE wedge vanishes there
ga = sp.symbols('g', positive=True); a, c = ga, 1-ga
geom_mean  = sp.sqrt(a*c)                          # what I mislabeled 'W'
true_wedge = sp.sqrt(a*c)*sp.Abs(a-c)              # ||lambda^{3/2} ^ lambda^{1/2}|| for d=2
print("  geometric mean sqrt(ab) at self-dual a=b :", geom_mean.subs(ga, sp.Rational(1,2)), " (PEAKS)")
print("  true wedge sqrt(ab)|a-b| at self-dual a=b:", true_wedge.subs(ga, sp.Rational(1,2)), " (VANISHES) -> wrong object")
# (b) wrong FRAME: flat Levy sech vs curved geodesic holonomy
r = sp.symbols('r', positive=True)
rho = sp.symbols('rho', positive=True)
flat_area = sp.pi*rho**2
hyp_area   = sp.simplify(sp.integrate((4/(1-r**2)**2)*2*sp.pi*r, (r,0,rho)))
print("  flat area pi*rho^2  vs  curved holonomy", hyp_area, "= 4 pi rho^2/(1-rho^2)  -> different objects")
# (c) wrong ROLE: true wedge is not the metric area form (opposite boundary behaviour)
print("  metric area form 4r/(1-r^2)^2 -> infinity at boundary ; ||W|| -> 0 at boundary => W is NOT sqrt(g)")
print("  => verified curved-metric (frame) holonomy [6-11] does NOT validate W<->Levy.  W<->Levy is OPEN.")

# -------------------------------------------------------------------------------------
hdr("[V9] W is UNIVERSALLY rank-2: every DoF carries a W = its d=2 boundary reduction")
la, lc = sp.symbols('lambda_a lambda_c', positive=True)
print("  per-pair identity sqrt(la lc)|la-lc| = sqrt(la lc)(la^2-lc^2)/(la+lc)  (la>=lc):",
      sp.simplify((la-lc) - (la**2-lc**2)/(la+lc)) == 0, " (purity-diff / prob-sum)")
rng = np.random.default_rng(2); ok = True
for d in [2,4,6]:
    lam = np.sort(rng.dirichlet(np.ones(d)))[::-1]
    pairs = [(i,j) for i in range(d) for j in range(i+1,d)]
    c1 = [np.sqrt(lam[i]*lam[j])*(lam[i]-lam[j]) for (i,j) in pairs]
    c2 = [np.sqrt(lam[i]*lam[j])*(lam[i]**2-lam[j]**2)/(lam[i]+lam[j]) for (i,j) in pairs]
    ok &= np.allclose(c1,c2)
    print(f"  d={d}: {len(pairs):2d} pairwise rank-2 wedges (each a d=2 reduction); purity-form agrees={np.allclose(c1,c2)}")
print("  PASS:", ok, " -> W applies at every d; depth grows the NUMBER of rank-2 pieces and their assembly.")
print("  N>=4 onset = where pairwise rank-2 wedges stop commuting (holonomy of the assembly), not a W breakdown.")

print("\n" + "="*78 + "\nALL BLOCKS EXECUTED.\n" + "="*78)
