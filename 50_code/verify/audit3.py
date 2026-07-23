# audit3.py — 07-19 evening session: seam-toll/Legendre weld, rung-ledger KL identification,
# the k-chain wiring braid, line-duality invariants. mpmath, 30 dps.
from mpmath import mp, mpf, log, sqrt, exp, atanh, cosh, tanh, floor, frac
mp.dps = 30
LN2, LN3 = log(2), log(3)

print("===== A. SEAM TOLL = BINARY KL = LEGENDRE AT THE SEAM SLOPE =====")
rho = LN2/LN3   # log_3(2), the seam slope
H2 = -(rho*log(rho) + (1-rho)*log(1-rho))/LN2          # entropy of the rho-coin, bits
toll = 1 - H2
KLb = (rho*log(2*rho) + (1-rho)*log(2*(1-rho)))/LN2    # KL(Bern(rho)||Bern(1/2)), bits
xs = 2*rho - 1; eta_s = atanh(xs)
leg = (xs*eta_s - log(cosh(eta_s)))/LN2                # Legendre transform of ln cosh at x_s, bits
print(f"rho = log_3 2 = {float(rho):.10f};  seam amplitude x_s = 2rho-1 = log_3(4/3) = {float(xs):.10f}")
print(f"toll = 1 - H2(rho)          = {float(toll):.10f} bits   (faces_seam: 0.0500)")
print(f"KL(Bern(rho)||Bern(1/2))    = {float(KLb):.10f} bits")
print(f"Legendre  x_s*eta_s - lncosh = {float(leg):.10f} bits")
print(f"dimension + toll = H2 + KL = {float(H2+KLb):.10f}  (= CE(Bern(rho), Bern(1/2)) = 1 bit exactly)")
# ledger law spot check: mechanical word of slope rho, K_n = ceil(n*rho); L_n = n ln2 - K_n ln3
mx = mpf(0); mn = mpf(0)
for n in range(1, 200001):
    Kn = floor(n*rho) + 1
    Ln = n*LN2 - Kn*LN3          # = -ln3*(1 - {n rho}) in this convention
    alt = -LN3*(1 - frac(n*rho))
    if n == 1: dev0 = abs(Ln - alt)
    mx = max(mx, Ln); mn = min(mn, Ln)
print(f"ledger law (K_n = floor+1 convention): L_n = -ln3*(1-{{n rho}}) exact? dev = {float(dev0):.1e}")
print(f"L_n range over n<=2e5: ({float(mn):.6f}, {float(mx):.6f})  vs (-ln3, 0) = ({float(-LN3):.6f}, 0)  [bounded ✓]")

print("\n===== B. R3.7 ADJACENT-RUNG KL LEDGER, IDENTIFIED =====")
# harmonic tower x_m^2 = 1/(m+1), u_m = m/(m+1)  [R3.1]
def klbern(p, q): return p*log(p/q) + (1-p)*log((1-p)/(1-q))
def klgauss(u2, u1): return (u2/u1 - 1 - log(u2/u1))/2
for m in (1, 2):
    p_new, p_old = mpf(1)/(m+2), mpf(1)/(m+1)
    print(f"rung {m}->{m+1}: KL(Bern(x2_{m+1})||Bern(x2_{m})) = {float(klbern(p_new, p_old)):.6f} nats"
          f"   [R3.7 logged: {'0.0567' if m==1 else '0.0164'}]"
          f"   Gaussian-witness KL(N(0,u_{m+1})||N(0,u_{m})) = {float(klgauss(1-p_new, 1-p_old)):.6f} (different ledger)")
m = 400
p_new, p_old = mpf(1)/(m+2), mpf(1)/(m+1)
print(f"asymptote m={m}: KL*2m^3 = {float(klbern(p_new,p_old)*2*m**3):.4f} (-> 1: the 1/(2m^3) Fisher/quasi-static law)")
c_m = log(1+mpf(1)/m)
print(f"per-rung capacity release c_400 = {float(c_m):.6f} ~ 1/m; waste/release -> 0 [quasi-static]")
# CE decomposition per rung: CE(new, old-code) = H(new) + KL — the 3b1b split on the tower
Hnew = -(p_new*log(p_new) + (1-p_new)*log(1-p_new))
CE = -(p_new*log(p_old) + (1-p_new)*log(1-p_old))
print(f"CE = H + KL check at m=400: {float(CE):.9f} = {float(Hnew):.9f} + {float(klbern(p_new,p_old)):.9f} -> dev {float(CE-Hnew-klbern(p_new,p_old)):.1e}")

print("\n===== C. THE k-CHAIN: A BRAID OF THREE WIRINGS =====")
x = sqrt(mpf('0.3')); u = 1-x**2; G2 = 1/u; snr = x**2/u; nsr = u/x**2
# Wiring A: G(k) = G^2(x)  <=>  u_k = u^2  (capacity doubling; inverse of the halving rung)
ukA = u**2; kA = sqrt(1-ukA)
print(f"[A] u_k=u^2: x^2+sqrt(u_k)={float(x**2+sqrt(ukA)):.12f} (=1)   k^2 = 2x^2-x^4: {float(kA**2):.10f} vs {float(2*x**2-x**4):.10f}")
print(f"[A] C_k = 2*C_x: {float(-log(ukA)):.10f} vs {float(-2*log(u)):.10f}   G(x/sqrt2) = sqrt2*x/k: "
      f"{float(1/sqrt(1-x**2/2)):.10f} vs {float(sqrt(2)*x/kA):.10f}")
print(f"[A] break line 'x^2 = u/sqrt(u_k)': RHS = {float(u/sqrt(ukA)):.6f} (=1 always, not x^2={float(x**2):.4f}) — off-by-one SNR<->G^2")
# Wiring A': sqrt(u_k) = NSR_x  (residual-root = noise-to-signal)
ukAp = nsr**2
print(f"[A'] sqrt(u_k)=NSR: 'x^2 = u/sqrt(u_k)': {float(u/sqrt(ukAp)):.10f} vs x^2 = {float(x**2):.10f}  EXACT")
print(f"[A'] '1/(x^2 sqrt(u_k)) - 1/sqrt(u_k) = 1': {float(1/(x**2*sqrt(ukAp)) - 1/sqrt(ukAp)):.12f}  EXACT")
print(f"[A'] next line should be '1/x^2 - 1 = sqrt(u_k)': {float(1/x**2-1):.10f} vs {float(sqrt(ukAp)):.10f}  (the chain wrote 1/u_k — the slip)")
# Wiring B: u_k = SNR_x (as the chain states; valid only x^2 <= 1/2)
ukB = snr
print(f"[B] u_k=SNR: '(1-x^2)/sqrt(u_k) = x^2': {float(u/sqrt(ukB)):.6f} vs {float(x**2):.6f}  (holds only at SNR=1)")
print(f"[B] 'sqrt(NSR)-sqrt(SNR) = x^2': {float(sqrt(nsr)-sqrt(snr)):.6f} vs {float(x**2):.6f}  (not an identity)")
# Final stretch: 1/x^2 - x^2 = G^2 as *identity* is false; as *definition* it is 2 sinh(2 lambda)
print(f"[final] 1/x^2 - x^2 = {float(1/x**2 - x**2):.6f} vs G^2 = {float(G2):.6f}  (not an identity)")
lam = -log(x)  # x = e^-lambda
print(f"[final-as-definition] 1/x^2 - x^2 = 2 sinh(2 lambda): {float(2*( (exp(2*lam)-exp(-2*lam))/2 )):.10f} ✓; "
      f"4th-root quartet = the four-cycle phases {{±1, ±i}} [structural]")
# sufficiency clause + nested identity
G1 = 1/sqrt(1-mpf('0.4')); snr2 = G1; u2 = 1/(1+snr2); x22 = 1-u2
print(f"[sufficiency] SNR_2=G_1: x2^2 = G_1*u_2 = G_1/G_2^2: {float(x22):.10f} vs {float(G1*u2):.10f}")
y = mpf('0.62'); print(f"[nested] G(1/G(y)) = 1/y: {float(1/sqrt(1-(sqrt(1-y**2))**2)):.10f} vs {float(1/y):.10f}"
      f"   => G^2(x1)/G(1/G(x2)) = G1^2*x2 [simplified form of the recalled relation]")

print("\n===== D. LINE / STANDING-WAVE BUDGET DICTIONARY =====")
gam = mpf('0.55')  # |Gamma|
xg = gam; ug = 1-gam**2; eta_g = atanh(gam)
vmax, vmin = 1+xg, 1-xg
print(f"|Gamma|=x={float(xg)}: amplitude max = 1+x = {float(vmax):.4f} (<=2: passivity numerator)")
print(f"SWR = (1+x)/(1-x) = e^(2 eta): {float(vmax/vmin):.10f} vs {float(exp(2*eta_g)):.10f}  [Cayley/odds coordinate]")
print(f"max*min = 1-x^2 = u = delivered fraction: {float(vmax*vmin):.10f} vs {float(ug):.10f}  [ratio reads eta, product reads u]")
print("Done.")
