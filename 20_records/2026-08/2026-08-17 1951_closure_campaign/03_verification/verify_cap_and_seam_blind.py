# Blind replication of the pincer doc's headline numbers, from the FILED DOC ONLY
# (agent scripts in /home/claude/closure2/ deliberately not read before this run).
# Targets: B(window1)=946.3 (identity 960.7, elliptic 0.420, log-block -15.12,
#          digammas -0.227, prime +0.013, +h(0)/2), B(window2)=276.1
#          (identity 282.7, geodesic +0.119, primes +0.084),
#          w = -0.761448+0.648225i, arg tau(chi)/2pi = -0.377046, arg w/2pi = +0.387756.
from mpmath import mp, mpf, mpc
import mpmath

mp.dps = 20
p = 1951

# --- character table: primitive root 3, chi_j(3^k) = zeta5^(j*k) ---
ind = {}
x = 1
for k in range(p - 1):
    ind[x] = k
    x = x * 3 % p
assert len(ind) == p - 1, "3 is not a primitive root mod 1951"
print("ind_3(2) mod 5 =", ind[2] % 5, " ind_3(5) mod 5 =", ind[5] % 5,
      " ind_3(148) mod 5 =", ind[148] % 5)

zeta5 = mpmath.e ** (2j * mpmath.pi / 5)

def make_chi(j):
    tab = [mpc(0)] * p
    for a in range(1, p):
        tab[a] = zeta5 ** ((j * ind[a]) % 5)
    return tab

# --- seam phase w for each of the four order-5 characters ---
E = [mpmath.e ** (2j * mpmath.pi * a / p) for a in range(p)]
DG = [mpc(0)] + [mpmath.digamma(mpf(a) / p) for a in range(1, p)]
LG = [mpc(0)] + [mpmath.loggamma(mpf(a) / p) for a in range(1, p)]

print("\n--- seam phases (route 1: FE; route 2: Lerch/loggamma) ---")
for j in (1, 2, 3, 4):
    chi = make_chi(j)
    tau_chi = sum(chi[a] * E[a] for a in range(1, p))
    tau_chibar = sum(chi[a].conjugate() * E[a] for a in range(1, p))
    L1chi = -sum(chi[a] * DG[a] for a in range(1, p)) / p
    L1chibar = -sum(chi[a].conjugate() * DG[a] for a in range(1, p)) / p
    w1 = (tau_chibar / mpmath.sqrt(p)) * L1chi / L1chibar
    # route 2: w = Lambda(0,chibar)/Lambda(1,chibar), Lambda(0,chibar)=2L'(0,chibar)=2*sum chibar(a) logGamma(a/p)
    w2 = 2 * sum(chi[a].conjugate() * LG[a] for a in range(1, p)) / (mpmath.sqrt(p) * L1chibar)
    print(f"j={j}: |tau|^2/N={mpmath.nstr(abs(tau_chi)**2/p, 8)}  "
          f"arg tau/2pi={mpmath.nstr(mpmath.arg(tau_chi)/(2*mpmath.pi), 6)}  "
          f"w={mpmath.nstr(w1, 7)}  |w|={mpmath.nstr(abs(w1), 8)}  "
          f"arg w/2pi={mpmath.nstr(mpmath.arg(w1)/(2*mpmath.pi), 6)}  "
          f"|w1-w2|={mpmath.nstr(abs(w1 - w2), 3)}")

# --- trace-side cap ---
mp.dps = 15
LOGN = mpmath.log(p)
PHI = (1 + mpmath.sqrt(5)) / 2
ELL3 = 4 * mpmath.log(PHI)           # 1.924847...
W3 = 2 * ELL3 / mpmath.sqrt(5)       # two classes, weight ell0/(2 sinh(ell/2)) = ell/sqrt5 each

def cap(L, with_geodesic, chi):
    def h(r):
        u = L * r
        if abs(u) < mpf("1e-12"):
            return mpf(1)
        return (mpmath.sin(u) / u) ** 4
    pts = [0, 1 / L, 5 / L, 20 / L, 100 / L, mpmath.inf]
    I_id = mpf(488) / 3 * 2 * mpmath.quad(lambda r: h(r) * r * mpmath.tanh(mpmath.pi * r), pts)
    I_ell = mpf(2) / (3 * mpmath.sqrt(3)) * 2 * mpmath.quad(
        lambda r: h(r) * mpmath.cosh(mpmath.pi * r / 3) / mpmath.cosh(mpmath.pi * r), pts)
    def g(u):
        return mpmath.quad(lambda r: h(r) * mpmath.cos(r * u), pts) / mpmath.pi
    g0 = g(0)
    logblock = -(3 * LOGN - 2 * mpmath.log(mpmath.pi)) * g0 - 2 * g0 * mpmath.log(2)
    I_psi1 = (1 / mpmath.pi) * 2 * mpmath.quad(
        lambda r: h(r) * mpmath.re(mpmath.digamma(1 + 1j * r)), pts)
    I_psih = (1 / mpmath.pi) * 2 * mpmath.quad(
        lambda r: h(r) * mpmath.re(mpmath.digamma(mpf(1) / 2 + 1j * r)), pts)
    X = 4 * L
    prime = mpf(0)
    for n, Lam in ((2, mpmath.log(2)), (3, mpmath.log(3)), (4, mpmath.log(2)), (5, mpmath.log(5))):
        if 2 * mpmath.log(n) < X:
            prime += 4 * Lam * mpmath.re(chi[n]) / n * g(2 * mpmath.log(n))
    geo = W3 * g(ELL3) if with_geodesic else mpf(0)
    B = I_id + I_ell + geo + mpf(1) / 2 + logblock - I_psi1 - I_psih + prime
    print(f"  L={mpmath.nstr(L,6)} (X=4L={mpmath.nstr(X,6)}): identity={mpmath.nstr(I_id,6)} "
          f"elliptic={mpmath.nstr(I_ell,4)} geodesic={mpmath.nstr(geo,4)} "
          f"logblock={mpmath.nstr(logblock,6)} digamma1={mpmath.nstr(-I_psi1,4)} "
          f"digamma1/2={mpmath.nstr(-I_psih,4)} prime={mpmath.nstr(prime,4)} "
          f"h(0)/2=0.5  g(0)={mpmath.nstr(g0,6)} [1/(3L)={mpmath.nstr(1/(3*L),6)}]")
    print(f"  ==> B = {mpmath.nstr(B, 7)}")
    return B

chi1 = make_chi(1)
print("\n--- window 1: L=0.4812 (X=1.9248), no hyperbolic ledger; target B=946.3 ---")
cap(mpf("0.4812"), False, chi1)
print("\n--- window 2: L=0.874 (X=3.496), t=3 ledger; target B=276.1 ---")
cap(mpf("0.874"), True, chi1)
print("\n(2*148+1)+2*(-11) =", (2 * 148 + 1) + 2 * (-11))
