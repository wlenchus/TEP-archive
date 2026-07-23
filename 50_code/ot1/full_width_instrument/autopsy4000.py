"""N=4000 autopsy: (A) fixed-kron pipeline at the form's own level -> expect the
form family (NON-REJECT, gauge points matching LMFDB); (B) reconstructed BUGGY kron
(even-exponent skip before p|D check, per the 07-04 bug log) corrupting E1 for the
even-D character -> demonstrate the false negative mechanism."""
import sys, time, itertools, numpy as np
from fractions import Fraction
sys.path.insert(0,'/home/claude/ot1_16000')
import decoder as D, decoder2 as D2
from sympy import factorint, jacobi_symbol
P=1000003; NCOL=1201; DEPTH=1200
def kron_ok(Dd,n):
    if n<=0: raise ValueError
    v=1
    for p,e in factorint(n).items():
        if p==2:
            if Dd%2==0: return 0
            s=1 if Dd%8 in (1,7) else -1
        else:
            if Dd%p==0: return 0
            s=int(jacobi_symbol(Dd,p))
        if e%2==1: v*=s
    return v
def kron_buggy(Dd,n):
    if n<=0: raise ValueError
    v=1
    for p,e in factorint(n).items():
        if e%2==0: continue          # the bug: parity skip BEFORE ramification check
        if p==2:
            if Dd%2==0: return 0
            s=1 if Dd%8 in (1,7) else -1
        else:
            if Dd%p==0: return 0
            s=int(jacobi_symbol(Dd,p))
        v*=s
    return v
def E1_with(kr, chiD, depth):
    m=abs(chiD); B1=Fraction(sum(kr(chiD,x)*x for x in range(1,m)),m)
    c=[0]*depth
    for d_ in range(1,depth):
        cd=kr(chiD,d_)
        if cd:
            for n_ in range(d_,depth,d_): c[n_]+=cd
    return [-B1/2]+[Fraction(v) for v in c[1:]]
H=np.zeros((561,NCOL))
for i,line in enumerate(open('host4000.csv')):
    for j,t in enumerate(line.rstrip('\n').split(',')[:NCOL]):
        if t!='0': H[i,j]=int(t)%P if '/' not in t else (int(t.split('/')[0])%P)*pow(int(t.split('/')[1])%P,P-2,P)%P
M=np.mod(H@H.T,P); n=M.shape[0]
Aug=np.concatenate([M,np.eye(n)],axis=1); r=0
for c in range(n):
    nz=np.nonzero(Aug[r:,c])[0]
    if nz.size==0: continue
    i=r+int(nz[0]); Aug[[r,i]]=Aug[[i,r]]
    Aug[r]=np.mod(Aug[r]*pow(int(Aug[r,c]),P-2,P),P)
    col=Aug[:,c].copy(); col[r]=0
    Aug=np.mod(Aug-np.outer(col,Aug[r]),P); r+=1
assert r==n, f"M rank {r}"
Minv=Aug[:,n:]
pd=D2.pdata_quintic(DEPTH)
def run(kr,label):
    D.DEPTH=DEPTH; D.E1_series=lambda chiD: E1_with(kr,chiD,DEPTH)
    D.kron=kr; D2.D.kron=kr
    F=D2.build_f2(pd,-4,0,DEPTH,{2:None,5:None})
    E=D.E1_series(-4)[:DEPTH]
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
    Aug2=np.concatenate([A,b.reshape(-1,1)],axis=1)
    rows,cols=Aug2.shape; piv=[]; rr=0
    tmp=np.empty_like(Aug2)
    for c in range(cols):
        nz=np.nonzero(Aug2[rr:,c])[0]
        if nz.size==0: continue
        i=rr+int(nz[0])
        if i!=rr: Aug2[[rr,i]]=Aug2[[i,rr]]
        Aug2[rr]*=pow(int(Aug2[rr,c]),P-2,P); np.mod(Aug2[rr],P,out=Aug2[rr])
        col=Aug2[:,c].copy(); col[rr]=0
        np.outer(col,Aug2[rr],out=tmp); Aug2-=tmp; np.mod(Aug2,P,out=Aug2)
        piv.append(c); rr+=1
        if rr==rows: break
    if nT in piv:
        print(f"[{label}] chi=-4: REJECT (aug rank {len(piv)}, nT {nT})"); return
    R=Aug2[:rr]; pivpos={c:i for i,c in enumerate(piv)}
    free=[c for c in range(nT) if c not in pivpos]
    sol=np.zeros(nT)
    for c,i in pivpos.items(): sol[c]=R[i,nT]
    null=[]
    for fc in free:
        v=np.zeros(nT); v[fc]=1
        for c,i in pivpos.items(): v[c]=np.mod(-R[i,fc],P)
        null.append(v)
    sing_idx={k:next(iter(Ts[k])) for k in range(nT) if len(Ts[k])==1}
    pm=lambda x:x==1 or x==P-1
    found=0
    for combo in itertools.product([1.0,float(P-1)],repeat=min(len(free),10)):
        v=sol.copy()
        for j,fc in enumerate(free[:10]):
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
        if ok: found+=1
    print(f"[{label}] chi=-4: NON-REJECT free={len(free)} gauge_pts={found} -> {'FORM FAMILY PRESENT' if found else 'no gauge point'}")
run(kron_ok, "FIXED-KRON")
run(kron_buggy, "BUGGY-KRON (reconstructed 07-04 bug)")
