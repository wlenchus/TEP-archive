#!/usr/bin/env python3
"""Adversarial verification: recompute the committed certification residual in mpmath 30-dps
arithmetic — exact zeta10 phases, exact golden ratio, mp.besselk kernel — no float64 anywhere.
If the 8.957e-15 float64 residual were rounding artifact, it evaporates here."""
import mpmath as mp, json
mp.mp.dps = 30

cls = {}
for line in open('../gp/classesX_doud1951.txt'):
    p, c = line.strip().split(':'); cls[int(p)] = int(c)
jl = {}
for line in open('chilog_1951.txt'):
    p, j = line.strip().split(':'); jl[int(p)] = int(j)
sol = {int(p): v for p, v in json.load(open('summit_base_oddGS.json'))['bits'].items()}

PHI = (1 + mp.sqrt(5)) / 2
def z10(j): return mp.e ** (1j * mp.pi * j / 5)
MT = {0: mp.mpf(2), 1: mp.mpf(0), 2: mp.mpf(1), 3: PHI, 4: 1/PHI}   # orientation B
N = mp.mpf(1951); X = 517

# a_n by exact Euler expansion
def primes(X):
    s = list(range(X+1)); out = []
    for i in range(2, X+1):
        if s[i]:
            out.append(i)
            for k in range(i*i, X+1, i): s[k] = 0
    return out
a = {1: mp.mpc(1)}
for n in range(2, X+1): a[n] = mp.mpc(0)
for p in primes(X):
    if p == 1951 or p not in cls or p not in jl: continue
    j = jl[p]; ch = z10(j)**2
    ap = mp.mpc(0) if cls[p] == 1 else sol[p] * z10(j) * MT[cls[p]]
    # inverse of 1 - ap T + ch T^2: c_k
    kmax = 0; pk = p
    while pk <= X: kmax += 1; pk *= p
    inv = [mp.mpc(1), ap]
    for k in range(2, kmax+1): inv.append(ap*inv[k-1] - ch*inv[k-2])
    b = dict(a)
    for k in range(1, kmax+1):
        pk = p**k
        for m in range(1, X//pk + 1):
            b[m*pk] = b[m*pk] + inv[k]*a[m]
    a = b

def ker(y):   # odd port: 4 y K0(2y)
    return 4*y*mp.besselk(0, 2*y) if y < 21 else mp.mpf(0)
def F(t):
    s = mp.mpc(0)
    for n in range(1, X+1):
        if a[n] != 0:
            s += a[n]*ker(mp.pi*n*t/mp.sqrt(N))
    return s

TG = [mp.mpf(v) for v in ['0.50','0.58','0.67','0.78','0.90','1.00','1.11','1.28','1.72','2.00']] + [1/mp.mpf('0.58'), 1/mp.mpf('0.67'), 1/mp.mpf('0.78'), 1/mp.mpf('0.90')]
Ft  = [F(t) for t in TG]
Fit = [F(1/t) for t in TG]
num = sum(Fit[i]*TG[i]*Ft[i] for i in range(len(TG)))
eps = num/abs(num)
res = max(abs(Fit[i] - eps*TG[i]*mp.conj(Ft[i])) for i in range(len(TG))) / max(abs(f) for f in Ft)
print(f"mpmath 30-dps recomputation of the committed certification:")
print(f"  residual = {mp.nstr(res, 6)}")
print(f"  eps      = {mp.nstr(eps.real, 9)} {'+' if eps.imag>=0 else '-'} {mp.nstr(abs(eps.imag), 9)}i")
print(f"  (float64 pipeline gave 8.957e-15 and eps = +0.885096-0.465408i)")
