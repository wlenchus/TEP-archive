#!/usr/bin/env python3
"""Deep twisted-FE certification using the EXTENDED construction data (~5e4 coefficients),
at conductor N*d^2 ~ 2e7. Also scans the ramified eigenvalue u in mu_10, which now carries
real weight because 1951 (resp. 2141) sits well inside the truncation range."""
import csv, numpy as np, sys
sys.path.insert(0, '.')
from instr2 import Arm, TGRID, inv_series, primes_upto, _fold

def load(csvfile):
    ap, ch = {}, {}
    for r in csv.DictReader(open(csvfile)):
        p = int(r['p'])
        ap[p] = complex(float(r['Re_a_p']), float(r['Im_a_p']))
        ch[p] = complex(float(r['Re_chi']), float(r['Im_chi']))
    return ap, ch

def kron(D, p):
    if D % p == 0: return 0
    if p == 2:                       # Kronecker symbol at 2: mod-8 rule (Euler's criterion is INVALID here)
        return {1:1, 7:1, 3:-1, 5:-1}.get(D % 8, 0)
    return 1 if pow(D % p, (p-1)//2, p) == 1 else -1

def deep(field, csvfile, d, base_port=1):
    ap, ch = load(csvfile)
    N = field * d * d
    X = int(np.ceil(11.71*np.sqrt(N)))
    port = base_port if d > 0 else 1 - base_port
    a = np.zeros(X+1, dtype=complex); a[1] = 1.0
    miss = 0
    for p in primes_upto(X):
        if p == field: continue
        kd = kron(d, p)
        if kd == 0: continue                       # p | d : twisted local factor = 1
        if p not in ap:
            miss += 1; continue
        kmax = int(np.log(X)/np.log(p))
        a = _fold(a, p, inv_series(np.asarray([1.0, -ap[p]*kd, ch[p]], dtype=complex), kmax), X)
    arm = Arm(float(N), port, X=X, tgrid=TGRID)
    Z10 = np.exp(1j*np.pi/5)
    kdN = kron(d, field)
    kmaxN = int(np.log(X)/np.log(field))
    print(f"\nDoud-{field} twist d={d:+d}: N={N} X={X} port={'odd' if port==1 else 'even'} "
          f"({len(primes_upto(X))} primes, {miss} missing from table)")
    best = None; scores = []
    for k in range(10):
        u = Z10**k
        au = _fold(a, field, inv_series(np.asarray([1.0, -u*kdN], dtype=complex), kmaxN), X)
        arm.set_a(au)
        r, eps = arm.residual()
        scores.append(r)
        if best is None or r < best[0]: best = (r, k, eps)
    r, k, eps = best
    ranked = sorted(scores)
    print("   u-scan (residual by zeta10^k): " + " ".join(f"{s:.2e}" for s in scores))
    print(f"   BEST u = zeta10^{k}: residual {r:.3e}  eps {eps.real:+.6f}{eps.imag:+.6f}i   "
          f"separation vs runner-up: {ranked[1]/ranked[0]:.1f}x")
    return k, r

for d in (5, 13, 41, 101):
    deep(1951, 'hecke_eigenvalues_doud1951_to1e5.csv', d)
for d in (5, 13, 101):
    deep(2141, 'hecke_eigenvalues_doud2141_to1e5.csv', d)
