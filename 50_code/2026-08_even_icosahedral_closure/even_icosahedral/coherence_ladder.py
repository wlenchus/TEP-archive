"""THE COHERENCE LADDER — Will's budget dictionary applied to the one-power criterion.
2026-08-13 (session B).  u := y,  G := 1/sqrt(u) = y^{-1/2}.

Calculus check (exact):  G = (1-x^2)^{-1/2}, dG/dx = x G^3 = d^2(theta)/dx^2  with
theta = arcsin x, d theta/dx = G.   So  y^{-3/2} = G^3 = (1/x) dG/dx.

Claim (the ladder): with terms t_n = n c_n K0(2 pi n y), S1 = sum |t_n|, S2 = (sum |t_n|^2)^{1/2},
Sigma = sum t_n, and m := |Sigma|/S1 the coherence meter:
   trivial (Cauchy-Schwarz, no cancellation):  m <= 1        <=> |Phi| << G^3
   random phases (incoherent):                 m ~ S2/S1 ~ 1/G  <=> |Phi| << G^2
   ARTIN criterion:                            m << 1/G^2 = u   <=> |Phi| << G
Measured below on the committed tables: the true m, the random-model prediction S2/S1,
and the criterion threshold u -- to see which tier the object actually occupies."""
import numpy as np, csv
from scipy.special import k0
CSV = {1951:"/root/.claude/projects/-home-claude/e1c6a220-faa1-5bd1-9d10-c0c3344b96cd/tool-results/project-doc-b99b6076-631d-43e3-92a2-b1e8923dc0c4.txt",
       2141:"/root/.claude/projects/-home-claude/e1c6a220-faa1-5bd1-9d10-c0c3344b96cd/tool-results/project-doc-70dab881-3783-468e-aa79-e35a5252de13.txt"}
NMAX=100000; PH=(1+np.sqrt(5))/2
def pa(s):
    s=s.strip()
    if s=="0": return 0j
    sg=1.0
    if s[0]=='+': s=s[1:]
    elif s[0]=='-': sg=-1.0; s=s[1:]
    f=1.0
    if s.endswith("*1/phi"): f=1/PH; s=s[:-6]
    elif s.endswith("*phi"): f=PH; s=s[:-4]
    elif s.endswith("*2"): f=2.0; s=s[:-2]
    return sg*f*np.exp(1j*np.pi*int(s[7:])/5)
def build(N):
    ap={};chi={}
    for r in csv.DictReader(open(CSV[N])):
        p=int(r['p']); ap[p]=pa(r['a_p_exact']); c=r['chi_p_exact'].strip()
        chi[p]=0j if c=='0' else np.exp(2j*np.pi*int(c[6:])/5)
    spf=np.arange(NMAX+1)
    for i in range(2,int(NMAX**0.5)+1):
        if spf[i]==i: spf[i*i::i]=np.minimum(spf[i*i::i],i)
    cn=np.zeros(NMAX+1,dtype=np.complex128); cn[1]=1
    for n in range(2,NMAX+1):
        p=int(spf[n]); m=n; k=0
        while m%p==0: m//=p; k+=1
        pk=p**k
        if cn[pk]==0 and pk!=1:
            pr,cu=1+0j,ap[p]
            for _ in range(k-1): pr,cu=cu,ap[p]*cu-chi[p]*pr
            cn[pk]=cu
        cn[n]=cn[pk] if m==1 else cn[pk]*cn[m]
    return cn
print("calculus check: d/dx[(1-x^2)^-1/2] - x G^3 at x=0.3,0.6,0.9:")
for x in (0.3,0.6,0.9):
    h=1e-7; G=lambda t:(1-t*t)**-0.5
    print(f"   x={x}: numeric {(G(x+h)-G(x-h))/(2*h):.9f}  xG^3 {x*G(x)**3:.9f}")
for N in (1951,2141):
    cn=build(N); nn=np.arange(NMAX+1,dtype=float); w=nn*cn
    print(f"\n===== N={N} =====")
    print(f"{'y':>10s} {'u=y':>10s} {'1/G':>10s} {'m measured':>12s} {'m random(S2/S1)':>16s} "
          f"{'criterion u':>12s} {'tier':>22s}")
    for y in (1e-2,3.16e-3,1e-3,3.16e-4,1.5e-4,1e-4):
        x=2*np.pi*y*nn[1:]; cut=min(NMAX,int(700/(2*np.pi*y))+2)
        K=np.zeros(NMAX); K[:cut]=k0(x[:cut])
        t=w[1:]*K
        S1=np.abs(t).sum(); S2=np.sqrt((np.abs(t)**2).sum()); Sig=t.sum()
        m=abs(Sig)/S1
        tier=("BEATS criterion" if m<y else ("between random and criterion" if m<S2/S1*1.5
              else "at/above random"))
        print(f"{y:10.2e} {y:10.2e} {np.sqrt(y):10.2e} {m:12.3e} {S2/S1:16.3e} {y:12.2e} {tier:>22s}")
