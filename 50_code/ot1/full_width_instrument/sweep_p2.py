import sys, time, json, os, itertools, numpy as np
from fractions import Fraction
sys.path.insert(0,'/home/claude/ot1_16000')
import decoder as D, decoder2 as D2
P=999983; NCOL=4801; DEPTH=4800
def fast_E1(chiD,depth):
    m=abs(chiD); B1=Fraction(sum(D.kron(chiD,x)*x for x in range(1,m)),m)
    c=[0]*depth
    for d_ in range(1,depth):
        cd=D.kron(chiD,d_)
        if cd:
            for n_ in range(d_,depth,d_): c[n_]+=cd
    return [-B1/2]+[Fraction(v) for v in c[1:]]
D.DEPTH=DEPTH; D.E1_series=lambda chiD: fast_E1(chiD,DEPTH)
H=np.load('H_p2.npy'); Minv=np.load('Minv_p2.npy')
RES='sweep_p2_results.json'; res=json.load(open(RES)) if os.path.exists(RES) else {}
pd=D2.pdata_quintic(DEPTH)
rng=np.random.default_rng(2)
def run_config(chiD,emb):
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
    S=rng.choice([-1.0,1.0],size=(nT+300,A.shape[0]))
    Aug=np.concatenate([np.mod(S@A,P),np.mod(S@b,P).reshape(-1,1)],axis=1)
    rows,cols=Aug.shape; piv=[]; r=0
    tmp=np.empty_like(Aug)
    for c in range(cols):
        nz=np.nonzero(Aug[r:,c])[0]
        if nz.size==0: continue
        i=r+int(nz[0])
        if i!=r: Aug[[r,i]]=Aug[[i,r]]
        Aug[r]*=pow(int(Aug[r,c]),P-2,P); np.mod(Aug[r],P,out=Aug[r])
        col=Aug[:,c].copy(); col[r]=0
        np.outer(col,Aug[r],out=tmp); Aug-=tmp; np.mod(Aug,P,out=Aug)
        piv.append(c); r+=1
        if r==rows: break
    if nT in piv: return dict(status='REJECT',nT=nT,rank=len(piv))
    R=Aug[:r]; pivpos={c:i for i,c in enumerate(piv)}
    free=[c for c in range(nT) if c not in pivpos]
    sol=np.zeros(nT)
    for c,i in pivpos.items(): sol[c]=R[i,nT]
    null=[]
    for fc in free:
        v=np.zeros(nT); v[fc]=1
        for c,i in pivpos.items(): v[c]=np.mod(-R[i,fc],P)
        null.append(v)
    res0=int(np.count_nonzero(np.mod(A@sol-b,P)))
    resn=[int(np.count_nonzero(np.mod(A@v,P))) for v in null]
    if res0 or any(resn): return dict(status=f'SKETCH-MISMATCH res0={res0}',nT=nT)
    sing_idx={k:next(iter(Ts[k])) for k in range(nT) if len(Ts[k])==1}
    pm=lambda x:x==1 or x==P-1
    pats=[]
    for combo in itertools.product([1.0,float(P-1)],repeat=len(free)):
        v=sol.copy()
        for j,fc in enumerate(free):
            delta=(combo[j]-v[fc])%P
            v=np.mod(v+delta*null[j],P)
        s={sing_idx[k]:int(v[k]) for k in sing_idx}
        if not all(pm(x) for x in s.values()): continue
        ok=True
        for k in range(nT):
            if len(Ts[k])>1:
                pr=1
                for q in Ts[k]: pr=(pr*s[q])%P
                if int(v[k])!=pr: ok=False; break
        if ok: pats.append({str(q):(1 if s[q]==1 else -1) for q in sorted(s)})
    return dict(status=f'NON-REJECT free={len(free)} gauge_pts={len(pats)}',nT=nT,rank=len(piv),patterns=pats)
for chiD,emb in [(-20,0),(-20,1)]:
    key=f"{chiD}_{emb}"
    if key in res: continue
    t0=time.time(); out=run_config(chiD,emb); out['secs']=round(time.time()-t0)
    res[key]=out; json.dump(res,open(RES,'w'))
    print(key, out['status'], f"({out['secs']}s)",flush=True)
