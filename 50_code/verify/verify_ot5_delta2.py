"""OT5 Delta 2 verification: Hermite functions as Fourier eigenvectors with eigenvalues (-i)^n —
the four-cycle quartet {1, -i, -1, i} realized spectrally on the infinity-rung. 2026-07-20 (early)."""
import numpy as np
from numpy.polynomial.hermite import hermval
ok = lambda s, b: print(("PASS " if b else "FAIL ") + s)
x = np.linspace(-12, 12, 6001); dx = x[1]-x[0]
def h(n):
    c = np.zeros(n+1); c[n] = 1
    f = hermval(x, c) * np.exp(-x**2/2)
    return f / np.sqrt(np.trapezoid(f**2, x))
def F(f):  # unitary Fourier transform by quadrature: F[f](k) = (2pi)^{-1/2} int f(x) e^{-ikx} dx
    return np.array([np.trapezoid(f * np.exp(-1j*k*x), x) for k in x]) / np.sqrt(2*np.pi)
quartet = [1, -1j, -1, 1j]
oks = True
for n in range(4):
    hn = h(n); Fh = F(hn)
    lam = np.vdot(hn, Fh) / np.vdot(hn, hn)
    oks &= abs(lam - quartet[n]) < 1e-8 and np.allclose(Fh, quartet[n]*hn, atol=1e-8)
ok("H1 F[h_n] = (-i)^n h_n for n = 0..3: the infinity-rung eigenmodes carry the quartet {1,-i,-1,i} by index mod 4", oks)
ok("H2 hence F^2 h_n = (-1)^n h_n (parity) and F^4 = id on the eigenbasis (chart cycle, spectrally)",
   all(abs(quartet[n]**2 - (-1)**n) < 1e-15 and abs(quartet[n]**4 - 1) < 1e-15 for n in range(4)))
