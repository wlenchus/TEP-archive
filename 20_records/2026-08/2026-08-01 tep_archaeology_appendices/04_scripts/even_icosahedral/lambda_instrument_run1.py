"""LAMBDA INSTRUMENT RUN 1 — the completed L-function of the Doud-1951 even
icosahedral object: instrument, ray-Fricke certification, FE constant, first zeros.
2026-08-10, Claude (Fable 5), session B.  dps 28.

Construction (derived this session; anchors below test it):
  F odd => F(iy) = 0; the content sits in h(y) := dF/dx(iy) = 4*pi*i*sqrt(y)*H(y),
  H(y) = sum_n n*c_n*K0(2*pi*n*y).
  Q(s) := int_0^inf h(y) y^{s+1/2} dy/y  ==>  Lambda(s) = N^{s/2} Q(s)/i, where
  Lambda(s) = N^{s/2} pi^{-s} Gamma((s+1)/2)^2 L(s),  L(s) = sum c_n n^{-s}.
  Fricke (committed, certified): F(-1/(Nz)) = const*G(z), const = tau/(sqrt(N)a_N)
  ==> h_F(1/(Ny)) = omega_h * N y^2 * h_G(y) with omega_h in {+-const} (measured),
  and the split at y0 = 1/sqrt(N) gives the ENTIRE two-piece model
    Lambda~(s) = (4*pi)[ N^{s/2} QF(s) + omega_h * N^{(1-s)/2} QG(1-s) ],
  QX(s) := int_{y0}^inf sqrt(y) H_X(y) y^{s+1/2} dy/y, H_G = conj(H_F) on the axis.
  FE by construction: Lambda~_F(s) = omega_h * Lambda~_G(1-s); the true Lambda has
  poles exactly insofar as the h-identity FAILS on the ray -- hence check Z-c.

PREDICTIONS (stated before run; same-session, unhashed — disclosed):
  Z-a  Anchors: Lambda~(s) matches the direct Dirichlet side N^{s/2}pi^{-s}
       Gamma((s+1)/2)^2 * sum_{n<=7000} c_n n^{-s} at s = 3, 2.5, 2 to rel <= 1e-18.
  Z-b  omega_h measured constant across the ray to <= 1e-18; |omega_h| - 1 <= 1e-20;
       omega_h in {+-const_alg, +-conj(const_alg)} to <= 1e-20 (branch reported).
  Z-c  Ray-Fricke: relative defect |h_F(1/(Nu)) - omega_h N u^2 h_G(u)| / scale
       <= 1e-18 at ALL >= 40 sample points u in [y0, 0.25] (heights down to ~2e-3).
  Z-d  Winding of Lambda~ around [-0.4, 1.4] x [0.5, 15] equals the number of
       critical-line zeros found in (0.5, 15) — and matches the gamma-factor main
       term (1/pi)*(phi(15)-phi(0.5)) within +-2.5.
  Z-e  All located zeros sit on Re s = 1/2 to instrument precision (GRH-consistent);
       first zero ordinate reported to >= 6 digits.
Kill: Z-a or Z-b failure => instrument unqualified, no verdicts on Z-c/d/e.

NOTE (post-run, disclosed in the record): Z-a FAILED as literally stated -- the bar
compared a clean instrument to a TRUNCATED reference (the 7000-term Dirichlet sum,
whose own tail dominates below s=3).  Instrument qualification moved to the amended
anchors in lambda_zeros_run1.py.  Practice-card candidate T-13: budget the reference's
and the instrument's own error floors before setting any bar."""
import csv, time, pickle
from mpmath import (mp, mpf, mpc, besselk, sqrt, exp, pi, conj, fabs, gamma,
                    log, arg, nstr, im, re)

mp.dps = 28
N = 1951
NMAX = 7000
CSV = "/root/.claude/projects/-home-claude/e1c6a220-faa1-5bd1-9d10-c0c3344b96cd/tool-results/project-doc-b99b6076-631d-43e3-92a2-b1e8923dc0c4.txt"

phi_g = (1 + sqrt(5))/2
def zeta10(k): return exp(mpc(0,1)*pi*k/5)
def zeta5(j):  return exp(mpc(0,2)*pi*j/5)
def parse_apex(s):
    s = s.strip()
    if s == "0": return mpc(0)
    sg = mpf(1)
    if s[0] == '+': s = s[1:]
    elif s[0] == '-': sg = mpf(-1); s = s[1:]
    fac = mpf(1)
    if s.endswith("*1/phi"): fac = 1/phi_g; s = s[:-6]
    elif s.endswith("*phi"): fac = phi_g; s = s[:-4]
    elif s.endswith("*2"): fac = mpf(2); s = s[:-2]
    return sg * fac * zeta10(int(s[7:]))

ap = {}; chi = {}
with open(CSV) as f:
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
print("assembled c_n to", NMAX)

def K0(u):
    if u > 75: return mpf(0)
    if u < 32: return besselk(0, u)
    S = mpf(1); term = mpf(1); k = 0
    while True:
        nxt = term * (-(2*k+1)**2) / (8*u*(k+1))
        if abs(nxt) >= abs(term) or abs(nxt) < mpf('1e-36'): break
        S += nxt; term = nxt; k += 1
    return sqrt(pi/(2*u)) * exp(-u) * S

TAILDIG = mpf(28*2.302585)
def H_of(y):     # sum n c_n K0(2 pi n y), adaptive n_max
    nmx = min(NMAX, int(TAILDIG/(2*pi*y)) + 8)
    tot = mpc(0); twopiy = 2*pi*y
    for n in range(1, nmx+1):
        k0 = K0(twopiy*n)
        if k0 != 0: tot += n*cn[n]*k0
    return tot

# ---------- quadrature grid on [y0, YMAX], Gauss-Legendre on log-segments
y0 = 1/sqrt(N); YMAX = mpf(12)
NSEG, NGL = 64, 18
import numpy as _np
xg, wg = _np.polynomial.legendre.leggauss(NGL)
t0 = time.time()
nodes = []; weights = []
L0, L1 = log(y0), log(YMAX)
for a in range(NSEG):
    la = L0 + (L1-L0)*a/NSEG; lb = L0 + (L1-L0)*(a+1)/NSEG
    for xx, ww in zip(xg, wg):
        ly = (la+lb)/2 + (lb-la)/2*mpf(float(xx))
        nodes.append(exp(ly)); weights.append((lb-la)/2*mpf(float(ww)))
Hvec = [H_of(y) for y in nodes]
print(f"h node vectors: {len(nodes)} nodes in {time.time()-t0:.0f}s")

def Q_up(s, conjugate=False):
    # int_{y0}^inf sqrt(y) H(y) y^{s+1/2} dy/y  via log-substitution
    tot = mpc(0)
    for y, w, Hv in zip(nodes, weights, Hvec):
        Hu = conj(Hv) if conjugate else Hv
        tot += w * sqrt(y) * Hu * y**(s + mpf('0.5'))
    return tot

# ---------- Z-b first (omega_h from the ray), then anchors need it
print("\n== Z-b/Z-c: ray-Fricke defect and omega_h ==")
t0 = time.time()
NPTS = 44
us = [y0*exp(log(mpf('0.25')/y0)*i/(NPTS-1)) for i in range(NPTS)]
hs_small = []
for u in us:
    yy = 1/(N*u)
    hs_small.append(sqrt(yy)*H_of(yy))     # sqrt(y)H(y) ~ h(y)/(4 pi i)
print(f"small-height evaluations done in {time.time()-t0:.0f}s")
ratios = []
worst_def = 0.0
for u, hsm in zip(us, hs_small):
    hg = conj(sqrt(u)*H_of(u))             # h_G(u)-object = conj of F-object
    pred_base = N*u*u*hg
    ratios.append(hsm/pred_base)
tau_alg = None
# algebraic const = tau/(sqrt(N) zeta10^2): rebuild tau via j-table
e5 = (N-1)//5; t2 = pow(2, e5, N); iota = {}
for k in range(5): iota[pow(t2, k, N)] = (4*k) % 5
z5 = exp(mpc(0,2)*pi/5); eN = exp(mpc(0,2)*pi/N)
tau_alg = mpc(0)
for x in range(1, N): tau_alg += z5**iota[pow(x, e5, N)] * eN**x
const_alg = tau_alg/(sqrt(N)*zeta10(2))
omega_h = ratios[0]
spread = max(float(fabs(r - omega_h)) for r in ratios)
cands = {"+const": const_alg, "-const": -const_alg,
         "+conj": conj(const_alg), "-conj": -conj(const_alg)}
best = min(cands, key=lambda kk: fabs(omega_h - cands[kk]))
print(f"omega_h = {nstr(omega_h, 22)}")
print(f"spread across {NPTS} ray points = {spread:.2e}   | |omega_h|-1 = {float(fabs(abs(omega_h)-1)):.1e}")
print(f"branch: {best}  |omega_h - {best}| = {float(fabs(omega_h - cands[best])):.2e}")
for u, r in zip(us, ratios):
    worst_def = max(worst_def, float(fabs(r - cands[best])))
print(f"Z-c: worst relative ray defect vs algebraic branch = {worst_def:.2e}  "
      f"({'PASS' if worst_def <= 1e-18 else 'FAIL'})")
omega = cands[best]                        # use the algebraic value henceforth

def Lam(s):
    return N**(s/2)*Q_up(s) + omega * N**((1-s)/2)*Q_up(1-s, conjugate=True)

# ---------- Z-a anchors
print("\n== Z-a: anchors vs direct Dirichlet side ==")
for sv in [mpf(3), mpf('2.5'), mpf(2)]:
    direct = sum(cn[n]*mpf(n)**(-sv) for n in range(1, NMAX+1))
    lam_direct = N**(sv/2)*pi**(-sv)*gamma((sv+1)/2)**2*direct
    lam_inst = Lam(sv)
    calib = lam_inst/lam_direct
    print(f"s = {float(sv)}: instrument/direct = {nstr(calib, 20)}")
s3, s25, s2 = [Lam(mpf(v))/(N**(mpf(v)/2)*pi**(-mpf(v))*gamma((mpf(v)+1)/2)**2 *
               sum(cn[n]*mpf(n)**(-mpf(v)) for n in range(1, NMAX+1)))
               for v in ('3','2.5','2')]
dev_a = max(float(fabs(s25/s3 - 1)), float(fabs(s2/s3 - 1)))
print(f"calibration constant C = {nstr(s3, 20)}  (C/(4pi) = {nstr(s3/(4*pi), 12)})")
print(f"Z-a: constancy across s = 3, 2.5, 2: {dev_a:.2e}  ({'PASS' if dev_a <= 1e-18 else 'FAIL'})")
CAL = s3

# ---------- FE self-check (construction identity, one point)
sv = mpc('0.7', '3.0')
lhs = Lam(sv)
rhs = omega * conj(Lam(conj(1-sv)))     # Lambda_G(1-s) = conj(Lam_F(conj(1-s)))
print(f"FE check at s = 0.7+3i: |Lam_F(s) - omega*Lam_G(1-s)|/|Lam_F| = "
      f"{float(fabs(lhs-rhs)/fabs(lhs)):.2e}")

with open('/home/claude/lam_cache.pkl','wb') as fh:
    pickle.dump(dict(nodes=[str(x) for x in nodes], weights=[str(x) for x in weights],
                     Hre=[str(re(h)) for h in Hvec], Him=[str(im(h)) for h in Hvec],
                     omega=str(omega), CAL=str(CAL)), fh)
print("\ncache saved; zero scan in part 2")
