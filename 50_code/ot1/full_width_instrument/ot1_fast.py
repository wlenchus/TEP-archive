"""Full-Sturm-width membership machinery via normal equations mod p.
rowspace test: g in rowspace(H) <=> H^T c = g solvable; with M = H H^T
invertible, c = M^{-1} H g is the unique candidate; verify exactly.
Checkpoints M-factor to disk. Hypothesis: the SOLVED-NO-GAUGE degeneracy
was a reduced-width artifact; full width (4801 cols, codim ~2480) should
collapse the free dimensions the way the corpus's full-Sturm CM control did."""
import sys, time, numpy as np
from fractions import Fraction
sys.path.insert(0,'/home/claude/ot1_16000')
import decoder as D

P1 = 1000003; NCOL = 4801
t0=time.time()
H = np.zeros((2321, NCOL), dtype=np.int64)
for i, line in enumerate(open('host16000_local.csv')):
    for j, t in enumerate(line.rstrip('\n').split(',')):
        if t != '0': H[i,j] = int(t) % P1
print(f"host {H.shape} ({time.time()-t0:.0f}s)", flush=True)
t0=time.time()
M = (H @ H.T) % P1     # int64 safe: 4801 * p^2 ~ 5e15 < 2^63
print(f"M = H H^T {M.shape} ({time.time()-t0:.0f}s)", flush=True)
# eliminate [M | I] -> [I | M^-1] mod p
t0=time.time()
n = M.shape[0]
Aug = np.concatenate([M, np.eye(n, dtype=np.int64)], axis=1) % P1
r = 0
for c in range(n):
    nz = np.nonzero(Aug[r:, c])[0]
    if nz.size == 0: continue
    i = r + int(nz[0]); Aug[[r,i]] = Aug[[i,r]]
    Aug[r] = (Aug[r] * pow(int(Aug[r,c]), P1-2, P1)) % P1
    col = Aug[:, c].copy(); col[r] = 0
    Aug = (Aug - np.outer(col, Aug[r])) % P1
    r += 1
print(f"M rank = {r}/{n} ({time.time()-t0:.0f}s)", flush=True)
if r == n:
    Minv = Aug[:, n:]
    np.save('Minv_p1.npy', Minv); np.save('H_p1.npy', H)
    print("M invertible; factor checkpointed", flush=True)
    def residual(v):   # v length NCOL; returns v - H^T (Minv (H v)) mod p
        c = (Minv @ ((H @ v) % P1)) % P1
        return (v - (H.T @ c)) % P1
    # bisection membership: theta-difference CM product
    def theta_diff(depth):
        a=[0]*(depth+1); b=[0]*(depth+1); B=int(depth**0.5)+2
        for x in range(-B,B+1):
            for y in range(-B,B+1):
                q1=x*x+5*y*y
                if 0<q1<=depth: a[q1]+=1
        for x in range(-2*B,2*B+1):
            for y in range(-2*B,2*B+1):
                q2=2*x*x+2*x*y+3*y*y
                if 0<q2<=depth: b[q2]+=1
        return [Fraction(a[n_]-b[n_],2) for n_ in range(depth+1)]
    def E1(chiD, depth):
        m=abs(chiD); B1=Fraction(sum(D.kron(chiD,x)*x for x in range(1,m)),m)
        c=[Fraction(0)]*(depth+1); c[0]=-B1/2
        for d_ in range(1,depth+1):
            cd=D.kron(chiD,d_)
            if cd:
                for n_ in range(d_,depth+1,d_): c[n_]+=cd
        return c
    f = theta_diff(4800); E = E1(-20, 4800)
    g = [Fraction(0)]*NCOL
    for m_ in range(1, NCOL):
        if f[m_]:
            fm=f[m_]
            for n_ in range(0, NCOL-m_):
                if E[n_]: g[m_+n_] += fm*E[n_]
    gv = np.array([(int(x.numerator)%P1)*pow(int(x.denominator)%P1,P1-2,P1)%P1 for x in g], dtype=np.int64)
    rres = residual(gv); nz = int(np.count_nonzero(rres))
    print(f"BISECTION (full width, p={P1}): residual nonzeros = {nz} -> {'PASS: host+reduction VALIDATED' if nz==0 else 'FAIL'}", flush=True)
else:
    print("M singular mod p1 — fall back to direct rref path", flush=True)
