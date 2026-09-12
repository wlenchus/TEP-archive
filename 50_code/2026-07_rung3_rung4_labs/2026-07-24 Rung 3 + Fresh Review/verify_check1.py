"""Independent verification of key TEP-corpus claims (2026-07-24 review session).
Checks: (1) eta(4t)eta(20t) dihedral-carrier claims; (2) dihedral leg x^3-x-1 vs eta(t)eta(23t);
(3) Frobenius magnitude classes for x^5+20x+16 at graded primes; (4) Kiepert quadratic;
(5) Collatz seam constants; (6) eta-quotient reach (character) arithmetic.
"""
import math
from fractions import Fraction

# ---------- eta products ----------
def eta_product(deltas, N):
    """q-expansion of prod eta(delta*tau) for list deltas, up to q^N (integer coeffs).
    eta(d t) = q^{d/24} prod (1-q^{dn}).  Total prefactor q^{sum(d)/24}."""
    pref = sum(deltas)
    assert pref % 24 == 0, "need integral leading exponent"
    shift = pref // 24
    # polynomial product of (1-q^{dn})
    coeffs = [0]*(N+1); coeffs[0] = 1
    for d in deltas:
        n = 1
        while d*n*(3*n-1)//2 <= N:  # use Euler pentagonal for each factor? simpler: multiply term by term
            n += 1
        # direct multiplication using pentagonal number theorem for prod(1-x^m) in variable x=q^d
        # prod_{n>=1}(1-x^n) = sum_k (-1)^k x^{k(3k-1)/2}, k over Z
        pent = {}
        k = 0
        while True:
            e1 = k*(3*k-1)//2; e2 = k*(3*k+1)//2
            if d*min(e1,e2) > N and k>0: break
            for e in {e1,e2}:
                if d*e <= N: pent[d*e] = pent.get(d*e,0) + ((-1)**(k%2))
            k += 1
        new = [0]*(N+1)
        for e,c in pent.items():
            if c==0: continue
            for i in range(0, N+1-e):
                if coeffs[i]: new[i+e] += c*coeffs[i]
        coeffs = new
    # shift by q^{shift}
    out = [0]*(N+1)
    for i in range(0, N+1-shift): out[i+shift] = coeffs[i]
    return out

def kronecker(a, n):
    """Kronecker symbol (a/n) for n>0."""
    if n == 0: return 1 if a in (1,-1) else 0
    if n < 0: raise ValueError
    result = 1
    a %= n if n%2==1 else 8*n  # keep sign info separately; simpler: implement properly
    return None

# proper Kronecker via sympy
import sympy
from sympy import primerange, isprime, factorint, sqrt, Rational, nsimplify

def kron(a, b):
    return int(sympy.ntheory.residue_ntheory.jacobi_symbol(a, b)) if b%2==1 and b>0 else _kron_full(a,b)

def _kron_full(a, b):
    # general Kronecker symbol
    if b == 0: return 1 if abs(a)==1 else 0
    sign = 1
    if b < 0:
        b = -b
        if a < 0: sign = -1
    # factor out 2s from b
    e2 = 0
    while b % 2 == 0: b//=2; e2+=1
    if e2:
        if a % 2 == 0: return 0
        if a % 8 in (3,5): sign *= (-1)**e2
    if b == 1: return sign
    return sign * int(sympy.jacobi_symbol(a % b, b))

def chi(D, n):
    """quadratic character mod |D| via Kronecker (D/n)"""
    return _kron_full(D, n)

N = 2100
c = eta_product([4,20], N)   # eta(4t)eta(20t), leading q^{24/24}=q^1
print("eta(4t)eta(20t) first coeffs a_1..a_50:", c[1:51])

# --- claim: weight-1 form, char in chi_{-20} class; Hecke: a_{p^2} = a_p^2 - chi_{-20}(p); mult; class table
ok_sq, bad_sq = 0, []
for p in primerange(3, 45):
    if p in (2,5): continue
    if p*p <= N:
        lhs = c[p*p]; rhs = c[p]**2 - chi(-20, p)
        if lhs == rhs: ok_sq += 1
        else: bad_sq.append((p, lhs, rhs))
print("square recursion a_{p^2}=a_p^2-chi_-20(p):", ok_sq, "OK,", "fails:", bad_sq)

ok_m, bad_m = 0, []
import itertools
for m in range(2, 46):
    for n in range(2, 46):
        if math.gcd(m,n)==1 and m*n<=N:
            if c[m*n] == c[m]*c[n]: ok_m+=1
            else: bad_m.append((m,n,c[m*n],c[m]*c[n]))
print("multiplicativity checks:", ok_m, "OK; fails:", len(bad_m), bad_m[:5])

# class table: split principal (p = x^2+5y^2) -> a_p = +-2 ; split nonprincipal (2x^2+2xy+3y^2) -> 0; inert -> 0
def qq_class(p):
    if p in (2,5): return 'ram'
    if chi(-20,p) == -1: return 'inert'
    # split: principal iff p represented by x^2+5y^2
    for x in range(0, int(math.isqrt(p))+1):
        r = p - x*x
        if r>=0 and r%5==0:
            y2 = r//5
            s = int(math.isqrt(y2))
            if s*s==y2: return 'principal'
    return 'nonprincipal'

tab = {}
for p in primerange(3, 300):
    if p in (2,5): continue
    cl = qq_class(p); tab.setdefault(cl, []).append((p, c[p]))
for cl, lst in tab.items():
    vals = set(v for _,v in lst)
    print(f"class {cl}: primes {len(lst)}, a_p values {sorted(vals)}")
print("a_2 =", c[2], " a_5 =", c[5])

# ---------- dihedral leg: x^3 - x - 1 vs eta(t)eta(23t) ----------
c23 = eta_product([1,23], 2000)
from sympy import Poly, symbols, GF
x = symbols('x')
ok, bad = 0, []
for p in primerange(2, 800):
    if p == 23:
        continue
    fp = Poly(x**3 - x - 1, x, modulus=p)
    nroots = len(fp.ground_roots())
    ap_galois = nroots - 1
    if c23[p] == ap_galois: ok += 1
    else: bad.append((p, c23[p], ap_galois))
print("x^3-x-1 vs eta(1,23): ", ok, "primes OK; fails:", bad[:5])

# ---------- Frobenius orders for x^5+20x+16 at graded primes ----------
# cycle type of factorization degrees -> element order in A5
f5 = x**5 + 20*x + 16
def frob_cycle(p):
    fp = Poly(f5, x, modulus=p)
    degs = sorted(q.degree() for q,_ in fp.factor_list()[1] for _ in range(_)) if False else None
    fl = fp.factor_list()[1]
    degs = []
    for q, m in fl: degs += [q.degree()]*m
    return sorted(degs)

graded = [3,7,11,13,17,19,23,29,31]
# claimed magnitude classes {1/phi,1,1,1/phi,1,1/phi,0,1,phi}
claim = ['1/phi','1','1','1/phi','1','1/phi','0','1','phi']
def mag_from_cycle(degs):
    import collections
    if degs == [5]: return 'phi-or-1/phi (order5)'
    if degs == [1,1,3]: return '1 (order3)'
    if degs == [1,2,2]: return '0 (order2)'
    if degs == [1,1,1,1,1]: return '2 (order1)'
    return f'? {degs}'
print("\nx^5+20x+16 Frobenius classes at graded primes:")
for p, cl in zip(graded, claim):
    print(f"  p={p}: factor degrees {frob_cycle(p)} -> {mag_from_cycle(frob_cycle(p))}   (record claims |a_p| class {cl})")

# Chebotarev tallies over primes < 2000 for A5 densities 1/60,15/60,20/60,24/60
import collections
tally = collections.Counter()
for p in primerange(7, 2000):
    if p in (2,5): continue
    t = tuple(frob_cycle(p))
    tally[t]+=1
tot = sum(tally.values())
print("Chebotarev tallies:", {k: round(v/tot,3) for k,v in sorted(tally.items())}, "(A5 expects (5):0.4, (1,1,3):0.333, (1,2,2):0.25, (1^5):0.017)")

# ---------- Kiepert quadratic ----------
from sympy import sqrt as ssqrt, expand, simplify, Integer
Zp = (271 + 145*ssqrt(5))/1013888
Zm = (271 - 145*ssqrt(5))/1013888
q1 = expand(32444416*Zp**2 - 17344*Zp - 1)
q2 = expand(32444416*Zm**2 - 17344*Zm - 1)
jp = 10400 - 4640*ssqrt(5)
jm = 10400 + 4640*ssqrt(5)
print("\nKiepert quadratic at claimed roots:", simplify(q1), simplify(q2))
print("N(j) =", expand(jp*jm), "= 2^12*5^3 =", 2**12*5**3)

# ---------- Collatz constants ----------
rho = math.log(2, 3)   # log_3 2
p_star = 2 - math.log2(3)
H2 = lambda p: -p*math.log2(p) - (1-p)*math.log2(1-p)
print("\nCollatz: p* = 2-log2 3 =", round(p_star,5), "(claim 0.41504)")
print("H2(1/log2 3) =", round(H2(1/math.log2(3)),5), "(claim 0.94996); thinning bits/step:", round(1 - H2(1/math.log2(3)),4), "(claim 0.0500/symbol; 0.0793 elsewhere -- check)")
print("1/(2 ln 3) =", round(1/(2*math.log(3)),7), "(claim 0.4551196)")
print("log2(3) - 1 =", round(math.log2(3)-1, 5), " (raw-step thinning candidate 0.585?)  2-log2(3)=", round(2-math.log2(3),5))

# ---------- eta-quotient character (reach) arithmetic ----------
# character of prod eta(d t)^{r_d}, weight k = (1/2) sum r_d : chi = ((-1)^k s / .) with s = prod d^{r_d}
for deltas in ([4,20],[1,5],[2,10],[8,40],[1,1],[5,5]):
    s = 1
    for d in deltas: s *= d
    k = len(deltas)//2
    D = (-1)**k * s
    # squarefree kernel of D
    fk = factorint(D)
    ker = 1
    for pr, e in fk.items():
        if pr == -1: ker *= -1 if e%2 else 1
        elif e % 2: ker *= pr
    print(f"eta{deltas}: weight {k}, s={s}, character disc class {ker}")
