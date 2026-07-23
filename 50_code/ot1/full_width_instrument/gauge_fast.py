"""chi=-4 emb=0: sketched solve + EXACT unsketched verification of solution/null space,
then 2^7 gauge search. Certifies free=7 and the gauge verdict without full unsketched rref."""
import sys, time, itertools, numpy as np
from fractions import Fraction
sys.path.insert(0,'/home/claude/ot1_16000')
import decoder as D, decoder2 as D2
P=1000003; NCOL=4801; DEPTH=4800
def fast_E1(chiD,depth):
    m=abs(chiD); B1=Fraction(sum(D.kron(chiD,x)*x for x in range(1,m)),m)
    c=[0]*depth
    for d_ in range(1,depth):
        cd=D.kron(chiD,d_)
        if cd:
            for n_ in range(d_,depth,d_): c[n_]+=cd
    return [-B1/2]+[Fraction(v) for v in c[1:]]
D.DEPTH=DEPTH; D.E1_series=lambda chiD: fast_E1(chiD,DEPTH)
H=np.load('H_p1.npy').astype(np.float64); Minv=np.load('Minv_p1.npy').astype(np.float64)
pd=D2.pdata_quintic(DEPTH)
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
rng=np.random.default_rng(7)
S=rng.choice([-1.0,1.0],size=(nT+300,A.shape[0]))
Aug=np.concatenate([np.mod(S@A,P),np.mod(S@b,P).reshape(-1,1)],axis=1)
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
R=Aug[:r]; pivpos={c:i for i,c in enumerate(piv)}
free=[c for c in range(nT) if c not in pivpos]
print(f"sketched: rank={len(piv)} free={len(free)} inconsistent={nT in piv}",flush=True)
sol=np.zeros(nT)
for c,i in pivpos.items(): sol[c]=R[i,nT]
null=[]
for fc in free:
    v=np.zeros(nT); v[fc]=1
    for c,i in pivpos.items(): v[c]=np.mod(-R[i,fc],P)
    null.append(v)
# EXACT verification against the full unsketched system
res0=int(np.count_nonzero(np.mod(A@sol-b,P)))
resn=[int(np.count_nonzero(np.mod(A@v,P))) for v in null]
print(f"EXACT verify: |A sol - b| nonzeros={res0}; null residuals={resn}",flush=True)
if res0==0 and all(x==0 for x in resn):
    print("certified: true solution space = sketched (free=7 exact)")
    sing_idx={k:next(iter(Ts[k])) for k in range(nT) if len(Ts[k])==1}
    cls={q:pd[q][0] for q in pd}
    fs=[(k,sing_idx.get(k)) for k in free]
    print("free coords:",[(sing_idx.get(k), cls.get(sing_idx.get(k)) if k in sing_idx else 'COMPOSITE:'+'.'.join(map(str,sorted(Ts[k])))) for k in free])
    pm=lambda x:x==1 or x==P-1
    found=0
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
        if ok:
            found+=1
            np.save(f'gauge_solution_{found}.npy', v)
    print(f"GAUGE SEARCH: {found} all-pm multiplicative points / {2**len(free)} combos")
    print("VERDICT chi=-4 emb=0:", "PASS-CANDIDATE — decode, pre-register, second prime" if found else "REJECT-BY-GAUGE")
