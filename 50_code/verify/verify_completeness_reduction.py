"""Verification base for the completeness-reduction theorem attempt. 2026-07-19/20.
Finite probability space (n=7), exact rational-free float checks at 1e-12.
Objects:
  - passive interface: row-stochastic M (positive, unital M1=1) with stationary state p (p^T M = p^T)
  - complete interface: conditional expectation E[.|B] onto a partition B (p-weighted)
Claims:
  T-A budget: Var(TY) + u_T(Y) = Var(Y) for ALL stationary passive T, u_T(Y) := E_p[T(Y^2) - (TY)^2] >= 0
  T-B chain rule (ledger): u_{Psi.Phi}(Y) = u_Phi(Y) + u_Psi(Phi Y)   [exact, all passive]
  T-C monotonicity: Var((Psi.Phi)Y) <= Var(Phi Y) <= Var(Y)          [all passive]
  T-D completeness surplus: u_T = E[(Y-TY)^2] (u is the honest MSE of the record) iff T is the CE
      (self-adjoint idempotent); generic stationary T has u != MSE.
  T-E tower/waste for CEs: u(B1) - u(B2) = ||R2 Y - R1 Y||^2 for B1 <= B2 (refinement); spend telescopes.
  T-F budget FAILS for a non-stationary idempotent (wrong-weight averaging): passivity is load-bearing.
"""
import numpy as np
rng = np.random.default_rng(20260719)
n = 7
def rand_stochastic():
    M = rng.random((n, n)) + 0.1
    return M / M.sum(1, keepdims=True)
def stationary(M):
    w, v = np.linalg.eig(M.T)
    i = np.argmin(np.abs(w - 1)); p = np.real(v[:, i]); p = np.abs(p); return p / p.sum()
E = lambda p, f: float(p @ f)
Var = lambda p, f: E(p, f**2) - E(p, f)**2
ok = lambda s, b: print(("PASS " if b else "FAIL ") + s)

M = rand_stochastic(); p = stationary(M)
Y = rng.standard_normal(n) * 2 + 1
TY = M @ Y; uT = E(p, M @ (Y**2) - TY**2)
ok("T-A budget exact for generic stationary passive map; u >= 0",
   abs(Var(p, TY) + uT - Var(p, Y)) < 1e-12 and uT >= -1e-14)

# second passive map sharing the same stationary state: mixture of M-powers and CEs w.r.t p
def ce_matrix(partition, p):
    T = np.zeros((n, n))
    for block in partition:
        w = p[block] / p[block].sum()
        for i in block: T[i, block] = w
    return T
B2 = [np.array([0,1]), np.array([2,3]), np.array([4,5,6])]          # finer
B1 = [np.array([0,1,2,3]), np.array([4,5,6])]                      # coarser
P2, P1 = ce_matrix(B2, p), ce_matrix(B1, p)
Psi = 0.3*np.linalg.matrix_power(M, 2) + 0.45*P2 + 0.25*P1          # stationary for p, passive
ok("   (sanity) Psi stationary & unital", np.allclose(p @ Psi, p) and np.allclose(Psi @ np.ones(n), 1))
lhs = E(p, (Psi @ M) @ (Y**2) - ((Psi @ M) @ Y)**2)
rhs = uT + E(p, Psi @ (TY**2) - (Psi @ TY)**2)
ok("T-B ledger chain rule u_{PsiPhi} = u_Phi + u_Psi(Phi Y), exact", abs(lhs - rhs) < 1e-12)
ok("T-C monotonicity Var((PsiPhi)Y) <= Var(Phi Y) <= Var(Y)",
   Var(p, (Psi @ M) @ Y) <= Var(p, TY) + 1e-12 and Var(p, TY) <= Var(p, Y) + 1e-12)

# T-D: completeness surplus
R2Y = P2 @ Y; u_ce = E(p, P2 @ (Y**2) - R2Y**2); mse_ce = E(p, (Y - R2Y)**2)
u_gen = uT; mse_gen = E(p, (Y - TY)**2)
D = np.diag(p)
ok("T-D1 CE: u = MSE of the record exactly; and CE is p-self-adjoint & idempotent",
   abs(u_ce - mse_ce) < 1e-12 and np.allclose(D @ P2, (D @ P2).T) and np.allclose(P2 @ P2, P2))
ok("T-D2 generic passive T: budget holds but u != MSE (readability fails)",
   abs(u_gen - mse_gen) > 1e-3)
# T-E tower/waste
R1Y = P1 @ Y
u1 = E(p, P1 @ (Y**2) - R1Y**2); u2 = u_ce
ok("T-E waste identity u(B1) - u(B2) = ||R2Y - R1Y||^2_p (refinement)",
   abs((u1 - u2) - E(p, (R2Y - R1Y)**2)) < 1e-12)
ok("   spend telescopes: Var(R1Y) + ||R2Y-R1Y||^2 = Var(R2Y)",
   abs(Var(p, R1Y) + E(p, (R2Y - R1Y)**2) - Var(p, R2Y)) < 1e-12)
# T-F: idempotent positive unital but NON-stationary (wrong weights) -> budget fails
q = rng.random(n); q = q / q.sum()   # wrong state
Pq = ce_matrix(B2, q)                 # idempotent, unital, positive, but p^T Pq != p^T
TqY = Pq @ Y; u_q = E(p, Pq @ (Y**2) - TqY**2)
ok("T-F budget FAILS for non-stationary idempotent (wrong-weight CE): passivity is the load-bearing generic input",
   abs(Var(p, TqY) + u_q - Var(p, Y)) > 1e-3 and np.allclose(Pq @ Pq, Pq))
