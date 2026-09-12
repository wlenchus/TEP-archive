"""
STRIKE 2a — the fold hunt (Will's Jacobian objection, 2026-08-01). Seed 20260802.
PREREGISTERED: on thin ellipses (spectrum at the pointy foci = tight corners of the
fitted sheet) with high-degree f (Chebyshev folds), Alignment predicts I >= 0 at all
c-maximizers, with I shrinking as eccentricity grows. KILL: any I < 0 at a maximizer.
Also: adversarial minimization of I among near-maximal-c polynomials.
"""
import numpy as np
from scipy.optimize import minimize
from numpy.polynomial import chebyshev as Ch
rng = np.random.default_rng(20260802)

def wboundary(A, m=512):
    th = np.linspace(0, 2*np.pi, m, endpoint=False)
    pts, nrm = [], []
    for t in th:
        H = (np.exp(-1j*t)*A + np.exp(1j*t)*A.conj().T)/2
        w, V = np.linalg.eigh(H); v = V[:, -1]
        pts.append(v.conj() @ A @ v); nrm.append(np.exp(1j*t))
    return np.array(pts), np.array(nrm)

def povm(A, eps=0.05, m=512):
    z, nu = wboundary(A, m)
    sig = z + eps*nu
    dsig = (np.roll(sig, -1) - np.roll(sig, 1))/2
    n = A.shape[0]; I_ = np.eye(n)
    Ms = []
    for s, ds in zip(sig, dsig):
        C = np.linalg.inv(s*I_ - A)*ds/(2j*np.pi)
        Ms.append(C + C.conj().T)
    Ms = np.array(Ms)
    return sig, Ms

def evalf(A, coef, sig, Ms):
    f_b = np.polyval(coef, sig); sup = np.abs(f_b).max()
    if sup < 1e-13: return 0.0, 0.0
    n = A.shape[0]; fA = np.zeros((n,n), complex)
    for c in coef: fA = fA @ A + c*np.eye(n)
    c = np.linalg.norm(fA, 2)/sup
    T = np.tensordot(f_b, Ms, axes=(0,0))
    x = np.linalg.svd(fA)[2].conj().T[:, 0]
    Ival = np.real(np.vdot(fA @ x, (T - fA) @ x))/sup**2
    return c, Ival

def cheb_seed(k, deg):
    ck = np.zeros(k+1); ck[k] = 1.0
    p = Ch.cheb2poly(ck)
    coef = np.zeros(deg+1, complex); coef[-(len(p)):] = p[::-1]
    return coef

def hunt(name, A, deg=12, restarts=30, eps=0.05):
    sig, Ms = povm(A, eps)
    def cI(v):
        return evalf(A, v[:deg+1] + 1j*v[deg+1:], sig, Ms)
    # stage 1: maximize c (random + Chebyshev-fold seeds)
    best = (0, 0, None)
    seeds = [np.concatenate([np.real(cheb_seed(k, deg)), np.imag(cheb_seed(k, deg))])
             for k in range(2, deg+1, 2)]
    seeds += [rng.standard_normal(2*(deg+1)) for _ in range(restarts)]
    for v0 in seeds:
        r = minimize(lambda v: -cI(v)[0], v0, method='Nelder-Mead',
                     options={'maxiter': 3500, 'fatol': 1e-12})
        c, Iv = cI(r.x)
        if c > best[0]: best = (c, Iv, r.x.copy())
    cmax, Imax, vbest = best
    # stage 2: adversarial — minimize I subject to c >= 0.9 cmax
    worstI = Imax
    for v0 in [vbest + 0.15*rng.standard_normal(vbest.shape) for _ in range(12)] + \
              [rng.standard_normal(2*(deg+1)) for _ in range(8)]:
        r = minimize(lambda v: cI(v)[1] + 60*max(0, 0.9*cmax - cI(v)[0])**2, v0,
                     method='Nelder-Mead', options={'maxiter': 3500, 'fatol': 1e-12})
        c, Iv = cI(r.x)
        if c >= 0.9*cmax and Iv < worstI: worstI = Iv
    print(f"{name:34s} c_max={cmax:7.4f}  I@max={Imax:+9.5f}  worst I (c>=0.9c_max)={worstI:+9.5f}  ceil={cmax*(2-cmax):+8.5f}")
    return cmax, Imax, worstI

print("== control ==")
hunt("J2 disk (control)", np.array([[0,2],[0,0]], complex), deg=8, restarts=20)
print("== thin ellipses: foci +-1, minor axis b (fitted-sheet corners) ==")
for b in [1.0, 0.4, 0.15]:
    A = np.array([[-1, b],[0, 1]], complex)
    hunt(f"ellipse 2x2 b={b}", A, deg=12, restarts=25)
print("== thin 3x3 / 4x4 (three/four eigenvalues under a thin sheet) ==")
for b in [0.3, 0.12]:
    A = np.diag([-1, 0, 1]).astype(complex); A[0,1] = A[1,2] = b
    hunt(f"thin 3x3 b={b}", A, deg=12, restarts=25)
A4 = np.diag([-1, -0.33, 0.33, 1]).astype(complex)
for i in range(3): A4[i, i+1] = 0.2
hunt("thin 4x4 b=0.2", A4, deg=12, restarts=20)
print("== raw Chebyshev fold-scaling on thinnest ellipse (no optimization) ==")
A = np.array([[-1, 0.15],[0, 1]], complex)
sig, Ms = povm(A, 0.05)
for k in [2, 4, 6, 8, 10, 12]:
    c, Iv = evalf(A, cheb_seed(k, 12), sig, Ms)
    print(f"  T_{k:2d}: c={c:7.4f}  I={Iv:+9.5f}")
