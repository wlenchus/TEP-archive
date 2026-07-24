# Carrier rung 1 (2026-07-24): CM20 control rebuild, eta-product identity test (FALSE), branch-exponent bookkeeping
# Reproduces: CM20 a2=-1,a5=+1,a3=-2; eta(4t)eta(20t) != CM20; leading exponents 1/4 (eta1*eta5), 1/2, -1/2 (sqrt t), -1 (t)
import math
N = 400
r1 = [0]*(N+1); r2 = [0]*(N+1)
L = int(math.isqrt(N))+2
for x in range(-L, L+1):
    for y in range(-L, L+1):
        n1 = x*x + 5*y*y
        if 0 < n1 <= N: r1[n1] += 1
        n2 = 2*x*x + 2*x*y + 3*y*y
        if 0 < n2 <= N: r2[n2] += 1
cm = [(r1[n]-r2[n])//2 for n in range(N+1)]
def eta_product(scales, N):
    shift = sum(scales); assert shift % 24 == 0; shift //= 24
    poly = [0]*(N+1); poly[0] = 1
    for s in scales:
        for n in range(1, N//s + 1):
            newp = poly[:]
            for k in range(N+1 - s*n):
                if poly[k]: newp[k + s*n] -= poly[k]
            poly = newp
    out = [0]*(N+1)
    for k in range(N+1-shift): out[k+shift] = poly[k]
    return out
e420 = eta_product([4,20], N)
print("CM20:", [(n,cm[n]) for n in range(1,30) if cm[n]!=0])
print("eta(4t)eta(20t):", [(n,e420[n]) for n in range(1,60) if e420[n]!=0][:10])
print("identity:", cm == e420)  # False — recorded negative
print("branch exponents: eta*eta5: 1/4 | eta2*eta10: 1/2 | (eta/eta5)^3: -1/2 (branched at both cusps) | t: -1 (single-valued)")
