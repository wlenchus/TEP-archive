"""THETA-BUDGET LENS — the budget in Jacobi theta form (Gamma(2)/lambda chart),
and the seam unit at Doud-1951. 2026-08-10, Claude (Fable 5), session B.

Checks (stated before run):
  T-a  Jacobi's quartic identity theta2^4 + theta4^4 = theta3^4 IS the elliptic
       budget x^2 + u = 1 under x^2 := lambda = theta2^4/theta3^4,
       u := theta4^4/theta3^4; G = 1/sqrt(u) = (theta3/theta4)^2. 30+ digits at
       four tau (incl. one off-geodesic).
  T-b  The anharmonic (S3) orbit of lambda equals the budget-station set
       {x^2, u, -SNR, 1/x^2, G^2, -1/SNR} as a multiset (the six gauge images).
  T-c  lambda(i) = 1/2 (the self-dual point sits at the Fricke fixed point in
       THIS chart; the 08-04 j-chart put the SEAM (x=0) there — chart-relative
       station, invariant point).
  T-d  Twisted-theta functional equation at N = 1951 with the exact pinned chi
       (chi(2) = zeta5^4): psi_chi(1/t) = (tau(chi)/sqrt(N)) * sqrt(t) *
       psi_chibar(t) — the seam-crossing unit of the chi-distorted budget IS
       tau(chi)/sqrt(N), pure phase. Two t values, ~30-digit agreement,
       branch (tau vs conj tau) reported as measured.
  T-e  The Maass form's Fricke constant = that same theta seam unit divided by
       a_N = zeta10^2: tau/(sqrt(N)*a_N) vs yesterday's stored 30-digit const.
Kill: any check failing is reported as-is."""
from mpmath import mp, mpf, mpc, exp, pi, sqrt, jtheta, fabs, nstr, conj

mp.dps = 45
def q_of(tau): return exp(mpc(0,1)*pi*tau)
def thetas(tau):
    q = q_of(tau)
    return jtheta(2,0,q), jtheta(3,0,q), jtheta(4,0,q)

print("== T-a/T-b: the lambda chart ==")
worstA = worstB = 0.0
for tau in [mpc(0,'0.6'), mpc(0,'1.0'), mpc(0,'1.7'), mpc('0.3','0.9')]:
    t2, t3, t4 = thetas(tau)
    lam = t2**4/t3**4; u = t4**4/t3**4
    worstA = max(worstA, float(fabs(lam + u - 1)))
    G2 = (t3/t4)**4
    worstA = max(worstA, float(fabs(G2 - 1/u)))
    x2 = lam; SNR = x2/u
    orbit = sorted([lam, 1-lam, lam/(lam-1), 1/lam, 1/(1-lam), (lam-1)/lam],
                   key=lambda z: (float(z.real), float(z.imag)))
    stations = sorted([x2, u, -SNR, 1/x2, G2, -1/SNR],
                      key=lambda z: (float(z.real), float(z.imag)))
    worstB = max(worstB, max(float(fabs(a-b)) for a, b in zip(orbit, stations)))
print(f"T-a: budget + G^2 identities, 4 tau: worst dev = {worstA:.2e}")
print(f"T-b: anharmonic orbit == budget stations: worst dev = {worstB:.2e}")

lam_i = jtheta(2,0,q_of(mpc(0,1)))**4 / jtheta(3,0,q_of(mpc(0,1)))**4
print(f"T-c: lambda(i) - 1/2 = {float(fabs(lam_i - mpf(1)/2)):.2e}  (self-dual AT the Fricke point)")

# ---- T-d: twisted theta FE at N = 1951, exact chi
print("\n== T-d: chi-twisted seam crossing at N = 1951 ==")
N = 1951
e5 = (N-1)//5
t0 = pow(2, e5, N); iota = {}
for k in range(5): iota[pow(t0, k, N)] = (4*k) % 5   # chi(2) = zeta5^4 pin
z5 = exp(mpc(0,2)*pi/5)
chival = [None]*N
for x in range(1, N): chival[x] = z5**iota[pow(x, e5, N)]
tau_chi = mpc(0)
eN = exp(mpc(0,2)*pi/N)
for x in range(1, N): tau_chi += chival[x]*eN**x
unit_exact = tau_chi/sqrt(N)
print(f"tau(chi)/sqrt(N) = {nstr(unit_exact, 30)}   | |unit| - 1 = {float(fabs(abs(unit_exact)-1)):.1e}")

def psi(t, bar=False):
    # sum_{n>=1} chi^{(bar)}(n) exp(-pi n^2 t / N); terms to 1e-42 tail
    s = mpc(0); n = 1
    while True:
        term = exp(-pi*n*n*t/N)
        if term < mpf('1e-44') and n > 50: break
        c = chival[n % N]
        if c is not None and n % N != 0:
            s += (conj(c) if bar else c)*term
        n += 1
    return s

for tv in ['1.37', '0.83']:
    t = mpf(tv)
    lhs = psi(1/t)
    rhs_base = sqrt(t)*psi(t, bar=True)
    unit_meas = lhs/rhs_base
    d1 = float(fabs(unit_meas - unit_exact))
    d2 = float(fabs(unit_meas - conj(unit_exact)))
    print(f"t = {tv}: measured unit = {nstr(unit_meas, 25)}")
    print(f"   |measured - tau/sqrt(N)| = {d1:.2e}   |measured - conj| = {d2:.2e}"
          f"   -> branch: {'tau(chi)' if d1 < d2 else 'CONJ (report!)'}")

# ---- T-e: the Maass Fricke constant = seam unit / a_N
print("\n== T-e: const_F = [theta seam unit] / a_N ==")
aN = exp(mpc(0,1)*pi*2/5)     # zeta10^2
cand = unit_exact/aN
stored = mpc('-0.885096398890473462526283071771', '0.465407740235501333474163837673')
print(f"tau/(sqrt(N)*a_N) = {nstr(cand, 30)}")
print(f"stored dps-40 Fricke const = {nstr(stored, 30)}")
print(f"|difference| = {float(fabs(cand - stored)):.2e}")
print(f"distortion factor a_N^-1 = zeta10^-2 = {nstr(1/aN, 20)}  (pure phase: reactive)")
