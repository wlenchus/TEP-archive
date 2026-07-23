"""Bisection CM control (their cm_control pattern): construct the level-20 weight-1
CM form of Q(sqrt(-5)) from binary quadratic forms with an independently coded
E1(chi_-20); multiply; reduce the single product vector against the FULL host.
Residual 0 => host rows contain the product => host + reduction validated,
independent of the decoder assembly path."""
import sys, time, numpy as np
from fractions import Fraction
sys.path.insert(0,'/home/claude/ot1_16000')
import decoder as D, decoder2 as D2

DEPTH_FULL = 4800; NCOL = DEPTH_FULL + 1
def theta_diff(depth):
    a = [0]*(depth+1)
    B = int(depth**0.5)+2
    for x in range(-B, B+1):
        for y in range(-B, B+1):
            n = x*x + 5*y*y
            if 0 < n <= depth: a[n] += 1
    b = [0]*(depth+1)
    for x in range(-2*B, 2*B+1):
        for y in range(-2*B, 2*B+1):
            n = 2*x*x + 2*x*y + 3*y*y
            if 0 < n <= depth: b[n] += 1
    return [Fraction(a[n]-b[n], 2) for n in range(depth+1)]

def E1(chiD, depth):
    m = abs(chiD)
    B1 = Fraction(sum(D.kron(chiD,x)*x for x in range(1,m)), m)
    c = [Fraction(0)]*(depth+1); c[0] = -B1/2
    for d in range(1, depth+1):
        cd = D.kron(chiD, d)
        if cd:
            for n in range(d, depth+1, d): c[n] += cd
    return c

t0=time.time()
f = theta_diff(DEPTH_FULL); E = E1(-20, DEPTH_FULL)
print(f"f a1..a9: {[str(f[i]) for i in range(1,10)]}  E0={E[0]} ({time.time()-t0:.0f}s)")
g = [Fraction(0)]*NCOL
for m_ in range(1, NCOL):
    fm = f[m_]
    if fm:
        for n in range(0, NCOL-m_):
            if E[n]: g[m_+n] += fm*E[n]
print(f"product built ({time.time()-t0:.0f}s); g[1..8] = {[str(g[i]) for i in range(1,9)]}")
for p in (1000003, 999983):
    host = np.zeros((2321, NCOL), dtype=np.int64)
    for i, line in enumerate(open('host16000_local.csv')):
        for j, t in enumerate(line.rstrip('\n').split(',')):
            if t != '0':
                host[i,j] = (int(t)) % p if '/' not in t else (int(t.split('/')[0])%p)*pow(int(t.split('/')[1])%p, p-2, p)%p
    gv = np.array([(int(x.numerator)%p)*pow(int(x.denominator)%p, p-2, p)%p for x in g], dtype=np.int64)
    t1=time.time()
    red, rank = D2.make_reducer(host, p)
    r = red(gv)
    nz = int(np.count_nonzero(r))
    print(f"p={p}: host rank={rank}, residual nonzeros={nz} ({time.time()-t1:.0f}s)  -> {'PASS (in row space)' if nz==0 else 'FAIL'}")
print("BISECTION CONTROL DONE")
