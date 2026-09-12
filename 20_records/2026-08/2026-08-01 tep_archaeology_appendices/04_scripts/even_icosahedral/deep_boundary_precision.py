"""DEEP-BOUNDARY PRECISION BLOCK — the sharpest residue bound the committed tables allow.
2026-08-13 (session B).  mp.dps 40 (series branch at 68); full 10^5 tables; rigorous
truncation tails via |c_n| <= d(n) <= 2 sqrt(n).

Reports, per field and per probe depth u  (y = 1/(Nu)):
   |Phi(y)| measured        (direct Galois-side series; NO fold assumed)
   tail bound               (rigorous, divisor-bounded)
   METER = (|Phi|+tail) * (N y)^{1/2}   = the Theorem-R bound on |d| for beta = 1/2
   D(u) = Phi(1/(Nu)) - eps N u^2 Psi(u)   (the fold defect itself)
   and the automorphy prediction N u^2 e^{-2 pi u}/2 for comparison.
"""
import csv, time
from mpmath import mp, mpf, mpc, sqrt, exp, pi, log, euler, fabs, nstr, conj, besselk

mp.dps = 40
NMAX = 100000
CSV = {1951: "/root/.claude/projects/-home-claude/e1c6a220-faa1-5bd1-9d10-c0c3344b96cd/tool-results/project-doc-b99b6076-631d-43e3-92a2-b1e8923dc0c4.txt",
       2141: "/root/.claude/projects/-home-claude/e1c6a220-faa1-5bd1-9d10-c0c3344b96cd/tool-results/project-doc-70dab881-3783-468e-aa79-e35a5252de13.txt"}
PHI = (1+sqrt(5))/2
def z10(k): return exp(mpc(0,1)*pi*k/5)
def z5(j):  return exp(mpc(0,2)*pi*j/5)
def parse(s):
    s = s.strip()
    if s == "0": return mpc(0)
    sg = mpf(1)
    if s[0] == '+': s = s[1:]
    elif s[0] == '-': sg = mpf(-1); s = s[1:]
    f = mpf(1)
    if s.endswith("*1/phi"): f = 1/PHI; s = s[:-6]
    elif s.endswith("*phi"): f = PHI; s = s[:-4]
    elif s.endswith("*2"): f = mpf(2); s = s[:-2]
    return sg*f*z10(int(s[7:]))

# --- fast high-precision K0
GAM = +euler
def K0series(x, wp=68):
    with mp.workprec(int(wp*3.33)):
        q = x*x/4
        I0 = mpf(1); term = mpf(1); S = mpf(0); H = mpf(0); k = 0
        while True:
            k += 1
            term = term*q/(k*k)
            H += mpf(1)/k
            I0 += term; S += term*H
            if term < mpf('1e-75') and k > x/2 + 5: break
        return -(log(x/2)+GAM)*I0 + S
def K0asym(x):
    S = mpf(1); t = mpf(1); k = 0
    while True:
        nx = t*(-(2*k+1)**2)/(8*x*(k+1))
        if abs(nx) >= abs(t) or abs(nx) < mpf('1e-48'): break
        S += nx; t = nx; k += 1
    return sqrt(pi/(2*x))*exp(-x)*S
def K0(x):
    return K0series(x) if x < 25 else (K0asym(x) if x < 200 else mpf(0))

def build(N):
    ap = {}; chi = {}
    for row in csv.DictReader(open(CSV[N])):
        p = int(row['p']); ap[p] = parse(row['a_p_exact'])
        c = row['chi_p_exact'].strip()
        chi[p] = mpc(0) if c == '0' else z5(int(c[6:]))
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
    return cn

def tailb(y):
    s = mpf(0)
    for n in range(NMAX+1, NMAX+60001):
        x = 2*pi*n*y
        s += sqrt(y)*n*2*sqrt(mpf(n))*sqrt(pi/(2*x))*exp(-x)
    n2 = NMAX+60001; x2 = 2*pi*n2*y
    s += sqrt(y)*n2*2*sqrt(mpf(n2))*sqrt(pi/(2*x2))*exp(-x2)/(1-exp(-2*pi*y))
    return s

EPS = {1951: None, 2141: None}
def eps_of(N, pin):
    e5 = (N-1)//5; t0 = pow(2, e5, N); io = {}
    for k in range(5): io[pow(t0, k, N)] = (k*pin) % 5
    z = exp(mpc(0,2)*pi/5); eN = exp(mpc(0,2)*pi/N); tau = mpc(0)
    for x in range(1, N): tau += z**io[pow(x, e5, N)]*eN**x
    return tau

for N, pin, aNk in ((1951, 4, 2), (2141, 1, 8)):
    t0 = time.time(); cn = build(N)
    tau = eps_of(N, pin); eps = -tau/(sqrt(N)*z10(aNk))
    print(f"\n===== N = {N} =====   (built in {time.time()-t0:.0f}s;  eps = {nstr(eps,12)})")
    print(f"{'u':>5s} {'y':>11s} {'|Phi(y)|':>14s} {'tail':>10s} {'METER (|d| bd)':>16s} "
          f"{'|D(u)|':>12s} {'predict Nu^2e^-2piu/2':>22s}")
    best = None
    for u in (mpf(5), mpf('5.5'), mpf(6), mpf('6.2')):
        y = 1/(N*u)
        t1 = time.time()
        twopiy = 2*pi*y
        tot = mpc(0)
        for n in range(1, NMAX+1):
            x = twopiy*n
            if x > 200: break
            k = K0(x)
            if k != 0: tot += n*cn[n]*k
        Phi = sqrt(y)*tot
        # dual profile at u (cheap: only a few terms matter)
        tw = 2*pi*u; tot2 = mpc(0)
        for n in range(1, 200):
            x = tw*n
            if x > 200: break
            tot2 += n*conj(cn[n])*K0(x)
        Psi = sqrt(u)*tot2
        D = Phi - eps*N*u*u*Psi
        tb = tailb(y)
        meter = (fabs(Phi)+tb)*sqrt(mpf(1)/u)
        pred = N*u*u*exp(-2*pi*u)/2
        print(f"{float(u):5.2f} {float(y):11.4e} {float(fabs(Phi)):14.5e} {float(tb):10.1e} "
              f"{float(meter):16.5e} {float(fabs(D)):12.3e} {float(pred):22.5e}   [{time.time()-t1:.0f}s]")
        if best is None or meter < best: best = meter
    print(f"  --> sharpest Theorem-R bound at this field:  |d| <= {float(best):.3e}")
