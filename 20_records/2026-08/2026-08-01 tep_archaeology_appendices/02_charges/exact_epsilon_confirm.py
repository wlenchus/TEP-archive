"""E-c CONFIRM — fresh dps-40 Fricke measurement at Doud-1951 vs the identified
algebraic constant  const = tau(chi) / (sqrt(N) * a_N),  a_N = zeta10^2.
2026-08-09 (session B), Claude (Fable 5).

PREDICTION (E-c, stated in exact_epsilon_certificate.py before either run):
  |const_dps40 - tau(chi)/(sqrt(N)*a_N)| <= 1e-28  at the fresh point
  z0 = (0.4 + 1.15i)/N  (same point as the session-B verification, so the first
  9 digits are also a regression check against that record).
Kill: a miss is reported as-is; the exact-eps claim then stays at the 4.5e-12 grade.

Also emitted for the record: 30-digit exact const at 1951, and the 20-digit
predicted const at 2141 (a forward prediction for any future re-measurement)."""
import csv, time
from mpmath import mp, mpf, mpc, besselk, sqrt, sin, exp, pi, conj, fabs, mpmathify, nstr

mp.dps = 40
N = 1951
NMAX = 40000
CSV = {
 1951: "/root/.claude/projects/-home-claude/e1c6a220-faa1-5bd1-9d10-c0c3344b96cd/tool-results/project-doc-b99b6076-631d-43e3-92a2-b1e8923dc0c4.txt",
 2141: "/root/.claude/projects/-home-claude/e1c6a220-faa1-5bd1-9d10-c0c3344b96cd/tool-results/project-doc-70dab881-3783-468e-aa79-e35a5252de13.txt"}

phi = (1 + sqrt(5))/2
def zeta10(k): return exp(mpc(0,1)*pi*k/5)
def zeta5(j):  return exp(mpc(0,2)*pi*j/5)

def parse_apex(s):
    s = s.strip()
    if s == "0": return mpc(0)
    sign = mpf(1)
    if s[0] == '+': s = s[1:]
    elif s[0] == '-': sign = mpf(-1); s = s[1:]
    fac = mpf(1)
    if s.endswith("*1/phi"): fac = 1/phi; s = s[:-6]
    elif s.endswith("*phi"): fac = phi; s = s[:-4]
    elif s.endswith("*2"): fac = mpf(2); s = s[:-2]
    assert s.startswith("zeta10^"), s
    return sign * fac * zeta10(int(s[7:]))

ap = {}; chi = {}
with open(CSV[N]) as f:
    for row in csv.DictReader(f):
        p = int(row['p'])
        ap[p] = parse_apex(row['a_p_exact'])
        c = row['chi_p_exact'].strip()
        chi[p] = mpc(0) if c == '0' else zeta5(int(c[6:]))

spf = list(range(NMAX+1))
for i in range(2, int(NMAX**0.5)+1):
    if spf[i] == i:
        for m in range(i*i, NMAX+1, i):
            if spf[m] == m: spf[m] = i

t0 = time.time()
cn = [None]*(NMAX+1); cn[1] = mpc(1)
for n in range(2, NMAX+1):
    p = spf[n]; m = n; k = 0
    while m % p == 0: m //= p; k += 1
    pk = p**k
    if cn[pk] is None:
        prev, cur = mpc(1), ap[p]
        for _ in range(k-1):
            prev, cur = cur, ap[p]*cur - chi[p]*prev
        cn[pk] = cur
    cn[n] = cn[pk] if m == 1 else cn[pk]*cn[m]
print(f"assembled c_n to {NMAX} in {time.time()-t0:.0f}s")

def K0(u):
    if u > 130: return mpf(0)
    if u < 32: return besselk(0, u)
    S = mpf(1); term = mpf(1); k = 0
    while True:
        nxt = term * (-(2*k+1)**2) / (8*u*(k+1))
        if abs(nxt) >= abs(term) or abs(nxt) < mpf('1e-48'): break
        S += nxt; term = nxt; k += 1
    return sqrt(pi/(2*u)) * exp(-u) * S

def point_vectors(y):
    twopiy = 2*pi*y
    return [K0(twopiy*n) for n in range(1, NMAX+1)]

def F_from(coeffs, Kv, x, y):
    tot = mpc(0); twopix = 2*pi*x
    for n in range(1, NMAX+1):
        if Kv[n-1] != 0:
            tot += coeffs[n]*Kv[n-1]*sin(twopix*n)
    return sqrt(y) * 2j * tot

z0 = mpc(mpf('0.4')/N, mpf('1.15')/N)
w = -1/(N*z0)
t0 = time.time()
Kvz = point_vectors(z0.imag); print(f"K vector (z-side) {time.time()-t0:.0f}s")
t0 = time.time()
Kvw = point_vectors(w.imag);  print(f"K vector (w-side) {time.time()-t0:.0f}s")
cbar = [None] + [conj(cn[n]) for n in range(1, NMAX+1)]
Fw = F_from(cn, Kvw, w.real, w.imag)
Gz = F_from(cbar, Kvz, z0.real, z0.imag)
const = Fw/Gz
print(f"\nconst (dps40, fresh measurement) = {nstr(const, 30)}")
print(f"| |const| - 1 | = {float(fabs(abs(const)-1)):.3e}")

# exact candidate: tau(chi)/(sqrt(N)*a_N), chi pinned by chi(2)=zeta5^4, a_N=zeta10^2
mp.dps = 50
def tau_of(Nf, pin_j2):
    e5 = (Nf-1)//5
    t0_ = pow(2, e5, Nf); iota = {}
    for k in range(5): iota[pow(t0_, k, Nf)] = (k*pin_j2) % 5
    z5 = exp(mpc(0,2)*pi/5); eN = exp(mpc(0,2)*pi/Nf)
    tau = mpc(0)
    for x in range(1, Nf):
        tau += z5**iota[pow(x, e5, Nf)] * eN**x
    return tau
tau1951 = tau_of(1951, 4)
cand = tau1951/(sqrt(1951)*zeta10(2))
mp.dps = 40
dev = fabs(const - cand)
print(f"cand  = tau(chi)/(sqrt(N)*a_N)       = {nstr(mpc(cand), 30)}")
print(f"|const - cand| = {float(dev):.3e}")
reg = fabs(const - mpc('-0.885096399', '0.465407740'))
print(f"regression vs session-B 9-digit print: {float(reg):.3e}")
print("E-c:", "PASS" if dev <= mpf('1e-28') else "FAIL")

mp.dps = 50
tau2141 = tau_of(2141, 1)
pred2141 = tau2141/(sqrt(2141)*zeta10(8))
print(f"\nforward prediction, 2141 (20 digits): const_2141 = {nstr(mpc(pred2141), 20)}")
print(f"vs their 11-digit record -0.00271583114+0.99999631212i: "
      f"{float(fabs(pred2141 - mpc('-0.00271583114','0.99999631212'))):.3e}")
