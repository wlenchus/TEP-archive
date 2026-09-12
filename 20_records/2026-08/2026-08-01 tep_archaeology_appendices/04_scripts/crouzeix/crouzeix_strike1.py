"""
STRIKE 1 — Crouzeix as a boundary-budget problem. 2026-08-01, seed 20260801.
PREREGISTERED PREDICTIONS (written before first run):
  P1: the boundary POVM M (harmonic-measure operator density on an inflated
      contour around W(A)) is pointwise PSD with total mass 2I, for every test matrix.
  P2: at known extremals (scaled Jordan J2 with f=z; J3 with f=z^2), c -> 2/(1+eps)
      and the interference I(f,x*) -> 0 (reflected channel silenced).
  P3: at optimizer-found maximizers on random 2x2/3x3/4x4, c < 2 and I >= 0 (alignment).
  P4: no maximizer found with I < 0.  [Any P4 failure = the discovery, not the failure.]
LEMMA (exact, 3 lines): c^2 + I = Re<f(A)x, Tx> <= ||T|| c <= 2c (sup|f|=1 on contour)
  => I <= c(2-c). Hence any Crouzeix violation (c>2) REQUIRES destructive
  interference I < 0 between the transmitted read f(A) and reflected read g(A)*.
"""
import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(20260801)

def wboundary(A, m=720):
    th = np.linspace(0, 2*np.pi, m, endpoint=False)
    pts, nrm = [], []
    for t in th:
        H = (np.exp(-1j*t)*A + np.exp(1j*t)*A.conj().T)/2
        w, V = np.linalg.eigh(H)
        v = V[:, -1]
        pts.append(v.conj() @ A @ v)
        nrm.append(np.exp(1j*t))
    return np.array(pts), np.array(nrm)

def povm(A, eps=0.05, m=720):
    z, nu = wboundary(A, m)
    sig = z + eps*nu                      # inflated contour, ccw
    dsig = (np.roll(sig, -1) - np.roll(sig, 1))/2
    n = A.shape[0]
    Ms, cauchy = [], np.zeros((n, n), complex)
    I_ = np.eye(n)
    for s, ds in zip(sig, dsig):
        R = np.linalg.inv(s*I_ - A)
        C = R*ds/(2j*np.pi)
        cauchy += C
        Ms.append(C + C.conj().T)         # dM = 2 Re[.]
    Ms = np.array(Ms)
    mass = Ms.sum(axis=0)
    minev = min(np.linalg.eigvalsh((M+M.conj().T)/2).min() for M in Ms)
    return sig, Ms, mass, cauchy, minev

def cval_and_I(A, coef, sig, Ms):
    f_b = np.polyval(coef, sig)           # f on contour
    sup = np.abs(f_b).max()
    if sup < 1e-14: return 0.0, 0.0, None
    fA = np.polyval(coef, A[np.newaxis][0]) if False else None
    # matrix polynomial:
    n = A.shape[0]; fA = np.zeros((n,n), complex)
    for c in coef: fA = fA @ A + c*np.eye(n)
    c = np.linalg.norm(fA, 2)/sup
    T = np.tensordot(f_b, Ms, axes=(0,0))
    G = T - fA                            # = g(A)^*
    U, S, Vh = np.linalg.svd(fA)
    x = Vh.conj().T[:, 0]                 # maximizing unit vector
    Ival = np.real(np.vdot(fA @ x, G @ x))/sup**2
    Tnorm = np.linalg.norm(T, 2)/sup
    return c, Ival, Tnorm

def maximize_c(A, deg=5, restarts=40, eps=0.05, m=720):
    sig, Ms, mass, cauchy, minev = povm(A, eps, m)
    massdev = np.linalg.norm(mass - 2*np.eye(A.shape[0]), 2)
    cauchydev = np.linalg.norm(cauchy - np.eye(A.shape[0]), 2)
    best = (0, 0, None)
    def obj(v):
        coef = v[:deg+1] + 1j*v[deg+1:]
        c, _, _ = cval_and_I(A, coef, sig, Ms)
        return -c
    for k in range(restarts):
        v0 = rng.standard_normal(2*(deg+1))
        r = minimize(obj, v0, method='Nelder-Mead',
                     options={'maxiter': 4000, 'fatol': 1e-12, 'xatol': 1e-10})
        if -r.fun > best[0]:
            coef = r.x[:deg+1] + 1j*r.x[deg+1:]
            c, Ival, Tn = cval_and_I(A, coef, sig, Ms)
            best = (c, Ival, Tn)
    return best, minev, massdev, cauchydev

def report(name, A, deg=5, restarts=40, eps=0.05):
    (c, Ival, Tn), minev, md, cd = maximize_c(A, deg, restarts, eps)
    ceil = c*(2-c)
    print(f"{name:28s} c={c:8.5f}  I={Ival:+10.6f}  ceiling c(2-c)={ceil:+9.6f}  "
          f"||T||/sup={Tn:7.5f}  minEig(M)={minev:+.2e}  |mass-2I|={md:.2e}  |Cauchy-I|={cd:.2e}")
    return c, Ival

print("== P1/P2 exact-extremal validations ==")
J2 = np.array([[0,2],[0,0]], complex)
report("J2=[[0,2],[0,0]] (disk)", J2)
J3 = np.array([[0,1,0],[0,0,1],[0,0,0]], complex)
report("J3 nilpotent (disk r=cos45)", J3)

print("\n== P3/P4 random sweeps ==")
for i in range(4):
    A = rng.standard_normal((2,2)) + 1j*rng.standard_normal((2,2))
    report(f"random 2x2 #{i+1}", A, restarts=30)
for i in range(4):
    A = rng.standard_normal((3,3)) + 1j*rng.standard_normal((3,3))
    report(f"random 3x3 #{i+1}", A, restarts=30)
for i in range(2):
    A = rng.standard_normal((4,4)) + 1j*rng.standard_normal((4,4))
    report(f"random 4x4 #{i+1}", A, restarts=25)

print("\n== near-extremal 3x3 family (Crabb-type, scaled) ==")
for a in [0.8, 1.0, 1.2]:
    C3 = np.array([[0,a,0],[0,0,a],[0,0,0]], complex)
    report(f"J3 scaled a={a}", C3, restarts=30)
