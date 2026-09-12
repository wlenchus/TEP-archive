#!/usr/bin/env python3
"""Second-summit decode, Doud-2141: 8 cells = nu-order {5,10} x port {even,odd} x orientation {A,B},
base-only S2 beam-128 per the qualified recipe. Usage: python3 summit2141.py <cellindex 0-7>"""
import numpy as np, json, sys
sys.path.insert(0, '.')
from instr2 import Arm, Xof, TGRID, inv_series, primes_upto, _fold
from qualify4 import WProblem

PHI = (1+np.sqrt(5))/2
N = 2141.0
cls = {}
for line in open('classesX_2141.txt'):
    p, c = line.strip().split(':'); cls[int(p)] = int(c)
jl = {}
for line in open('chilog_2141.txt'):
    p, j = line.strip().split(':'); jl[int(p)] = int(j)

def build(order, port, orient):
    """order in (5,10); orient 'A': m(3)=1/phi,m(4)=phi; 'B': swapped."""
    MT = {0: 2.0, 1: 0.0, 2: 1.0}
    MT[3], MT[4] = (1/PHI, PHI) if orient == 'A' else (PHI, 1/PHI)
    def theta_p(p):
        j = jl.get(p)
        if j is None: return None
        return np.exp(1j*np.pi*(j % 5)/5) if order == 5 else np.exp(1j*np.pi*j/10)
    arm = Arm(N, port)
    X = arm.X
    bitp = [p for p in sorted(cls) if p <= X and p != 2141 and cls[p] in (0, 2, 3, 4) and p in jl]
    cands = {}
    for p in bitp:
        th = theta_p(p); m = MT[cls[p]]; ch = th*th
        cands[p] = ([1.0, -th*m, ch], [1.0, th*m, ch])
    def fixed(p):
        c = cls.get(p); th = theta_p(p)
        if c is None or th is None or p == 2141: return None
        if c == 1: return [1.0, 0.0, th*th]
        return None
    return arm, bitp, cands, fixed

