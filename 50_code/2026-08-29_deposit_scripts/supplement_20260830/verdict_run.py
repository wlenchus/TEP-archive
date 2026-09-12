import numpy as np, csv
from scipy.special import k0
rng=np.random.default_rng(1951)

path="data/hecke_eigenvalues_doud1951_to1e5.csv"
X=100000
ap={}; chp={}
with open(path) as f:
    for row in csv.DictReader(f):
        p=int(row['p']); ap[p]=complex(float(row['Re_a_p']),float(row['Im_a_p'])); chp[p]=complex(float(row['Re_chi']),float(row['Im_chi']))
c=np.zeros(X+1,dtype=complex); c[1]=1
for p in sorted(ap):
    if p>X: continue
    chi_p=0.0 if p==1951 else chp[p]
    pk=[1.0+0j, ap[p]]; q=p*p
    while q<=X: pk.append(ap[p]*pk[-1]-chi_p*pk[-2]); q*=p
    for i,q in enumerate([p**k for k in range(1,len(pk)) if p**k<=X],start=1):
        for m in range(1,X//q+1):
            if m%p: c[m*q]=c[m]*pk[i]
n=np.arange(1,X+1); cn=c[1:]; N=1951.0
absc=np.abs(cn)

def measure(coef,u):
    y=1.0/(N*u); arg=2*np.pi*n*y
    K=np.where(arg<700,k0(np.minimum(arg,700)),0.0); w=n*K
    Phi=np.sum(coef*w); D=np.sum((np.abs(coef)**2)*(w**2))
    # truncation floor: |c_m| <= d(m) <= m; tail Phi <= sum_{m>X} m^2 K0(2 pi m y), K0(z)~sqrt(pi/2z)e^-z
    z=2*np.pi*(X+1)*y
    tail = (X+1)**2 * np.sqrt(np.pi/(2*z))*np.exp(-z) / (2*np.pi*y) if z<700 else 0.0
    r=abs(Phi)**2/D
    floor=(tail**2)/D if D>0 else 0
    return y,r,floor

print("TRUE 1951 object — full precision, with truncation floors:")
print(f"{'u':>5} {'ratio':>13} {'ratio/y':>12} {'trunc-floor':>12}  clean?")
for u in [0.85,1.0,1.25,1.5,2.0,3.0,4.0,6.0,8.0]:
    y,r,fl=measure(cn,u)
    print(f"{u:5} {r:13.4e} {r/y:12.4e} {fl:12.1e}   {'YES' if r>100*fl or r<1e-25 else 'floor!'}")

print("\nPHASE-SCRAMBLE CONTROL (same |c_n|, uniform random phases; 12 seeds) — the T-C4 discriminator:")
for u in [0.85,1.25,2.0,4.0]:
    vals=[]
    for s in range(12):
        ph=np.exp(2j*np.pi*rng.random(X)); vals.append(measure(absc*ph,u)[1])
    y=1.0/(N*u)
    print(f"  u={u}: scrambled ratio mean={np.mean(vals):.3f} median={np.median(vals):.3f}  (true object: {measure(cn,u)[1]:.3e})")

print("\nSIGN TEST — Fricke-consistency of the collapse: first Fourier mode of the 0-cusp expansion")
# |F(iy)| vs eps * (Fricke image leading term): amplitude ~ 2*sqrt(y')*|c_1|*K0(2 pi y') with y' = 1/(N y), times |eps|=1
for u in [1.5,2.0,3.0]:
    y=1.0/(N*u); yp=u  # y' = 1/(Ny) = u
    arg=2*np.pi*n*y; K=np.where(arg<700,k0(np.minimum(arg,700)),0.0)
    F=np.sqrt(y)*np.sum(cn*K)          # F(iy) one-sided
    pred=np.sqrt(1.0/(N*y))*k0(2*np.pi*u)/np.sqrt(N*y*y)  # crude scale of Fricke leading term (up to eps, lattice factors)
    print(f"  u={u}: |F(iy)|={abs(F):.3e}   e^(-2 pi u) scale={np.exp(-2*np.pi*u):.3e}   ratio={abs(F)/np.exp(-2*np.pi*u):.3f}")
