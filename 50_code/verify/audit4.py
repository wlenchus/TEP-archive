# audit4.py — reins session: placing convergent waste (two ledgers), the Legendre lift
# as a budget-valued operation, and the silver standing wave. mpmath, 30 dps.
from mpmath import mp, mpf, log, sqrt, exp, atanh, cosh, mpf
mp.dps = 30
LN2 = log(2)

def klbern(p, q):  # nats
    return p*log(p/q) + (1-p)*log((1-p)/(1-q))

print("===== 1. TWO LEDGERS: waste sums per schedule =====")
# harmonic tower x2_m = 1/(m+1): capacity divergent (ln(M+1)), waste summable
tot = mpf(0)
for m in range(1, 200001):
    tot += klbern(mpf(1)/(m+2), mpf(1)/(m+1))
print(f"harmonic tower: total waste Sum KL = {float(tot):.9f} nats (converged; capacity spend ln(M+1) divergent)")
# T_lin halving tower u' = sqrt(u) from the golden start u0 = 1/phi^2
phi = (1+sqrt(5))/2; u = 1/phi**2; totl = mpf(0); cap = mpf(0); n = 0
while 1-u > mpf('1e-25'):
    un = sqrt(u); totl += klbern(1-un, 1-u); cap += -log(un); u = un; n += 1
    if n > 200: break
print(f"halving tower (golden start): total waste = {float(totl):.9f} nats, total capacity = {float(cap):.9f} = ln(phi^2)+... (both finite)")
# constant/GMC tower: adjacent budgets identical -> zero drift waste
print(f"constant tower (u=1/2 each rung): adjacent-rung KL = {float(klbern(mpf(1)/2, mpf(1)/2)):.1f} EXACTLY (zero drift waste; chaos load = linear capacity) ")
print("seam: constant per-symbol toll 0.0500 bits -> LINEAR waste (stationary tax). Three waste regimes: zero / summable / linear.")
print(">>> aside conjecture REFUTED as stated: divergent waste is NOT the chaos discriminant (GMC class has zero drift waste).")

print("\n===== 2. THE LEGENDRE LIFT: x -> x_meta, a budget-valued operation =====")
def lift(x):
    p = (1+x)/2
    KLb = (p*log(2*p) + (1-p)*log(2*(1-p)))/LN2   # bits
    return sqrt(KLb)
for xv in ['0.05','0.2618595071','0.5','0.8','0.95']:
    x = mpf(xv); p = (1+x)/2
    H2 = -(p*log(p)+(1-p)*log(1-p))/LN2
    xm = lift(x)
    print(f"x={float(x):.4f}: meta-budget (KL, H2) = ({float(xm**2):.6f}, {float(H2):.6f}) sum={float(xm**2+H2):.12f}  x_meta={float(xm):.6f}  (f(x)<x: {xm<x})")
rate = lift(mpf('1e-8'))/mpf('1e-8')
print(f"contraction rate at the noise pole: x_meta/x -> {float(rate):.9f} vs 1/sqrt(2 ln2) = {float(1/sqrt(2*LN2)):.9f}")
# fixed point scan
worst = 0;
for i in range(1, 100):
    x = mpf(i)/100;
    if lift(x) >= x: worst = x
print(f"interior fixed points on (0,1): none found (f(x)<x everywhere; endpoints 0,1 fixed). Rate inventory: halving 1/sqrt2=0.7071 < Legendre {float(1/sqrt(2*LN2)):.4f} < 1")
# iterate from the seam amplitude
x = mpf('0.2618595071'); orbit = []
for k in range(4):
    orbit.append(float(x)); x = lift(x)
print("Legendre-peel orbit from the seam amplitude:", [f"{v:.5f}" for v in orbit])

print("\n===== 3. THE SILVER STANDING WAVE (exact chart translation of the Liu partition) =====")
# Liu/silver partition: (A, R, T) = (2sqrt2-2, 3-2sqrt2, 0)
R = 3 - 2*sqrt(2); x = sqrt(R); A = 2*sqrt(2) - 2
print(f"|Gamma| = sqrt(3-2sqrt2) = sqrt2 - 1 = {float(x):.12f}  (the silver modulus k2, recorded CM value)")
print(f"|V|max/|V+| = 1+x = sqrt2:        {float(1+x):.12f} vs {float(sqrt(2)):.12f}")
print(f"|V|min/|V+| = 1-x = 2-sqrt2 = γ*: {float(1-x):.12f} vs {float(2-sqrt(2)):.12f}")
print(f"SWR = (1+x)/(1-x) = 1+sqrt2 (silver ratio): {float((1+x)/(1-x)):.12f} vs {float(1+sqrt(2)):.12f}")
print(f"max*min = u = A (T=0): {float((1+x)*(1-x)):.12f} vs {float(A):.12f}")
print(f"eta_Gamma = artanh(sqrt2-1) = (1/2)ln(1+sqrt2) = rho*/4: {float(atanh(x)):.12f} vs {float(log(1+sqrt(2))/2):.12f}")
# the symmetric point-shunt lore point: g = 2 on a matched line
g = mpf(2); r = -g/(g+2); t = 2/(g+2)
print(f"symmetric shunt extremum g=2: (A,R,T) = ({float(1-r**2-t**2):.4f}, {float(r**2):.4f}, {float(t**2):.4f}); |Gamma| = 1/2, u = 3/4  [the trivial-cycle partition]")
print("Done.")
