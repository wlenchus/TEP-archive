"""DEEP-BOUNDARY METER — the pole meter of the fold defect at Doud-1951 and -2141.
2026-08-13 (session B). Full 10^5 coefficient tables; float64 survey.

THEOREM R (derived this session, see record): with Phi(y) = sqrt(y) sum_n n c_n K0(2 pi n y),
poles of L(F,w) at w0 force  Phi(y) NOT= o( y^{-(Re w0 + 1/2)} )  as y -> 0.
Since Re w0 in (0,1) for any critical-strip pole, the WEAKEST possible blow-up is y^{-1/2}.
Hence the single sufficient statistic:
        METER(y) := |Phi(y)| * (N y)^{1/2}
A pole anywhere in the strip forces limsup METER > 0 (and -> infinity if Re w0 > 1/2).
Entirety predicts METER -> 0.  No epsilon, no fold constant, no dual needed: the meter is
convention-independent.

PREREG (stated before run; same-session, unhashed):
  M-a  METER decreases over the probed range at both fields (>= 1 decade of decrease
       from y=1e-2 to y=1e-4), i.e. no pole floor emerges.
  M-b  The local log-slope of |Phi| stays ABOVE -1/2 (no y^{-1/2} blow-up) over the
       deep decade.
  M-c  Both fields behave alike (the phenomenon is structural, not field-specific).
Kill K-M: if METER trends upward or flattens at a positive floor over the deep decade,
that is a POLE SIGNAL and is reported as such at headline volume.
"""
import numpy as np, csv, time
from scipy.special import k0

CSV = {1951: "/root/.claude/projects/-home-claude/e1c6a220-faa1-5bd1-9d10-c0c3344b96cd/tool-results/project-doc-b99b6076-631d-43e3-92a2-b1e8923dc0c4.txt",
       2141: "/root/.claude/projects/-home-claude/e1c6a220-faa1-5bd1-9d10-c0c3344b96cd/tool-results/project-doc-70dab881-3783-468e-aa79-e35a5252de13.txt"}
NMAX = 100000
phi_g = (1+np.sqrt(5))/2

def parse_apex(s):
    s = s.strip()
    if s == "0": return 0j
    sg = 1.0
    if s[0] == '+': s = s[1:]
    elif s[0] == '-': sg = -1.0; s = s[1:]
    fac = 1.0
    if s.endswith("*1/phi"): fac = 1/phi_g; s = s[:-6]
    elif s.endswith("*phi"): fac = phi_g; s = s[:-4]
    elif s.endswith("*2"): fac = 2.0; s = s[:-2]
    k = int(s[7:])
    return sg*fac*np.exp(1j*np.pi*k/5)

def build(N):
    ap = {}; chi = {}
    for row in csv.DictReader(open(CSV[N])):
        p = int(row['p']); ap[p] = parse_apex(row['a_p_exact'])
        c = row['chi_p_exact'].strip()
        chi[p] = 0j if c == '0' else np.exp(2j*np.pi*int(c[6:])/5)
    spf = np.zeros(NMAX+1, dtype=np.int64); spf[:] = np.arange(NMAX+1)
    for i in range(2, int(NMAX**0.5)+1):
        if spf[i] == i: spf[i*i::i] = np.minimum(spf[i*i::i], i)
    cn = np.zeros(NMAX+1, dtype=np.complex128); cn[1] = 1
    for n in range(2, NMAX+1):
        p = int(spf[n]); m = n; k = 0
        while m % p == 0: m //= p; k += 1
        pk = p**k
        if cn[pk] == 0 and pk != 1:
            prev, cur = 1+0j, ap[p]
            for _ in range(k-1): prev, cur = cur, ap[p]*cur - chi[p]*prev
            cn[pk] = cur
        cn[n] = cn[pk] if m == 1 else cn[pk]*cn[m]
    return cn

# divisor bound for the tail:  |c_n| <= d(n) <= 2 sqrt(n)
def tail_bound(y, M=NMAX):
    n = np.arange(M+1, M+40001, dtype=float)
    x = 2*np.pi*n*y
    t = np.sqrt(y)*n*(2*np.sqrt(n))*np.sqrt(np.pi/(2*x))*np.exp(-x)
    s = t.sum()
    n2 = M+40001; x2 = 2*np.pi*n2*y
    s += np.sqrt(y)*n2*2*np.sqrt(n2)*np.sqrt(np.pi/(2*x2))*np.exp(-x2)/(1-np.exp(-2*np.pi*y))
    return s

for N in (1951, 2141):
    t0 = time.time(); cn = build(N)
    nn = np.arange(NMAX+1, dtype=float); w = nn*cn          # n c_n
    print(f"\n===== N = {N} =====  built c_n to {NMAX} in {time.time()-t0:.0f}s; "
          f"max|c_n| = {np.abs(cn[1:]).max():.3f}")
    ys = np.logspace(-2, -4, 121)
    Phi = np.zeros(len(ys), dtype=np.complex128); tails = np.zeros(len(ys))
    t0 = time.time()
    for i, y in enumerate(ys):
        x = 2*np.pi*y*nn[1:]
        cut = min(NMAX, int(700/(2*np.pi*y))+2)
        K = np.zeros(NMAX); K[:cut] = k0(x[:cut])
        Phi[i] = np.sqrt(y)*np.dot(w[1:], K)
        tails[i] = tail_bound(y)
    print(f"survey done in {time.time()-t0:.0f}s")
    meter = np.abs(Phi)*np.sqrt(N*ys)
    print(f"{'y':>10s} {'|Phi(y)|':>12s} {'METER':>12s} {'tail':>10s}")
    for i in range(0, len(ys), 10):
        print(f"{ys[i]:10.3e} {abs(Phi[i]):12.4e} {meter[i]:12.4e} {tails[i]:10.1e}")
    # decade statistics (robust to oscillation): max and RMS of METER per half-decade
    print("  half-decade   max METER    rms METER    max|Phi|")
    edges = np.logspace(-2, -4, 5)
    for a, b in zip(edges[:-1], edges[1:]):
        m = (ys <= a) & (ys >= b)
        print(f"  [{b:.1e},{a:.1e}]  {meter[m].max():10.3e}  {np.sqrt((meter[m]**2).mean()):10.3e}"
              f"  {np.abs(Phi[m]).max():10.3e}")
    lo = (ys <= 1e-2)&(ys >= 3.2e-3); hi = (ys <= 3.2e-4)&(ys >= 1e-4)
    ratio = meter[lo].max()/meter[hi].max()
    print(f"  METER max drop across the probed range: factor {ratio:.3g}")
    # local log-slope of |Phi| in the deep decade
    sl = np.polyfit(np.log(ys[hi]), np.log(np.abs(Phi[hi])), 1)[0]
    print(f"  deep-decade log-slope d log|Phi| / d log y = {sl:+.3f}   "
          f"(pole floor requires <= -0.5)   -> {'NO POLE SIGNAL' if sl > -0.5 else 'POLE SIGNAL'}")
    np.save(f'/home/claude/phi_{N}.npy', np.vstack([ys, Phi.real, Phi.imag, tails]))
