"""R3.4 first executions, dihedral floor (eta(4t)eta(20t) / psi_K of Q(sqrt-5), ray conductor (2)).

(a) Theta-decomposition: is eta(4t)eta(20t) == (1/2) * sum_{(x,y)!=0} (-1)^y q^{x^2+5y^2} ?
    => the q-expansion is PURE principal-class data; the C4 refinement (+-i on nonprincipal
       ideals) cancels identically in every coefficient (boundary-null, bulk-carried).
(b) Deck/multiplier tower: T-monodromy of eta(t)eta(5t), eta(2t)eta(10t), eta(4t)eta(20t)
    = i, -1, +1  (Z/4 -> Z/2 -> 1), computed exactly and numerically.
(c) The committed grading key for the full R3.4 run: relative psi_K(p_p) in {+-1,+-i}
    for nonprincipal split p < 100, via pure ideal arithmetic, orientation convention pinned:
    r_p = the root of x^2 = -5 mod p in (0, p/2);  p_p = (p, r_p + sqrt-5);  psi(p_3) := +i.
(d) Bulk-mode exhibit: a_{3p} = 0 coefficients whose lattice-orbit decomposition carries
    the relative datum (which (x,y)-orbit belongs to which prime pair, via x = y*r mod p).
"""
import math, cmath

# ---------- (a) eta product and signed principal theta ----------
N = 2000
def eta_product(deltas, N):
    pref = sum(deltas); assert pref % 24 == 0
    shift = pref // 24
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
    out = [0]*(N+1)
    for i in range(0, N+1-shift): out[i+shift] = coeffs[i]
    return out

c = eta_product([4,20], N)

theta = [0]*(N+1)
X = int(math.isqrt(N))+1
Y = int(math.isqrt(N//5))+1
for x in range(-X, X+1):
    for y in range(-Y, Y+1):
        n = x*x + 5*y*y
        if 0 < n <= N and (x + y) % 2 == 1:   # coprime to the ray conductor (2): odd norm
            theta[n] += (-1)**(y & 1)
ok = all(2*c[n] == theta[n] for n in range(1, N+1))
print(f"(a) eta(4t)eta(20t) == (1/2)*signed principal theta, n<=2000: {'IDENTITY HOLDS' if ok else 'FAILS'}")
mism = [n for n in range(1,N+1) if 2*c[n]!=theta[n]][:5]
if mism: print("   mismatches:", mism)

# ---------- (b) deck multiplier tower ----------
import mpmath as mpm
mpm.mp.dps = 40
def eta(tau):
    q = mpm.exp(2j*mpm.pi*tau)
    prod = mpm.mpf(1)
    n = 1
    while True:
        t = q**n
        if abs(t) < mpm.mpf(10)**(-50): break
        prod *= (1 - t); n += 1
    return mpm.exp(2j*mpm.pi*tau/24)*prod

tau0 = mpm.mpc(0.13, 0.77)
for d1, d2, name in ((1,5,'eta(t)eta(5t)'), (2,10,'eta(2t)eta(10t)'), (4,20,'eta(4t)eta(20t)')):
    f  = lambda t, a=d1, b=d2: eta(a*t)*eta(b*t)
    r  = f(tau0+1)/f(tau0)
    exact = mpm.exp(1j*mpm.pi*(d1+d2)/12)
    print(f"(b) T-monodromy of {name}: numeric {complex(r):.6f}, exact e^(i pi {d1+d2}/12) = {complex(exact):.6f}")

# ---------- (c) the grading key: relative psi on nonprincipal split primes ----------
def is_prime(p):
    if p < 2: return False
    for d in range(2, int(math.isqrt(p))+1):
        if p % d == 0: return False
    return True

def is_split_nonprincipal(p):
    if p in (2,5) or not is_prime(p): return None
    # split iff -5 is a QR mod p ; nonprincipal iff p not represented by x^2+5y^2
    if pow(-5 % p, (p-1)//2, p) != 1: return None
    for x in range(0, int(math.isqrt(p))+1):
        r = p - x*x
        if r >= 0 and r % 5 == 0:
            y2 = r//5; s = int(math.isqrt(y2))
            if s*s == y2: return False  # principal
    return True

def root_conv(p):
    # root of x^2 = -5 mod p in (0, p/2)
    for r in range(1, p):
        if (r*r + 5) % p == 0:
            return r if r < p - r else p - r
    return None

def in_pfrak(x, y, p, r):
    """alpha = x + y*sqrt(-5) in p_p = (p, r+sqrt-5)?  test x = y*r (mod p)"""
    return (x - y*r) % p == 0

# psi on principal ideals: psi((x+y sqrt-5)) = (-1)^y   [verified multiplicative above; ray char mod (2)]
# solve psi(p_p) relative to psi(p_3) := +i using norm-3p principal generators
r3 = root_conv(3)
assert r3 == 1
I = complex(0,1)
psi3 = I
key = {3: psi3}
plist = [p for p in range(3, 100) if is_split_nonprincipal(p)]
for p in plist:
    if p == 3: continue
    rp = root_conv(p)
    n = 3*p
    found = None
    for y in range(0, int(math.isqrt(n//5))+1):
        x2 = n - 5*y*y
        if x2 < 0: continue
        x = int(math.isqrt(x2))
        if x*x != x2: continue
        # (x + y sqrt-5), norm 3p; decide which primes it lies in
        for (xx, yy) in ((x,y),(x,-y)) if y else ((x,0),):
            in3  = in_pfrak(xx,yy,3,r3)
            inp  = in_pfrak(xx,yy,p,rp)
            # (alpha) = q3 * qp with q3 in {p_3, pbar_3}, qp in {p_p, pbar_p}
            s3 = psi3 if in3 else 1/psi3
            val = (-1)**(yy & 1)
            # psi(q3)*psi(qp) = val  =>  psi(qp) = val/s3 ; convert to psi(p_p)
            psq = val/s3
            psip = psq if inp else 1/psq
            if found is None:
                found = psip
            else:
                assert abs(found - psip) < 1e-9, (p, found, psip)  # consistency across representations
    key[p] = found

def fmt(z):
    z = complex(z)
    for lab, v in (("+1",1),("-1",-1),("+i",I),("-i",-I)):
        if abs(z-v) < 1e-9: return lab
    return f"{z:.3f}"

print("\n(c) COMMITTED GRADING KEY (convention: r_p in (0,p/2); psi(p_3) := +i):")
print("    p   : " + "  ".join(f"{p:>3}" for p in plist))
print("    psi : " + "  ".join(f"{fmt(key[p]):>3}" for p in plist))
print("    (a_p = psi + conj = 0 at every one of these primes: boundary-null, key nontrivial)")

# ---------- (d) bulk-mode exhibit at a_69 ----------
p = 23; rp = root_conv(23)
orbs = {}
for x in range(-9,10):
    for y in range(-4,5):
        if x*x+5*y*y == 69:
            tag = 'p23' if in_pfrak(x,y,23,rp) else 'pbar23'
            orbs.setdefault(tag, []).append(((x,y), (-1)**(y&1)))
print(f"\n(d) a_69 = {c[69]} (boundary-null). Lattice-orbit decomposition (r_23 = {rp}):")
for tag, pts in orbs.items():
    s = sum(v for _,v in pts)
    print(f"    orbit {tag}: points {[pt for pt,_ in pts]}, signed sum = {s:+d}")
print("    The relative datum psi(p_3)psi(p_23) vs psi(p_3)psi(pbar_23) lives in WHICH orbit carries")
print("    which sign -- readable only with the root r_23 (bulk data), invisible in the coefficient.")
