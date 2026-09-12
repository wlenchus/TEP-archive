import numpy as np, csv
from math import sqrt
phi=(1+sqrt(5))/2

def load(path):
    rows=[]
    with open(path) as f:
        for row in csv.DictReader(f): rows.append(row)
    return rows

def analyze(rows,label,N):
    freq={}; m2={}; 
    for r in rows:
        cl=r['proj_class']; a2=float(r['Re_a_p'])**2+float(r['Im_a_p'])**2
        freq[cl]=freq.get(cl,0)+1; m2.setdefault(cl,[]).append(a2)
    n=len(rows)
    cheb={'1A':1/60,'2A':15/60,'3A':20/60,'5A':12/60,'5B':12/60}
    pred={'1A':4.0,'2A':0.0,'3A':1.0,'5A':phi**2,'5B':phi**-2}
    print(f"\n{label} (pi(1e5)={n} primes): class equidistribution + per-class RS means")
    tot=0
    for cl in sorted(freq):
        f=freq[cl]/n; mm=np.mean(m2[cl]); tot+=f*mm
        c=cheb.get(cl,float('nan')); p=pred.get(cl,float('nan'))
        print(f"  {cl}: freq {f:.5f} (Chebotarev {c:.5f}, dev {abs(f-c)/c*100 if c else 0:+.2f}%)   mean|a_p|^2 = {mm:.6f} (class value {p:.6f})")
    print(f"  GLOBAL mean |a_p|^2 = {tot:.6f}   (RS/irreducibility prediction: 1.000000)")
    return tot

r1=load("/root/.claude/projects/-home-claude/17b2fbcf-cb76-5cd8-bb47-c85d94234441/tool-results/project-doc-b99b6076-631d-43e3-92a2-b1e8923dc0c4.txt")
r2=load("/root/.claude/projects/-home-claude/17b2fbcf-cb76-5cd8-bb47-c85d94234441/tool-results/project-doc-70dab881-3783-468e-aa79-e35a5252de13.txt")
analyze(r1,"DOUD-1951",1951)
analyze(r2,"DOUD-2141",2141)

# Sigma |c_n|^2 / X linear-growth trend on the extended coefficients (1951)
from scipy.special import k0
exec(open('three_tier.py').read().split('X=100000')[0])
X=100000
ap={int(r['p']):complex(float(r['Re_a_p']),float(r['Im_a_p'])) for r in r1}
chp={int(r['p']):complex(float(r['Re_chi']),float(r['Im_chi'])) for r in r1}
c=build(ap,chp,X,1951)
cum=np.cumsum(np.abs(c[1:])**2)
print("\nDOUD-1951: Sigma_{n<=X}|c_n|^2 / X  (RS linear-growth probe; constant = Res-driven, finite):")
for x in [1000,5000,20000,50000,100000]:
    print(f"  X={x:6d}: {cum[x-1]/x:.6f}")
