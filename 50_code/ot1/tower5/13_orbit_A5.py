#!/usr/bin/env python3
"""
TOWER5 - script 13 (v2): icosahedral A5 on the X(5) hauptmodul r, from the two
VERIFIED generators: S: r->zeta5 r, V: r->(1-phi r)/(phi+r).
Group build at dps=50 with distance-based projective dedupe; validation
(order 60, order profile, j-invariance); five V4 -> five A4; right cosets;
five coset-invariant values at r(tau_pm) computed at dps=100.
Compute-then-grade.
"""
import mpmath as mp
import sys, itertools, pickle
sys.path.insert(0, "/home/claude/tower5")

# ---------- phase 1: structure at dps=50 ----------
mp.mp.dps = 50
I = mp.mpc(0, 1)
phi = (1 + mp.sqrt(5))/2
z5 = mp.e**(2*mp.pi*I/5)
z10 = mp.e**(2*mp.pi*I/10)

def make_gens():
    S = mp.matrix([[z10, 0], [0, 1/z10]])
    nv = 1/(I*mp.sqrt(mp.sqrt(5)*phi))
    V = mp.matrix([[-phi*nv, nv], [nv, phi*nv]])
    return S, V

S, V = make_gens()

def mmul(A, B):
    return mp.matrix([[A[0,0]*B[0,0]+A[0,1]*B[1,0], A[0,0]*B[0,1]+A[0,1]*B[1,1]],
                      [A[1,0]*B[0,0]+A[1,1]*B[1,0], A[1,0]*B[0,1]+A[1,1]*B[1,1]]])

def pdist(A, B):
    """projective distance: min over sign lambda with det-1 matrices: A ~ -A."""
    d1 = max(abs(A[i,j]-B[i,j]) for i in range(2) for j in range(2))
    d2 = max(abs(A[i,j]+B[i,j]) for i in range(2) for j in range(2))
    return min(d1, d2)

TOL = mp.mpf(10)**-25

def find(lst, M):
    for idx, N in enumerate(lst):
        if pdist(N, M) < TOL:
            return idx
    return -1

# BFS
G = [mp.eye(2)]
frontier = [mp.eye(2)]
rounds = 0
while frontier and len(G) < 200:
    rounds += 1
    newf = []
    for M in frontier:
        for g in (S, V):
            P = mmul(M, g)
            if find(G, P) < 0:
                G.append(P)
                newf.append(P)
    frontier = newf
print("group order (projective) =", len(G), " after", rounds, "BFS rounds (expect 60)")

def proj_order(M):
    P = M
    for n in range(1, 11):
        if pdist(P, mp.eye(2)) < TOL:
            return n
        P = mmul(P, M)
    return None

orders = {}
elt_order = []
for M in G:
    o = proj_order(M)
    elt_order.append(o)
    orders[o] = orders.get(o, 0) + 1
print("order profile:", dict(sorted(orders.items(), key=lambda kv: (kv[0] or 99))), " (expect {1:1,2:15,3:20,5:24})")

def mobius(M, z):
    den = M[1,0]*z + M[1,1]
    return (M[0,0]*z + M[0,1])/den

def j_icos(r):
    num = r**20 - 228*r**15 + 494*r**10 + 228*r**5 + 1
    den = r**5*(r**10 + 11*r**5 - 1)**5
    return -num**3/den

zt = mp.mpc('0.3123', '0.1618')
base = j_icos(zt)
worst = max(abs(j_icos(mobius(M, zt)) - base)/abs(base) for M in G[::7])
print("j-invariance spot check, worst rel dev =", mp.nstr(worst, 4))

# involutions -> V4 -> A4
inv_idx = [i for i, o in enumerate(elt_order) if o == 2]
print("#involutions =", len(inv_idx))
v4s = []
seen_trips = []
for a, b in itertools.combinations(inv_idx, 2):
    AB = mmul(G[a], G[b])
    BA = mmul(G[b], G[a])
    if pdist(AB, BA) < TOL:
        c = find(G, AB)
        trip = tuple(sorted([a, b, c]))
        if trip not in seen_trips:
            seen_trips.append(trip)
            v4s.append(trip)
print("#V4 subgroups =", len(v4s), " (expect 5)")

def minv(M):
    return mp.matrix([[M[1,1], -M[0,1]], [-M[1,0], M[0,0]]])

a4s = []
for trip in v4s:
    members = []
    v4mats = [G[i] for i in trip]
    for idx, M in enumerate(G):
        Mi = minv(M)
        ok = True
        for W in v4mats:
            C = mmul(mmul(M, W), Mi)
            ci = find(G, C)
            if ci not in trip:
                ok = False
                break
        if ok:
            members.append(idx)
    a4s.append(members)
print("A4 sizes:", [len(a) for a in a4s], " (expect all 12)")

A4_idx = a4s[0]
# right cosets A4*g
reps = []
covered = set()
for gidx, M in enumerate(G):
    if gidx in covered:
        continue
    reps.append(gidx)
    for h in A4_idx:
        P = mmul(G[h], M)
        pi = find(G, P)
        covered.add(pi)
print("#right cosets =", len(reps), " (expect 5)")

# word reconstruction so phase 2 can rebuild matrices at dps=100:
# store each element as its matrix at dps=50 (strings); phase 2 refines by
# re-BFS'ing words. Simpler: store WORDS via BFS bookkeeping - redo BFS with words.
G2 = [mp.eye(2)]
words = [""]
frontier = [(mp.eye(2), "")]
while frontier:
    newf = []
    for M, w in frontier:
        for g, gl in ((S, "S"), (V, "V")):
            P = mmul(M, g)
            if find(G2, P) < 0:
                G2.append(P)
                words.append(w + gl)
                newf.append((P, w + gl))
    frontier = newf
# map G indices to words
word_of = []
for M in G:
    i2 = find(G2, M)
    word_of.append(words[i2])
print("word table built; longest word:", max(len(w) for w in word_of))

with open("/home/claude/tower5/orbit_words.pkl", "wb") as f:
    pickle.dump({"words": word_of, "A4_idx": A4_idx, "reps_idx": reps,
                 "v4s": v4s, "elt_order": elt_order}, f)

# ---------- phase 2: coset values at dps=100 ----------
mp.mp.dps = 100
I = mp.mpc(0, 1)
phi = (1 + mp.sqrt(5))/2
z10 = mp.e**(2*mp.pi*I/10)
S, V = make_gens()

def word_mat(w):
    M = mp.eye(2)
    for ch in w:
        M = mmul(M, S if ch == "S" else V)
    return M

A4_mats = [word_mat(word_of[i]) for i in A4_idx]
rep_mats = [word_mat(word_of[i]) for i in reps]

from tower5_rr import r0_p, r0_m

def coset_values(r0, seed):
    vals = []
    for R in rep_mats:
        z = mobius(R, r0)
        s = mp.mpc(0)
        for H in A4_mats:
            s += seed(mobius(H, z))
        vals.append(s)
    return vals

def esym(vals):
    es = [mp.mpc(1)]
    for v in vals:
        new = [mp.mpc(1)]
        for k in range(1, len(es)+1):
            prev = es[k] if k < len(es) else mp.mpc(0)
            new.append(prev + v*es[k-1])
        es = new
    return es[1:]

for name, r0 in [("+", r0_p), ("-", r0_m)]:
    print(f"\n===== branch ({name}), r0 = {mp.nstr(r0, 30)} =====")
    vals = coset_values(r0, lambda w: w)
    dmin = min(abs(vals[a]-vals[b]) for a in range(5) for b in range(a+1, 5))
    print(f" seed z: five right-coset values (min pairwise |diff| = {mp.nstr(dmin, 4)}):")
    for v in vals:
        print("    u =", mp.nstr(v, 45))
    es = esym(vals)
    for i, e in enumerate(es):
        print(f"    e{i+1} =", mp.nstr(e, 50))
    with open(f"/home/claude/tower5/uvals_{'p' if name=='+' else 'm'}.txt", "w") as f:
        for v in vals:
            f.write(mp.nstr(mp.re(v), 95) + " " + mp.nstr(mp.im(v), 95) + "\n")

print("\n[saved orbit_words.pkl, uvals_p.txt, uvals_m.txt]")
