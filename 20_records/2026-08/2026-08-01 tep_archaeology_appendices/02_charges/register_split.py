"""Register-split theorems: eigenreduction of the crease functional + tests.
2026-08-09, seed 20260809. Stated-before-run block (see PREDICTIONS below).
[Delivered with crease_functionals_eigenreduction_and_the_5_27_theorem_DraftV1_20260809.md;
 speed-patched parameters (restarts/maxiter/ensemble sizes) as run are reflected below.]

Objects (Delta 5 / Addendum 2 conventions, disk domain, z0 = 0):
  f = finite Blaschke product, deg <= 3:  f(z) = prod (z-a_j)/(1-conj(a_j) z)
  I(f,x) = Re[ conj(f(0)) <f(A)x, x> ],  unit x
  T1 claim: min_x I(f,x) = lambda_min(H_f),  H_f = (conj(f0) fA + f0 fA*)/2
  m = |<f(A)x,x>| / ||f(A)x||  ; cosD = cos(arg<fAx,x> - arg f0)
  t = ||f(A)x||/2, rho = |f0|/2, k = m cosD, xp2 = t^2+rho^2+2 t rho k

NOTE (post-run, load-bearing): this script computes the STATE-WORST functional
min_x I(f,x). The corpus's Delta 5 / Addendum 2 / P-R functional evaluates I at
the EXTREMAL vector x_top(f). The two differ; J2 separates them (see record §0/§3).

PREDICTIONS (written before any run of sections C/D):
  P-a  Zero violations of cosD = -1 (tol 1e-3) at crease optima (I < -1e-8),
       across all ensembles, both registers.  [tests D-1 forcing]
  P-b  m = 1 to 1e-10 at optima for normal A; m < 0.999 at optima for the
       scaled-Jordan family.  [T2 corollaries]
  P-c  Mixed-summand family A(s) = diag(N_norm, J3(s)): the global crease
       minimum sits in the normal block for small s and in the Jordan block
       for large s; m(s) jumps discontinuously ~1 -> ~m_J at a crossing s*
       while I_min(s) is continuous (kink only).  [T2 mixed consequence]
Kill: any counterexample is reported as such, full row printed.
"""
import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(20260809)

def blaschke_mat(A, zeros):
    n = A.shape[0]; F = np.eye(n, dtype=complex)
    for a in zeros:
        F = F @ (A - a*np.eye(n)) @ np.linalg.inv(np.eye(n) - np.conj(a)*A)
    return F
def f0_of(zeros):
    v = 1.0+0j
    for a in zeros: v *= (-a)
    return v
def Hf(A, zeros):
    F = blaschke_mat(A, zeros); f0 = f0_of(zeros)
    return 0.5*(np.conj(f0)*F + f0*F.conj().T), F, f0
def Imin_and_data(A, zeros):
    H, F, f0 = Hf(A, zeros)
    w, V = np.linalg.eigh(H)
    x = V[:, 0]; Imin = w[0]
    Fx = F @ x; nFx = np.linalg.norm(Fx)
    ip = np.vdot(x, Fx)          # <f(A)x, x> = x* F x
    m = abs(ip)/nFx if nFx > 1e-300 else np.nan
    cosD = np.cos(np.angle(ip) - np.angle(f0)) if abs(f0) > 0 and abs(ip) > 0 else np.nan
    return Imin, m, cosD, x, F, f0, nFx
def param_to_zeros(u, deg):
    z = []
    for j in range(deg):
        w = u[2*j] + 1j*u[2*j+1]
        z.append(w/(1.0+abs(w)))     # open-disk embedding
    return z
def deepest_crease(A, deg=3, restarts=10):
    best = None
    for _ in range(restarts):
        u0 = rng.normal(0, 1.2, size=2*deg)
        res = minimize(lambda u: Imin_and_data(A, param_to_zeros(u, deg))[0],
                       u0, method='Nelder-Mead',
                       options=dict(maxiter=350, xatol=1e-10, fatol=1e-12))
        if best is None or res.fun < best.fun: best = res
    zeros = param_to_zeros(best.x, deg)
    return zeros, Imin_and_data(A, zeros)

def J(n, s=None):
    s = 1/np.cos(np.pi/(n+1)) if s is None else s
    M = np.zeros((n, n), dtype=complex)
    for i in range(n-1): M[i, i+1] = s
    return M
def upper2(l1, l2, g):
    return np.array([[l1, g], [0, l2]], dtype=complex)

# ---------- A. identity checks (T1 anchor) ----------
print("== A. T1 identity: I(f,x) = <H_f x, x>; min_x I = lambda_min(H_f) ==")
worst = 0.0; worst_rq = 0.0
for _ in range(100):
    n = rng.integers(2, 6)
    A = rng.normal(0, .4, (n, n)) + 1j*rng.normal(0, .4, (n, n))
    A /= (1.3*np.linalg.norm(A, 2))
    zeros = [ (rng.normal(0,.5)+1j*rng.normal(0,.5)) for _ in range(3) ]
    zeros = [ z/(1+abs(z)) for z in zeros ]
    H, F, f0 = Hf(A, zeros)
    x = rng.normal(0,1,n) + 1j*rng.normal(0,1,n); x /= np.linalg.norm(x)
    I_direct = np.real(np.conj(f0)*np.vdot(x, F@x))
    I_quad = np.real(np.vdot(x, H@x))
    worst = max(worst, abs(I_direct - I_quad))
    w = np.linalg.eigvalsh(H)
    worst_rq = max(worst_rq, max(0.0, w[0] - I_quad))   # lambda_min <= any Rayleigh
print(f"max |I_direct - <Hx,x>| over random (A,f,x): {worst:.3e}")
print(f"max (lambda_min - Rayleigh) violation: {worst_rq:.3e}  (should be <=0 up to eps)")

# ---------- B. the seven test matrices (STATE-WORST optima; not Addendum 2's numbers) ----------
print("\n== B. state-worst optima on the Addendum 2 matrix set ==")
anchors = [
    ("J2", J(2)), ("J3", J(3)), ("J4", J(4)),
    ("2x2(0.6,-0.6,g=0.5)", upper2(0.6, -0.6, 0.5)),
    ("2x2(0.3,-0.7,g=0.9)", upper2(0.3, -0.7, 0.9)),
    ("normal diag(0.7,0.2)", np.diag([0.7, 0.2]).astype(complex)),
    ("normal diag(0.95,0)",  np.diag([0.95, 0.0]).astype(complex)),
]
print(f"{'matrix':24s} {'I_min':>12s} {'m':>8s} {'cosD':>8s} {'t':>7s} {'rho':>7s} {'x_p':>7s}")
for name, A in anchors:
    zeros, (Imin, m, cosD, x, F, f0, nFx) = deepest_crease(A)
    t = nFx/2; rho = abs(f0)/2; k = (m*cosD) if np.isfinite(m) else np.nan
    xp = np.sqrt(max(0.0, t*t + rho*rho + 2*t*rho*k))
    print(f"{name:24s} {Imin:12.6e} {m:8.4f} {cosD:8.4f} {t:7.4f} {rho:7.4f} {xp:7.4f}")

# ---------- C. T2 + cosD ensemble sweep ----------
print("\n== C. ensemble sweep: m and cosD at crease optima ==")
viol_cos, viol_m_norm, viol_m_jordan, n_crease = 0, 0, 0, 0
worst_cos, worst_m_norm, best_m_jordan = 1.0, 1.0, 0.0
def rand_normal_mat(n):
    d = (rng.uniform(0.2, 0.95, n))*np.exp(1j*rng.uniform(0, 2*np.pi, n))
    Q = np.linalg.qr(rng.normal(0,1,(n,n)) + 1j*rng.normal(0,1,(n,n)))[0]
    return Q @ np.diag(d) @ Q.conj().T
ens = [("normal", rand_normal_mat(int(rng.integers(2,5)))) for _ in range(14)]
ens += [("jordan", J(int(rng.integers(3,6)))) for _ in range(6)]
ens += [("uptri", np.triu(rng.normal(0,.4,(3,3)) + 1j*rng.normal(0,.4,(3,3)), 1)
                 + np.diag(rng.uniform(-.6,.6,3))) for _ in range(10)]
for kind, A in ens:
    if np.linalg.norm(A,2) > 1.6: A = A/ (1.1*np.linalg.norm(A,2))
    zeros, (Imin, m, cosD, x, F, f0, nFx) = deepest_crease(A, restarts=6)
    if Imin < -1e-8:
        n_crease += 1
        if cosD > -1 + 1e-3: viol_cos += 1; print("  cosD VIOLATION:", kind, Imin, m, cosD)
        worst_cos = min(worst_cos, -cosD)
        if kind == "normal":
            worst_m_norm = min(worst_m_norm, m)
            if abs(m-1) > 1e-8: viol_m_norm += 1; print("  m NORMAL VIOLATION:", m)
        if kind == "jordan":
            best_m_jordan = max(best_m_jordan, m)
            if m > 0.999: viol_m_jordan += 1; print("  m JORDAN VIOLATION:", m)
print(f"creases: {n_crease} | cosD violations: {viol_cos} (max dev: {1-worst_cos:.2e})")
print(f"normal-register m: violations {viol_m_norm}, worst m = {worst_m_norm:.12f}")
print(f"jordan m: violations {viol_m_jordan}, max m = {best_m_jordan:.6f}")

# ---------- D. mixed-summand switching (P-c) ----------
print("\n== D. mixed-summand register switching: A(s) = diag(normal, J3 scaled by s) ==")
Dn = np.diag([0.7, 0.2]).astype(complex)
print(f"{'s':>5s} {'I_min':>12s} {'m':>8s} {'block':>7s}")
prev_block = None; jumps = []
for s in np.linspace(0.2, 1.4, 9):
    A = np.zeros((5,5), dtype=complex); A[:2,:2] = Dn; A[2:,2:] = J(3)*s/ (1/np.cos(np.pi/4))
    zeros, (Imin, m, cosD, x, F, f0, nFx) = deepest_crease(A, restarts=8)
    wt_norm = np.linalg.norm(x[:2])**2
    block = "NORM" if wt_norm > 0.5 else "JORD"
    if prev_block and block != prev_block: jumps.append(s)
    prev_block = block
    print(f"{s:5.2f} {Imin:12.6e} {m:8.5f} {block:>7s}")
print("register switch(es) near s =", jumps if jumps else "NONE (P-c fails)")

# ---------- E. T2 reducing-eigenvector check ----------
print("\n== E. T2: |m-1| vs reducing residual ||F*x - conj(mu) x|| ==")
for name, A in anchors:
    zeros, (Imin, m, cosD, x, F, f0, nFx) = deepest_crease(A, restarts=6)
    mu = np.vdot(x, F@x)
    red = np.linalg.norm(F.conj().T @ x - np.conj(mu)*x)
    print(f"{name:24s} |m-1| = {abs(m-1):.3e}   reducing residual = {red:.3e}")

# ---------- F. T3 exact witness (added post-derivation) ----------
print("\n== F. T3: Mobius a=1/3 on J2: exact -5/27; extremal functional contrast ==")
a = 1/3; f0 = -a; fp = 1 - a*a
A = np.array([[0,2],[0,0]], dtype=complex)
F = f0*np.eye(2) + fp*A
ph = -np.angle(np.conj(f0)*fp) + np.pi
x = np.array([1/np.sqrt(2), np.exp(1j*ph)/np.sqrt(2)])
print("I(state-worst witness) =", np.real(np.conj(f0)*np.vdot(x, F@x)), " vs -5/27 =", -5/27)
H = 0.5*(np.conj(f0)*F + f0*F.conj().T)
print("lambda_min(H_f) =", np.linalg.eigvalsh(H)[0])
U,S,Vh = np.linalg.svd(F); xt = Vh[0].conj()
print("I_ext (same f, extremal vector) =", np.real(np.conj(f0)*np.vdot(xt, F@xt)), " (>= 0 per Delta 5 §2)")
