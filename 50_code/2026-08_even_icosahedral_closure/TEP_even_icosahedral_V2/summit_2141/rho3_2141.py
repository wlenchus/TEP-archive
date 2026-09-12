#!/usr/bin/env python3
"""rho3 re-certification for Doud-2141 under the exact poc3 protocol (deg-3 kernel, X=16*sqrt(N),
t-grid [0.8,1.25], 2x2 gauge scan, conductor scan, negative battery)."""
import numpy as np, mpmath as mp, json
mp.mp.dps = 22
from scipy.interpolate import CubicSpline
lg, vals = np.load("../gp/kernel_grid.npy")
SP = CubicSpline(lg, vals)
lo, hi = float(np.exp(lg[0])), float(np.exp(lg[-1]))
def phi3(y):
    y = np.asarray(y, dtype=float); out = np.zeros_like(y)
    m = y < hi; yy = np.clip(y[m], lo, hi); out[m] = SP(np.log(yy)); return out
PI32 = float(mp.pi)**1.5
G1 = (np.sqrt(5)-1)/2; G2 = (np.sqrt(5)+1)/2
def sieve(X, locfac):
    a = np.zeros(X+1); a[1] = 1.0
    isc = np.ones(X+1, dtype=bool); isc[:2] = False
    for i in range(2, int(X**0.5)+1):
        if isc[i]: isc[i*i::i] = False
    for p in np.nonzero(isc)[0]:
        p = int(p); kmax = int(np.log(X)/np.log(p))
        poly = locfac(p)
        inv = np.zeros(kmax+1); inv[0] = 1.0
        for k in range(1, kmax+1):
            s = 0.0
            for j in range(1, min(k, len(poly)-1)+1): s += poly[j]*inv[k-j]
            inv[k] = -s
        b = a.copy()
        for k in range(1, kmax+1):
            if inv[k] == 0.0: continue
            pk = p**k
            if pk > X: break
            b[pk::pk] += inv[k]*a[1:(X//pk)+1]
        a = b
    return a
def theta(a, X, N, tgrid, eps=1.0):
    n = np.arange(1, X+1)
    Ft  = np.array([float(np.dot(a[1:], phi3(n*(PI32*t/np.sqrt(N))))) for t in tgrid])
    Fit = np.array([float(np.dot(a[1:], phi3(n*(PI32/t/np.sqrt(N))))) for t in tgrid])
    return float(np.max(np.abs(Fit - eps*np.array(tgrid)*Ft))/np.max(np.abs(Ft)))
TG = np.array([0.80, 0.87, 0.93, 1.00, 1.07, 1.15, 1.25])
cls = {}
for line in open('classesX_2141.txt'):
    p, c = line.strip().split(':'); cls[int(p)] = int(c)
def loc(ram, swap):
    def f(p):
        if p in ram: return ram[p]
        c = cls.get(p)
        if c is None or c < 0: return np.array([1.0])
        if swap and c in (3, 4): c = 7 - c
        return {0: np.array([1.,-3.,3.,-1.]), 1: np.array([1.,1.,-1.,-1.]),
                2: np.array([1.,0.,0.,-1.]),
                3: np.convolve([1.,-1.],[1.,-G1,1.]), 4: np.convolve([1.,-1.],[1.,G2,1.])}[c]
    return f
N = 2141.0**2; X = int(16*np.sqrt(N))
best = None
for s in (1.0, -1.0):
    for swap in (False, True):
        a = sieve(X, loc({2141: np.array([1.0, -s])}, swap))
        rp = theta(a, X, N, TG, 1.0); rm = theta(a, X, N, TG, -1.0)
        r, ep = (rp, 1) if rp <= rm else (rm, -1)
        print(f"  ram-sign {s:+.0f} swap {int(swap)}: residual {r:.3e} (eps {ep})")
        if best is None or r < best[0]: best = (r, s, swap, ep, a)
r, s, swap, ep, a = best
print(f"BEST: ram-sign {s:+.0f} faceswap {int(swap)} eps {ep}  residual {r:.3e}")
print("conductor scan:")
for mult in (0.9, 0.95, 1.0, 1.05, 1.1):
    print(f"  N*{mult}: {theta(a, X, N*mult, TG, ep):.3e}")
rng = np.random.default_rng(2141)
clss = dict(cls)
ks = [p for p in clss if p <= X and clss[p] in (3, 4)]
for p in rng.choice(ks, size=len(ks)//3, replace=False):
    clss[int(p)] = 7 - clss[int(p)]
cls2 = cls; cls = clss
afs = sieve(X, loc({2141: np.array([1.0, -s])}, swap))
cls = cls2
print(f"NEG face-scramble 30%: {theta(afs, X, N, TG, ep):.3e}")
json.dump({'residual': r, 'ram_sign': s, 'faceswap': bool(swap), 'eps': ep}, open('rho3_2141_recert.json', 'w'))
