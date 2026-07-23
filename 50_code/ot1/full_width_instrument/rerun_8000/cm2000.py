import sys, time, numpy as np
from fractions import Fraction
sys.path.insert(0,'/home/claude/tep-archive/50_code/ot1/full_width_instrument')
import decoder as D, decoder2 as D2
P = 1000003; NCOL = 601; DEPTH = 600
def fast_E1(chiD, depth):
    m=abs(chiD); B1=Fraction(sum(D.kron(chiD,x)*x for x in range(1,m)),m)
    c=[0]*depth
    for d_ in range(1,depth):
        cd=D.kron(chiD,d_)
        if cd:
            for n_ in range(d_,depth,d_): c[n_]+=cd
    return [-B1/2]+[Fraction(v) for v in c[1:]]
D.DEPTH=DEPTH; D.E1_series=lambda chiD: fast_E1(chiD, DEPTH)
t0=time.time()
H=np.load('/home/claude/ot1_8000/H_p1_2000.npy').astype(np.float64); Minv=np.load('/home/claude/ot1_8000/Minv_p1_2000.npy').astype(np.float64)
pd=D2.pdata_cm20(DEPTH)
F=D2.build_f2(pd,-20,0,DEPTH,{2:D.ONE,5:D.ONE})
E=D.E1_series(-20)[:DEPTH]
Emod=np.array([(int(e.numerator)%P)*pow(int(e.denominator)%P,P-2,P)%P for e in E],dtype=np.float64)
blocks={}
for m_,d in F.items():
    if m_>DEPTH: continue
    for T,v in d.items():
        for c in range(4):
            x=v[c]
            if x==0: continue
            if T not in blocks: blocks[T]=np.zeros((4,NCOL))
            xm=(int(x.numerator)%P)*pow(int(x.denominator)%P,P-2,P)%P
            L=min(len(E),NCOL-m_)
            blocks[T][c,m_:m_+L]=np.mod(blocks[T][c,m_:m_+L]+xm*Emod[:L],P)
Ts=[T for T in blocks if T!=frozenset()]; nT=len(Ts)
V=np.zeros((NCOL,4*(nT+1)))
for k,T in enumerate(Ts):
    V[:,4*k:4*k+4]=blocks[T].T
V[:,4*nT:4*nT+4]=blocks[frozenset()].T
print(f"emission {nT} monomials ({time.time()-t0:.0f}s)",flush=True)
t0=time.time()
HV=np.mod(H@V,P); MC=np.mod(Minv@HV,P); RV=np.mod(V-H.T@MC,P)
print(f"residuals via BLAS ({time.time()-t0:.0f}s)",flush=True)
t0=time.time()
A=np.zeros((4*NCOL,nT)); 
for k in range(nT): A[:,k]=RV[:,4*k:4*k+4].T.reshape(-1)
b=np.mod(-RV[:,4*nT:4*nT+4].T.reshape(-1),P)
rowmask=(A.any(axis=1))|(b!=0)
A=A[rowmask]; b=b[rowmask]
Aug=np.concatenate([A,b.reshape(-1,1)],axis=1)
rows,cols=Aug.shape; piv=[]; r=0
for c in range(cols):
    nz=np.nonzero(Aug[r:,c])[0]
    if nz.size==0: continue
    i=r+int(nz[0]); Aug[[r,i]]=Aug[[i,r]]
    Aug[r]=np.mod(Aug[r]*pow(int(Aug[r,c]),P-2,P),P)
    col=Aug[:,c].copy(); col[r]=0
    Aug=np.mod(Aug-np.outer(col,Aug[r]),P)
    piv.append(c); r+=1
    if r==rows: break
print(f"system {A.shape}, aug rank={len(piv)}, inconsistent={nT in piv} ({time.time()-t0:.0f}s)",flush=True)
R=Aug[:r]
if nT in piv: print("VERDICT: REJECT — unexpected for CM control; investigate")
else:
    free=[c for c in range(nT) if c not in piv]
    sol=np.zeros(nT)
    pivpos={c:i for i,c in enumerate(piv)}
    for c,i in pivpos.items(): sol[c]=R[i,nT]
    print(f"free = {len(free)}   (was 244 at width 2701)")
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
    nonpm=[q for q,s in split if s is None]
    print(f"ram: a2={ram.get(2)} a5={ram.get(5)} (record: -1,+1)")
    print(f"split vs genus char: {ok} match / {flip} anti / {len(nonpm)} non-pm of {len(split)}")
    print("VERDICT:", "PASS — full-width CM control" if len(free)<=1 and not nonpm and (ok==len(split) or flip==len(split)) else "PARTIAL — see counts")
