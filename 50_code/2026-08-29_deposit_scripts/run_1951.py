import numpy as np, csv
from scipy.special import k0

path="/root/.claude/projects/-home-claude/17b2fbcf-cb76-5cd8-bb47-c85d94234441/tool-results/project-doc-b99b6076-631d-43e3-92a2-b1e8923dc0c4.txt"
X=100000
ap={}; chp={}
with open(path) as f:
    for row in csv.DictReader(f):
        p=int(row['p'])
        ap[p]=complex(float(row['Re_a_p']),float(row['Im_a_p']))
        chp[p]=complex(float(row['Re_chi']),float(row['Im_chi']))
        if p==1951: print("p=1951 row: a_p =",row['a_p_exact'],"chi =",row['chi_p_exact'],"prov =",row['provenance'])
print("primes loaded:",len(ap))

c=np.zeros(X+1,dtype=complex); c[1]=1
for p in sorted(ap):
    if p>X: continue
    chi_p = 0.0 if p==1951 else chp[p]
    pk=[1.0+0j, ap[p]]
    q=p*p
    while q<=X:
        pk.append(ap[p]*pk[-1]-chi_p*pk[-2]); q*=p
    powers=[p**k for k in range(1,len(pk)) if p**k<=X]
    for i,q in enumerate(powers,start=1):
        for m in range(1,X//q+1):
            if m%p: c[m*q]=c[m]*pk[i]

n=np.arange(1,X+1); cn=c[1:]
N=1951.0
print("\nTRUE OBJECT doud-1951 (X=1e5): ratio/y curve  [control showed ~1.4..0.5 falling; Harper-model: noisy ~O(1) no rate]")
us=[0.85,1.0,1.25,1.5,2.0,2.5,3.0,4.0,5.0,6.0,8.0]
rows=[]
for u in us:
    y=1.0/(N*u); arg=2*np.pi*n*y
    K=np.where(arg<700,k0(np.minimum(arg,700)),0.0); w=n*K
    Phi2=abs(np.sum(cn*w))**2; D=np.sum((abs(cn)**2)*(w**2))
    r=Phi2/D; rows.append((u,y,r,r/y))
    print(f"  u={u:4}: ratio/y = {r/y:8.3f}   (ratio={r:.6f}, y={y:.6e})")
lo=[(np.log(y),np.log(r)) for u,y,r,ry in rows if u>=1.0]
A=np.polyfit([a for a,b in lo],[b for a,b in lo],1)
print(f"\nlog-log slope of ratio vs y over u in [1,8]: {A[0]:.3f}   [true-control genre: ~+1..+2.5; model genre: ~0 +/- noise]")
