import numpy as np, csv
from scipy.special import k0
rng=np.random.default_rng(229)

def load(path):
    ap={}; chp={}
    with open(path) as f:
        for row in csv.DictReader(f):
            p=int(row['p']); ap[p]=complex(float(row['Re_a_p']),float(row['Im_a_p'])); chp[p]=complex(float(row['Re_chi']),float(row['Im_chi']))
    return ap,chp

def build(ap,chp,X,N):
    c=np.zeros(X+1,dtype=complex); c[1]=1
    for p in sorted(ap):
        if p>X: continue
        chi_p=0.0 if p==N else chp[p]
        pk=[1.0+0j, ap[p]]; q=p*p
        while q<=X: pk.append(ap[p]*pk[-1]-chi_p*pk[-2]); q*=p
        for i,q in enumerate([p**k for k in range(1,len(pk)) if p**k<=X],start=1):
            for m in range(1,X//q+1):
                if m%p: c[m*q]=c[m]*pk[i]
    return c

def ratio(c,N,u,X):
    n=np.arange(1,X+1); y=1.0/(N*u); arg=2*np.pi*n*y
    K=np.where(arg<700,k0(np.minimum(arg,700)),0.0); w=n*K
    return abs(np.sum(c[1:]*w))**2/np.sum((np.abs(c[1:])**2)*(w**2))

X=100000; N=1951
ap,chp=load("data/hecke_eigenvalues_doud1951_to1e5.csv")

# TIER 3: Chebotarev-random multiplicative model — permute (a_p, chi_p) pairs across primes (ramified 1951 held fixed)
print("MODEL TIER (multiplicative, Chebotarev-correct pairs, random assignment; 8 seeds):")
ps=[p for p in sorted(ap) if p<=X and p!=1951]
for u in [1.0,2.0,3.0,4.0,6.0]:
    vals=[]
    for s in range(8):
        perm=rng.permutation(len(ps))
        ap2={1951:ap[1951]}; chp2={1951:chp[1951]}
        for i,p in enumerate(ps): ap2[p]=ap[ps[perm[i]]]; chp2[p]=chp[ps[perm[i]]]
        cm=build(ap2,chp2,X,N)
        vals.append(ratio(cm,N,u,X))
    print(f"  u={u}: model ratio mean={np.mean(vals):.4f} median={np.median(vals):.4f} min={np.min(vals):.2e}")
