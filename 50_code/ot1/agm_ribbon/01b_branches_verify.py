#!/usr/bin/env python3
"""
AGM ribbon - LINK 1 continued: exact branch solutions and numerical verification.
From the Groebner basis (01_kiepert_reduction.py):
  genuine branches: 1728Z-1 != 0, lam = -4, mu = (95008 - 129777664 Z)/145,
  Z roots of 32444416 Z^2 - 17344 Z - 1 = 0  => Z = (271 +/- 145 sqrt5)/1013888.
Verify: the fractional map sends the 5 Brioschi roots exactly onto the 5 roots of
x^5+20x+16.  Then emit exact j = 1728 - 1/Z (Brioschi normalization Z_B = 1/(1728-j),
to be independently CERTIFIED formula-free in script 02 via the E-congruence).
Compute-then-grade: all intermediates printed before any comparison to ground truth.
"""
import sympy as sp
import mpmath as mp
mp.mp.dps = 60

sqrt5 = sp.sqrt(5)
branches = {}
for sgn in (+1, -1):
    Zx = sp.Rational(271, 1013888) + sgn*sp.Rational(145, 1013888)*sqrt5
    lamx = sp.Integer(-4)
    mux = (95008 - 129777664*Zx)/145
    branches[sgn] = (lamx, sp.simplify(sp.radsimp(mux)), sp.simplify(Zx))

x = sp.symbols('x')
target = x**5 + 20*x + 16

for sgn, (lamx, mux, Zx) in branches.items():
    print(f"=== branch sign {sgn:+d} ===")
    print("  Z  =", Zx, "  ~", sp.N(Zx, 30))
    print("  lam=", lamx, "  mu =", mux, "  ~", sp.N(mux, 30))
    # exact j = 1728 - 1/Z
    jx = sp.simplify(sp.radsimp(1728 - 1/Zx))
    print("  j  = 1728 - 1/Z =", jx, "  ~", sp.N(jx, 30))
    print("  j norm  =", sp.expand((jx)*(jx.subs(sqrt5, -sqrt5))), "= factor:",
          sp.factorint(int(sp.expand(jx*jx.subs(sqrt5, -sqrt5)))))
    print("  j trace =", sp.expand(jx + jx.subs(sqrt5, -sqrt5)))
    # numeric verification of the root map
    Zn = mp.mpf(int(271 + sgn*0))  # placeholder; use high-precision algebraic value
    s5 = mp.sqrt(mp.mpf(5))
    Zn = (mp.mpf(271) + sgn*145*s5)/mp.mpf(1013888)
    mun = (95008 - 129777664*Zn)/145
    lamn = mp.mpf(-4)
    # Brioschi roots
    co = [1, 0, -10*Zn, 0, 45*Zn**2, -Zn**2]
    br = mp.polyroots(co, maxsteps=200, extraprec=200)
    ys = [(lamn + mun*xk)/(xk**2/Zn - 3) for xk in br]
    resid = [abs(yk**5 + 20*yk + 16) for yk in ys]
    print("  mapped roots y_k residuals |y^5+20y+16|:", ["%.2e" % r for r in resid])
    print("  y_k =", [mp.nstr(yk, 20) for yk in ys])
    print()

print("Quintic roots of x^5+20x+16 (reference):")
qr = mp.polyroots([1, 0, 0, 0, 20, 16], maxsteps=200, extraprec=200)
for r in qr:
    print("  ", mp.nstr(r, 25))
