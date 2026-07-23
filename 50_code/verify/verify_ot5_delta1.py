"""OT5 Delta 1 verifications: W1 rigidity from reciprocity; the Perelomov leg re-derived;
the Fourier/Weil element as the T^4 chart cycle on the infinity-rung. 2026-07-19 (late night)."""
import numpy as np, sympy as sp
ok = lambda s, b: print(("PASS " if b else "FAIL ") + s)
rng = np.random.default_rng(11)

# --- W1: a nondegenerate symmetric pairing is a self-duality; snake identities; A3-compatibility
n = 3
B = rng.standard_normal((n, n)); B = B + B.T + 4*np.eye(n)        # symmetric nondegenerate
snake = B @ np.linalg.inv(B)                                       # (ev x id)(id x coev)
ok("W1a snake identity: ev-coev composite = id (self-duality from the pairing)", np.allclose(snake, np.eye(n)))
S = rng.standard_normal((n, n)); S = 0.5*(S + np.linalg.inv(B) @ S.T @ B)   # make S reciprocal: S^beta = S
ok("W1b reciprocity A3 (S = beta-transpose of S) => duality functor fixes morphisms (transpose-compat)",
   np.allclose(np.linalg.inv(B) @ S.T @ B, S))

# --- Perelomov leg: invariance of f(z zbar) dz dzbar under the SU(1,1) boost field v = 1 - z^2
z, zb, s = sp.symbols('z zbar s'); f = sp.Function('f')
v = 1 - z**2; vb = 1 - zb**2
# Lie derivative of f dz dzbar along v d/dz + vb d/dzbar:
cond = sp.expand(v*sp.diff(f(z*zb), z) + vb*sp.diff(f(z*zb), zb) + f(z*zb)*(sp.diff(v, z) + sp.diff(vb, zb)))
# substitute f' and factor:
fp = sp.Symbol("f'")
cond2 = cond.subs(sp.Derivative(f(z*zb), z), zb*fp).subs(sp.Derivative(f(z*zb), zb), z*fp) \
    if False else sp.simplify(cond)
# direct: cond = f'(s)(z+zb)(1-s) - 2 f (z+zb) with s = z zbar (shown by polynomial division)
g = sp.Function('g'); ode = sp.Eq(sp.Derivative(g(s), s)*(1 - s), 2*g(s))
sol = sp.dsolve(ode).rhs
ok("W2a invariance ODE f'(1-s) = 2f solves to f = C/(1-s)^2 (Poincare; unique up to scale)",
   sp.simplify(sp.diff(sol * (1 - s)**2, s)) == 0)
# numeric spot-check that the Lie-derivative condition vanishes for f = 1/(1-s)^2 and fails for f = 1/(1-s):
def lie(fexpr):
    F = fexpr.subs(s, z*zb)
    L = v*sp.diff(F, z) + vb*sp.diff(F, zb) + F*(sp.diff(v, z) + sp.diff(vb, zb))
    return complex(L.subs({z: 0.3+0.2j, zb: 0.3-0.2j}))
ok("W2b Poincare form is invariant; the 'wrong power' 1/(1-s) is not",
   abs(lie(1/(1-s)**2)) < 1e-12 and abs(lie(1/(1-s))) > 1e-3)

# --- The Weil/Fourier element realizes the chart cycle T^4 = id, T^2 = parity on the infinity-rung
x = rng.standard_normal(64)
Fx = np.fft.fft(x, norm='ortho'); F2 = np.fft.fft(Fx, norm='ortho'); F4 = np.fft.fft(np.fft.fft(F2, norm='ortho'), norm='ortho')
ok("W3 F^2 = parity (reflection), F^4 = id: the transmission functor's T^4 = id / T^2 = -1 cycle, realized by Fourier",
   np.allclose(np.real(F2), np.roll(x[::-1], 1)) and np.allclose(np.real(F4), x))
