"""R3.4-e opening computations.
(1) The vanishing test: transported-ray-weight lattice thetas of nonprincipal prime ideals
    Theta~_p(q) = (1/2) sum_{x = y*r mod p, x+y odd} (-1)^y q^{(x^2+5y^2)/p}
    Claim to test: these vanish IDENTICALLY (the analytic q-face is closed at every
    lattice resolution -- the would-be shortcut evaluator cannot exist).
(2) Extend the frozen key to p < 300 (committed now, BEFORE any formula is fitted:
    the fit-then-blind-grade protocol uses p<100 to fit, 100<p<300 to grade).
(3) Depth-model instances: eta(t)eta(2t) = CM form of Q(sqrt-2)? T-monodromy order 8?
    (deck order = 2^{v2(cond chi-family)}: {1,5}-tower mu4/cond-4-family;
     {1,2}-tower mu8/cond-8-family).
(4) Capacity table: Sturm(Gamma_0(N), wt 2) = psi(N)/6 vs the campaign's recorded widths.
"""
import math

# ---------- shared arithmetic ----------
def is_prime(p):
    if p < 2: return False
    return all(p % d for d in range(2, int(math.isqrt(p))+1))

def root_conv(p):
    for r in range(1, p):
        if (r*r + 5) % p == 0:
            return r if r < p - r else p - r
    return None

def is_split_nonprincipal(p):
    if p in (2,5) or not is_prime(p): return None
    if pow(-5 % p, (p-1)//2, p) != 1: return None
    for x in range(0, int(math.isqrt(p))+1):
        rr = p - x*x
        if rr >= 0 and rr % 5 == 0:
            y2 = rr//5; s = int(math.isqrt(y2))
            if s*s == y2: return False
    return True

# ---------- (1) vanishing test ----------
print("(1) transported-ray-weight lattice thetas of p_p (60 q-terms):")
for p in (3, 7, 23):
    r = root_conv(p)
    NB = 60*p
    co = [0]*(61)
    B = int(math.isqrt(NB))+1
    for x in range(-B, B+1):
        for y in range(-(int(math.isqrt(NB//5))+1), int(math.isqrt(NB//5))+2):
            n = x*x + 5*y*y
            if 0 < n <= NB and n % p == 0 and (x+y) % 2 == 1 and (x - y*r) % p == 0:
                co[n//p] += (-1)**(y & 1)
    nz = [k for k,v in enumerate(co) if v != 0]
    print(f"    p={p} (r={r}): nonzero coefficients through q^60: {nz if nz else 'NONE -- vanishes identically'}")

# ---------- (2) key extension to p < 300 ----------
I = complex(0,1)
def in_pfrak(x, y, p, r): return (x - y*r) % p == 0
r3 = root_conv(3); psi3 = I
def rel_psi(p):
    rp = root_conv(p); n = 3*p; found = None
    for y in range(0, int(math.isqrt(n//5))+1):
        x2 = n - 5*y*y
        if x2 < 0: continue
        x = int(math.isqrt(x2))
        if x*x != x2: continue
        for (xx, yy) in ((x,y),(x,-y)) if y else ((x,0),):
            s3 = psi3 if in_pfrak(xx,yy,3,r3) else 1/psi3
            val = (-1)**(yy & 1)
            psq = val/s3
            psip = psq if in_pfrak(xx,yy,p,rp) else 1/psq
            if found is None: found = psip
            else: assert abs(found - psip) < 1e-9, (p, found, psip)
    return found

def fmt(z):
    for lab, v in (("+1",1),("-1",-1),("+i",I),("-i",-I)):
        if abs(complex(z)-v) < 1e-9: return lab
    return "??"

plist = [p for p in range(3, 300) if is_split_nonprincipal(p)]
key = {p: (psi3 if p == 3 else rel_psi(p)) for p in plist}
print("\n(2) EXTENDED KEY, p < 300 (fit zone p<100 | blind-grade zone 100<p<300):")
row1 = "    " + "  ".join(f"{p:>4}" for p in plist)
row2 = "    " + "  ".join(f"{fmt(key[p]):>4}" for p in plist)
print(row1); print(row2)

# ---------- (3) depth-model instances ----------
N = 800
def eta_product(deltas, N):
    pref = sum(deltas)
    coeffs = [0]*(N+1); coeffs[0] = 1
    for d in deltas:
        pent = {}
        k = 0
        while True:
            e1 = k*(3*k-1)//2; e2 = k*(3*k+1)//2
            if d*min(e1,e2) > N and k > 0: break
            for e in {e1, e2}:
                if d*e <= N: pent[d*e] = pent.get(d*e,0) + ((-1)**(k%2))
            k += 1
        new = [0]*(N+1)
        for e,c in pent.items():
            if c == 0: continue
            for i in range(0, N+1-e):
                if coeffs[i]: new[i+e] += c*coeffs[i]
        coeffs = new
    return coeffs, pref

co12, pref = eta_product([1,2], N)   # leading exponent 3/24 = 1/8 -> mu_8 deck
print(f"\n(3) eta(t)eta(2t): leading cusp exponent {pref}/24 = 1/8  => deck mu_8; "
      f"T-monodromy = e^(i pi 3/12) = e^(i pi/4), order 8")
# shifted series: q^{1/8} * sum co12[n] q^n ; as a form: f = sum a_m q^m with m = (8n+1)/8... use
# the classical statement: eta(t)eta(2t) = sum_{x,y} (weight) q^{(x^2+2y^2)/8}-type; verify instead
# the Hecke structure of eta(8t)eta(16t) (the 8-rescale, integral exponents, level 128, chi_-8 class):
c8, _ = eta_product([8,16], 2000)
def _factor(n):
    fs=[]; d=2
    while d*d<=n:
        while n%d==0: fs.append(d); n//=d
        d+=1
    if n>1: fs.append(n)
    return fs
def kron_p(D,p):
    if p==2: return 0 if D%2==0 else (1 if D%8 in (1,7) else -1)
    if D%p==0: return 0
    return 1 if pow(D%p,(p-1)//2,p)==1 else -1
def kron(D,n):
    r=1
    for p in _factor(n): r*=kron_p(D,p)
    return r
ok_sq = sum(1 for p in range(3,44) if is_prime(p) and p*p<=2000 and c8[p*p]==c8[p]**2-kron(-8,p))
bad = [(p, c8[p*p], c8[p]**2-kron(-8,p)) for p in range(3,44) if is_prime(p) and p*p<=2000 and c8[p*p]!=c8[p]**2-kron(-8,p)]
okm = sum(1 for m in range(2,45) for n in range(2,45) if math.gcd(m,n)==1 and m*n<=2000 and c8[m*n]==c8[m]*c8[n])
print(f"    eta(8t)eta(16t): weight-1 Hecke square-recursion vs chi_-8: {ok_sq} OK, fails {bad[:3]}")
print(f"    multiplicativity checks OK: {okm};  => the {{1,2}}-tower is the chi_-8-family carrier (Q(sqrt-2))")
print(f"    depth model: minimal-tower deck order 2^v2(cond): {{1,5}}: 1/4 -> mu4 (cond 4,20); {{1,2}}: 1/8 -> mu8 (cond 8,40)")

# ---------- (4) capacity table ----------
def psi_idx(N):
    r = N
    for p in set(_factor(N)):
        r = r // p * (p+1)
    return r
print("\n(4) capacity ledger (weight 2 hosts): Sturm = psi(N)/6 = message length; C = ln N (global capacity)")
print(f"    {'N':>6} {'lnN':>7} {'psi(N)':>7} {'Sturm':>6}  recorded-width outcome")
rec = {800:'R', 1600:'R', 2000:'R', 4000:'NR free 3', 8000:'NR free 7', 16000:'NR free 7 (width 2701: free 244 -- capacity violation; full 4801: free 7)'}
for Nl in (800, 1600, 2000, 4000, 8000, 16000):
    print(f"    {Nl:>6} {math.log(Nl):>7.3f} {psi_idx(Nl):>7} {psi_idx(Nl)//6:>6}  {rec[Nl]}")
