"""
STRIKE 2c — exact-disk adversarial test of Alignment. Seed 20260804.
On centered disks with nilpotent A, the reflection has CLOSED FORM: g(A)* = f(0)·I
(residue computation; no POVM, no quadrature error). So
    I(f,x) = Re[ f(0) * conj( x* f(A) x ) ],   x = top right-singular vector of f(A).
PREREGISTERED:
  P6a (J2): I >= 0 at EVERY (f, maximizer) — claimed as a two-line theorem found in
      design: x1 = conj(a0) b / (lam - |a0|^2) x2 forces the cross term positive:
      I = |a0|^2 (1 + |b|^2 |x2|^2/(lam - |a0|^2)) >= 0, zero iff a0 = 0 (Berger sector).
      Numerics must find min I = 0 (at a0 -> 0), never negative.
  P6b (J3, J4): OPEN — conjectured I >= 0 at near-maximizers (confidence ~0.6).
      A finding of I < 0 with c >= threshold = THE CREASE: Alignment's clean form dies
      on the very domain where Crouzeix is a theorem, forcing the corridor restatement.
"""
import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(20260804)

def make(n):
    A = np.zeros((n, n), complex)
    for i in range(n-1): A[i, i+1] = 1.0
    r = np.cos(np.pi/(n+1))     # numerical radius of J_n
    return A, r

CIRC = np.exp(2j*np.pi*np.arange(2048)/2048)

def ledger_disk(A, r, coef):
    zb = r*CIRC
    fb = np.polyval(coef, zb); sup = np.abs(fb).max()
    if sup < 1e-13: return None
    coef = coef/sup
    n = A.shape[0]; fA = np.zeros((n, n), complex)
    for cc in coef: fA = fA @ A + cc*np.eye(n)
    c = np.linalg.norm(fA, 2)
    x = np.linalg.svd(fA)[2].conj().T[:, 0]
    a0 = coef[-1]                       # f(0), post-normalization
    W = a0*np.conj(x.conj() @ fA @ x)   # f(0)*conj(<f(A)>_x): exact cross term
    return c, np.real(W), np.imag(W), abs(a0)

def strike(n, deg, cthr, label, restarts=60):
    A, r = make(n)
    def L(v): return ledger_disk(A, r, v[:deg+1] + 1j*v[deg+1:])
    # sanity: c_max via direct extremal f = z^{n-1}
    ext = np.zeros(deg+1); ext[deg+1-n] = 1.0
    cext = ledger_disk(A, r, ext + 0j)[0]
    # adversarial: minimize I subject to c >= cthr
    worst = (1e9, None)
    for k in range(restarts):
        v0 = rng.standard_normal(2*(deg+1))
        rr = minimize(lambda v: (lambda q: q[1] + 80*max(0, cthr - q[0])**2)(L(v)),
                      v0, method='Nelder-Mead', options={'maxiter': 4000, 'fatol': 1e-13})
        q = L(rr.x)
        if q[0] >= cthr and q[1] < worst[0]: worst = (q[1], q)
    # dense random scan at maximizer-agnostic points (for the J2 theorem check)
    scanmin = 1e9
    for _ in range(4000):
        v = rng.standard_normal(2*(deg+1))
        q = L(v)
        if q and q[1] < scanmin: scanmin = q[1]
    wI, q = worst
    print(f"{label}: c_extremal={cext:.5f} | adversarial (c>={cthr}): "
          f"min I = {wI:+.2e} (c={q[0]:.4f}, J={q[2]:+.2e}, |a0|={q[3]:.4f}) | "
          f"random-scan min I = {scanmin:+.2e}")

print("== P6a: J2 (theorem check: min I must be >= 0, ->0 only via a0->0) ==")
strike(2, 6, 1.85, "J2 deg6")
print("== P6b: J3, J4 (open) ==")
strike(3, 8, 1.85, "J3 deg8")
strike(4, 8, 1.72, "J4 deg8")
