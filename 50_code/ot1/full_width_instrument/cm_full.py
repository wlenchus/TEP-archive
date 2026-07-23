"""Full-width CM decoder control. Hypothesis: SOLVED-NO-GAUGE at reduced width was
an under-constraint artifact; at full Sturm width (4801 cols, ~9900 constraint
coords vs ~800 monomials) the system should pin everything: PASS free<=1."""
import sys, time, numpy as np
from fractions import Fraction
sys.path.insert(0,'/home/claude/ot1_16000')
import decoder as D, decoder2 as D2

P = 1000003; NCOL = 4801; DEPTH = 4800
def fast_E1(chiD, depth):
    m=abs(chiD); B1=Fraction(sum(D.kron(chiD,x)*x for x in range(1,m)),m)
    c=[0]*depth
    for d_ in range(1,depth):
        cd=D.kron(chiD,d_)
        if cd:
            for n_ in range(d_,depth,d_): c[n_]+=cd
    return [-B1/2]+[Fraction(v) for v in c[1:]]
D.DEPTH = DEPTH; D.E1_series = lambda chiD: fast_E1(chiD, DEPTH)

t0=time.time()
H = np.load('H_p1.npy'); Minv = np.load('Minv_p1.npy')
print(f"loaded checkpoints ({time.time()-t0:.0f}s)", flush=True)
t0=time.time()
pd = D2.pdata_cm20(DEPTH)
F = D2.build_f2(pd, -20, 0, DEPTH, {2: D.ONE, 5: D.ONE})
E = D.E1_series(-20)[:DEPTH]
Emod = np.array([(int(e.numerator)%P)*pow(int(e.denominator)%P,P-2,P)%P for e in E], dtype=np.int64)
blocks={}
for m_,d in F.items():
    if m_>DEPTH: continue
    for T,v in d.items():
        for c in range(4):
            x=v[c]
            if x==0: continue
            if T not in blocks: blocks[T]=np.zeros((4,NCOL),dtype=np.int64)
            xm=(int(x.numerator)%P)*pow(int(x.denominator)%P,P-2,P)%P
            L=min(len(E),NCOL-m_)
            blocks[T][c,m_:m_+L]=(blocks[T][c,m_:m_+L]+xm*Emod[:L])%P
print(f"emission built: {len(blocks)} monomials ({time.time()-t0:.0f}s)", flush=True)
t0=time.time()
Ts=[T for T in blocks if T!=frozenset()]
V=np.zeros((NCOL, 4*(len(Ts)+1)), dtype=np.int64)
for k,T in enumerate(Ts):
    for c in range(4): V[:,4*k+c]=blocks[T][c]
for c in range(4): V[:,4*len(Ts)+c]=blocks[frozenset()][c]
RV = (V - H.T @ ((Minv @ ((H @ V) % P)) % P)) % P     # residuals, batched
print(f"residuals batched ({time.time()-t0:.0f}s)", flush=True)
t0=time.time()
nT=len(Ts)
A=np.zeros((4*NCOL,nT),dtype=np.int64); b=np.zeros(4*NCOL,dtype=np.int64)
for k in range(nT):
    A[:,k]=RV[:,4*k:4*k+4].T.reshape(-1)
b=(-RV[:,4*nT:4*nT+4].T.reshape(-1))%P
keep=np.nonzero((A.sum(axis=1)+b)%P)[0]
keep=np.unique(np.concatenate([keep, np.nonzero(b)[0]]))
A=A[keep]; b=b[keep]
print(f"system {A.shape} after dropping trivially-zero rows ({time.time()-t0:.0f}s)", flush=True)
t0=time.time()
Aug=np.concatenate([A,b.reshape(-1,1)],axis=1)%P
R,piv=D2.rref_modp(Aug,P)
print(f"aug rank={len(piv)}, monomials={nT}, inconsistent={nT in piv} ({time.time()-t0:.0f}s)", flush=True)
if nT in piv:
    print("VERDICT: REJECT (inconsistent) — unexpected for the CM control; investigate")
else:
    free=[c for c in range(nT) if c not in piv]
    sol=np.zeros(nT,dtype=np.int64)
    for i,c in enumerate(piv): sol[c]=R[i,nT]
    print(f"free = {len(free)}  (was 244 at width 2701)")
    sing={next(iter(Ts[k])):int(sol[k]) for k in range(nT) if len(Ts[k])==1}
    def genus(p_):
        y=0
        while 5*y*y<=p_:
            r_=p_-5*y*y; xr=int(r_**0.5)
            for xx in (xr-1,xr,xr+1):
                if xx>=0 and xx*xx==r_: return 1
            y+=1
        return -1
    pm=lambda v:1 if v==1 else (-1 if v==P-1 else None)
    ram={q:pm(sing[q]) for q in (2,5) if q in sing}
    split=[(q,pm(sing[q])) for q in sorted(sing) if q not in (2,5)]
    ok=sum(1 for q,s in split if s==genus(q)); flip=sum(1 for q,s in split if s==-genus(q))
    bad=[(q,s) for q,s in split if s is None]
    print(f"ram signs: a2={ram.get(2)} a5={ram.get(5)} (record: -1,+1)")
    print(f"split signs vs independent genus char: {ok} match / {flip} anti / {len(bad)} non-pm of {len(split)}")
    verdict = "PASS" if (len(free)<=1 and not bad and (ok==len(split) or flip==len(split))) else "PARTIAL"
    print(f"VERDICT: {verdict} — full-width CM control")
