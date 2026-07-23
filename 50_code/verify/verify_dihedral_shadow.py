# verify_dihedral_shadow.py — 2026-07-20: the D_inf -> D_4 check (Will's greenlight)
# Model: Collatz odd-step mirror dressings s+ (x -> 1-x), s- (x -> -1-x)  [division-of-labor SS1:
#   U± = s± ∘ (−3x), mirrors at ±1/2; dihedral closure over the translation lattice].
# Elements of the affine group: (e, b) : x -> e*x + b, e in {+1,-1}, b in Z.
# Chart group side (Delta 1): S_side (θ->-θ), S_face (θ->π-θ), R (θ->θ+π/2); D4 ~ {±1}-signed
#   b mod 4 dihedral; central bit = antipode.
import random
random.seed(11)
P = []
def check(name, ok):
    P.append(bool(ok)); print(("PASS " if ok else "FAIL ") + name)

def comp(f, g):   # f after g
    (e1, b1), (e2, b2) = f, g
    return (e1*e2, e1*b2 + b1)
ID = (1, 0); sP = (-1, 1); sM = (-1, -1)

# 1. Structure: involutions; t2 = s+ ∘ s- = translation by +2; all group translations are even
check("D1 s+^2 = s-^2 = id ; s+∘s- = t_2 (x -> x+2)",
      comp(sP, sP) == ID and comp(sM, sM) == ID and comp(sP, sM) == (1, 2))
words = []
for _ in range(4000):
    w = ID
    for _ in range(random.randint(1, 12)):
        w = comp(w, random.choice([sP, sM]))
    words.append(w)
check("D2 every translation in <s+,s-> is by an even integer (lattice 2Z)",
      all(b % 2 == 0 for (e, b) in words if e == 1))
# free product Z2*Z2: alternating words are never trivial except the empty word
def alt_word(n, start):
    w = ID; g = [sP, sM]
    for i in range(n):
        w = comp(w, g[(start + i) % 2])
    return w
check("D3 free-product check: alternating words of length 1..40 are all nontrivial [generic1 flag: "
      "any two involutions receive a morphism from Z2*Z2 — existence of phi is automatic]",
      all(alt_word(n, s) != ID for n in range(1, 41) for s in (0, 1)))

# 2. Mirror classes: b mod 4 in {1,3} is a conjugacy invariant; s+ and s- are NOT conjugate in the group
def conj(g, h):  # g h g^-1
    (e, b) = g
    ginv = (e, -e*b) if e == 1 else (e, e*b)  # inverse of (e,b) is (e, -e*b); for e=-1: (-1, b)
    ginv = (e, -b) if e == 1 else (-1, b)
    return comp(comp(g, h), ginv)
ok = True
for (e, b) in words[:1500]:
    c = conj((e, b), sP)
    ok = ok and (c[0] == -1 and c[1] % 4 == 1)
check("D4 conjugacy invariant: class of s+ keeps b ≡ 1 (mod 4); s- (b ≡ 3) is unreachable — "
      "the two ends are NON-conjugate in the dihedral closure", ok)

# 3. phi: reduce (e, b) mod 4 — the depth-2 / mod-4 shadow. Image sits inside D4.
def phi(g): return (g[0], g[1] % 4)
ok = True
for _ in range(3000):
    g, h = random.choice(words), random.choice(words)
    ok = ok and phi(comp(g, h)) == (phi(g)[0]*phi(h)[0], (phi(g)[0]*phi(h)[1] + phi(g)[1]) % 4)
check("D5 phi(e,b) = (e, b mod 4) is a homomorphism (verified on 3000 random pairs)", ok)
img = {phi(w) for w in words} | {phi(sP), phi(sM), phi(ID)}
check("D6 image of phi has order 4 = {id, antipode, S_side-class, S_face-class} ≅ D2 ⊂ D4 — "
      "the quarter-turn R (odd b) is NOT in the image", len(img) == 4 and all(b % 2 == 0 or e == -1 for (e, b) in img))
check("D7 the conjugator is the missing half-rung: R = phi(t_1), and t_1 (x -> x+1) is not in <s+,s->",
      all((1, 1) != phi(w) for w in words))  # no group element maps to the quarter-turn

# 4. Kernel and the central bit: ker phi = translations by 4Z; central bit = translation by 2 (mod 4)
check("D8 ker phi = {(1, 4k)}: phi(t_2) = antipode (central), phi(t_4) = id — chart reads the "
      "translation cocycle mod 4 (bottom two bits of the 2-adic anholonomy)",
      phi((1, 2)) == (1, 2) and phi((1, 4)) == (1, 0) and phi(comp((1, 2), (1, 2))) == (1, 0))

# 5. The end-separating torsion character chi (odd on translations) = pullback of the central-bit
#    detector beta through phi. beta on the image: +1 on {id, S_side-class}, -1 on {antipode, S_face-class}.
def chi(g):   # chi(t2) = -1, chi(s+) = +1  =>  chi(e,b): +1 iff b mod 4 in {0,1}
    return 1 if g[1] % 4 in (0, 1) else -1
def beta(q):  # on D4-image: does the element carry the antipode?
    return 1 if q[1] % 4 in (0, 1) else -1
ok = all(chi(comp(g, h)) == chi(g)*chi(h) for g in words[:60] for h in words[:60])
ok2 = all(chi(w) == beta(phi(w)) for w in words)
check("D9 chi is a character (60x60 pairs) and chi = beta ∘ phi: the end-separating torsion "
      "character IS the pullback of the D4 central bit", ok and ok2)
check("D10 chi separates the ends: chi(s+) = +1, chi(s-) = -1, chi(t2) = -1",
      chi(sP) == 1 and chi(sM) == -1 and chi((1, 2)) == -1)

# 6. Collatz-word content: pure 3x+1 words use only s+ (one mirror class): central charge needs both
#    ends — the charge is live exactly on cross-end (level-transfer / expulsion) moves.
w_pure = ID
for _ in range(7):
    w_pure = comp(w_pure, sP)
check("D11 pure single-end mirror words never acquire the central charge "
      "(chi = +1 on all s+ words); charge requires end-mixing", chi(w_pure) == 1 and phi(w_pure) in {(1, 0), (-1, 1)})

print("\n%d/%d PASS" % (sum(P), len(P)))
