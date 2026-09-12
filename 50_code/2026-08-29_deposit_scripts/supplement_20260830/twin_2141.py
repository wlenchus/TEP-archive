import numpy as np, csv
from scipy.special import k0
exec(open('three_tier.py').read().split('X=100000')[0])  # reuse load/build/ratio defs
X=100000; N=2141
ap,chp=load("data/hecke_eigenvalues_doud2141_to1e5.csv")
print("ramified row present:", 2141 in ap, " a_2141 =", ap.get(2141))
c=build(ap,chp,X,N)
n=np.arange(1,X+1)
print("TRUE OBJECT doud-2141 twin reading (with truncation floors):")
for u in [0.85,1.0,1.5,2.0,3.0,4.0,6.0]:
    y=1.0/(N*u); arg=2*np.pi*n*y
    K=np.where(arg<700,k0(np.minimum(arg,700)),0.0); w=n*K
    Phi2=abs(np.sum(c[1:]*w))**2; D=np.sum((np.abs(c[1:])**2)*(w**2))
    z=2*np.pi*(X+1)*y
    tail=(X+1)**2*np.sqrt(np.pi/(2*z))*np.exp(-z)/(2*np.pi*y) if z<700 else 0.0
    fl=(tail**2)/D
    r=Phi2/D
    print(f"  u={u:4}: ratio={r:.4e}  ratio/y={r/y:.4e}  floor={fl:.1e}  {'clean' if r>100*fl or r<1e-25 else 'FLOOR'}")
