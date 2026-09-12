#!/usr/bin/env python3
"""Seal the grade: (1) total-positivity of gamma across all 60 even orderings (constructed lift's
infinity-type: totally positive <=> rho(c)=+I <=> the chi_{-1951} twist-parity story closes);
(2) FE-certificate of the CONSTRUCTED signs (twisted to committed convention), with p=2,137
resolved by 4-way scan."""
import numpy as np, json, itertools, sys
sys.path.insert(0, '.')
from instr2 import Arm, Xof, TGRID, inv_series, primes_upto, _fold

# ---- (1) total positivity ----
import subprocess
gp = r'''
P = x^5 - x^4 - 780*x^3 - 1795*x^2 + 3106*x + 344;
ps = polsym(P, 8); G = matrix(5,5,i,j, ps[i+j-1]);
orth(GG) = {my(n = matsize(GG)[1]); if(n == 0, return(matrix(0,0))); if(n == 1, my(c = GG[1,1], s); if(!issquare(c, &s), error("nonsq")); return(Mat(1/s))); my(H = matconcat([GG, matrix(n,1); matrix(1,n), Mat(-1)])); my(v = qfsolve(H)); my(w = v[1..n], t = v[n+1]); my(v1 = w/t); my(K = matker(Mat((GG*v1)~))); my(B2 = orth(K~*GG*K)); matconcat([Mat(v1), K*B2]);}
B = orth(G);
default(realprecision, 80);
rts = real(polroots(P));
c = 0; neg = 0;
{
forperm(5, s,
  my(sv = Vec(s));
  \\ even permutations only
  my(par = 1, t = sv);
  for(i = 1, 5, for(j = i+1, 5, if(t[i] > t[j], par = -par)));
  if(par == 1,
    my(V = matrix(5,5,i,j, rts[sv[i]]^(j-1)));
    my(gm = matdet(matid(5) + V*B));
    c++;
    if(gm < 0, neg++)));
}
print(c, " even orderings, negatives: ", neg);
quit
'''
open('totpos.gp','w').write(gp)
r = subprocess.run(['gp','-q'], stdin=open('totpos.gp'), capture_output=True, text=True, timeout=300)
print("(1) gamma conjugates:", r.stdout.strip(), " => constructed lift rho(c) = +I iff negatives = 0")

# ---- (2) FE certificate of constructed signs ----
PHI = (1+np.sqrt(5))/2
MT = {0: 2.0, 1: 0.0, 2: 1.0, 3: PHI, 4: 1/PHI}   # orientation B
sig = {}
for line in open('crespo_signs.txt'):
    p, m, s = line.strip().split(':'); sig[int(p)] = (int(m), int(s))
cls = {}
for line in open('../gp/classesX_doud1951.txt'):
    p, c = line.strip().split(':'); cls[int(p)] = int(c)
jl = {}
for line in open('chilog_1951.txt'):
    p, j = line.strip().split(':'); jl[int(p)] = int(j)
def kron1951m(p):   # chi_{-1951}(p) for odd p != 1951
    r = pow((-1951) % p, (p-1)//2, p)
    return 1 if r == 1 else -1
def constr_sign(p):
    m, sq = sig[p]; lab = cls[p]
    if lab == 0: return +1 if sq == 1 else -1
    if lab == 2: return -1 if sq == 1 else +1
    if lab == 3: return -1 if sq == 1 else +1
    if lab == 4: return +1 if sq == 1 else -1
    return None
Z10 = np.exp(1j*np.pi/5)
N = 1951.0
arm = Arm(N, 1, tgrid=TGRID)   # odd port
X = arm.X
def build(b2, b137):
    a = np.zeros(X+1, dtype=complex); a[1] = 1.0
    for p in primes_upto(X):
        c = cls.get(p); j = jl.get(p)
        if c is None or j is None or p == 1951: continue
        kmax = int(np.log(X)/np.log(p))
        th = Z10**(j % 10); ch = th*th
        if c == 1:
            poly = [1.0, 0.0, ch]
        else:
            if p == 2: bn = b2
            elif p == 137: bn = b137
            elif p in sig and constr_sign(p) is not None:
                bn = constr_sign(p) * kron1951m(p) * (-1)**(j % 2)   # constructed -> nebentypus convention
            else:
                return None
            poly = [1.0, -bn*th*MT[c], ch]
        a = _fold(a, p, inv_series(np.asarray(poly, dtype=complex), kmax), X)
    return a
comm = {int(p): v for p, v in json.load(open('summit_base_oddGS.json'))['bits'].items()}
print("(2) FE certificate of CONSTRUCTED coefficients (4-way scan of the two index-denominator bits):")
for b2 in (+1, -1):
    for b137 in (+1, -1):
        a = build(b2, b137)
        arm.set_a(a)
        r, eps = arm.residual()
        mark = " <== committed values" if (b2 == comm[2] and b137 == comm[137]) else ""
        print(f"   b2={b2:+d} b137={b137:+d}: residual {r:.3e}  eps {eps.real:+.5f}{eps.imag:+.5f}i{mark}")
