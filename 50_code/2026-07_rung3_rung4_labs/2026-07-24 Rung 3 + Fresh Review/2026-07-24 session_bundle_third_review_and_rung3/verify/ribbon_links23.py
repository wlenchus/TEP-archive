"""Independent replication of AGM-ribbon links 2-3: j± -> lambda -> tau (AGM), round-trip,
plus the 5-adic depth datum v_sqrt5(j) = 3.  Fresh implementation (mpmath only)."""
from mpmath import mp, mpf, mpc, sqrt, ellipk, ellipfun, jtheta, exp, pi, polyroots, mpmathify, fabs, im, re

mp.dps = 60

s5 = sqrt(mpf(5))
jp = 10400 - 4640*s5   # j(+) branch  (record: j± = 10400 ∓ 4640*sqrt5)
jm = 10400 + 4640*s5   # j(-) branch

# lambda from j:  j = 256 (1 - L + L^2)^3 / (L^2 (1-L)^2)
def lambdas_from_j(j):
    # solve 256(1-L+L^2)^3 - j L^2 (1-L)^2 = 0  (degree 6)
    cs = [0]*7
    # expand 256(1 - L + L^2)^3
    import itertools
    # (1 - L + L^2)^3 coefficients: use polynomial mult
    p = [1, -1, 1]  # 1 - L + L^2 (ascending)
    def pmul(a, b):
        r = [0]*(len(a)+len(b)-1)
        for i, x in enumerate(a):
            for k, y in enumerate(b):
                r[i+k] += x*y
        return r
    c3 = pmul(pmul(p, p), p)
    A = [256*x for x in c3] + [0]*0   # degree 6 ascending
    # j * L^2 (1-L)^2 = j * (L^2 - 2L^3 + L^4)
    B = [0, 0, 1, -2, 1]
    poly = [0]*7
    for i, x in enumerate(A): poly[i] += x
    for i, x in enumerate(B):
        poly[i] -= j*x
    # descending for polyroots
    return polyroots(list(reversed(poly)), maxsteps=200, extraprec=120)

def tau_from_lambda(L):
    # tau = i K(1-L) / K(L)   (K = complete elliptic integral with parameter m = lambda)
    return 1j*ellipk(1-L)/ellipk(L)

def j_from_tau(tau):
    q = exp(1j*pi*tau)   # nome for theta functions (half period ratio convention)
    t2 = jtheta(2, 0, q); t3 = jtheta(3, 0, q)
    L = (t2/t3)**4
    return 256*(1 - L + L**2)**3/(L**2*(1-L)**2)

for name, j in (("j(+) = 10400-4640*sqrt5", jp), ("j(-) = 10400+4640*sqrt5", jm)):
    print(f"--- {name}  ({complex(j).real:.6f}) ---")
    best = None
    for L in lambdas_from_j(j):
        try:
            t = tau_from_lambda(L)
            if im(t) <= 0: continue
            jj = j_from_tau(t)
            err = fabs(jj - j)
            if best is None or err < best[2]:
                best = (L, t, err)
        except Exception:
            continue
    L, t, err = best
    print(f"  lambda = {complex(L)}")
    print(f"  tau    = {complex(t)}")
    print(f"  |tau|  = {fabs(t)}")
    print(f"  round-trip |j(tau)-j| = {float(err):.3e}")

# 5-adic depth datum: v_sqrt5( j ) in Z[phi]:  N(j) = 2^12*5^3, tr(j)=20800
# j± are conjugates; v_5(N(j)) = 3 (odd) => the prime sqrt5 divides j to exact order 3
Nj = (10400**2 - 5*4640**2)
v5 = 0
n = Nj
while n % 5 == 0: n //= 5; v5 += 1
v2 = 0
while n % 2 == 0: n //= 2; v2 += 1
print(f"\nN(j) = {Nj} = 2^{v2} * 5^{v5} * {n}   -> v_sqrt5(j) = {v5} (the a_5 = 3 datum), 2-part 2^{v2} (not 2^5)")
