#!/usr/bin/env python3
"""alpha-complex control: L(s,eta)^2, eta = quintic character mod 11 (g=2). Theorem-grade, entire,
N = 121, nebentypus eta^2 (order 5, even), complex coefficients and eps. Bar 5e-12.
Also: loud negatives (wrong-N, conj-arm disabled i.e. F instead of conj(F))."""
import numpy as np, sys
sys.path.insert(0, '.')
from instr2 import Arm, sieve, Xof

IND11 = {1:0, 2:1, 3:8, 4:2, 5:4, 6:9, 7:7, 8:3, 9:6, 10:5}
Z5 = np.exp(2j*np.pi/5)
def eta(n):
    r = n % 11
    return None if r == 0 else Z5 ** (IND11[r] % 5)

N = 121.0
arm = Arm(N, 0)
def loc(p):
    e = eta(p)
    if e is None:
        return None
    return np.convolve([1.0, -e], [1.0, -e])
arm.set_a(sieve(arm.X, loc))
r, eps = arm.residual()
x, et, gnew = arm.meter(eps)
print(f"ALPHA-COMPLEX L(eta)^2 (N=121, quintic nebentypus): residual {r:.3e}  eps {eps.real:+.6f}{eps.imag:+.6f}i  meter dev {np.max(np.abs(gnew-2)):.3e}")
# predicted eps from Gauss sum: eps = (tau(eta)/sqrt(11))^2 ... tau(eta) = sum_a eta(a) e(a/11)
tau = sum(eta(a) * np.exp(2j*np.pi*a/11) for a in range(1, 11))
eps_pred = (tau / np.sqrt(11)) ** 2
print(f"  predicted eps (Gauss^2): {eps_pred.real:+.6f}{eps_pred.imag:+.6f}i   |match| = {abs(eps - eps_pred):.2e}")
# negatives
armw = Arm(N*1.05, 0, X=arm.X); armw.set_a(arm.a); rw, _ = armw.residual()
# conj-arm sabotage: residual with F(1/t) - eps t F(t) (no conjugation)
d = arm.Fi - eps * arm.t * arm.F
rnc = float(np.max(np.abs(d))/np.max(np.abs(arm.F)))
print(f"  NEG wrong-N*1.05: {rw:.3e}   NEG no-conjugation arm: {rnc:.3e}")
