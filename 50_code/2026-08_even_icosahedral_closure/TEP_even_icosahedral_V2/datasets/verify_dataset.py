#!/usr/bin/env python3
"""Dataset self-check: rebuild the L-series from the CSV a_p column ALONE (no bit tables, no class
dictionary) and re-certify against the pre-registered FE. Catches any emitter/orientation error."""
import csv, numpy as np, sys
sys.path.insert(0, '.')
from instr2 import Arm, Xof, TGRID, inv_series, primes_upto, _fold

def check(csvfile, N, label):
    ap = {}; ch = {}
    for r in csv.DictReader(open(csvfile)):
        p = int(r['p'])
        ap[p] = complex(float(r['Re_a_p']), float(r['Im_a_p']))
        ch[p] = complex(float(r['Re_chi']), float(r['Im_chi']))
    X = Xof(N)
    arm = Arm(float(N), 1, tgrid=TGRID)   # odd port (both fields)
    a = np.zeros(X+1, dtype=complex); a[1] = 1.0
    for p in primes_upto(X):
        if p not in ap:
            continue
        kmax = int(np.log(X)/np.log(p))
        a = _fold(a, p, inv_series(np.asarray([1.0, -ap[p], ch[p]], dtype=complex), kmax), X)
    arm.set_a(a)
    r, eps = arm.residual()
    x, eta, g = arm.meter(eps)
    print(f"{label}: FE residual from CSV alone = {r:.3e}   eps = {eps.real:+.6f}{eps.imag:+.6f}i   "
          f"max|G_new-2| = {np.max(np.abs(g-2)):.2e}")

check('hecke_eigenvalues_doud1951.csv', 1951, 'Doud-1951')
check('hecke_eigenvalues_doud2141.csv', 2141, 'Doud-2141')
