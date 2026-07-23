"""Icosahedral decoder v1 — PRIMITIVES SUBSET.
Transcribed 2026-07-21 from Drive 'Untitled document.txt' (= decoder.py per the
corpus catalog; kron FIXED version), markdown escapes removed. The v1 __main__
runner and 2000-host logic are omitted; decoder2.py imports only the pieces
below (qmul/qadd/qscale, constants, kron, cycle_type, parity5, E1_series).
"""
import numpy as np
from fractions import Fraction
from sympy import primerange, jacobi_symbol, factorint, Poly, symbols

X = symbols('x'); NCOL = 601; DEPTH = 600

# ---------------- Q(sqrt5,i) as 4-vectors over Q: e0=1, e1=r5, e2=i, e3=i*r5
def qmul(a, b):
    a0,a1,a2,a3 = a; b0,b1,b2,b3 = b
    return (a0*b0 + 5*a1*b1 - a2*b2 - 5*a3*b3,
            a0*b1 + a1*b0 - a2*b3 - a3*b2,
            a0*b2 + a2*b0 + 5*(a1*b3 + a3*b1),
            a0*b3 + a3*b0 + a1*b2 + a2*b1)
def qadd(a,b): return tuple(x+y for x,y in zip(a,b))
def qscale(c,a): return tuple(c*x for x in a)
Z4=(Fraction(0),)*4; ONE=(Fraction(1),Fraction(0),Fraction(0),Fraction(0))
PHI=(Fraction(1,2),Fraction(1,2),Fraction(0),Fraction(0))
IPHI=(Fraction(-1,2),Fraction(1,2),Fraction(0),Fraction(0))
IU=(Fraction(0),Fraction(0),Fraction(1),Fraction(0))

# ---------------- kronecker (FIXED: ramification checked before parity skip)
def kron(D, n):
    if n <= 0: raise ValueError
    v = 1
    for p, e in factorint(n).items():
        if p == 2:
            if D % 2 == 0: return 0
            s = 1 if D % 8 in (1,7) else -1
        else:
            if D % p == 0: return 0
            s = int(jacobi_symbol(D, p))
        if e % 2 == 1: v *= s
    return v

# ---------------- projective data for x^5 + 20x + 16
def cycle_type(p):
    f = Poly(X**5 + 20*X + 16, X, modulus=p)
    return tuple(sorted((g.degree() for g,_ in f.factor_list()[1]), reverse=True))

DSQ = 32000  # sqrt(disc), disc = 32000^2

def parity5(p):
    def mulmod(a,b):
        r=[0]*9
        for i,ai in enumerate(a):
            if ai:
                for j,bj in enumerate(b): r[i+j]=(r[i+j]+ai*bj)%p
        for i in range(8,4,-1):
            c=r[i]
            if c: r[i]=0; r[i-4]=(r[i-4]-20*c)%p; r[i-5]=(r[i-5]-16*c)%p
        return r[:5]
    def powp(a):
        e,base,out=p,a[:],[1,0,0,0,0]
        while e:
            if e&1: out=mulmod(out,base)
            base=mulmod(base,base); e>>=1
        return out
    orbit=[[0,1,0,0,0]]
    for _ in range(4): orbit.append(powp(orbit[-1]))
    V=[1,0,0,0,0]
    for i in range(5):
        for j in range(i+1,5):
            d=[(orbit[j][k]-orbit[i][k])%p for k in range(5)]
            V=mulmod(V,d)
    assert all(c==0 for c in V[1:])
    v=V[0]%p; s=DSQ%p
    if v==s: return +1
    if v==(-s)%p: return -1
    raise RuntimeError(p)

# ---------------- E1(chi) q-expansion, length DEPTH (module global)
def E1_series(chiD):
    m=abs(chiD)
    B1=Fraction(sum(kron(chiD,a)*a for a in range(1,m)), m)
    E=[ -B1/2 ] + [ Fraction(sum(kron(chiD,d) for d in range(1,n+1) if n%d==0)) for n in range(1,DEPTH) ]
    return E
