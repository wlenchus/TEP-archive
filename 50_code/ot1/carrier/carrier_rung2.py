# Carrier rung 2 (2026-07-24): eta(4t)eta(20t) = weight-1 CM form of Q(sqrt-5) with ORDER-4 ray-class character
# (psi^2 = genus character; values ±i on the nonprincipal class). Verified: 12/12 square-recursions, 66/66 multiplicativity.
# Also: reach-lemma arithmetic (uniform 2^a-rescaled {1,5}-tower reaches exactly {1,chi5,chi-4,chi-20}; chi8-family unreachable).
import math
N = 2000
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
F = eta_product([4,20], N)
def chi20(p):
    return (1 if p%4==1 else -1)*(1 if p%5 in (1,4) else -1)
primes = [p for p in range(3,44) if all(p%d for d in range(2,p)) and p not in (2,5)]
sq = [(p, F[p], F[p*p], F[p]*F[p]-chi20(p)) for p in primes if p*p<=N]
mult = sum(F[p*q]==F[p]*F[q] for i,p in enumerate(primes) for q in primes[i+1:] if p*q<=N)
princ = lambda p: any(x*x+5*y*y==p for x in range(int(math.isqrt(p))+2) for y in range(int(math.isqrt(p))+2))
print("square-recursions:", all(a[2]==a[3] for a in sq), len(sq)); print("multiplicativity:", mult)
print("class table:", [(p, F[p], "principal" if princ(p) else ("split-nonprinc" if chi20(p)==1 else "inert")) for p in primes])
