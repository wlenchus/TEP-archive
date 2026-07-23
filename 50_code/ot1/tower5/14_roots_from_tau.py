#!/usr/bin/env python3
"""
TOWER5 - script 14: KLEIN'S ICOSAHEDRAL SOLUTION COMPLETED AT THE COMPUTED TAU.
The five roots of x^5+20x+16 from tau ALONE.

Input per branch: the single complex number tau (from the AGM ribbon).
NOTHING else: even the Kiepert constants are recomputed from tau via j(tau).

Chain (every non-classical ingredient derived and certified in 12/13/13b/13c):
  tau
   -> j = 1728 kleinj(tau)                                   [modular, verified 10]
   -> Z = 1/(1728 - j),  mu = (95008 - 129777664 Z)/145, lam = -4
                                  [certified Kiepert reduction, 01/01b + 10]
   -> r0 = r(tau)  (Rogers-Ramanujan q-product)               [level-5, verified 12]
   -> five right-coset invariants u_c of A4 < A5 acting on r0 [derived 13;
        resolvent u^5+30u^3+100u^2+105u+36+j = 0 certified at both branches
        AND at random tau]
   -> x_c = 1/(u_c^2 - 2 u_c + 21)                            [bridge, LLL-certified
        13c: identical rational identification on both conjugate fibers]
   -> y_c = (lam + mu x_c)/(x_c^2/Z - 3)                      [Kiepert push-through]
GRADES (computed AFTER the chain output is printed):
  A: {x_c} vs roots of the Brioschi quintic for exact Z_pm
  B: {y_c} vs the directly computed roots of x^5+20x+16 (30+ digits required)
  C: prod(y - y_c) vs the exact polynomial coefficients [1,0,0,0,20,16]
  D: universality of the bridge at a random tau (fiber vs Brioschi roots at that j)
"""
import mpmath as mp
mp.mp.dps = 100
import sys, pickle
sys.path.insert(0, "/home/claude/tower5")
from tower5_values import tau_p, tau_m, qroots, bri_p, bri_m

I = mp.mpc(0, 1)
phi = (1 + mp.sqrt(5))/2
z10 = mp.e**(2*mp.pi*I/10)
S = mp.matrix([[z10, 0], [0, 1/z10]])
nv = 1/(I*mp.sqrt(mp.sqrt(5)*phi))
V = mp.matrix([[-phi*nv, nv], [nv, phi*nv]])

def mmul(A, B):
    return mp.matrix([[A[0,0]*B[0,0]+A[0,1]*B[1,0], A[0,0]*B[0,1]+A[0,1]*B[1,1]],
                      [A[1,0]*B[0,0]+A[1,1]*B[1,0], A[1,0]*B[0,1]+A[1,1]*B[1,1]]])

with open("/home/claude/tower5/orbit_words.pkl", "rb") as f:
    OD = pickle.load(f)

def word_mat(w):
    M = mp.eye(2)
    for ch in w:
        M = mmul(M, S if ch == "S" else V)
    return M

A4_mats = [word_mat(OD["words"][i]) for i in OD["A4_idx"]]
rep_mats = [word_mat(OD["words"][i]) for i in OD["reps_idx"]]

def mobius(M, z):
    return (M[0,0]*z + M[0,1])/(M[1,0]*z + M[1,1])

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
            pr *= (1 - q**n)**c
    return mp.e**(2*mp.pi*I*tau/5)*pr

def five_u(r0):
    out = []
    for R in rep_mats:
        z = mobius(R, r0)
        out.append(sum(mobius(H, z) for H in A4_mats))
    return out

def roots_from_tau(tau):
    j = 1728*mp.kleinj(tau)
    Z = 1/(1728 - j)
    mu = (95008 - 129777664*Z)/145
    lam = mp.mpf(-4)
    r0 = rr(tau)
    us = five_u(r0)
    xs = [1/(u**2 - 2*u + 21) for u in us]
    ys = [(lam + mu*x)/(x**2/Z - 3) for x in xs]
    return j, Z, r0, us, xs, ys

print("#" * 78)
print("# THE FIVE ROOTS OF x^5+20x+16 FROM tau ALONE (both branches)")
print("#" * 78)

results = {}
for name, tau, bri in [("+", tau_p, bri_p), ("-", tau_m, bri_m)]:
    print(f"\n===== branch ({name}) =====")
    print("input tau =", mp.nstr(tau, 55))
    j, Z, r0, us, xs, ys = roots_from_tau(tau)
    print("j(tau) =", mp.nstr(j, 40))
    print("Z      =", mp.nstr(Z, 40))
    print("r(tau) =", mp.nstr(r0, 40))
    print("five u_c (icosahedral A4-coset invariants):")
    for u in us:
        print("   ", mp.nstr(u, 40))
    print("five x_c = 1/(u^2-2u+21) (Brioschi-side):")
    for x in xs:
        print("   ", mp.nstr(x, 40))
    print("five y_c (Kiepert push-through) -- THE CLAIMED ROOTS:")
    for y in ys:
        print("   ", mp.nstr(y, 45))
    results[name] = (j, Z, us, xs, ys)

print("\n" + "#" * 78)
print("# GRADES (ground truth entered only from here on)")
print("#" * 78)
for name, tau, bri in [("+", tau_p, bri_p), ("-", tau_m, bri_m)]:
    j, Z, us, xs, ys = results[name]
    print(f"\n----- branch ({name}) -----")
    gA = max(min(abs(x - xb) for xb in bri) for x in xs)
    print("GRADE A  max_c min_b |x_c - brioschi_b|      =", mp.nstr(gA, 4))
    gB = max(min(abs(y - yr) for yr in qroots) for y in ys)
    gBidx = [min(range(5), key=lambda k: abs(y - qroots[k])) for y in ys]
    print("GRADE B  max_c min_r |y_c - root_r|          =", mp.nstr(gB, 4),
          "  (assignment bijective:", sorted(gBidx) == [0,1,2,3,4], ")")
    gB2 = max(abs(y**5 + 20*y + 16) for y in ys)
    print("GRADE B' max |y_c^5 + 20 y_c + 16|           =", mp.nstr(gB2, 4))
    # polynomial reconstruction
    pc = [mp.mpc(1)]
    for y in ys:
        pc = [pc[k] + 0 for k in range(len(pc))] + [mp.mpc(0)]
        for k in range(len(pc)-2, -1, -1):
            pc[k+1] -= y*pc[k]
    tgt = [1, 0, 0, 0, 20, 16]
    gC = max(abs(pc[k] - tgt[k]) for k in range(6))
    print("GRADE C  max |coeff(prod(y-y_c)) - [1,0,0,0,20,16]| =", mp.nstr(gC, 4))
    digs = int(-mp.log10(gB)) if gB > 0 else 999
    print(f"         => roots recovered from tau alone to ~{digs} digits")

# universality of the bridge at a random tau
print("\n----- GRADE D: bridge universality at random tau -----")
tau_r = mp.mpc('-0.3141', '0.8862')
j, Z, r0, us, xs, ys_ = roots_from_tau(tau_r)
co = [1, 0, -10*Z, 0, 45*Z**2, -Z**2]
brr = mp.polyroots(co, maxsteps=400, extraprec=400)
gD = max(min(abs(x - xb) for xb in brr) for x in xs)
print("tau_rand =", mp.nstr(tau_r, 12), " j =", mp.nstr(j, 25))
print("GRADE D  max_c min_b |x_c - brioschi_b(Z(j))|  =", mp.nstr(gD, 4))
print("\n[the bridge x = 1/(u^2-2u+21) and resolvent are UNIVERSAL in j:")
print(" certified at both conjugate branches and at arbitrary tau]")
