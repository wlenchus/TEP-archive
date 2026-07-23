import sys, time, json, os, numpy as np
from fractions import Fraction
sys.path.insert(0,'/home/claude/tep-archive/50_code/ot1/full_width_instrument')
import decoder as D, decoder2 as D2
P=1000003; NCOL=601; DEPTH=600
def fast_E1(chiD,depth):
    m=abs(chiD); B1=Fraction(sum(D.kron(chiD,x)*x for x in range(1,m)),m)
    c=[0]*depth
    for d_ in range(1,depth):
        cd=D.kron(chiD,d_)
        if cd:
            for n_ in range(d_,depth,d_): c[n_]+=cd
    return [-B1/2]+[Fraction(v) for v in c[1:]]
D.DEPTH=DEPTH; D.E1_series=lambda chiD: fast_E1(chiD,DEPTH)
RES='sweep2000_results_p1.json'
res=json.load(open(RES)) if os.path.exists(RES) else {}
H=np.load('/home/claude/ot1_8000/H_p1_2000.npy').astype(np.float64); Minv=np.load('/home/claude/ot1_8000/Minv_p1_2000.npy').astype(np.float64)
t0=time.time(); pd=D2.pdata_quintic(DEPTH)
from collections import Counter
print(f"pdata census {Counter(c for c,_ in pd.values())} ({time.time()-t0:.0f}s)",flush=True)
rng=np.random.default_rng(20260723)
for chiD in (-4,-8,-20,-40):
    for emb in (0,1):
        key=f"{chiD}_{emb}"
        if key in res: continue
        t0=time.time()
        F=D2.build_f2(pd,chiD,emb,DEPTH,{2:None,5:None})
        E=D.E1_series(chiD)[:DEPTH]
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
        for k,T in enumerate(Ts): V[:,4*k:4*k+4]=blocks[T].T
        V[:,4*nT:4*nT+4]=blocks[frozenset()].T
        RV=np.mod(V-H.T@np.mod(Minv@np.mod(H@V,P),P),P)
        A=np.zeros((4*NCOL,nT))
        for k in range(nT): A[:,k]=RV[:,4*k:4*k+4].T.reshape(-1)
        b=np.mod(-RV[:,4*nT:4*nT+4].T.reshape(-1),P)
        rowmask=(A.any(axis=1))|(b!=0); A=A[rowmask]; b=b[rowmask]
        # rank-preserving row sketch to ~nT+256 rows (±1 entries, exact in f64)
        S=rng.choice([-1.0,1.0],size=(nT+256,A.shape[0]))
        As=np.mod(S@A,P); bs=np.mod(S@b,P)
        Aug=np.concatenate([As,bs.reshape(-1,1)],axis=1)
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
        status='REJECT' if nT in piv else f'SOLVED(free={nT-(len(piv)-(1 if nT in piv else 0))})'
        if nT not in piv:
            free=nT-len([c for c in piv if c<nT]); status=f'NON-REJECT(free={free})'
        res[key]=dict(status=status,nT=nT,rank=len(piv),rows_kept=int(rowmask.sum()),secs=round(time.time()-t0))
        json.dump(res,open(RES,'w'),indent=1)
        print(f"chi={chiD:+d} emb={emb}: {status} nT={nT} rank={len(piv)} ({time.time()-t0:.0f}s)",flush=True)
print("SWEEP STATE:",json.dumps(res))
