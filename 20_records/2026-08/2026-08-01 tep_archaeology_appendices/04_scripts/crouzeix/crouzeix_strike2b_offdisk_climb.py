"""
STRIKE 2b' — off-disk healing + the climbing test. Seed 20260806.
PREREGISTERED:
  P7 (off-disk): creases (I<0 at near-maximizers) exist below the local summit on
     non-circular domains too; depth pinches toward the local summit, resolvable only
     down to the POVM noise floor (~1e-5 at eps=0.025, m=768 — floor stated honestly).
  P8 (climbing heals): c-ascent started FROM a crease configuration raises I to >= 0
     before reaching the summit; no path carries a crease to the top. This is the
     checkable face of the Maximizing-Crease Characterization (violation <=> a crease
     AT a maximizer above 2; see Delta 4).
"""
import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(20260806)

# ---------- exact-disk machinery (nilpotent A) ----------
CIRC = np.exp(2j*np.pi*np.arange(2048)/2048)
def ledger_disk(A, r, coef):
    fb = np.polyval(coef, r*CIRC); sup = np.abs(fb).max()
    if sup < 1e-13: return None
    coef = coef/sup
    n = A.shape[0]; fA = np.zeros((n,n), complex)
    for cc in coef: fA = fA @ A + cc*np.eye(n)
    c = np.linalg.norm(fA, 2)
    x = np.linalg.svd(fA)[2].conj().T[:, 0]
    W = coef[-1]*np.conj(x.conj() @ fA @ x)
    return c, np.real(W)

# ---------- POVM machinery (general A) ----------
def povm(A, eps=0.025, m=768):
    th = np.linspace(0, 2*np.pi, m, endpoint=False)
    pts, nrm = [], []
    for t in th:
        H = (np.exp(-1j*t)*A + np.exp(1j*t)*A.conj().T)/2
        w, V = np.linalg.eigh(H); v = V[:, -1]
        pts.append(v.conj() @ A @ v); nrm.append(np.exp(1j*t))
    sig = np.array(pts) + eps*np.array(nrm)
    dsig = (np.roll(sig, -1) - np.roll(sig, 1))/2
    n = A.shape[0]; Ms = []
    for s, ds in zip(sig, dsig):
        C = np.linalg.inv(s*np.eye(n) - A)*ds/(2j*np.pi)
        Ms.append(C + C.conj().T)
    return sig, np.array(Ms)
def ledger_povm(A, coef, sig, Ms):
    fb = np.polyval(coef, sig); sup = np.abs(fb).max()
    if sup < 1e-13: return None
    coef = coef/sup; fb = fb/sup
    n = A.shape[0]; fA = np.zeros((n,n), complex)
    for cc in coef: fA = fA @ A + cc*np.eye(n)
    c = np.linalg.norm(fA, 2)
    T = np.tensordot(fb, Ms, axes=(0,0))
    x = np.linalg.svd(fA)[2].conj().T[:, 0]
    return c, np.real(np.vdot(fA @ x, (T - fA) @ x))

# ---------- Part 1: off-disk creases + healing ----------
print("== P7: off-disk families (POVM, eps=0.025, m=768; noise floor ~1e-5) ==")
fams = []
A1 = np.zeros((3,3), complex); A1[0,1]=A1[1,2]=1.0; A1 += 0.05*np.diag([1,-0.5,-0.5]); fams.append(("J3+0.05*asym", A1, 8))
A2 = np.zeros((3,3), complex); A2[0,1]=A2[1,2]=1.0; A2 += 0.15*np.diag([1,-0.5,-0.5]); fams.append(("J3+0.15*asym", A2, 8))
A3 = np.array([[0,2],[0.5*np.exp(1j*np.pi/3),0]], complex); fams.append(("P(0.5,pi/3) 2x2", A3, 6))
for name, A, deg in fams:
    sig, Ms = povm(A)
    def L(v): return ledger_povm(A, v[:deg+1] + 1j*v[deg+1:], sig, Ms)
    # find local summit
    best = 0; bv = None
    for _ in range(18):
        r = minimize(lambda v: -(L(v)[0] if L(v) else 0), rng.standard_normal(2*(deg+1)),
                     method='Nelder-Mead', options={'maxiter': 3000, 'fatol': 1e-12})
        if -r.fun > best: best, bv = -r.fun, r.x.copy()
    cmax = best
    out = [f"{name}: c_max~{cmax:.4f} |"]
    for frac in [0.90, 0.95, 0.975]:
        thr = frac*cmax; worst = 1e9
        for _ in range(16):
            r = minimize(lambda v: (lambda q: (q[1] + 100*max(0, thr - q[0])**2) if q else 1e6)(L(v)),
                         bv + 0.3*rng.standard_normal(bv.shape), method='Nelder-Mead',
                         options={'maxiter': 3000, 'fatol': 1e-13})
            q = L(r.x)
            if q and q[0] >= thr and q[1] < worst: worst = q[1]
        out.append(f"I_min(c>={frac:.3f}c_max)={worst:+.2e}")
    print("  " + "  ".join(out))

# ---------- Part 2: climbing heals (exact disk, J3) ----------
print("== P8: climbing test (exact disk J3): ascend c from crease starts, track I ==")
A = np.zeros((3,3), complex); A[0,1]=A[1,2]=1.0; r3 = np.cos(np.pi/4); deg = 8
def Ld(v):
    q = ledger_disk(A, r3, v[:deg+1] + 1j*v[deg+1:])
    return q if q else (0, 0)
# find crease starts (c>=1.85, I<0)
starts = []
for _ in range(40):
    rr = minimize(lambda v: (lambda q: q[1] + 100*max(0, 1.85 - q[0])**2)(Ld(v)),
                  rng.standard_normal(2*(deg+1)), method='Nelder-Mead',
                  options={'maxiter': 4000, 'fatol': 1e-14})
    c, Iv = Ld(rr.x)
    if c >= 1.85 and Iv < -1e-5: starts.append((Iv, c, rr.x.copy()))
starts.sort(); starts = starts[:3]
for k, (I0, c0, v0) in enumerate(starts):
    traj = []
    def cb(vk): traj.append(Ld(vk))
    minimize(lambda v: -Ld(v)[0], v0, method='Nelder-Mead', callback=cb,
             options={'maxiter': 6000, 'fatol': 1e-14})
    cs = np.array([t[0] for t in traj]); Is = np.array([t[1] for t in traj])
    crossed = np.argmax(Is >= 0) if (Is >= 0).any() else -1
    cfin, Ifin = cs[-1], Is[-1]
    if crossed >= 0:
        print(f"  start {k}: (c={c0:.4f}, I={I0:+.2e}) -> I crosses >=0 at c={cs[crossed]:.4f} -> ends (c={cfin:.4f}, I={Ifin:+.2e})")
    else:
        print(f"  start {k}: (c={c0:.4f}, I={I0:+.2e}) -> I NEVER crosses; ends (c={cfin:.4f}, I={Ifin:+.2e})  [CREASE CARRIED]")
