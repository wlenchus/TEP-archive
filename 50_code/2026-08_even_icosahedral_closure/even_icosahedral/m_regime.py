"""m = sqrt(u)?  The incoherent-tier law, its constant, and where the object leaves it.
2026-08-13 (session B).  Result: S2/S1 = c*sqrt(u) with c -> ~2.23 (the incompressibility
/ flatness law, a theorem about the K-Bessel weights); the OBJECT's meter m tracks it for
N*y >~ 1 and collapses super-exponentially below N*y = 1 -- the fold seam in the height
coordinate, located at y = 1/N = 5.13e-4 to three digits."""
import numpy as np, csv
from scipy.special import k0
CSV={1951:"/root/.claude/projects/-home-claude/e1c6a220-faa1-5bd1-9d10-c0c3344b96cd/tool-results/project-doc-b99b6076-631d-43e3-92a2-b1e8923dc0c4.txt"}
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
N=1951
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
nn=np.arange(NMAX+1,dtype=float); w=nn*cn
print(f"1/N = {1/N:.4e}   (the fold seam in y)")
print(f"{'y':>10s} {'Ny (fold u)':>12s} {'S2/S1':>11s} {'sqrt(y)':>10s} {'c=ratio':>9s} {'m actual':>11s} {'m/sqrt(y)':>11s}")
for y in (3e-2,1e-2,3e-3,1e-3,7e-4,5.13e-4,4e-4,3.16e-4,2e-4,1.5e-4,1e-4):
    x=2*np.pi*y*nn[1:]; cut=min(NMAX,int(700/(2*np.pi*y))+2)
    K=np.zeros(NMAX); K[:cut]=k0(x[:cut]); t=w[1:]*K
    S1=np.abs(t).sum(); S2=np.sqrt((np.abs(t)**2).sum()); m=abs(t.sum())/S1
    print(f"{y:10.2e} {N*y:12.3f} {S2/S1:11.4e} {np.sqrt(y):10.3e} {S2/S1/np.sqrt(y):9.3f} "
          f"{m:11.3e} {m/np.sqrt(y):11.3e}")
