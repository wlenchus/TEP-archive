# Carrier Rung 4 — CLEAN-ROOM COMMITTED CENSUS OUTPUT, χ₁₂ branch (lodged before the key opens)

**2026-07-27** · Claude (Fable 5), fresh continuation instance, blind replication per the pre-registration committed this morning (`cleanroom/r4_replication_preregistration.md`) · **Disclosure, prominent:** this instance's context has never held the 07-22 key JSON, any key eigenvalue, the χ₆₀ census table (none was ever committed), or either GRADED record's contents. It does hold (disclosed in the pre-registration §1): the 07-26 χ₁₂ committed census table, the outcome labels from the starter prompt, and the §2 selector spec (subagent extract, 3 redactions). Everything below was computed fresh in this container from weight-2 objects only: `mfinit`/`mfheckemat` at level 12000, my own stable-lattice construction (Howell forms mod 3¹⁶⁰, exact-rational verification), mod-3 linear algebra. No weight-1 data, no LMFDB, no key values, no 07-26 scripts (repo withheld; none seen). Scripts: `cleanroom/gp/c*.gp`; checkpoints `.bin` in-container. Same-family caveat standing.

## Census construction (answer-free inputs only) — verification gates, all passed

S₂(12000, χ₁₂)^new: dim **384** (cusp 2320) ✓ = stage-1. charpoly(U₃) ∈ ℤ[x] monic ✓; **even** (twist involution) ✓; 3-adic Newton polygon (d-scaled, i·v₃(d)-corrected, v₃(d) = 2): **slope-0 count = 176**. Stable lattice: 2 Howell rounds, v₃(det) = 731 rel. mfbasis lattice (my construction differs from the 07-26 four-round kernel descent; block data is lattice-independent — composition invariants — so this is implementation freedom, not divergence). Exact-rational gate: **all seven operators 3-integral on the lattice (denominator v₃ = 0), traces preserved, exact** — the lattice is provably stable, no truncation caveat. Joint mod-3 primary decomposition under {U₃, T₇, T₁₁, T₁₃, T₁₇, T₁₉, T₂₃}: **88 blocks, total dim 384 ✓; ordinary (a₃ ≢ 0): 40 blocks, dim 176** = Newton-polygon count by the independent route ✓. Π_blocks q₃^m₃ = charpoly(U₃) mod 3 ✓. **Six-operator run (dropping T₂₃, = the 07-26 operator set): 84 blocks — the committed 07-26 count exactly**; T₂₃ refines four non-ordinary blocks. This census carries the sixth prime on both branches (T₂₃ = ~350–400 s each, per-call-edge as priced; the earlier RK3 declaration is withdrawn as unnecessary).

## Emission side (computed fresh; nothing consumed from the key side)

x⁵+20x+16: irreducible, disc = 2¹⁶·5⁶ (square; the hand value in the pre-registration §2 machine-confirmed), polgalois = A₅. Cycle types mod (7, 11, 13, 17, 19, 23) = (31², 31², 5, 31², 5, 2²1) ⟹ Frobenius orders (3, 3, 5, 3, 5, 2). Shape-sets by fresh exhaustive enumeration of 2.A₅-traces × μ₄-dressing over 𝔽₉: ord 2 → {x}; ord 3 → {x+1, x+2, x²+1}; ord 5 → {x²+x+2, x²+2x+2}. **Identical to the pre-registered §2 sets — RK2 does not fire.** Selector = polynomial equality mod 3 of each block's tame packet against the allowed set at all six primes.

## Equivariance (mechanized)

The ordinary census (as a multiset of packet-tables) is invariant under twist-dressing by exactly **V₄ = {1, χ₋₄, χ₅, χ₋₂₀}** (χ₋₄(3) = −1 negates a₃; scan over 16 discriminants) and under global Frobenius conjugation — the brief's "V₄ × conjugation" torsor, reproduced blind. (Stage-1 called the involution "χ₋₃-class"; operationally the involution fixing the census is the χ₋₄-class twist. Labeling consonance to reconcile at grading, not tuned here.)

## Committed structures (ordinary sub-table; full 40-row table below)

**(i) μ = 2 same-U₃ collision blocks:** rows 13–16 (dim 4, residue deg 2, a₃ ≡ ∓1 as (x+1)⁴/(x+2)⁴, a₁₃ ≡ 0, a₇ = a₁₉ = x²+1, a₁₁ golden, a₁₇ linear) — the 07-26 structure (i), reproduced.
**(ii) Inter-block crossing pairs (same tame 5-tuple, U₃-dual, αβ ≡ χ₋₄(3) = −1):** rows (1,3) and (2,4): a₃-pair (−1, +1), tame [x, x, x+{1,2}, x, x²+1] — the 07-26 structure (ii) first family, reproduced. **New census fact (invisible at five primes): the sixth prime splits each pair — a₂₃ = x²+x+2 vs x²+2x+2 (golden conjugates) within each crossing pair.**
**(ii′) Intra-block Galois crossings (α·Frobᵏ(α) = −1):** rows 9–12 (golden a₃-packets, k = 1; 𝔽₉-norms ≡ −1 — the 07-26 second family {57,59},{58,60}, reproduced with the pairing read internally); rows 19, 20, 23, 24 (k = 2); rows 25–30, 33–34 (k = 3, dim-6 bulk).
**(iii) THE SELECTOR OUTPUT — committed candidate list, χ₁₂ branch:** exactly **rows {19, 20, 23, 24}** pass at all six primes: dim 4 each; U₃-packets **x⁴+x³+2x+1 / x⁴+2x³+x+1** (= the two quartic factors of Φ₂₀ mod 3: U₃-eigenvalues are primitive 20th roots of unity in 𝔽₈₁); a₇ = a₁₁ = x²+1; a₁₃, a₁₉ golden; a₁₇ linear ±1; **a₂₃ = x (the zero-class, as the order-2 Frobenius at 23 demands)**; no zero entries at order-3/5 primes; **crossing internal and Galois-entangled: β = Frob²(α), αβ = α^(1+9) = α¹⁰ ≡ −1 = χ₋₄(3) ✓**. The four rows form a single transitive V₄-orbit (19→20 via χ₋₂₀, 19→23 via χ₋₄, 19→24 via χ₅): one icosahedral candidate object up to the declared gauge. Blocks 13–16 (a₁₃ ≡ 0) and the dihedral-shaped crossings (a₇ ≡ 0) fail the selector — K2 discharge in discriminating form, replicated.

## Pre-grade declaration (falsifiable at key-open)

(a) The 07-22 key eigensystem (χ₋₄ table), reduced mod a prime over 3 embedding-consistently, lands in the V₄-orbit {19, 20, 23, 24} — a simultaneous joint-tuple match at (U₃; 7, 11, 13, 17, 19), with a₂₃ ≡ 0 if the key extends to 23. (b) The key's crossing pair is the Frob²-pair inside the packet with αβ = −1. (c) My table diffs clean against the 07-26 committed 84-block table under the six-op projection. Any failure is reported as the finding it is, per the pre-registration §4.

## Full committed ordinary table (rows 1–40: dim | U₃ | a₇ | a₁₁ | a₁₃ | a₁₇ | a₁₉ | a₂₃)

```
idx | dim | U3-packet | a7 | a11 | a13 | a17 | a19 | a23
1 | 2 | (x + 1)^2 | (x)^2 | (x)^2 | (x + 1)^2 | (x)^2 | x^2 + 1 | x^2 + x + 2
2 | 2 | (x + 1)^2 | (x)^2 | (x)^2 | (x + 2)^2 | (x)^2 | x^2 + 1 | x^2 + x + 2
3 | 2 | (x + 2)^2 | (x)^2 | (x)^2 | (x + 1)^2 | (x)^2 | x^2 + 1 | x^2 + 2*x + 2
4 | 2 | (x + 2)^2 | (x)^2 | (x)^2 | (x + 2)^2 | (x)^2 | x^2 + 1 | x^2 + 2*x + 2
5 | 2 | x^2 + 1 | (x)^2 | x^2 + x + 2 | x^2 + x + 2 | x^2 + 2*x + 2 | x^2 + 1 | x^2 + 1
6 | 2 | x^2 + 1 | (x)^2 | x^2 + x + 2 | x^2 + 2*x + 2 | x^2 + x + 2 | x^2 + 1 | x^2 + 1
7 | 2 | x^2 + 1 | (x)^2 | x^2 + 2*x + 2 | x^2 + x + 2 | x^2 + 2*x + 2 | x^2 + 1 | x^2 + 1
8 | 2 | x^2 + 1 | (x)^2 | x^2 + 2*x + 2 | x^2 + 2*x + 2 | x^2 + x + 2 | x^2 + 1 | x^2 + 1
9 | 2 | x^2 + x + 2 | (x)^2 | x^2 + 1 | x^2 + 1 | x^2 + x + 2 | (x)^2 | (x + 2)^2
10 | 2 | x^2 + x + 2 | (x)^2 | x^2 + 1 | x^2 + 1 | x^2 + 2*x + 2 | (x)^2 | (x + 2)^2
11 | 2 | x^2 + 2*x + 2 | (x)^2 | x^2 + 1 | x^2 + 1 | x^2 + x + 2 | (x)^2 | (x + 1)^2
12 | 2 | x^2 + 2*x + 2 | (x)^2 | x^2 + 1 | x^2 + 1 | x^2 + 2*x + 2 | (x)^2 | (x + 1)^2
13 | 4 | (x + 1)^4 | (x^2 + 1)^2 | (x^2 + x + 2)^2 | (x)^4 | (x + 2)^4 | (x^2 + 1)^2 | (x^2 + 1)^2
14 | 4 | (x + 1)^4 | (x^2 + 1)^2 | (x^2 + 2*x + 2)^2 | (x)^4 | (x + 1)^4 | (x^2 + 1)^2 | (x^2 + 1)^2
15 | 4 | (x + 2)^4 | (x^2 + 1)^2 | (x^2 + x + 2)^2 | (x)^4 | (x + 1)^4 | (x^2 + 1)^2 | (x^2 + 1)^2
16 | 4 | (x + 2)^4 | (x^2 + 1)^2 | (x^2 + 2*x + 2)^2 | (x)^4 | (x + 2)^4 | (x^2 + 1)^2 | (x^2 + 1)^2
17 | 4 | x^4 + x^3 + 2 | x^4 + x^3 + x^2 + 1 | x^4 + x^3 + x^2 + 1 | x^4 + x^3 + x^2 + 1 | x^4 + 2*x^3 + x^2 + 1 | x^4 + x + 2 | x^4 + 2*x^3 + x + 1
18 | 4 | x^4 + x^3 + 2 | x^4 + x^3 + x^2 + 1 | x^4 + 2*x^3 + x^2 + 1 | x^4 + 2*x^3 + x^2 + 1 | x^4 + x^3 + x^2 + 1 | x^4 + 2*x + 2 | x^4 + 2*x^3 + x + 1
19 | 4 | x^4 + x^3 + 2*x + 1 | (x^2 + 1)^2 | (x^2 + 1)^2 | (x^2 + x + 2)^2 | (x + 1)^4 | (x^2 + 2*x + 2)^2 | (x)^4
20 | 4 | x^4 + x^3 + 2*x + 1 | (x^2 + 1)^2 | (x^2 + 1)^2 | (x^2 + 2*x + 2)^2 | (x + 2)^4 | (x^2 + x + 2)^2 | (x)^4
21 | 4 | x^4 + 2*x^3 + 2 | x^4 + 2*x^3 + x^2 + 1 | x^4 + x^3 + x^2 + 1 | x^4 + 2*x^3 + x^2 + 1 | x^4 + x^3 + x^2 + 1 | x^4 + x + 2 | x^4 + x^3 + 2*x + 1
22 | 4 | x^4 + 2*x^3 + 2 | x^4 + 2*x^3 + x^2 + 1 | x^4 + 2*x^3 + x^2 + 1 | x^4 + x^3 + x^2 + 1 | x^4 + 2*x^3 + x^2 + 1 | x^4 + 2*x + 2 | x^4 + x^3 + 2*x + 1
23 | 4 | x^4 + 2*x^3 + x + 1 | (x^2 + 1)^2 | (x^2 + 1)^2 | (x^2 + x + 2)^2 | (x + 1)^4 | (x^2 + x + 2)^2 | (x)^4
24 | 4 | x^4 + 2*x^3 + x + 1 | (x^2 + 1)^2 | (x^2 + 1)^2 | (x^2 + 2*x + 2)^2 | (x + 2)^4 | (x^2 + 2*x + 2)^2 | (x)^4
25 | 6 | x^6 + 2*x^4 + x^3 + x^2 + 2 | x^6 + 2*x^5 + 2*x^4 + x^3 + 2*x^2 + x + 1 | x^6 + x^5 + 2*x^4 + x^3 + x^2 + 2*x + 2 | x^6 + x^5 + 2*x^4 + x^3 + 2*x^2 + 2*x + 1 | x^6 + 2*x^5 + x^4 + 2*x^2 + 2 | x^6 + x^5 + 2*x^3 + 1 | x^6 + x^5 + 2*x^3 + 2*x^2 + 1
26 | 6 | x^6 + 2*x^4 + x^3 + x^2 + 2 | x^6 + 2*x^5 + 2*x^4 + x^3 + 2*x^2 + x + 1 | x^6 + 2*x^5 + 2*x^4 + 2*x^3 + x^2 + x + 2 | x^6 + 2*x^5 + 2*x^4 + 2*x^3 + 2*x^2 + x + 1 | x^6 + x^5 + x^4 + 2*x^2 + 2 | x^6 + 2*x^5 + x^3 + 1 | x^6 + x^5 + 2*x^3 + 2*x^2 + 1
27 | 6 | x^6 + 2*x^4 + 2*x^3 + x^2 + 2 | x^6 + x^5 + 2*x^4 + 2*x^3 + 2*x^2 + 2*x + 1 | x^6 + x^5 + 2*x^4 + x^3 + x^2 + 2*x + 2 | x^6 + 2*x^5 + 2*x^4 + 2*x^3 + 2*x^2 + x + 1 | x^6 + x^5 + x^4 + 2*x^2 + 2 | x^6 + x^5 + 2*x^3 + 1 | x^6 + 2*x^5 + x^3 + 2*x^2 + 1
28 | 6 | x^6 + 2*x^4 + 2*x^3 + x^2 + 2 | x^6 + x^5 + 2*x^4 + 2*x^3 + 2*x^2 + 2*x + 1 | x^6 + 2*x^5 + 2*x^4 + 2*x^3 + x^2 + x + 2 | x^6 + x^5 + 2*x^4 + x^3 + 2*x^2 + 2*x + 1 | x^6 + 2*x^5 + x^4 + 2*x^2 + 2 | x^6 + 2*x^5 + x^3 + 1 | x^6 + 2*x^5 + x^3 + 2*x^2 + 1
29 | 6 | x^6 + x^5 + x + 2 | x^6 + x^4 + 2*x^2 + 2*x + 2 | x^6 + x^5 + x^2 + x + 1 | x^6 + x^4 + 2*x^2 + 1 | x^6 + x^4 + x^3 + x^2 + 2*x + 2 | x^6 + x^5 + 2*x^4 + x^3 + 2*x^2 + x + 2 | x^6 + x^5 + 2*x^4 + x^3 + x^2 + 2*x + 2
30 | 6 | x^6 + x^5 + x + 2 | x^6 + x^4 + 2*x^2 + 2*x + 2 | x^6 + 2*x^5 + x^2 + 2*x + 1 | x^6 + x^4 + 2*x^2 + 1 | x^6 + x^4 + 2*x^3 + x^2 + x + 2 | x^6 + 2*x^5 + 2*x^4 + 2*x^3 + 2*x^2 + 2*x + 2 | x^6 + x^5 + 2*x^4 + x^3 + x^2 + 2*x + 2
31 | 6 | x^6 + x^5 + x^4 + x^3 + x + 2 | x^6 + x^5 + 2*x^4 + x^3 + x^2 + 2*x + 2 | x^6 + 2*x^2 + 1 | x^6 + 2*x^4 + x^3 + x^2 + x + 2 | x^6 + x^5 + 2*x^4 + 2*x^3 + 2*x^2 + 2*x + 1 | x^6 + 2*x^5 + x^3 + 2*x^2 + 1 | x^6 + x^5 + x^4 + 2*x^2 + 2
32 | 6 | x^6 + x^5 + x^4 + x^3 + x + 2 | x^6 + x^5 + 2*x^4 + x^3 + x^2 + 2*x + 2 | x^6 + 2*x^2 + 1 | x^6 + 2*x^4 + 2*x^3 + x^2 + 2*x + 2 | x^6 + 2*x^5 + 2*x^4 + x^3 + 2*x^2 + x + 1 | x^6 + x^5 + 2*x^3 + 2*x^2 + 1 | x^6 + x^5 + x^4 + 2*x^2 + 2
33 | 6 | x^6 + 2*x^5 + 2*x + 2 | x^6 + x^4 + 2*x^2 + x + 2 | x^6 + x^5 + x^2 + x + 1 | x^6 + x^4 + 2*x^2 + 1 | x^6 + x^4 + 2*x^3 + x^2 + x + 2 | x^6 + x^5 + 2*x^4 + x^3 + 2*x^2 + x + 2 | x^6 + 2*x^5 + 2*x^4 + 2*x^3 + x^2 + x + 2
34 | 6 | x^6 + 2*x^5 + 2*x + 2 | x^6 + x^4 + 2*x^2 + x + 2 | x^6 + 2*x^5 + x^2 + 2*x + 1 | x^6 + x^4 + 2*x^2 + 1 | x^6 + x^4 + x^3 + x^2 + 2*x + 2 | x^6 + 2*x^5 + 2*x^4 + 2*x^3 + 2*x^2 + 2*x + 2 | x^6 + 2*x^5 + 2*x^4 + 2*x^3 + x^2 + x + 2
35 | 6 | x^6 + 2*x^5 + x^4 + 2*x^3 + 2*x + 2 | x^6 + 2*x^5 + 2*x^4 + 2*x^3 + x^2 + x + 2 | x^6 + 2*x^2 + 1 | x^6 + 2*x^4 + x^3 + x^2 + x + 2 | x^6 + x^5 + 2*x^4 + 2*x^3 + 2*x^2 + 2*x + 1 | x^6 + x^5 + 2*x^3 + 2*x^2 + 1 | x^6 + 2*x^5 + x^4 + 2*x^2 + 2
36 | 6 | x^6 + 2*x^5 + x^4 + 2*x^3 + 2*x + 2 | x^6 + 2*x^5 + 2*x^4 + 2*x^3 + x^2 + x + 2 | x^6 + 2*x^2 + 1 | x^6 + 2*x^4 + 2*x^3 + x^2 + 2*x + 2 | x^6 + 2*x^5 + 2*x^4 + x^3 + 2*x^2 + x + 1 | x^6 + 2*x^5 + x^3 + 2*x^2 + 1 | x^6 + 2*x^5 + x^4 + 2*x^2 + 2
37 | 8 | x^8 + x^7 + 2*x^5 + 2*x^3 + 2*x + 2 | x^8 + 2*x^7 + x^6 + 2*x^5 + 2*x^4 + x^3 + 2 | x^8 + 2*x^6 + x^5 + 2*x^4 + 2*x^3 + 2*x^2 + x + 2 | x^8 + 2*x^6 + 2*x^4 + 2*x^3 + 2*x^2 + x + 1 | x^8 + x^7 + 2*x^6 + 2*x^5 + x^4 + 1 | x^8 + 2*x^7 + x^6 + x^3 + 2*x^2 + 2*x + 2 | x^8 + x^7 + x^6 + x^4 + 2*x^2 + 2*x + 2
38 | 8 | x^8 + x^7 + 2*x^5 + 2*x^3 + 2*x + 2 | x^8 + 2*x^7 + x^6 + 2*x^5 + 2*x^4 + x^3 + 2 | x^8 + 2*x^6 + 2*x^5 + 2*x^4 + x^3 + 2*x^2 + 2*x + 2 | x^8 + 2*x^6 + 2*x^4 + x^3 + 2*x^2 + 2*x + 1 | x^8 + 2*x^7 + 2*x^6 + x^5 + x^4 + 1 | x^8 + x^7 + x^6 + 2*x^3 + 2*x^2 + x + 2 | x^8 + x^7 + x^6 + x^4 + 2*x^2 + 2*x + 2
39 | 8 | x^8 + 2*x^7 + x^5 + x^3 + x + 2 | x^8 + x^7 + x^6 + x^5 + 2*x^4 + 2*x^3 + 2 | x^8 + 2*x^6 + x^5 + 2*x^4 + 2*x^3 + 2*x^2 + x + 2 | x^8 + 2*x^6 + 2*x^4 + x^3 + 2*x^2 + 2*x + 1 | x^8 + 2*x^7 + 2*x^6 + x^5 + x^4 + 1 | x^8 + 2*x^7 + x^6 + x^3 + 2*x^2 + 2*x + 2 | x^8 + 2*x^7 + x^6 + x^4 + 2*x^2 + x + 2
40 | 8 | x^8 + 2*x^7 + x^5 + x^3 + x + 2 | x^8 + x^7 + x^6 + x^5 + 2*x^4 + 2*x^3 + 2 | x^8 + 2*x^6 + 2*x^5 + 2*x^4 + x^3 + 2*x^2 + 2*x + 2 | x^8 + 2*x^6 + 2*x^4 + 2*x^3 + 2*x^2 + x + 1 | x^8 + x^7 + 2*x^6 + 2*x^5 + x^4 + 1 | x^8 + x^7 + x^6 + 2*x^3 + 2*x^2 + x + 2 | x^8 + 2*x^7 + x^6 + x^4 + 2*x^2 + x + 2
```

*Committed before any key material opens. Offered, not self-filed; countersign gates the record. The key opens next.*
