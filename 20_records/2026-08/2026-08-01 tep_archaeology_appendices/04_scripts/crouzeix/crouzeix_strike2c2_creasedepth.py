"""
STRIKE 2c-2 — crease-depth profile. Seed 20260805.
QUESTION: does the J3 crease heal as c -> 2 (I_min(c) -> 0^-: benign, summit rigidity)
or stay open (bounded-negative corridor all the way up)?
PREREGISTERED: healing predicted (the cap on the disk is a theorem; the circle ledger
forces I >= c(2-c)+... at the limit: at c = 2 exactly, I <= c(2-c) = 0 AND the
saturated-circle/total-collapse structure should pinch I -> 0 from below too).
Depth profile: min I at c >= {1.85, 1.90, 1.95, 1.98} for J3; J4 fixed with seeds.
"""
import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(20260805)
CIRC = np.exp(2j*np.pi*np.arange(2048)/2048)

def make(n):
    A = np.zeros((n, n), complex)
    for i in range(n-1): A[i, i+1] = 1.0
    return A, np.cos(np.pi/(n+1))

def ledger(A, r, coef):
    fb = np.polyval(coef, r*CIRC); sup = np.abs(fb).max()
    if sup < 1e-13: return None
    coef = coef/sup
    n = A.shape[0]; fA = np.zeros((n, n), complex)
    for cc in coef: fA = fA @ A + cc*np.eye(n)
    c = np.linalg.norm(fA, 2)
    x = np.linalg.svd(fA)[2].conj().T[:, 0]
    W = coef[-1]*np.conj(x.conj() @ fA @ x)
    return c, np.real(W), np.imag(W), abs(coef[-1])

def probe(n, deg, cthr, restarts=50):
    A, r = make(n)
    ext = np.zeros(2*(deg+1)); ext[deg+1-n] = 1.0     # f = z^{n-1} seed (real part slot)
    def L(v): return ledger(A, r, v[:deg+1] + 1j*v[deg+1:])
    def obj(v):
        q = L(v)
        if q is None: return 1e6
        return q[1] + 120*max(0, cthr - q[0])**2
    worst = (1e9, None)
    seeds = [ext + 0.25*rng.standard_normal(ext.shape) for _ in range(restarts//2)] + \
            [rng.standard_normal(2*(deg+1)) for _ in range(restarts//2)]
    for v0 in seeds:
        rr = minimize(obj, v0, method='Nelder-Mead',
                      options={'maxiter': 4500, 'fatol': 1e-14})
        q = L(rr.x)
        if q and q[0] >= cthr and q[1] < worst[0]: worst = (q[1], q)
    if worst[1] is None:
        print(f"  J{n} c>={cthr}: no config found above threshold"); return
    wI, q = worst
    print(f"  J{n} c>={cthr:.2f}: min I = {wI:+.3e}  (c={q[0]:.4f}, J={q[2]:+.1e}, |a0|={q[3]:.4f})")

print("== J3 crease-depth profile ==")
for cthr in [1.85, 1.90, 1.95, 1.98]:
    probe(3, 8, cthr)
print("== J4 (fixed, seeded) ==")
for cthr in [1.75, 1.85]:
    probe(4, 8, cthr, restarts=40)
