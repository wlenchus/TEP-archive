"""Validate the FE tester on the KNOWN level-20 CM form (weight 1, chi_-20).
Then rerun the decoded series with a proper small-prime scramble and an N-scan."""
import sys, json, cmath, math, random
sys.path.insert(0,'/home/claude/ot1_16000')
import decoder2 as D2
from sympy import factorint
def theta_an(nmax):
    a=[0]*(nmax+1); b=[0]*(nmax+1); B=int(nmax**0.5)+2
    for x in range(-B,B+1):
        for y in range(-B,B+1):
            q1=x*x+5*y*y
            if 0<q1<=nmax: a[q1]+=1
            q2=2*x*x+2*x*y+3*y*y
            if 0<q2<=nmax: b[q2]+=1
    for x in range(-2*B,2*B+1):
        for y in range(-2*B,2*B+1):
            q2=2*x*x+2*x*y+3*y*y
            if 0<q2<=nmax and abs(x)>B: b[q2]+=1
    return [complex((a[n]-b[n])/2,0) for n in range(nmax+1)]
NMAX=4800
def FE_test(an,N,label,ys=(0.8,1.0,1.25,1.6)):
    SQ=math.sqrt(N)
    def F(y):
        t=2*math.pi*y/SQ
        return sum(an[n]*cmath.exp(-t*n) for n in range(1,len(an)))
    def G(y):
        t=2*math.pi*y/SQ
        return sum(an[n].conjugate()*cmath.exp(-t*n) for n in range(1,len(an)))
    out=[]
    for y in ys:
        lhs=F(1/y); rhs=G(y)*y
        r=lhs/rhs if abs(rhs)>1e-30 else complex('nan')
        out.append((y,r))
    e0=out[0][1]
    drift=max(abs(r-e0) for _,r in out)
    print(f"[{label}] N={N}: eps~{e0:.6f} |eps|={abs(e0):.8f} max-drift={drift:.3e}")
    return drift
an_cm=theta_an(NMAX)
print("== POSITIVE CONTROL: level-20 CM form ==")
FE_test(an_cm,20,"CM20")
FE_test(an_cm,80,"CM20-wrongN(80)")
