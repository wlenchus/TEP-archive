import numpy as np
from scipy.special import k0

def hecke_extend(cp, chi, X):
    """multiplicative extension: c_{p^{k+1}} = c_p c_{p^k} - chi(p) c_{p^{k-1}}"""
    c = np.zeros(X+1, dtype=complex); c[1]=1.0
    primes=[p for p in range(2,X+1) if all(p%q for q in range(2,int(p**.5)+1))]
    for p in primes:
        # prime powers
        pk=[1.0+0j, cp[p]]
        q=p*p
        while q<=X:
            pk.append(cp[p]*pk[-1]-chi[p]*pk[-2]); q*=p
        # fill multiplicatively
        powers=[p**k for k in range(1,len(pk)) if p**k<=X]
        for i,q in enumerate(powers,start=1):
            for m in range(1, X//q+1):
                if m%p: c[m*q]=c[m]*pk[i]
    return c

def ratio_curve(c, N, us, X):
    n=np.arange(1,X+1); cn=c[1:X+1]
    out=[]
    for u in us:
        y=1.0/(N*u)
        arg=2*np.pi*n*y
        K=np.where(arg<700, k0(np.minimum(arg,700)), 0.0)
        w=n*K
        Phi2=abs(np.sum(cn*w))**2          # |Phi|^2 / y
        D=np.sum((abs(cn)**2)*(w**2))      # D
        ratio=Phi2/D
        out.append((u,y,ratio,ratio/y))
    return out

# ---- CONTROL: x^3 - 4x - 1, disc 229, L = zeta_F/zeta ----
X=6000
def roots_mod(p): return sum(1 for x in range(p) if (x**3-4*x-1)%p==0)
primes=[p for p in range(2,X+1) if all(p%q for q in range(2,int(p**.5)+1))]
cp=np.zeros(X+1); chi=np.zeros(X+1)
def kron229(p):
    if p==229: return 0
    # 229 ≡ 1 mod 4 => (229/p)=(p/229) by reciprocity
    return pow(p,114,229)==1 and 1 or -1
for p in primes:
    cp[p]=roots_mod(p)-1
    chi[p]=0 if p==229 else (1 if pow(p%229,114,229)==1 else -1)
c=hecke_extend(cp,chi,X)
print("control c_n real?", np.allclose(c.imag,0), " c_229 =", c[229].real)
res=ratio_curve(c.real.astype(complex),229,[1,2,3,4,6],X)
print("CONTROL disc-229 (record: u=1,2,3,4,6 -> 1.38, 1.88, 1.26, 0.91, 0.54):")
for u,y,r,ry in res: print(f"  u={u}: ratio/y = {ry:8.3f}   (ratio={r:.5f}, y={y:.6f})")
