"""Scan (N, a2-mode, a5-mode) for FE consistency of the decoded chi_-4 system.
Also calibrated negative control: flip signs at small primes {3,7,11,13}."""
import sys, json, cmath, math
sys.path.insert(0,'/home/claude/ot1_16000')
import decoder2 as D2
from sympy import factorint
NMAX=4800
res=json.load(open('sweep_p2_results.json'))
sol=res['-4_0']['patterns'][0]
pd=D2.pdata_quintic(NMAX)
PHI=(1+math.sqrt(5))/2; IPHI=1/PHI
def kron4(p): return 0 if p%2==0 else (1 if p%4==1 else -1)
def build_an(a2=0j, a5=0j, flip=()):
    ap={}
    for q,(cls,par) in pd.items():
        if cls=='2': ap[q]=0j; continue
        s=sol.get(str(q))
        if s is None: continue
        if q in flip: s=-s
        mag={'1':2.0,'3':1.0}.get(cls) or (PHI if par==+1 else IPHI)
        ap[q]=s*mag*(1.0 if kron4(q)==1 else 1j)
    an=[0j]*(NMAX+1); an[1]=1+0j
    pk={}
    for q,a in [(2,a2),(5,a5)]+list(ap.items()):
        chi=0 if q in (2,5) else kron4(q)
        A=[1+0j,a if q in (2,5) else ap[q]]
        while q**len(A)<=NMAX:
            A.append(A[-1]*A[1]-chi*A[-2])
        pk[q]=A
    for n in range(2,NMAX+1):
        val=1+0j; ok=True
        for q,e in factorint(n).items():
            if q not in pk or e>=len(pk[q]): ok=False; break
            val*=pk[q][e]
        an[n]=val if ok else 0j
    return an
def drift(an,N):
    SQ=math.sqrt(N); out=[]
    for y in (0.8,1.0,1.3,1.7):
        t1=2*math.pi/(SQ*y); t2=2*math.pi*y/SQ
        lhs=sum(an[n]*cmath.exp(-t1*n) for n in range(1,NMAX+1))
        rhs=y*sum(an[n].conjugate()*cmath.exp(-t2*n) for n in range(1,NMAX+1))
        if abs(rhs)<1e-25: return 9e9,0
        out.append(lhs/rhs)
    e0=out[0]
    return max(abs(r-e0) for r in out), abs(e0)
Ns=[16000,8000,32000,4000,2000,64000,20000,40000,80000,128000,1000,500,400,256000,160000]
base=build_an()
print("== N-scan, a2=a5=0 ==")
best=[]
for N in Ns:
    d,m=drift(base,N); best.append((d,N)); print(f"  N={N}: drift={d:.3e} |eps|={m:.4f}")
print("== negative control (flip 3,7,11,13) at best N ==")
bN=min(best)[1]
d,m=drift(build_an(flip=(3,7,11,13)),bN); print(f"  N={bN} flipped: drift={d:.3e}")
print("== a2/a5 modes at N=16000 and 64000 ==")
modes=[0j,1+0j,-1+0j,1j,-1j,(1+1j)/math.sqrt(2)]
for N in (16000,64000,32000):
    bb=None
    for a2 in modes:
        for a5 in modes:
            d,m=drift(build_an(a2=a2,a5=a5),N)
            if bb is None or d<bb[0]: bb=(d,a2,a5,m)
    print(f"  N={N}: best drift={bb[0]:.3e} at a2={bb[1]:.3f} a5={bb[2]:.3f} |eps|={bb[3]:.4f}")
