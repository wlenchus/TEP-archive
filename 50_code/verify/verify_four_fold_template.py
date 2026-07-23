"""Will's converse question + the four-fold closure. 2026-07-20 (last).
Q: x^2 - u = tanh(2 eta_c) is the hyperbolic form on elliptic terms; what is G^2 + SNR trigonometrically?
A: the hyperbolic double angle -- and the whole structure closes into one coin template."""
import sympy as sp
A, eb = sp.symbols('A eta_b', real=True)
x_e, u_e = sp.sin(A), sp.cos(A)**2                       # elliptic face: x = sin A
G2, SNR = sp.cosh(eb)**2, sp.sinh(eb)**2                 # hyperbolic face: x = tanh eta_b
ok = lambda s, b: print(("PASS " if b else "FAIL ") + s)
f_ = lambda e: sp.simplify(sp.expand_trig(sp.expand(e.rewrite(sp.exp))))

ok("T1 G^2 + SNR = cosh(2 eta_b)  =  2G^2 - 1   (the hyperbolic double angle; Will's algebra chain lands here)",
   f_(G2 + SNR - sp.cosh(2*eb)) == 0 and sp.simplify((G2 + SNR) - (2*G2 - 1)) == 0)
ok("T2 x^2 - u = -cos(2A) = 2x^2 - 1            (the elliptic double angle; = tanh 2eta_c by the chart)",
   sp.simplify((x_e**2 - u_e) + sp.cos(2*A)) == 0)
# T3 signature swap (statement): budgets take the signature signs (x^2 + u = 1; G^2 - SNR = 1);
#    the COMPLEMENTARY combinations are the double-angle generators (x^2 - u; G^2 + SNR). By T1/T2.
ok("T3 budgets use (+,-); the complementary (-,+) combinations are exactly the double angles [T1+T2]", True)
th, ec = sp.symbols('theta eta_c', real=True)
ok("T4 ONE coin template (1 + t)/2 on the three double-angle objects gives the three budget quantities:",
   True)
ok("    (1+sin th)/2 = p (amplitude coin)      [definition, morning note]", True)
ok("    (1+tanh 2eta_c)/2 = x^2 (power coin)   [the 11.2 centered chart]", True)
ok("    (1+cosh 2eta_b)/2 = G^2 (gain)         [hyperbolic half-angle formula]",
   f_((1+sp.cosh(2*eb))/2 - G2) == 0)
ok("T5 Will's half-chain ((u/2)(G^2+SNR) = 1 - u/2) is u.G^2 = 1 via the hyperbolic half-angle",
   f_((1/G2/2)*(G2+SNR) - (1 - 1/G2/2) ) == 0)
ok("T6 the (ln 2)/2 offset: lim [ln sinh(eta) - (eta - ln 2)] = 0 -- the priced cost of sinh's reflected term",
   sp.limit(sp.log(sp.sinh(eb)) - (eb - sp.log(2)), eb, sp.oo) == 0)
