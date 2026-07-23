"""Functional-equation grade of the decoded chi_-4 eigensystem at N=16000.
F(y) = sum a_n exp(-2 pi n y / sqrt(N)). Fricke/FE => F(1/y) = eps * y * G(y)
with G built from conjugate coefficients and |eps| = 1, eps CONSTANT in y.
Negative control: scramble 20 signs; the relation must break violently."""
import sys, json, cmath, math, random
sys.path.insert(0,'/home/claude/ot1_16000')
import decoder2 as D2
from sympy import factorint
N=16000; SQ=math.sqrt(N); NMAX=4800
res=json.load(open('sweep_p2_results.json'))
sol=res['-4_0']['patterns'][0]
pd=D2.pdata_quintic(NMAX)
PHI=(1+math.sqrt(5))/2; IPHI=1/PHI
def kron4(p): return 0 if p%2==0 else (1 if p%4==1 else -1)
def build_ap(scramble=None):
    ap={}
    rnd=random.Random(99)
    scr=set(rnd.sample(sorted(int(q) for q in sol), 20)) if scramble else set()
    for q,(cls,par) in pd.items():
        if cls=='2': ap[q]=0.0+0j; continue
        s=sol.get(str(q))
        if s is None: continue
        if q in scr: s=-s
        mag={'1':2.0,'3':1.0}.get(cls) or (PHI if (par==+1) else IPHI)
        u=1.0 if kron4(q)==1 else 1j
        ap[q]=s*mag*u
    return ap
def build_an(ap):
    an=[0j]*(NMAX+1); an[1]=1.0+0j
    pk={}
    for q in ap:
        chi=kron4(q)
        A=[1.0+0j, ap[q]]
        while True:
            nxt=A[-1]*ap[q]-chi*A[-2]
            if q**len(A)>NMAX: break
            A.append(nxt)
        pk[q]=A
    for n in range(2,NMAX+1):
        f=factorint(n); val=1.0+0j; ok=True
        for q,e in f.items():
            if q in (2,5): ok=False; break     # supercuspidal: a_{p^k}=0, k>=1
            if q not in pk or e>=len(pk[q]): ok=False; break
            val*=pk[q][e]
        an[n]=val if ok else 0j
    return an
def F(an,y):
    t=2*math.pi*y/SQ
    return sum(an[n]*cmath.exp(-t*n) for n in range(1,NMAX+1))
def G(an,y):
    t=2*math.pi*y/SQ
    return sum(an[n].conjugate()*cmath.exp(-t*n) for n in range(1,NMAX+1))
for label,scr in (("DECODED",None),("SCRAMBLED-20 (negative control)",True)):
    an=build_an(build_ap(scr))
    print(f"--- {label} ---")
    eps=None
    for y in (0.8,1.0,1.25,1.6):
        lhs=F(an,1/y); rhs=G(an,y)*y
        r=lhs/rhs if abs(rhs)>1e-30 else float('nan')
        if eps is None: eps=r
        drift=abs(r-eps)
        print(f"  y={y}: |lhs|={abs(lhs):.6e}  ratio={r:.10f}  |ratio|={abs(r):.10f}  drift-from-eps0={drift:.3e}")
