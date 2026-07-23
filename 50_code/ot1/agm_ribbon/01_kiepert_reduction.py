#!/usr/bin/env python3
"""
AGM ribbon - LINK 1 (reviewer interpolation A, labeled):
x^5+20x+16  ->  Brioschi parameter Z_B  (classical Kiepert fractional reduction,
derived symbolically from scratch; no formulas imported from literature/memory).

Record basis (06-29 Thread D): the procedure is pinned only BY REFERENCE to
"Klein's 1884 icosahedral solution"; the record itself gives no reduction formula.
This script derives the classical reduction: roots of the Brioschi quintic
    B_Z(x) = x^5 - 10 Z x^3 + 45 Z^2 x - Z^2
are mapped by the fractional substitution
    y = (lam + mu*x) / (x^2/Z - 3)
to a quintic in y; we require that quintic to equal x^5 + 20x + 16
(already principal: y^5 + 5a y^2 + 5b y + c with a=0, b=4, c=16).

All output printed BEFORE any grading (compute-then-grade discipline).
"""
import sympy as sp

lam, mu, Z, x, y = sp.symbols('lam mu Z x y')

B = x**5 - 10*Z*x**3 + 45*Z**2*x - Z**2
# numerator form of  y*(x^2/Z - 3) - (lam + mu x),  cleared by Z:
N = y*(x**2 - 3*Z) - Z*(lam + mu*x)

print("== Deriving the transformed quintic P(y) = Res_x(B, N) / D(Z) ==")
R = sp.resultant(B, N, x)
R = sp.expand(R)

# D(Z) = prod(x_k^2 - 3Z) over Brioschi roots; independently: D = B(s)*B(-s), s=sqrt(3Z)
s = sp.sqrt(3*Z)
D = sp.expand((s**5 - 10*Z*s**3 + 45*Z**2*s - Z**2)*(-(s**5) + 10*Z*s**3 - 45*Z**2*s - Z**2))
D = sp.simplify(D)
print("D(Z) = prod(x_k^2-3Z) =", sp.factor(D))

P = sp.Poly(sp.cancel(R/D), y)
coeffs = P.all_coeffs()
print("degree in y:", P.degree(), " leading coeff:", sp.simplify(coeffs[0]))

C4 = sp.simplify(coeffs[1]); C3 = sp.simplify(coeffs[2]); C2 = sp.simplify(coeffs[3])
C1 = sp.simplify(coeffs[4]); C0 = sp.simplify(coeffs[5])
print("\nC4 (y^4 coeff) =", sp.factor(C4))
print("C3 (y^3 coeff) =", sp.factor(C3))
print("C2 (y^2 coeff) =", sp.factor(C2))
print("C1 (y^1 coeff) =", sp.factor(C1))
print("C0 (y^0 coeff) =", sp.factor(C0))

# Target: y^5 + 0*y^4 + 0*y^3 + 0*y^2 + 20*y + 16
eqs = [sp.Eq(C4, 0), sp.Eq(C3, 0), sp.Eq(C2, 0), sp.Eq(C1, 20), sp.Eq(C0, 16)]
print("\n== Solving the matching system over QQbar (groebner) ==")
polys = [sp.numer(sp.together(C4)), sp.numer(sp.together(C3)), sp.numer(sp.together(C2)),
         sp.numer(sp.together(C1 - 20)), sp.numer(sp.together(C0 - 16))]
polys = [sp.expand(p) for p in polys]
for i, p in enumerate(polys):
    print(f"  eq{i}: total degree {sp.Poly(p,[lam,mu,Z]).total_degree()}")

G = sp.groebner(polys, lam, mu, Z, order='lex')
print("\nGroebner basis (lex, lam > mu > Z):")
for g in G.exprs:
    print("  ", sp.factor(g))

# The eliminant in Z alone:
elim = [g for g in G.exprs if g.free_symbols <= {Z}]
if elim:
    EZ = sp.factor(elim[0])
    print("\nZ-eliminant:", EZ)
    roots = sp.roots(sp.Poly(elim[0], Z))
    print("Z roots (with multiplicity):")
    for r, m in roots.items():
        print("   Z =", sp.nsimplify(r), " mult", m, " approx", complex(sp.N(r, 30)))
else:
    print("\nNo pure-Z eliminant in basis; solving system directly:")
    sols = sp.solve(polys, [lam, mu, Z], dict=True)
    for sd in sols:
        print("  ", {k: sp.simplify(v) for k, v in sd.items()})

# Full solutions (lam, mu, Z):
print("\n== Full solutions (lam, mu, Z) ==")
sols = sp.solve(polys, [lam, mu, Z], dict=True)
for sd in sols:
    lam_v = sp.simplify(sd[lam]); mu_v = sp.simplify(sd[mu]); Z_v = sp.simplify(sd[Z])
    print("  lam =", lam_v, "; mu =", mu_v, "; Z =", Z_v)
    print("    numeric: lam=", complex(sp.N(lam_v, 25)), " mu=", complex(sp.N(mu_v, 25)),
          " Z=", complex(sp.N(Z_v, 25)))
