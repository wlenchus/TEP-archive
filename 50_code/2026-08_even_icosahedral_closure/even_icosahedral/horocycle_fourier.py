"""THE HOROCYCLE FOURIER TEST — the parabolic-port instrument.
2026-08-13 (session B).  A NEW functional: not pointwise, but the full Fourier
decomposition of F along a horocycle at the OTHER cusp.

*** SEE ERRATUM_mode0_is_not_the_parabolic_port_20260813B.md: the MODE-0 billing below
*** is WITHDRAWN.  For an odd (sin-type) form F|W is odd in x by parity alone, so mode 0
*** vanishes structurally at every cusp.  What mode 0 actually tests (given oddness) is
*** 1-periodicity of F|W, i.e. invariance under W^{-1} T W = [[1,0],[-N,1]] -- the
*** PARABOLIC GENERATOR AT THE CUSP 0.  That is a real automorphy test at one group
*** element, necessary but not sufficient, and it says nothing about Eisenstein occupancy.
*** The mode-matching (n >= 1), the must-be-zero band, and the collapse are unaffected.

Object: (F|W)(z) := F(-1/(Nz)).  Expand in x at fixed y and read the modes.
  * MODE 0: see erratum banner above.
  * MODES n >= 1, if the fold holds, must equal  const * sqrt(y) * conj(c_n) * K0(2 pi n y),
    with const = tau(chi)/(sqrt(N) a_N) = -eps  (the sign slip is disclosed in the record).
  * THE COLLAPSE: at y = 1 each evaluation of F|W needs ~10^5 K-Bessel terms
    (Im w ~ 1/(2N)), yet the prediction says the whole x-profile has only ~3
    nonzero modes.  A 512-point transform therefore tests ~250 independent
    "must-be-zero" statements at once.

PREREG (stated before run; same-session, unhashed):
  H-a  |mode 0| / scale <= 1e-10
  H-b  modes 1..5 match eps*sqrt(y)*conj(c_n)*K0(2 pi n y) to <= 1e-10 relative
       [FAILED AS WRITTEN -- sign: the constant is -eps, not eps; passes exactly corrected]
  H-c  modes 6..255 (the "must-be-zero" band) all <= 1e-10 of the mode-1 scale
Kill K-H: any of the three failing at 1e-6 is a POSITIVE defect signal, reported
as such at headline volume (it would be evidence AGAINST automorphy).
"""
import numpy as np, csv
from scipy.special import k0
CSV={1951:"/root/.claude/projects/-home-claude/e1c6a220-faa1-5bd1-9d10-c0c3344b96cd/tool-results/project-doc-b99b6076-631d-43e3-92a2-b1e8923dc0c4.txt",
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
def eps_of(N,pin,aNk):
    e5=(N-1)//5; t0=pow(2,e5,N); io={}
    for k in range(5): io[pow(t0,k,N)]=(k*pin)%5
    z=np.exp(2j*np.pi/5); eN=np.exp(2j*np.pi/N); tau=0j
    for x in range(1,N): tau+=z**io[pow(x,e5,N)]*eN**x
    return -tau/(np.sqrt(N)*np.exp(1j*np.pi*aNk/5))

for N,pin,aNk in ((1951,4,2),(2141,1,8)):
    cn=build(N); eps=eps_of(N,pin,aNk)
    print(f"\n===== N={N} =====  eps = {eps:.10f}")
    for Y in (1.0, 0.5):
        M=512
        xs=np.arange(M)/M
        u=-xs/(N*(xs**2+Y**2)); v=Y/(N*(xs**2+Y**2))
        nmaxs=np.minimum(NMAX,(700/(2*np.pi*v)).astype(int)+2)
        FW=np.zeros(M,dtype=np.complex128)
        for j in range(M):
            nm=int(min(nmaxs[j], 30000))
            n=np.arange(1,nm+1)
            FW[j]=np.sqrt(v[j])*2j*np.sum(cn[1:nm+1]*k0(2*np.pi*n*v[j])*np.sin(2*np.pi*n*u[j]))
        # Fourier modes:  FW(x) = sum_k  A_k e(kx)
        A=np.fft.fft(FW)/M
        pred=lambda n: eps*np.sqrt(Y)*np.conj(cn[n])*k0(2*np.pi*n*Y)
        scale=abs(pred(1))
        print(f"  y={Y}:  terms/eval ~ {int(nmaxs.max())};  |mode1 predicted| = {scale:.4e}")
        print(f"    MODE 0 (see erratum banner): |A0| = {abs(A[0]):.3e}"
              f"   rel = {abs(A[0])/scale:.3e}")
        for n in (1,2,3,4,5):
            p=pred(n); rel=abs(A[n]-p)/max(abs(p),1e-300)
            print(f"    mode {n}: measured {abs(A[n]):.6e}  predicted {abs(p):.6e}  rel dev {rel:.2e}")
        band=np.abs(A[6:256])/scale
        print(f"    must-be-zero band (modes 6..255): max rel = {band.max():.3e}, "
              f"median {np.median(band):.2e}   -> {'PASS' if band.max()<1e-6 else 'CHECK'}")
