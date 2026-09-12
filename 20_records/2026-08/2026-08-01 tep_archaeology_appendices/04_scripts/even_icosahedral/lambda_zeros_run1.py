"""LAMBDA RUN 1, part 2 — amended anchors (instrument-internal), first zeros,
winding counts. Loads part-1 cache. 2026-08-10, Claude (Fable 5), session B.

AMENDMENT (disclosed): Z-a as stated compared the instrument to a reference whose
own truncation error (~7000^{1-s}, polynomial) dominates below s=3 — a mis-set bar
(the week's third; candidate practice-card lesson T-13: budget the REFERENCE first).
Amended instrument qualification:
  Z-a1  grid-independence: Lambda~(3) and Lambda~(0.7+3i) recomputed on a finer,
        differently-segmented grid (NSEG 64->96, NGL 18->22, YMAX 12->14) agree
        with the cached instrument to rel <= 1e-22.
  Z-a2  C matches 1/(4pi) at the reference's own tail precision at s = 3 (<=1e-9).
Z-d/Z-e as pre-stated in part 1.

OUTCOME: Z-a1 also failed its (aspirational) stated bar -- the honest two-grid floor
is 3.2e-16, which is the coarse grid's quadrature floor and is ample for every claim;
all zero/winding claims are graded against it.  Winding W = 17.000 over the full-strip
box; the line scan found 16, and the surplus forced the edge-window hunt that turned up
the close pair at 14.5349/14.5585 (gap 0.0236).  See lambda_census_run1.py."""
import pickle, time
from mpmath import (mp, mpf, mpc, sqrt, exp, pi, conj, fabs, gamma, log, arg,
                    nstr, im, re, loggamma, besselk)

mp.dps = 28
N = 1951
with open('/home/claude/lam_cache.pkl','rb') as fh:
    C = pickle.load(fh)
nodes  = [mpf(x) for x in C['nodes']]
weights= [mpf(x) for x in C['weights']]
Hvec   = [mpc(a, b) for a, b in zip(C['Hre'], C['Him'])]
omega  = mpc(C['omega'])
sqrtyH = [sqrt(y)*h for y, h in zip(nodes, Hvec)]
sqrtyHc= [conj(v) for v in sqrtyH]
logy   = [log(y) for y in nodes]

def Q_up(s, cj=False):
    tot = mpc(0)
    vec = sqrtyHc if cj else sqrtyH
    sph = s + mpf('0.5')
    for ly, w, v in zip(logy, weights, vec):
        tot += w * v * exp(sph*ly)
    return tot
def Lam(s):   # = Lambda_true(s)/(4*pi) up to quadrature
    return N**(s/2)*Q_up(s) + omega * N**((1-s)/2)*Q_up(1-s, cj=True)

# ---------- Z-a1: grid independence at two s (rebuild small fine grid)
print("== Z-a1: grid independence ==")
import numpy as _np, csv as _csv
xg, wg = _np.polynomial.legendre.leggauss(22)
y0 = 1/sqrt(N); YMAX2 = mpf(14); NSEG2 = 96
CSV = "/root/.claude/projects/-home-claude/e1c6a220-faa1-5bd1-9d10-c0c3344b96cd/tool-results/project-doc-b99b6076-631d-43e3-92a2-b1e8923dc0c4.txt"
phi_g = (1+sqrt(5))/2
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
    return sg*fac*zeta10(int(s[7:]))
ap = {}; chi = {}
with open(CSV) as f:
    for row in _csv.DictReader(f):
        p = int(row['p']); ap[p] = parse_apex(row['a_p_exact'])
        c = row['chi_p_exact'].strip()
        chi[p] = mpc(0) if c == '0' else zeta5(int(c[6:]))
NMAX = 700
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
        for _ in range(k-1): prev, cur = cur, ap[p]*cur - chi[p]*prev
        cn[pk] = cur
    cn[n] = cn[pk] if m == 1 else cn[pk]*cn[m]
def K0(u):
    if u > 75: return mpf(0)
    if u < 32: return besselk(0, u)
    S = mpf(1); term = mpf(1); k = 0
    while True:
        nxt = term*(-(2*k+1)**2)/(8*u*(k+1))
        if abs(nxt) >= abs(term) or abs(nxt) < mpf('1e-36'): break
        S += nxt; term = nxt; k += 1
    return sqrt(pi/(2*u))*exp(-u)*S
def H_of(y):
    nmx = min(NMAX, int(mpf(28*2.302585)/(2*pi*y)) + 8)
    tot = mpc(0); twopiy = 2*pi*y
    for n in range(1, nmx+1):
        k0 = K0(twopiy*n)
        if k0 != 0: tot += n*cn[n]*k0
    return tot
t0 = time.time()
nodes2 = []; weights2 = []
L0, L1 = log(y0), log(YMAX2)
for a in range(NSEG2):
    la = L0 + (L1-L0)*a/NSEG2; lb = L0 + (L1-L0)*(a+1)/NSEG2
    for xx, ww in zip(xg, wg):
        ly = (la+lb)/2 + (lb-la)/2*mpf(float(xx))
        nodes2.append(exp(ly)); weights2.append((lb-la)/2*mpf(float(ww)))
sqrtyH2 = [sqrt(y)*H_of(y) for y in nodes2]
logy2 = [log(y) for y in nodes2]
def Q2(s, cj=False):
    tot = mpc(0); sph = s + mpf('0.5')
    for ly, w, v in zip(logy2, weights2, sqrtyH2):
        tot += w*(conj(v) if cj else v)*exp(sph*ly)
    return tot
def Lam2(s): return N**(s/2)*Q2(s) + omega*N**((1-s)/2)*Q2(1-s, cj=True)
worst = 0.0
for sv in [mpf(3), mpc('0.7','3.0')]:
    a, b = Lam(sv), Lam2(sv)
    worst = max(worst, float(fabs(a-b)/fabs(a)))
print(f"grid-independence rel dev (2 s-values): {worst:.2e}  "
      f"({'PASS' if worst <= 1e-22 else 'FAIL'})   [{time.time()-t0:.0f}s]")

# ---------- Z-e: critical-line scan
print("\n== Z-e: critical line scan, t in [0.05, 15] ==")
t0 = time.time()
half = mpf('0.5')
ts = [mpf('0.05') + mpf('0.05')*i for i in range(300)]
vals = [Lam(mpc(half, t)) for t in ts]
mags = [float(fabs(v)) for v in vals]
mins = []
for i in range(1, len(ts)-1):
    if mags[i] < mags[i-1] and mags[i] < mags[i+1]:
        mins.append(i)
print(f"scan done ({time.time()-t0:.0f}s); candidate minima at t ~ "
      + ", ".join(f"{float(ts[i]):.2f}" for i in mins))
def refine(tl, tr):
    for _ in range(60):
        tm1 = tl + (tr-tl)*mpf('0.382'); tm2 = tl + (tr-tl)*mpf('0.618')
        if fabs(Lam(mpc(half, tm1))) < fabs(Lam(mpc(half, tm2))): tr = tm2
        else: tl = tm1
        if tr - tl < mpf('1e-12'): break
    tz = (tl+tr)/2
    return tz, fabs(Lam(mpc(half, tz)))
zeros = []
t0 = time.time()
for i in mins:
    tz, depth = refine(ts[i]-mpf('0.05'), ts[i]+mpf('0.05'))
    scale = max(mags[max(0,i-2)], mags[min(len(mags)-1,i+2)])
    zeros.append((tz, depth, depth/scale))
print("refined:")
for tz, d, rel in zeros:
    tag = "ZERO (on-line)" if rel < 1e-12 else "shallow minimum (NOT a zero — investigate)"
    print(f"   t = {nstr(tz, 12)}   |Lambda| = {float(d):.2e}  rel {float(rel):.1e}   {tag}")
nz = sum(1 for _,_,r in zeros if r < 1e-12)

# ---------- Z-d: winding around [-0.4,1.4] x [0.5,15]
print("\n== Z-d: winding count ==")
t0 = time.time()
s1, s2, T1, T2 = mpf('-0.4'), mpf('1.4'), mpf('0.5'), mpf('15.0')
path = []
NB, NV = 36, 260
for i in range(NB+1): path.append(mpc(s1 + (s2-s1)*i/NB, T1))
for i in range(1, NV+1): path.append(mpc(s2, T1 + (T2-T1)*i/NV))
for i in range(1, NB+1): path.append(mpc(s2 - (s2-s1)*i/NB, T2))
for i in range(1, NV+1): path.append(mpc(s1, T2 - (T2-T1)*i/NV))
prev = None; total = mpf(0); mindig = 1e9
for spt in path:
    v = Lam(spt)
    mindig = min(mindig, float(fabs(v)))
    a = arg(v)
    if prev is not None:
        d = a - prev
        while d > pi: d -= 2*pi
        while d < -pi: d += 2*pi
        total += d
    prev = a
W = total/(2*pi)
print(f"winding W = {nstr(W, 10)}  (min |Lambda| on contour = {mindig:.1e})  [{time.time()-t0:.0f}s]")
def phi_main(t):
    s = mpc(half, t)
    return im((s/2)*log(N) - s*log(pi) + 2*loggamma((s+1)/2))
expect = (phi_main(T2) - phi_main(T1))/pi
print(f"gamma-main-term expectation (1/pi)[phi(T2)-phi(T1)] = {nstr(expect, 8)}")
print(f"Z-d: W = {float(W):.3f} vs zeros-found = {nz} vs main term = {float(expect):.2f}"
      f"   ({'PASS' if abs(float(W)-nz) < 0.4 and abs(float(W)-float(expect)) <= 2.5 else 'CHECK'})")

# central value, in the true normalization (x 4 pi)
lam_half = 4*pi*Lam(half)
Lhalf = lam_half/(N**mpf('0.25')*pi**mpf('-0.5')*gamma(mpf('0.75'))**2)
print(f"\ncentral values: Lambda(1/2) = {nstr(lam_half, 15)}")
print(f"               L(1/2)      = {nstr(Lhalf, 15)}")
print(f"first zeros (ordinates): " + ", ".join(nstr(tz, 10) for tz, d, r in zeros if r < 1e-12))
