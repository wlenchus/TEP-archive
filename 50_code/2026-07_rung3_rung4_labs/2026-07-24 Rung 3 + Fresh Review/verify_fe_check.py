"""Independent functional-equation test of the pre-registered OT1 eigensystem.
Own implementation (not the corpus's fe_grade.py): weight-1 FE  F(y) = eps * y^-1 * conj(F)(1/y)
with F(y) = sum a_n e^{-2 pi n y / sqrt(N)}.  If N is the true conductor, the ratio
R(y) = y * F(y) / conj(F(1/y)) is a y-independent unimodular constant.
Scan the 8 quadratic twists (cond | 40) of the decoded solution_0 table, N in {4000, 8000, 16000}.
"""
import json, math, cmath

with open('/home/claude/TEP-archive/50_code/ot1/full_width_instrument/2026-07-22 ot1_16000_PREREGISTERED_prediction.json') as fh:
    data = json.load(fh)

s5 = math.sqrt(5)
def parse(s):
    sgn = 1 if s[0]=='+' else -1
    body = s[1:]
    mult = 1
    if body.endswith('*i'): mult = 1j; body = body[:-2]
    elif body.endswith('*1'): body = body[:-2]
    if body == '1': mag = 1.0
    elif body == '(sqrt5-1)/2': mag = (s5-1)/2
    elif body == '(1+sqrt5)/2': mag = (1+s5)/2
    else: raise ValueError(body)
    return sgn*mag*mult

def kron(D, n):
    # Kronecker symbol (D/n), n>0
    if math.gcd(abs(D), n) != 1: return 0
    result = 1
    a = D; b = n
    # use quadratic reciprocity via Jacobi; handle 2s and sign of a
    def jacobi(a, b):
        assert b > 0 and b % 2 == 1
        a %= b; r = 1
        while a:
            while a % 2 == 0:
                a //= 2
                if b % 8 in (3,5): r = -r
            a, b = b, a
            if a % 4 == 3 and b % 4 == 3: r = -r
            a %= b
        return r if b == 1 else 0
    e2 = 0
    while b % 2 == 0: b //= 2; e2 += 1
    if e2:
        if a % 2 == 0: return 0
        if a % 8 in (3,5): result *= (-1)**e2
    if a < 0 and False: pass
    result *= jacobi(a if a>0 else a % (4*b) if b>1 else a, b) if b>1 else 1
    # jacobi needs a mod b handled with sign: (a/b) for negative a: (a/b) = (-1/b)^{sign} (|a|/b)
    return result

def kron2(D, n):
    # cleaner: full Kronecker via factorization of n
    if n == 0: return 0
    res = 1
    if n < 0: n = -n
    for p in _factor(n):
        res *= _kron_p(D, p)
        if res == 0: return 0
    return res

def _factor(n):
    fs = []
    d = 2
    while d*d <= n:
        while n % d == 0: fs.append(d); n //= d
        d += 1
    if n > 1: fs.append(n)
    return fs

def _kron_p(D, p):
    if p == 2:
        if D % 2 == 0: return 0
        return 1 if D % 8 in (1,7) else -1
    if D % p == 0: return 0
    return pow(D % p, (p-1)//2, p) == 1 and 1 or -1

TW = [1, -4, 5, 8, -8, -20, 40, -40]   # quadratic characters by discriminant-ish codes; use kron2(t, n)

NMAX = 260
def build_an(ap, chiD, tw):
    """multiplicative extension with recursion a_{p^{r+1}} = a_p a_{p^r} - chi(p) a_{p^{r-1}}, a_2=a_5=0.
    tw = twist discriminant code; twisted coefficients eps(p) a_p, nebentypus chi*eps^2 = chi."""
    a = [0]*(NMAX+1); a[1] = 1
    # prime powers
    pp = {}
    for p in range(2, NMAX+1):
        if all(p % q for q in range(2, int(p**0.5)+1)):
            if p in (2,5):
                vals = {1:1, p:0}
            else:
                apv = ap.get(str(p))
                if apv is None:  # a_p = 0 class-2 prime (not listed)
                    apv = 0
                else:
                    apv = parse(apv['a_p'])
                apv = apv * kron2(tw, p)
                chp = kron2(chiD, p) * (kron2(tw, p)**2 if kron2(tw,p)!=0 else 0)
                # note: if tw ramifies p (kron=0) then twisted a_p = 0 and Euler factor degenerates;
                # for p | 40 only p=2,5 anyway.
                vals = {1:1, p:apv}
                q = p*p; prev, cur = 1, apv
                while q <= NMAX:
                    nxt = apv*cur - kron2(chiD,p)*prev  # chi of the ORIGINAL form for untwisted recursion
                    # twisted form g=f x eps: b_p = eps(p)a_p, b_{p^2} = b_p^2 - chi eps^2(p) = ...
                    # since eps^2 = 1 on p coprime to 40, chi_g(p) = chi(p). recursion consistent.
                    vals[q] = nxt; prev, cur = cur, nxt; q *= p
                pp[p] = vals
                continue
            pp[p] = vals
    for n in range(2, NMAX+1):
        m = n; prod = 1
        for p in _factor_u(n):
            e = 0
            while m % p == 0: m //= p; e += 1
            prod *= pp[p].get(p**e, 0)
        a[n] = prod
    return a

def _factor_u(n):
    return sorted(set(_factor(n)))

def F(a, y, N):
    s = 0
    for n in range(1, NMAX+1):
        s += a[n]*cmath.exp(-2*math.pi*n*y/math.sqrt(N))
    return s

def fe_ratio(a, N):
    """return list of eps(y) = y*F(y)/conj(F(1/y)) at test y; constant & unimodular iff FE holds."""
    out = []
    for y in (1.0, 1.15, 1.3):
        num = y*F(a, y, N)
        den = F(a, 1/y, N).conjugate()
        out.append(num/den if abs(den) > 1e-25 else float('nan'))
    return out

for branch, chiD in (("chi_-4", -4), ("chi_-20", -20)):
    ap = data[branch]["a_p_table_p<=200"]
    print(f"\n===== branch {branch} =====")
    for tw in TW:
        a = build_an(ap, chiD, tw)
        for N in (4000, 8000, 16000):
            r = fe_ratio(a, N)
            spread = max(abs(r[i]-r[0]) for i in range(len(r)))
            mod = abs(r[0])
            if spread < 1e-6 and abs(mod-1) < 1e-6:
                print(f"  twist {tw:>3}, N={N}: FE PASS  eps = {r[0]:.10f} spread {spread:.2e}")
            elif tw == 1:
                print(f"  twist {tw:>3}, N={N}: fail (spread {spread:.2e}, |eps| {mod:.4f})")
