#!/usr/bin/env python3
"""
TOWER5 - script 13b: the u -> Brioschi bridge.
Theory (derived in-session): C(u) = C(x,Z) with x a Brioschi root over Z(j);
[C(u):C(x)] = 2 since Z is a root of the irreducible quadratic
Z^2(45x-1) - 10x^3 Z + x^5 (discriminant x^5(4-80x), not a square)
=> x = (a u^2 + b u + c)/(d u^2 + e u + f) for constants (per fiber) a..f.
Procedure: for each of the 120 pairings of the five u-values with the five
Brioschi roots, solve the 5x6 homogeneous system; emit normalized coefficient
vectors for PARI lindep identification over Q(zeta20) (basis 1..zeta20^7).
Also: universality check of the resolvent u^5+30u^3+100u^2+105u+36+j at a random tau.
"""
import mpmath as mp
mp.mp.dps = 100
import sys, itertools
sys.path.insert(0, "/home/claude/tower5")
from tower5_values import bri_p, bri_m, tau_p, tau_m

def load_u(tag):
    vals = []
    with open(f"/home/claude/tower5/uvals_{tag}.txt") as f:
        for line in f:
            a, b = line.split()
            vals.append(mp.mpc(mp.mpf(a), mp.mpf(b)))
    return vals

u_p = load_u("p"); u_m = load_u("m")

# --- universality check of the resolvent at random tau (independent of branches) ---
import pickle
with open("/home/claude/tower5/orbit_words.pkl", "rb") as f:
    OD = pickle.load(f)
I = mp.mpc(0, 1)
phi = (1 + mp.sqrt(5))/2
z10 = mp.e**(2*mp.pi*I/10)
S = mp.matrix([[z10, 0], [0, 1/z10]])
nv = 1/(I*mp.sqrt(mp.sqrt(5)*phi))
V = mp.matrix([[-phi*nv, nv], [nv, phi*nv]])
def mmul(A, B):
    return mp.matrix([[A[0,0]*B[0,0]+A[0,1]*B[1,0], A[0,0]*B[0,1]+A[0,1]*B[1,1]],
                      [A[1,0]*B[0,0]+A[1,1]*B[1,0], A[1,0]*B[0,1]+A[1,1]*B[1,1]]])
def word_mat(w):
    M = mp.eye(2)
    for ch in w:
        M = mmul(M, S if ch == "S" else V)
    return M
A4_mats = [word_mat(OD["words"][i]) for i in OD["A4_idx"]]
rep_mats = [word_mat(OD["words"][i]) for i in OD["reps_idx"]]
def mobius(M, z):
    return (M[0,0]*z + M[0,1])/(M[1,0]*z + M[1,1])
def coset_values(r0):
    out = []
    for R in rep_mats:
        z = mobius(R, r0)
        out.append(sum(mobius(H, z) for H in A4_mats))
    return out

def leg5(n):
    m = n % 5
    return 0 if m == 0 else (1 if m in (1, 4) else -1)
def rr(tau):
    q = mp.e**(2*mp.pi*I*tau)
    nmax = int(mp.ceil(mp.mp.dps*mp.log(10)/(2*mp.pi*mp.im(tau)))) + 30
    pr = mp.mpc(1)
    for n in range(1, nmax+1):
        c = leg5(n)
        if c:
            pr *= (1-q**n)**c
    return mp.e**(2*mp.pi*I*tau/5)*pr

tau_r = mp.mpc('0.2718', '1.0281')
r_r = rr(tau_r)
jr = 1728*mp.kleinj(tau_r)
ur = coset_values(r_r)
resid = [u**5 + 30*u**3 + 100*u**2 + 105*u + 36 + jr for u in ur]
print("== universality of the derived resolvent at random tau =", mp.nstr(tau_r, 12), "==")
print("   j(tau_rand) =", mp.nstr(jr, 30))
print("   |u^5+30u^3+100u^2+105u+36+j| for the five coset values:",
      [mp.nstr(abs(x), 4) for x in resid])

# --- pairing fits ---
def fit_pairings(uvals, xroots, tag):
    print(f"\n== branch ({tag}): 120 pairing fits (nullspace of 5x6) ==")
    out = []
    for pi, perm in enumerate(itertools.permutations(range(5))):
        rows = []
        for c in range(5):
            u = uvals[c]; x = xroots[perm[c]]
            rows.append([u*u, u, mp.mpc(1), -x*u*u, -x*u, -x])
        A = mp.matrix(rows)
        # nullspace via SVD (full matrices so the null row is present)
        U, Ssv, Vh = mp.svd_c(A, full_matrices=True)
        null = [mp.conj(Vh[5, k]) for k in range(6)]
        # residual quality
        res = max(abs(sum(A[r, k]*null[k] for k in range(6))) for r in range(5))
        # normalize by the entry of largest modulus
        kmax = max(range(6), key=lambda k: abs(null[k]))
        nv_ = [z/null[kmax] for z in null]
        out.append((perm, nv_, res))
    return out

def emit(cands, tag):
    with open(f"/home/claude/tower5/bridge_cands_{tag}.txt", "w") as f:
        for perm, nv_, res in cands:
            f.write("P " + "".join(str(p) for p in perm) + " " + mp.nstr(res, 4) + "\n")
            for z in nv_:
                f.write(mp.nstr(mp.re(z), 90) + " " + mp.nstr(mp.im(z), 90) + "\n")
    print(f"   wrote bridge_cands_{tag}.txt ({len(cands)} candidates)")

cp = fit_pairings(u_p, bri_p, "+")
cm = fit_pairings(u_m, bri_m, "-")
emit(cp, "p"); emit(cm, "m")
print("\nnullspace residuals max:", mp.nstr(max(c[2] for c in cp+cm), 4))
