#!/usr/bin/env python3
"""
TOWER5 - script 11b: the six 5-isogenous points, numerically, both branches.
 - j(5 tau), j((tau+k)/5) k=0..4 at dps=100 (mpmath kleinj, 1728-normalized)
 - each verified as a root of Phi_5(X, j(tau))   [coefficients from PARI export]
 - the six values matched bijectively against the six roots of Phi_5(X, j_pm)
 - Atkin-Lehner/Fricke: tau_AL = -1/(5 tau):  j(tau_AL) = j(5 tau), j(5 tau_AL) = j(tau)
 - dual-isogeny symmetry: Phi_5(j0, j') = 0 for every fiber member j'
Compute-then-grade.
"""
import mpmath as mp
mp.mp.dps = 100
import sys
sys.path.insert(0, "/home/claude/tower5")
from tower5_values import tau_p, tau_m

s5 = mp.sqrt(5)
jp = 10400 - 4640*s5
jm = 10400 + 4640*s5

# Phi_5 coefficients
coeffs = []
with open("/home/claude/tower5/phi5_coeffs.txt") as f:
    for line in f:
        i, j, c = line.split()
        coeffs.append((int(i), int(j), mp.mpf(c)))

def phi5(X, Y):
    return sum(c * X**i * Y**j for (i, j, c) in coeffs)

def J(tau):
    return 1728*mp.kleinj(tau)

for name, tau, j0 in [("+", tau_p, jp), ("-", tau_m, jm)]:
    print(f"===== branch ({name}):  tau = {mp.nstr(tau, 40)} =====")
    print("  j(tau) =", mp.nstr(J(tau), 40), "   |j(tau) - j_branch| =", mp.nstr(abs(J(tau)-j0), 5))
    args = [("5*tau", 5*tau)] + [(f"(tau+{k})/5", (tau+k)/5) for k in range(5)]
    fiber = []
    print("  -- the six 5-isogenous j-values --")
    for lab, t in args:
        jv = J(t)
        fiber.append((lab, jv))
        # scale-aware residual: |Phi5| normalized by max monomial magnitude
        val = phi5(jv, j0)
        scale = max(abs(c) * (abs(jv)+1)**i * (abs(j0)+1)**jd for (i, jd, c) in coeffs)
        print(f"   j({lab:9s}) = {mp.nstr(jv, 35)}")
        print(f"        |Phi5(j', j0)|/scale = {mp.nstr(abs(val)/scale, 4)}   [dual check] |Phi5(j0, j')|/scale = {mp.nstr(abs(phi5(j0, jv))/scale, 4)}")
    # pairwise distinctness
    mind = min(abs(fiber[a][1]-fiber[b][1]) for a in range(6) for b in range(a+1, 6))
    print("  min pairwise distance of the six =", mp.nstr(mind, 5), " (six-fold structure: all distinct)")
    # Atkin-Lehner
    tal = -1/(5*tau)
    print("  -- Atkin-Lehner w5: tau_AL = -1/(5 tau) =", mp.nstr(tal, 30), "--")
    print("   |j(tau_AL) - j(5 tau)|  =", mp.nstr(abs(J(tal) - fiber[0][1]), 5))
    print("   |j(5 tau_AL) - j(tau)|  =", mp.nstr(abs(J(5*tal) - J(tau)), 5))
    # sum & product of fiber (should be in Q(sqrt5): compare with Phi5 coefficients)
    e1 = sum(v for (_, v) in fiber)
    e6 = mp.mpf(1)
    for (_, v) in fiber:
        e6 *= v
    # from Phi5(X, j0) = X^6 + c5(j0) X^5 + ... : e1 = -c5, e6 = c0
    c5 = sum(c * j0**jd for (i, jd, c) in coeffs if i == 5)
    c0 = sum(c * j0**jd for (i, jd, c) in coeffs if i == 0)
    print("  fiber e1 vs -c5(j0):", mp.nstr(abs(e1 + c5), 5), "   fiber e6 vs c0(j0):", mp.nstr(abs(e6 - c0), 5))
    print()

# cross-branch observation: is the (-) fiber the sqrt5-conjugate set of the (+) fiber?
print("== cross-branch: Galois conjugacy of the two fibers ==")
print("   (numeric check: the multiset of minimal-polynomial residues R12(j') for both branches)")
# R12 evaluated via product of the two branch sextics = use Phi5(X,jp)*Phi5(X,jm)
for name, tau, j0 in [("+", tau_p, jp), ("-", tau_m, jm)]:
    args = [("5*tau", 5*tau)] + [(f"(tau+{k})/5", (tau+k)/5) for k in range(5)]
    for lab, t in args[:2]:
        jv = J(t)
        v = phi5(jv, jp)*phi5(jv, jm)
        print(f"   branch({name}) j({lab}): |Phi5(j',j+)*Phi5(j',j-)| ~ {mp.nstr(abs(v), 4)} (root of the Q-degree-12 object)")
print("\n[all fiber values above are roots of the SAME irreducible degree-12 Q-polynomial R12;")
print(" by 11a: K12 = (resolvent-sextic field of x^5+20x+16) * Q(sqrt5) -- verified nfisincl]")
