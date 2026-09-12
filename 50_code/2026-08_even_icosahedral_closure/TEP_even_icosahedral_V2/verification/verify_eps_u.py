#!/usr/bin/env python3
"""Verification avenue 1: the Atkin-Li epsilon/u cross-lock.
For a newform of prime level p with ramified nebentypus chi, the FE sign satisfies
eps = c * tau(chi^s) * u^t / sqrt(p) for a port-dependent constant c and convention signs s,t.
The decode NEVER used this identity. Solving for u from the measured eps must land EXACTLY on
a 10th root of unity if bits+eps+dictionary are right -- measure-zero under error.
Calibration: the same pipeline on Ind psi_2089 (prime level, even port, eps=+1, a_D=+1, tau(chi_D)=+sqrt(D))."""
import mpmath as mp
mp.mp.dps = 40

# exact Gauss sum tau(chi^k) for canonical quintic chi mod 1951 (chi(3)=zeta5)
jl = {}
for line in open('chilog_1951.txt'):
    p, j = line.strip().split(':'); jl[int(p)] = int(j)
# need j(a) for ALL a mod 1951, not just primes: rebuild discrete log via generator 3
P = 1951
dlog = {}
x = 1
for k in range(P-1):
    dlog[x] = k % 5
    x = (x*3) % P
Z5 = mp.e ** (2j*mp.pi/5)
# sanity vs prime table
ok = all(dlog[p % P] == jl[p] for p in jl if p != P and p < P)
print("dlog table vs chilog primes:", "MATCH" if ok else "MISMATCH")

def tau(k):
    return sum((Z5**((k*dlog[a]) % 5)) * mp.e**(2j*mp.pi*a/P) for a in range(1, P))

t1 = tau(1); t4 = tau(4)
print(f"|tau(chi)|/sqrt(1951) = {mp.nstr(abs(t1)/mp.sqrt(P), 12)}  (must be 1)")
eps = mp.mpc('0.885096399', '-0.46540774')   # measured (mpmath 30-dps recompute)
eps = eps/abs(eps)

Z10 = mp.e ** (1j*mp.pi/5)
best = []
for s, tk in (('chi', t1), ('chibar', t4)):
    for t_exp in (1, -1):
        for ci, c in (('+1', 1), ('-1', -1), ('+i', 1j), ('-i', -1j)):
            # eps = c * tau * u^t / sqrt(p)  =>  u^t = eps*sqrt(p)/(c*tau)
            rhs = eps * mp.sqrt(P) / (c * tk)
            u = rhs if t_exp == 1 else 1/rhs
            # distance to nearest mu10 element
            dists = [(abs(u - Z10**k), k) for k in range(10)]
            d, k = min(dists)
            best.append((float(d), s, t_exp, ci, k))
best.sort()
print("hypothesis scan: eps = c * tau(x) * u^t / sqrt(p); distance of solved u to nearest zeta10^k:")
for d, s, t_exp, ci, k in best[:5]:
    print(f"  tau({s}), t={t_exp:+d}, c={ci}:  u -> zeta10^{k}  distance {d:.3e}")
print(f"  (worst of all 16: {best[-1][0]:.3e}; a uniform-random phase sits ~0.31 from mu10 on average)")
