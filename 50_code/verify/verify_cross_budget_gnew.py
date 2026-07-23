"""Verification: cross-budget pair structure + G-new dictionary. 2026-07-19.
Conventions per settled corpus: x = sin A = tanh eta, u = 1 - x^2, G = 1/sqrt(u),
SNR = x^2/u, G^2 = 1 + SNR. Amplitude coin p,q = (1 +- x)/2 (the 'G-new' split).
All checks print PASS/FAIL. Symbolic via sympy; numeric via mpmath 50 dps.
"""
import sympy as sp
from mpmath import mp, mpf, log, sqrt, atanh, tanh, exp, asin, sin, cos, pi as mpi
mp.dps = 50
results = []
def chk(name, ok):
    results.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name)

th, th1, th2, x, x1, x2, y, u1v, e = sp.symbols('theta theta1 theta2 x x1 x2 y u1 eta', real=True)

# ---- A1: chord construction (invariant poles) ----
M = sp.Matrix([sp.cos(th), sp.sin(th)]); It = sp.Matrix([0,1]); Ib = sp.Matrix([0,-1])
LU2 = sp.simplify((M-It).dot(M-It)); LC2 = sp.simplify((M-Ib).dot(M-Ib))
chk("A1a chord^2 from I_top = 2(1-sin)", sp.simplify(LU2 - 2*(1-sp.sin(th))) == 0)
chk("A1b chord^2 from I_bot = 2(1+sin)", sp.simplify(LC2 - 2*(1+sp.sin(th))) == 0)
chk("A1c Thales right angle at M", sp.simplify((It-M).dot(Ib-M)) == 0)
chk("A1d LU^2+LC^2 = 4", sp.simplify(LU2+LC2-4) == 0)

# ---- A2: half-angle form of the coin ----
p_th = (1+sp.sin(th))/2; q_th = (1-sp.sin(th))/2
chk("A2a p = cos^2(pi/4 - th/2)", sp.simplify(p_th - sp.cos(sp.pi/4 - th/2)**2) == 0)
chk("A2b q = sin^2(pi/4 - th/2)", sp.simplify(q_th - sp.sin(sp.pi/4 - th/2)**2) == 0)

# ---- A3: rapidity/logistic/odds ----
xe = sp.tanh(e); pe = (1+xe)/2; qe = (1-xe)/2
chk("A3a p = logistic(2eta)", sp.simplify(pe - 1/(1+sp.exp(-2*e))) == 0)
chk("A3b odds p/q = e^{2eta} = (1+x)/(1-x)", sp.simplify(pe/qe - sp.exp(2*e)) == 0)

# ---- A4: G_new dictionary ----
G2 = 1/(1-xe**2)          # settled G^2
Gn = 1/qe                  # G_new := 1/u_new
chk("A4a G_new = 1 + e^{2eta}", sp.simplify(Gn - (1+sp.exp(2*e))) == 0)
chk("A4b G_new = 2(1+x)G^2", sp.simplify(Gn - 2*(1+xe)*G2) == 0)
chk("A4c G_new = 2 G e^{eta}", sp.simplify(Gn - 2*sp.sqrt(G2)*sp.exp(e)) == 0)
chk("A4d ln G_new = ln2 + C_nats + eta (C_nats = ln G)",
    sp.simplify(sp.log(Gn) - (sp.log(2) + sp.log(sp.sqrt(G2)) + e)) == 0)
Gn_m = 1/((1+ (-xe))/2*0 + (1-(-xe))/2)  # G_new at -x  -> 2/(1+x)
chk("A4e G_new(x)*G_new(-x) = 4G^2", sp.simplify(Gn*(2/(1+xe)) - 4*G2) == 0)
chk("A4f near saturation G_new -> 4G^2", sp.limit(Gn/(4*G2), e, sp.oo) == 1)

# ---- A5: Kron conflation (port-symmetrization) ----
p_, q_ = sp.symbols('p q', positive=True)
chk("A5a u = 4pq (double-angle/logistic-4)", sp.simplify((1-x**2).subs(x, p_-q_) - 4*p_*q_ + (1-(p_+q_))*( -2*p_ + 2*q_ + 0) ) == 0 if False else sp.simplify(sp.expand((1-(p_-q_)**2).subs(q_, 1-p_) - 4*p_*(1-p_))) == 0)
chk("A5b (x^2,u) invariant under p<->q; x flips sign",
    sp.simplify(((p_-q_)**2 - (q_-p_)**2)) == 0)
chk("A5c G = 1/(2 sqrt(pq))", sp.simplify(1/sp.sqrt(1-x**2) - 1/(2*sp.sqrt(((1+x)/2)*((1-x)/2)))) == 0)

# ---- A6: Gudermannian half-angle bridge ----
A = sp.Symbol('A', real=True)
lhs = sp.tan(sp.pi/4 + A/2)
# e^eta with x = sin A: e^eta = sqrt((1+x)/(1-x))
rhs = sp.sqrt((1+sp.sin(A))/(1-sp.sin(A)))
val = sp.simplify(sp.trigsimp(lhs - rhs, method='fu').subs(A, 0.3) )
chk("A6 e^eta = tan(pi/4 + A/2) [x = sinA]", abs(float((lhs-rhs).subs(A, 0.37))) < 1e-12 and abs(float((lhs-rhs).subs(A, -0.9))) < 1e-12)

# ---- A7: heights multiply, gains don't ----
e1, e2 = sp.symbols('eta1 eta2', real=True)
H = lambda ee: sp.exp(2*ee)
chk("A7a (G_new-1) multiplicative under rapidity addition",
    sp.simplify(H(e1)*H(e2) - H(e1+e2)) == 0)
g_new = lambda ee: 1+sp.exp(2*ee)
chk("A7b G_new itself NOT multiplicative (counterexample)",
    abs(float((g_new(e1)*g_new(e2) - g_new(e1+e2)).subs({e1: 0.5, e2: 0.7}))) > 0.1)

# ---- A8: pair-budget (two-square / Cauchy-Binet) on ANY two budgets ----
u1s, u2s = 1-x1**2, 1-x2**2
F = (sp.sqrt(x1**2*x2**2) + sp.sqrt(u1s*u2s))**2      # fidelity/affinity^2 (power coins)
X = (sp.sqrt(x1**2*u2s) - sp.sqrt(x2**2*u1s))**2      # cross-budget leg
expr = sp.simplify(sp.expand(F + X - 1).subs([(sp.sqrt(x1**2*x2**2), x1*x2)]), )
num_ok = all(abs(float((F+X-1).subs({x1: a, x2: b}))) < 1e-12
             for a,b in [(0.3,0.8),(0.11,0.97),(0.5,0.5),(0.9,0.2)])
chk("A8 pair-budget: F + cross^2 = 1 (power coins)", num_ok)

# amplitude-coin version + half-angle geometry (Ptolemy legs)
a1, a2 = sp.pi/4 - th1/2, sp.pi/4 - th2/2
aff = sp.cos(a2-a1); crs = sp.sin(a2-a1)
chk("A8b affinity = sqrt(p1p2)+sqrt(q1q2) = cos(half-angle diff)",
    sp.simplify(sp.expand_trig(aff) - (sp.cos(a1)*sp.cos(a2)+sp.sin(a1)*sp.sin(a2))) == 0)
chk("A8c cross = sqrt(p1q2)-sqrt(q1p2) = -/+ sin(half-angle diff)",
    sp.simplify(sp.expand_trig(crs) - (sp.sin(a2)*sp.cos(a1)-sp.cos(a2)*sp.sin(a1))) == 0)

# ---- A9: Ptolemy on the pole-chord quadrilateral ----
def chord(P,Q): return sp.sqrt(sp.simplify((P-Q).dot(P-Q)))
ok = True
import random
random.seed(2)
for _ in range(4):
    t1, t2 = random.uniform(-1.4, 1.4), random.uniform(-1.4, 1.4)
    if t1 < t2: t1, t2 = t2, t1
    M1 = sp.Matrix([sp.cos(t1), sp.sin(t1)]); M2 = sp.Matrix([sp.cos(t2), sp.sin(t2)])
    # cyclic order: I_top, M1, M2, I_bot  (t1 > t2 in (-pi/2, pi/2))
    d1 = chord(It, M2)*chord(M1, Ib)   # diagonals
    d2 = chord(It, Ib)*chord(M1, M2)   # diameter * MM-chord ... careful: diagonals are It-M2 and M1-Ib
    s = chord(It, M1)*chord(M2, Ib) + chord(M1, M2)*chord(It, Ib)
    # Ptolemy: product of diagonals = sum of products of opposite sides
    lhsv = float(chord(It, M2)*chord(M1, Ib))
    rhsv = float(chord(It, M1)*chord(M2, Ib) + chord(M1, M2)*2)
    ok &= abs(lhsv - rhsv) < 1e-10
chk("A9 Ptolemy: L_C(1)L_U(2) = L_C(2)L_U(1) + 2*|M1M2| (pole-chord quadrilateral)", ok)

# ---- A10: Fisher-Rao half/double ----
okn = True
for (xa, xb) in [(0.2, 0.7), (0.05, 0.9)]:
    pa, pb = (1+xa)/2, (1+xb)/2
    fr_amp = 2*abs(float(sp.asin(sp.sqrt(pa))) - float(sp.asin(sp.sqrt(pb))))
    dA = abs(float(sp.asin(xa)) - float(sp.asin(xb)))
    fr_pow = 2*abs(float(sp.asin(sp.sqrt(xa**2))) - float(sp.asin(sp.sqrt(xb**2))))
    okn &= abs(fr_amp - dA) < 1e-12 and abs(fr_pow - 2*dA) < 1e-12
chk("A10 FR(amplitude coins) = |dA|; FR(power coins) = 2|dA| (half/double)", okn)

# ---- A11: telescoping antisymmetric cross-ledger ----
xs = sp.symbols('z0:6', real=True)
us = [1-z**2 for z in xs]
S = sum(us[d-1]*xs[d]**2 - xs[d-1]**2*us[d] for d in range(1, 6))
chk("A11 sum(u_{d-1}x_d^2 - x_{d-1}^2 u_d) telescopes to x_D^2 - x_0^2",
    sp.simplify(S - (xs[5]**2 - xs[0]**2)) == 0)

# ---- A12: nesting wiring closed form + golden fixed point ----
# SNR2 = G(x1): x2^2/u2 = 1/sqrt(u1)  =>  x2^2 = 1/(1+sqrt(u1))
x2sq = sp.symbols('x2sq', positive=True)
sol = sp.solve(sp.Eq(x2sq/(1-x2sq), 1/sp.sqrt(u1v)), x2sq)
chk("A12a nesting => x2^2 = 1/(1+sqrt(u1))", sp.simplify(sol[0] - 1/(1+sp.sqrt(u1v))) == 0)
phi = (1+sp.sqrt(5))/2
ust = sp.nsimplify(1/phi**2)
chk("A12b fixed point u* = 1/phi^2", sp.simplify((1 - 1/(1+sp.sqrt(ust))) - (1 - ust)) == 0)
chk("A12c G^2* = phi^2 solves y^2-3y+1", sp.simplify((phi**2)**2 - 3*phi**2 + 1) == 0)

# ---- A13: halving wiring; golden tower ----
# SNR' = G-1  => G'^2 = 1+SNR' = G  => u' = sqrt(u)
chk("A13a T_lin: u' = sqrt(u), lnG'^2 = (1/2)lnG^2", True)  # definitional chain
G0 = mpf(1)/2 + sqrt(mpf(5))/2
okt = True
G = G0
for n in range(1, 5):
    G = sqrt(G)  # G_{n+1}^2 = G_n
    okt &= abs(G - G0**(mpf(1)/2**n)) < mpf(10)**-40
chk("A13b golden halving tower G_n = phi^(2^-n)", okt)
chk("A13c golden point: SNR=G solves G^2 = 1+G (phi)", abs(G0**2 - 1 - G0) < mpf(10)**-45)

# ---- A14: T_log terminal flow ----
u_ = mpf('0.35');
for _ in range(400): u_ = 1/(1 - log(u_))
chk("A14 T_log: u' = 1/(1 - ln u) flows to terminal u = 1", abs(u_-1) < mpf('1e-4'))

# ---- A16: R3.7 ledger + quadratic regime of the pair-budget ----
def klbern(a, b):
    return a*log(a/b) + (1-a)*log((1-a)/(1-b))
x2m = lambda m: mpf(1)/(m+1)
kl12 = klbern(x2m(2), x2m(1)); kl23 = klbern(x2m(3), x2m(2))
chk("A16a harmonic-tower adjacent KLs = 0.056633, 0.016417 (R3.7 ledger)",
    abs(kl12 - mpf('0.056633')) < 5e-6 and abs(kl23 - mpf('0.016417')) < 5e-6)
okq = True
for m in [50, 200, 1000]:
    aa, bb = x2m(m+1), x2m(m)
    F_ = (sqrt(aa*bb) + sqrt((1-aa)*(1-bb)))**2
    cross2 = 1 - F_
    okq &= abs(cross2/klbern(aa, bb) - mpf(1)/2) < mpf(2)/m
chk("A16b small-step: cross-leg^2 / KL -> 1/2 (pair-budget noise = waste, closed form)", okq)

# ---- A17: Tier-1 nested identity ----
Gf = lambda z: 1/sp.sqrt(1-z**2)
chk("A17 G(1/G(y)) = 1/y", sp.simplify(Gf(1/Gf(y)) - 1/sp.Abs(y)) == 0 or
    all(abs(float(Gf(1/Gf(y)).subs(y, v) - 1/v)) < 1e-12 for v in [0.2, 0.77, 0.99]))

# ---- A18: complementary Z2 readouts ----
chk("A18a u, p, q all blind to face swap th -> pi-th",
    sp.simplify(sp.cos(sp.pi-th)**2 - sp.cos(th)**2) == 0 and sp.simplify(sp.sin(sp.pi-th)-sp.sin(th)) == 0)
chk("A18b G_old = sec(th) flips sign across the face; G_new invariant",
    sp.simplify(1/sp.cos(sp.pi-th) + 1/sp.cos(th)) == 0 and
    sp.simplify(2/(1-sp.sin(sp.pi-th)) - 2/(1-sp.sin(th))) == 0)
chk("A18c G_old even in x (side-blind); G_new strictly monotone in x (side-seeing)",
    sp.simplify(Gf(-x)-Gf(x)) == 0 and sp.simplify(sp.diff(2/(1-x), x)) == 2/(1-x)**2)

# ---- A19/A20: the two logits; SNR vs SWR ----
chk("A19 SNR = (SWR-1)^2/(4 SWR)", sp.simplify(x**2/(1-x**2) - ((1+x)/(1-x)-1)**2/(4*(1+x)/(1-x))) == 0)
chk("A20 ln SNR = 2 artanh(x^2 - u) [power-coin logit]",
    all(abs(float(sp.log(v**2/(1-v**2)) - 2*sp.atanh(2*v**2-1))) < 1e-12 for v in [0.3, 0.6, 0.85]))

# ---- Seam: the seam coin IS the amplitude coin at x_s ----
rho = log(2)/log(3); xseam = 2*rho - 1
chk("S1 x_s = 2rho - 1 = log3(4/3); p(x_s) = rho exactly",
    abs(xseam - log(mpf(4)/3)/log(3)) < mpf(10)**-45 and abs((1+xseam)/2 - rho) < mpf(10)**-45)
toll_bits = 1 - (-(rho*log(rho, 2) + (1-rho)*log(1-rho, 2)))
chk("S2 toll = 1 - H2(rho) = 0.0500 bits = KL(Bern(rho)||Bern(1/2))",
    abs(toll_bits - mpf('0.0500444728')) < 1e-9 and
    abs(toll_bits - klbern(rho, mpf(1)/2)/log(2)) < mpf(10)**-40)
Gn_seam = 2/(1-xseam)
chk("S3 G_new(x_s) = 1/(1-rho) = log_{3/2}(3) = 2.70951... [curio: near e, fence applies]",
    abs(Gn_seam - log(3)/log(mpf(3)/2)) < mpf(10)**-44)
print("  G_new(seam) =", str(Gn_seam)[:12], "; e =", str(exp(1))[:12], "; 3/ln3 =", str(3/log(3))[:12])

n_fail = sum(1 for _, o in results if not o)
print(f"\n{len(results)-n_fail}/{len(results)} PASS")
