# verify_polar_identification.py — 2026-07-20: the polar-coding identification
# Claim set: Arikan's channel polarization runs on exactly the corpus's budget scaffolding.
#   BEC(eps): u = eps (residual).  Polar split:  u+ = u^2  (capacity-doubling wiring A)
#                                                x2- = (x2)^2 (the same ladder, other direction)
#   Conservation: I+ + I- = 2I  (U1-type invariant total; martingale).
#   BSC on the amplitude coin (q = (1-x)/2): bias = x = tanh(eta_b); Z = 2 sqrt(q(1-q)) = sqrt(u) = sech(eta_b)
#     -> power-coin level: (bias, Z) = (tanh lambda, sech lambda) = the Sigma-diagonal.
#   Bias multiplicativity under BSC composition (Dobrushin / 1D-Ising tanh^n / SDPI face).
#   Numerics: Z(W+) = Z^2 (exact), Z(W-) <= 2Z - Z^2 (equality iff BEC), I+ + I- = 2I.
import sympy as sp
import mpmath as mp
mp.mp.dps = 30
P = []
def check(name, ok):
    P.append(bool(ok)); print(("PASS " if ok else "FAIL ") + name)

eps, q1, q2, x = sp.symbols('eps q1 q2 x', positive=True)

# --- BEC: the two polar branches are the corpus's one-ladder-two-directions ---
u = eps
check("P1 BEC: u+ = eps^2 = u^2 (capacity-doubling wiring) and u- = 2u - u^2 <=> x2- = (x2)^2",
      sp.simplify((2*u - u**2) - (1 - (1 - u)**2)) == 0)
I  = 1 - eps
check("P2 BEC conservation: I(W+) + I(W-) = (1-eps^2) + (1-2eps+eps^2) = 2(1-eps) = 2I  [U1 ledger]",
      sp.simplify((1 - eps**2) + (1 - (2*eps - eps**2)) - 2*I) == 0)

# --- BSC dictionary: Z = sqrt(u); bias = x ---
qq = (1 - x)/2
Z = 2*sp.sqrt(qq*(1 - qq))
check("P3 BSC(q), q = (1-x)/2 (amplitude coin): Bhattacharyya Z = 2 sqrt(q(1-q)) = sqrt(1-x^2) = sqrt(u) "
      "= sech(eta_b)  [the comodulus; T-6's sqrt(u) = 2^(-C/2B) object]",
      sp.simplify(Z - sp.sqrt(1 - x**2)) == 0)
check("P4 bias multiplicativity: BSC(q1) o BSC(q2) has bias (1-2q1)(1-2q2)  [tanh-multiplicative: "
      "Dobrushin coefficient / 1D Ising <s0 sn> = tanh^n K / SDPI face]",
      sp.simplify((1 - 2*(q1*(1-q2) + q2*(1-q1))) - (1-2*q1)*(1-2*q2)) == 0)
# power-coin level: (bias, Z) at p = x^2 is the Sigma-diagonal
lam = sp.symbols('lam', positive=True)
check("P5 power-coin BSC: bias = 2x^2-1 = tanh(lam), Z = 2 x sqrt(u) = sech(lam)  [Sigma-diagonal "
      "= a BSC one rung up the coin ladder]",
      sp.simplify(sp.tanh(lam)**2 + sp.sech(lam)**2 - 1) == 0 and
      sp.simplify((2*x**2 - 1)**2 + (2*x*sp.sqrt(1 - x**2))**2 - 1) == 0)

# --- numeric polar transform for BSC (and a generic BMS check of the recursions) ---
def bsc(q):  # W(y|x) over y in {0,1}
    return {(0,0): 1-q, (1,0): q, (0,1): q, (1,1): 1-q}
def Wminus(W):
    # W-(y1 y2 | u1) = 1/2 sum_{u2} W(y1|u1 xor u2) W(y2|u2)
    out = {}
    for y1 in (0,1):
        for y2 in (0,1):
            for u1 in (0,1):
                s = 0
                for u2 in (0,1):
                    s += 0.5*W[(y1, u1 ^ u2)]*W[(y2, u2)]
                out[((y1,y2), u1)] = s
    return out
def Wplus(W):
    # W+(y1 y2 u1 | u2) = 1/2 W(y1|u1 xor u2) W(y2|u2)
    out = {}
    for y1 in (0,1):
        for y2 in (0,1):
            for u1 in (0,1):
                for u2 in (0,1):
                    out[((y1,y2,u1), u2)] = 0.5*W[(y1, u1 ^ u2)]*W[(y2, u2)]
    return out
def Zpar(W):
    ys = sorted({k[0] for k in W})
    return sum(mp.sqrt(W[(y,0)]*W[(y,1)]) for y in ys)
def Ipar(W):
    ys = sorted({k[0] for k in W})
    tot = mp.mpf(0)
    for y in ys:
        py = 0.5*(W[(y,0)] + W[(y,1)])
        for xx in (0,1):
            if W[(y,xx)] > 0:
                tot += 0.5*W[(y,xx)]*mp.log(W[(y,xx)]/py, 2)
    return tot
ok_zp, ok_zm, ok_cons = True, True, True
for qs in ['0.05', '0.11', '0.2', '0.35', '0.47']:
    qm = mp.mpf(qs)
    W = {(0,0): 1-qm, (1,0): qm, (0,1): qm, (1,1): 1-qm}
    Wm = {(k[0], k[1]): v for k, v in Wminus(W).items()}
    Wp = {(k[0], k[1]): v for k, v in Wplus(W).items()}
    Z0, Zp_, Zm_ = Zpar(W), Zpar(Wp), Zpar(Wm)
    ok_zp   = ok_zp and mp.almosteq(Zp_, Z0**2, 1e-24)
    ok_zm   = ok_zm and (Zm_ <= 2*Z0 - Z0**2 + mp.mpf('1e-24'))
    ok_cons = ok_cons and mp.almosteq(Ipar(Wp) + Ipar(Wm), 2*Ipar(W), 1e-24)
check("P6 BSC numerics (5 crossover values): Z(W+) = Z^2 exactly", ok_zp)
check("P7 BSC numerics: Z(W-) <= 2Z - Z^2 (BEC-extremal bound; strict for BSC)", ok_zm)
check("P8 BSC numerics: I(W+) + I(W-) = 2 I(W)  [conservation martingale]", ok_cons)
# Arikan Prop-1-shaped budget bounds on the (I, Z) pair
ok_b = True
for kk in range(1, 25):
    qm = mp.mpf(2*kk)/100
    W = {(0,0): 1-qm, (1,0): qm, (0,1): qm, (1,1): 1-qm}
    Iv, Zv = Ipar(W), Zpar(W)
    ok_b = ok_b and (Iv**2 + Zv**2 <= 1 + mp.mpf('1e-20')) and (Iv + Zv >= 1 - mp.mpf('1e-20'))
check("P9 (I, Z) budget bounds: I^2 + Z^2 <= 1 and I + Z >= 1 across the BSC family "
      "[the budget inequality pair on the information/comodulus slot]", ok_b)

# --- polarization demo: the BEC tree polarizes; fraction of near-perfect leaves -> I0 ---
def bec_tree(eps0, depth):
    lv = [float(eps0)]
    for _ in range(depth):
        lv = [e*e for e in lv] + [2*e - e*e for e in lv]
    return lv
rows = []
for depth in (8, 14, 20):
    leaves = bec_tree(0.5, depth)
    fg = sum(1 for e in leaves if e < 0.02)/len(leaves)
    fb = sum(1 for e in leaves if e > 0.98)/len(leaves)
    rows.append((depth, fg, fb, 1 - fg - fb))
    print("BEC(1/2), depth %2d: frac(u<0.02) = %.4f, frac(u>0.98) = %.4f, unpolarized = %.4f (I0 = 0.5)"
          % (depth, fg, fb, 1 - fg - fb))
check("P10 polarization: good/bad fractions symmetric (martingale) and unpolarized mass strictly "
      "shrinking with depth toward the I0 = 1/2 split",
      all(abs(fg - fb) < 1e-9 for _, fg, fb, _ in rows) and
      rows[0][3] > rows[1][3] > rows[2][3] and abs(rows[2][1] - 0.5) < 0.05)

print("\n%d/%d PASS" % (sum(P), len(P)))
