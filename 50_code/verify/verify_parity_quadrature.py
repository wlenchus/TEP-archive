"""Verification: parity bits, quadrature, and the chart group. 2026-07-19 (Delta to the
cross-budget/odds-gauge note). Bits on the measure circle M(th) = (cos th, sin th):
side s = sign(sin th) [which pole], face f = sign(cos th) [which sheet].
Settled conventions as in verify_cross_budget_gnew.py.
"""
import sympy as sp, itertools, numpy as np
th, A, e = sp.symbols('theta A eta', real=True)
res = []
def ok(n, b):
    res.append(bool(b)); print(("PASS " if b else "FAIL ") + n)

# W1: the odds gauge is the secant gauge quarter-advanced, halved, squared
Gn = 2/(1-sp.sin(th))
ok("W1a G_new = sec^2(pi/4 + th/2) = csc^2(pi/4 - th/2)",
   sp.simplify(Gn - 1/sp.cos(sp.pi/4 + th/2)**2) == 0 and sp.simplify(Gn - 1/sp.sin(sp.pi/4 - th/2)**2) == 0)
ok("W1b G_new(th) = [G_old((th + pi/2)/2)]^2  (quarter-turn -> halve -> square)",
   sp.simplify(Gn - (1/sp.cos((th+sp.pi/2)/2))**2) == 0)

# W2: quarter-turn acts on the bit pair as zeta -> i*zeta (zeta = f + i s): Z4, nonsplit
okk = True
for t in [0.3, 1.8, 3.5, 5.2]:
    s, f = np.sign(np.sin(t)), np.sign(np.cos(t))
    s2, f2 = np.sign(np.sin(t+np.pi/2)), np.sign(np.cos(t+np.pi/2))
    okk &= np.isclose(complex(f2 + 1j*s2), 1j*complex(f + 1j*s))
ok("W2 quarter-turn: (s,f) -> (f,-s) = multiplication by i on f+is (Z4, nonsplit ext of Z2 by Z2)", okk)

# W3: chart group D4 = <R, S_side>; center; commutator; single-bit flips are mirrors only
R = np.array([[0,-1],[1,0]]); S1 = np.diag([1,-1]); S2 = np.diag([-1,1]); I2 = np.eye(2, dtype=int)
inv = lambda M: np.round(np.linalg.inv(M)).astype(int)
def close(gens):
    G = [I2]; changed = True
    while changed:
        changed = False
        for g in list(G):
            for h in gens:
                x = g@h
                if not any((x==y).all() for y in G): G.append(x); changed = True
    return G
G = close([R, S1])
ok("W3a |<R,S_side>| = 8 (the dihedral chart group D4)", len(G) == 8)
ctr = [g for g in G if all((g@h==h@g).all() for h in G)]
ok("W3b center = {I, -I}: the antipode is the central bit", len(ctr) == 2 and any((g==-I2).all() for g in ctr))
comm = close([a@b@inv(a)@inv(b) for a in G for b in G])
ok("W3c commutator subgroup = {I, R^2 = -I}: the central bit IS the commutator charge",
   len(comm) == 2 and any((g==-I2).all() for g in comm))
ok("W3d S_side * S_face = -I", (S1@S2 == -I2).all())
ok("W3e [R, S_side] = R^2 = -I (quarter-transport vs side-flip fails to commute by exactly the central bit)",
   (R@S1@inv(R)@S1 == -I2).all())
ok("W3f R S_side R^-1 = S_face (the two involution instruments are one instrument carried 90 deg)",
   (R@S1@inv(R) == S2).all())
ok("W3g abelianization conflates the two flips: S_side*S_face lies in [G,G] "
   "(abelian shadow sees THAT a parity flipped, not WHICH)",
   any((S1@S2==g).all() for g in comm))
# Bit-action classification: which elements act as a UNIFORM single-bit flip?
def bit_action(M):
    acts = set()
    for t in [0.3, 2.0, 3.6, 5.3]:
        P = np.array([np.cos(t), np.sin(t)]); Q = M@P
        acts.add((int(np.sign(P[1])*np.sign(Q[1])), int(np.sign(P[0])*np.sign(Q[0]))))
    return acts  # {(±1 side kept/flipped, ±1 face kept/flipped)} — singleton iff diagonal action
diag_flip_side = [g for g in G if bit_action(g)=={(-1,1)}]
diag_flip_face = [g for g in G if bit_action(g)=={(1,-1)}]
rot_uniform = [np.linalg.matrix_power(R,k) for k in range(4) if len(bit_action(np.linalg.matrix_power(R,k)))==1]
ok("W3h uniform side-flip = {S_side} and uniform face-flip = {S_face} ONLY (mirrors); "
   "rotations R, R^3 act pointwise-one-bit but non-uniformly (quadrant-dependent) — not single-parity operators",
   [ (g==S1).all() for g in diag_flip_side ] == [True] and [ (g==S2).all() for g in diag_flip_face ] == [True]
   and len(rot_uniform) == 2)  # only I (both kept) and R^2 (both flipped) act uniformly among rotations

# W4: the extension is the F2-Heisenberg (extraspecial +type), not Q8
els = [np.array([[1,a,c],[0,1,b],[0,0,1]]) for a,b,c in itertools.product([0,1],repeat=3)]
def order(M):
    X = M.copy(); k = 1
    while not ((X - np.eye(3)) % 2 == 0).all():
        X = (X@M) % 2; k += 1
    return k
ok("W4 UT(3,F2) order profile {1, 2^5, 4^2} = D4's (Q8: {1, 2^1, 4^6}) — the chart realizes the +type/Heisenberg germ",
   sorted(order(M) for M in els) == [1,2,2,2,2,2,4,4])

# W5: chord amplitudes (sqrt p, sqrt q) = (cos a, sin a), a = pi/4 - th/2: a spinor of the circle
a = sp.pi/4 - th/2
ok("W5 one circuit th -> th+2pi sends (sqrt p, sqrt q) -> -(sqrt p, sqrt q); 4pi restores (monodromy = central bit)",
   sp.simplify(sp.cos(a - sp.pi) + sp.cos(a)) == 0 and sp.simplify(sp.sin(a - sp.pi) + sp.sin(a)) == 0)

# W6: coin ladder: amplitude coin = power coin o h, h(A) = pi/4 + A/2; h has no finite period
ok("W6a sin^2(pi/4 + A/2) = (1 + sin A)/2 (one half-angle rung + quarter phase)",
   sp.simplify(sp.sin(sp.pi/4 + A/2)**2 - (1+sp.sin(A))/2) == 0)
h = lambda x: sp.pi/4 + x/2
ok("W6b h^4 != id — the mod-4 salience lives on the quadrant charge zeta, not on the angle",
   sp.simplify(h(h(h(h(A)))) - A) != 0)

# W7: one quarter-move, two faces
ok("W7a elliptic face (on-budget): u(th + pi/2) = x^2(th) — quarter-turn = signal<->noise swap = SNR -> 1/SNR",
   sp.simplify(sp.cos(th+sp.pi/2)**2 - sp.sin(th)**2) == 0)
ok("W7b hyperbolic transport of the same move: tanh(eta + i pi/2) = coth(eta) — x -> 1/x, the off-budget exit "
   "(v -> c^2/v: the phase-velocity/group-velocity dual, v_p v_g = c^2)",
   sp.simplify(sp.tanh(e + sp.I*sp.pi/2) - sp.coth(e)) == 0)
ok("W7c G_old(A + pi/2) = -1/sin A: under the quarter-move the gain migrates to the dual slot with a face sign",
   sp.simplify(1/sp.cos(A+sp.pi/2) + 1/sp.sin(A)) == 0)

print(f"\n{sum(res)}/{len(res)} PASS")
