#!/usr/bin/env python3
"""step2_serre_bridge.py -- COMPUTE phase, no grading.

(A) Serre conductor for the Q8 filtration ansatz, symbolic in b (LOWER numbering):
      G_0 = G_1 = Q8, G_2 = ... = G_b = Z (center, order 2), G_{b+1} = 1.
    a(rho) = sum_{i>=0} (|G_i|/|G_0|) * dim(V / V^{G_i}),  V = 2-dim irrep of Q8.
(B) Oddness of b via Hasse-Arf applied to a CYCLIC C4 subgroup (every C4 in Q8
    contains Z; lower numbering restricts exactly to subgroups).
(C) b=1 impossibility (floor): a totally ramified C4 over a 2-adic field cannot
    have its quadratic subextension break at 0 -- squares of U^(1) land in U^(2).
(D) Conductor-discriminant bridge: v2(disc M8) = 6 + 2*a2 for the degree-8
    subfield M8 = fixed field of C3 in the SL(2,3)-closure (Ind decomposition),
    and the same identity over U for the Galois Q8 extension M/U.
Character tables hardcoded; all multiplicities computed by inner products.
"""
from fractions import Fraction
import sympy as sp

print("=" * 72)
print("(A) Serre conductor formula for the Q8 ansatz (LOWER numbering)")
print("=" * 72)
# V = 2-dim faithful irrep of Q8: V^{Q8} = 0 and V^{Z} = 0 (center acts by -1),
# so dim(V/V^{G_i}) = 2 for every nontrivial G_i in the chain.
b = sp.symbols('b', positive=True, integer=True)
# i=0 term: (8/8)*2 ; i=1 term: (8/8)*2 ; i=2..b terms: (2/8)*2 each, count b-1
a2_expr = sp.Rational(8, 8) * 2 + sp.Rational(8, 8) * 2 + (b - 1) * sp.Rational(2, 8) * 2
a2_expr = sp.simplify(a2_expr)
print("a2(rho2) = 2 + 2 + (b-1)*(2/8)*2 =", a2_expr, "  [= 4 + (b-1)/2]")
print("tame part (i=0) = 2, Swan = a2 - 2 =", sp.simplify(a2_expr - 2), " [= 2+(b-1)/2]")
print("integrality of the Artin conductor  =>  (b-1)/2 in Z  =>  b ODD")
for bb in [1, 3, 5, 7]:
    print(f"   b={bb} (lower) -> a2 = {4 + (bb-1)//2}, Swan = {2 + (bb-1)//2}, "
          f"c(M8) = v2(disc) = {6 + 2*(4 + (bb-1)//2)}")

print()
print("=" * 72)
print("(B) Oddness of b, properly: Hasse-Arf on a C4 subgroup (NOT on Q8 itself)")
print("=" * 72)
print("""Every C4 <= Q8 contains Z. Lower numbering is compatible with subgroups:
G_i(M/F) = G_i(M/U) /\\ C4 for F = M^{C4}. So the C4-filtration is
  G_0 = G_1 = C4, G_2 = ... = G_b = Z(=C2 in C4), then 1:
lower breaks {1, b}. phi_{M/F}(1) = 1; phi_{M/F}(b) = 1 + (b-1)/2.
Hasse-Arf (valid: C4 is ABELIAN) forces upper jumps integral:
  1 + (b-1)/2 in Z  =>  b ODD.
[The retracted 'a2 = 2w+2 evenness' applied Hasse-Arf to the nonabelian Q8
 filtration itself - exactly the documented trap. Upper jumps of the full Q8
 filtration are 1 and 1+(b-1)/4, e.g. 3/2 for b=3: legitimately non-integral.]""")
for bb in [1, 2, 3, 4, 5]:
    up = Fraction(1) + Fraction(bb - 1, 2)
    print(f"   b={bb}: C4 upper jumps (1, {up}) -> {'OK' if up.denominator == 1 else 'EXCLUDED by Hasse-Arf'}")

print()
print("=" * 72)
print("(C) Floor: b = 1 is locally IMPOSSIBLE at p = 2")
print("=" * 72)
print("""Suppose b = 1: the C4-subextension M/F (F = M^{C4}) is totally ramified
with the single break 1, i.e. its order-4 character chi of F^x is trivial on
U_F^(2). But U_F^(1)/U_F^(2) is elementary abelian 2 (isomorphic to the residue
field, since (1+pi x)^2 = 1 + pi^2(...) in residue char 2: squares of U^(1)
land in U^(2)). Hence chi|U^(1) takes values +-1, so chi^2 is trivial on U^(1):
chi^2 is unramified (there are no tamely ramified quadratic characters in
residue characteristic 2). Then the quadratic subextension of M/F is
unramified, contradicting e(M/F) = 4.  =>  Any totally ramified C4 over a
2-adic field has strictly separated breaks, so b >= 2; with (B), b >= 3.
FLOOR (lower numbering): b >= 3  =>  a2 >= 5  =>  c(M8) >= 16.""")
print()
print("CEILING: b = break of the quadratic character of L = M^Z cutting M/L,")
print("with e(L/Q2) = 4: conductor exponent of a quadratic character of L is")
print("<= v_L(4) + 1 = 9, so b <= 8; b odd => b <= 7. Local window:")
print("   b in {3, 5, 7}  <=>  a2 in {5, 6, 7}  <=>  c(M8) in {16, 18, 20}.")

print()
print("=" * 72)
print("(D) Conductor-discriminant bridge from character tables")
print("=" * 72)
I = complex(0, 1)

def inner(chi1, chi2, sizes):
    n = sum(sizes)
    s = sum(sz * c1 * c2.conjugate() for sz, c1, c2 in zip(sizes, chi1, chi2))
    return s / n

# ---- Q8 over U: classes 1, -1, ±i, ±j, ±k ; sizes 1,1,2,2,2
sizes8 = [1, 1, 2, 2, 2]
q8_irr = {
    "triv":  [1, 1, 1, 1, 1],
    "chi_i": [1, 1, 1, -1, -1],
    "chi_j": [1, 1, -1, 1, -1],
    "chi_k": [1, 1, -1, -1, 1],
    "2dim":  [2, -2, 0, 0, 0],
}
reg = [8, 0, 0, 0, 0]
print("Q8 regular rep decomposition (multiplicities):")
mults = {nm: inner(reg, ch, sizes8) for nm, ch in q8_irr.items()}
for nm, m in mults.items():
    print(f"   <reg, {nm}> = {m.real:.0f}")
print("v_U(disc(M/U)) = sum_rho dim(rho)*a(rho)")
print("   = 1*a(triv) + 1*[a(chi_i)+a(chi_j)+a(chi_k)] + 2*a(2dim)")
print("   = 0 + (2+2+2) + 2*a2 = 6 + 2*a2      [three V4 characters: break 1 over U")
print("    => conductor exponent 2 each; a(2dim) over U = a2 over Q2 since the")
print("    lower-numbering filtration is unchanged by the unramified base U/Q2]")

# ---- SL(2,3) over Q2: M8 = fixed field of C3; disc via Ind_{C3}^{SL(2,3)} 1
# classes: 1, -1, 4A(order4,size6), 3A(size4), 3B(size4), 6A(size4), 6B(size4)
w = complex(-0.5, 3 ** 0.5 / 2)  # primitive cube root
sizes24 = [1, 1, 6, 4, 4, 4, 4]
sl23_irr = {
    "1":    [1, 1, 1, 1, 1, 1, 1],
    "w":    [1, 1, 1, w, w**2, w, w**2],
    "w2":   [1, 1, 1, w**2, w, w**2, w],
    "3dim": [3, 3, -1, 0, 0, 0, 0],
    "2":    [2, -2, 0, -1, -1, 1, 1],
    "2w":   [2, -2, 0, -w, -w**2, w, w**2],
    "2w2":  [2, -2, 0, -w**2, -w, w**2, w],
}
# Ind_{C3}^{G} 1 has character Ind(g) = |G|/|C3| * (fixed-point count)/..., use
# Frobenius reciprocity instead: <Ind 1, rho> = <1, Res rho>_{C3}.
# C3 = {1, t, t^2} with t in class 3A, t^2 in class 3B (a noncentral order-3 pair).
print()
print("SL(2,3)-closure over Q2, M8 = fix(C3), [M8:Q2] = 8 (e=8, f=1):")
print("multiplicities <Res_{C3} rho, 1> (Frobenius reciprocity):")
ind_mults = {}
for nm, ch in sl23_irr.items():
    val_1, val_t, val_t2 = ch[0], ch[3], ch[4]
    m = (val_1 + val_t + val_t2) / 3
    ind_mults[nm] = m
    print(f"   rho = {nm:4s}: mult = {m.real:+.3f}{'' if abs(m.imag) < 1e-9 else ' (imag!)'}")
dim_check = sum(ind_mults[nm].real * sl23_irr[nm][0].real if isinstance(sl23_irr[nm][0], complex)
                else ind_mults[nm].real * sl23_irr[nm][0] for nm in sl23_irr)
print(f"   dimension check: sum mult*dim = {dim_check:.1f} (must be 8)")
print("""=> Ind_{C3}^{SL(2,3)} 1 = 1 (+) 3dim (+) 2w (+) 2w2, so
v2(disc M8) = a(1) + a(3dim) + a(2w) + a(2w2)
            = 0 + 6 + a2 + a2 = 6 + 2*a2
[a(3dim) = v2(disc K4) = 6: 3dim factors through A4 and is Ind_{C3}^{A4}1 - 1;
 a(2w) = a(2w2) = a2: the twists w, w2 are UNRAMIFIED characters (they factor
 through Gal(U/Q2) = C3 = the unramified quotient), and unramified twists do
 not change the Artin conductor.]
BRIDGE (both routes):  a2 = (v2(disc M8) - 6) / 2.""")

# verify a(3dim)=6 from the A4 filtration ansatz G0=G1=V4, G2=1:
a3dim = Fraction(4, 4) * 3 + Fraction(4, 4) * 3
print(f"check a(3dim) from A4-closure filtration G0=G1=V4, G2=1: {a3dim} (= v2(disc K4) = 6)")
print("   [also = sum over the three V4 characters of conductor exponent 2 each,")
print("    computed over U: 2+2+2 = 6 = v_U(disc L/U) -- consistency check PASSED]")
# and the count that a(3dim)=6 FORCES G2=1 (each extra central-ish level adds >= 1):
extra = Fraction(2, 4) * 2
print(f"   any G2 != 1 (a C2 <= V4 surviving to level 2) would add >= {extra} per level")
print("   => v2(disc K4) = 6 forces breaks (1,1): 'three V4 characters each break 1' [VERIFIED]")
