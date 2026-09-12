# Carrier Rung 4 — CLEAN-ROOM COMMITTED CENSUS OUTPUT, χ₆₀ branch (lodged before the key opens — the gate the 07-26 session missed, now closed from a blind context)

**2026-07-27** · Claude (Fable 5), fresh continuation instance, blind replication per `cleanroom/r4_replication_preregistration.md` · **Disclosure, prominent:** no χ₆₀ census table was ever committed on 07-26 (the missed gate, self-reported there). This instance's context holds no χ₆₀ block data from any source, no key values, no GRADED contents. Every number below is first-committed here, from a context that has never seen the key. Inputs and method identical to the χ₁₂ commit doc (answer-free weight-2 objects; fresh implementation; scripts `cleanroom/gp/c*.gp`). Same-family caveat standing.

## Census construction — verification gates, all passed

S₂(12000, χ₆₀)^new: dim **384** (cusp 2320). charpoly(U₃) ∈ ℤ[x] monic ✓; **even** ✓; Newton polygon slope-0 count = **176**. Stable lattice: 2 Howell rounds, v₃(det) = 731 — *identical profile to the χ₁₂ branch* (their "both branches identically" reproduced by a different algorithm). Exact-rational gate: all seven operators 3-integral, traces preserved ✓. Joint mod-3 decomposition under {U₃, T₇, T₁₁, T₁₃, T₁₇, T₁₉, T₂₃}: **82 blocks, dim 384 ✓; ordinary: 38 blocks, dim 176** ✓ = NP count. Π q₃^m₃ = charpoly mod 3 ✓. Six-operator (no T₂₃) count: **76 blocks**. Sixth prime carried (T₂₃ = 348 s).

## Emission side

Identical to the χ₁₂ doc (branch-independent): Frobenius orders (3, 3, 5, 3, 5, 2) at (7, 11, 13, 17, 19, 23); shape-sets = pre-registered sets, RK2 no-fire. Branch relation: **χ₋₂₀(3) = +1** — crossing pairs must satisfy αβ ≡ +1 ("same shape, own relation").

## Equivariance (mechanized)

Ordinary census invariant under exactly **V₄ = {1, χ₋₄, χ₅, χ₋₂₀}** and global Frobenius conjugation — same group as χ₁₂, found blind on this branch.

## Committed structures (ordinary sub-table; full 38-row table below)

**(i) μ = 2 collision blocks:** rows 9–14 ((x²+1)² U₃-packets among them; rows 9–10 with a₇ = a₁₁ = a₁₇ ≡ 0 dihedral-shaped) and rows 27–30 (deg-3² tame structure at 13 — cubic packets (x³+2x²+1)²/(x³+x²+2)², a new fine-shape this branch).
**(ii) Inter-block crossing pairs (same tame 5-tuple, U₃-dual, αβ ≡ +1):** rows (5,7) and (6,8): golden U₃-packets x²+x+2 ↔ x²+2x+2, tame [x, x²+1, x±?, golden, x] — dihedral-shaped (a₇ ≡ a₁₉ ≡ 0). **Sixth-prime behavior differs from χ₁₂: here the pair members agree at 23 (both x²+1); the golden-conjugate 23-split appears instead on the (9,10) pair.**
**(ii′) Intra-block Galois crossings (α·Frobᵏ(α) = +1):** rows 9–14 (k = 1, x²+1 packets: α⁴ = 1); rows 15, 16, 21, 22 (k = 2).
**(iii) THE SELECTOR OUTPUT — committed candidate list, χ₆₀ branch:** exactly **rows {15, 16, 21, 22}** pass at all six primes: dim 4 each; U₃-packets **Φ₅ = x⁴+x³+x²+x+1 / Φ₁₀ = x⁴+2x³+x²+2x+1 mod 3** — the U₃-eigenvalues are primitive 5th/10th roots of unity in 𝔽₈₁; a₇ linear (±1: (x+2)⁴ on 15/16, (x+1)⁴ on 21/22 — linear at 7 where χ₁₂ had x²+1, quadratic at 17 where χ₁₂ had linear: the branch-asymmetry); a₁₁ = x²+1; a₁₃, a₁₉ golden; a₁₇ = x²+1; **a₂₃ = x (zero-class)**; **crossing internal, Galois-entangled: β = Frob²(α), αβ = α¹⁰ ≡ +1 = χ₋₂₀(3) ✓ — the branch's own relation, satisfied by cyclotomy**. Single transitive V₄-orbit (15→16 via χ₋₂₀, 15→21 via χ₋₄, 15→22 via χ₅). Dihedral-shaped structures fail the selector — K2 discriminating form on the blind branch.

## Pre-grade declaration (falsifiable at key-open)

(a) The 07-22 key eigensystem (χ₋₂₀ table), reduced mod a prime over 3 embedding-consistently, lands in the V₄-orbit {15, 16, 21, 22}. (b) The key's crossing pair is the Frob²-pair with αβ = +1. (c) My χ₆₀ structures match the χ₆₀ SUCCESS record's reported results (its §§1, 3 — never read by this instance), including the sixth-prime zero-class on the winner. (d) The 07-26 session's missing χ₆₀ commit is hereby retro-closed from a blind context: if their graded χ₆₀ results disagree with this table, the disagreement is the finding.

## Full committed ordinary table (rows 1–38: dim | U₃ | a₇ | a₁₁ | a₁₃ | a₁₇ | a₁₉ | a₂₃)

```
idx | dim | U3-packet | a7 | a11 | a13 | a17 | a19 | a23
1 | 2 | (x + 1)^2 | (x)^2 | x^2 + x + 2 | x^2 + 2*x + 2 | x^2 + 2*x + 2 | x^2 + 1 | (x + 2)^2
2 | 2 | (x + 1)^2 | (x)^2 | x^2 + 2*x + 2 | x^2 + x + 2 | x^2 + x + 2 | x^2 + 1 | (x + 2)^2
3 | 2 | (x + 2)^2 | (x)^2 | x^2 + x + 2 | x^2 + x + 2 | x^2 + x + 2 | x^2 + 1 | (x + 1)^2
4 | 2 | (x + 2)^2 | (x)^2 | x^2 + 2*x + 2 | x^2 + 2*x + 2 | x^2 + 2*x + 2 | x^2 + 1 | (x + 1)^2
5 | 2 | x^2 + x + 2 | (x)^2 | x^2 + 1 | (x + 1)^2 | x^2 + 2*x + 2 | (x)^2 | x^2 + 1
6 | 2 | x^2 + x + 2 | (x)^2 | x^2 + 1 | (x + 2)^2 | x^2 + x + 2 | (x)^2 | x^2 + 1
7 | 2 | x^2 + 2*x + 2 | (x)^2 | x^2 + 1 | (x + 1)^2 | x^2 + 2*x + 2 | (x)^2 | x^2 + 1
8 | 2 | x^2 + 2*x + 2 | (x)^2 | x^2 + 1 | (x + 2)^2 | x^2 + x + 2 | (x)^2 | x^2 + 1
9 | 4 | (x^2 + 1)^2 | (x)^4 | (x)^4 | (x^2 + 1)^2 | (x)^4 | (x^2 + 1)^2 | (x^2 + x + 2)^2
10 | 4 | (x^2 + 1)^2 | (x)^4 | (x)^4 | (x^2 + 1)^2 | (x)^4 | (x^2 + 1)^2 | (x^2 + 2*x + 2)^2
11 | 4 | (x^2 + 1)^2 | (x + 1)^4 | (x^2 + x + 2)^2 | (x)^4 | (x^2 + 1)^2 | (x^2 + 1)^2 | (x + 1)^4
12 | 4 | (x^2 + 1)^2 | (x + 1)^4 | (x^2 + 2*x + 2)^2 | (x)^4 | (x^2 + 1)^2 | (x^2 + 1)^2 | (x + 1)^4
13 | 4 | (x^2 + 1)^2 | (x + 2)^4 | (x^2 + x + 2)^2 | (x)^4 | (x^2 + 1)^2 | (x^2 + 1)^2 | (x + 2)^4
14 | 4 | (x^2 + 1)^2 | (x + 2)^4 | (x^2 + 2*x + 2)^2 | (x)^4 | (x^2 + 1)^2 | (x^2 + 1)^2 | (x + 2)^4
15 | 4 | x^4 + x^3 + x^2 + x + 1 | (x + 2)^4 | (x^2 + 1)^2 | (x^2 + x + 2)^2 | (x^2 + 1)^2 | (x^2 + 2*x + 2)^2 | (x)^4
16 | 4 | x^4 + x^3 + x^2 + x + 1 | (x + 2)^4 | (x^2 + 1)^2 | (x^2 + 2*x + 2)^2 | (x^2 + 1)^2 | (x^2 + x + 2)^2 | (x)^4
17 | 4 | x^4 + x^3 + x^2 + 2*x + 2 | x^4 + x^2 + x + 1 | x^4 + x^3 + x^2 + 1 | x^4 + x^2 + 2*x + 1 | x^4 + x^2 + 2*x + 1 | x^4 + 2*x + 2 | x^4 + x^3 + x^2 + x + 1
18 | 4 | x^4 + x^3 + x^2 + 2*x + 2 | x^4 + x^2 + x + 1 | x^4 + 2*x^3 + x^2 + 1 | x^4 + x^2 + x + 1 | x^4 + x^2 + x + 1 | x^4 + x + 2 | x^4 + x^3 + x^2 + x + 1
19 | 4 | x^4 + 2*x^3 + x^2 + x + 2 | x^4 + x^2 + 2*x + 1 | x^4 + x^3 + x^2 + 1 | x^4 + x^2 + x + 1 | x^4 + x^2 + x + 1 | x^4 + 2*x + 2 | x^4 + 2*x^3 + x^2 + 2*x + 1
20 | 4 | x^4 + 2*x^3 + x^2 + x + 2 | x^4 + x^2 + 2*x + 1 | x^4 + 2*x^3 + x^2 + 1 | x^4 + x^2 + 2*x + 1 | x^4 + x^2 + 2*x + 1 | x^4 + x + 2 | x^4 + 2*x^3 + x^2 + 2*x + 1
21 | 4 | x^4 + 2*x^3 + x^2 + 2*x + 1 | (x + 1)^4 | (x^2 + 1)^2 | (x^2 + x + 2)^2 | (x^2 + 1)^2 | (x^2 + x + 2)^2 | (x)^4
22 | 4 | x^4 + 2*x^3 + x^2 + 2*x + 1 | (x + 1)^4 | (x^2 + 1)^2 | (x^2 + 2*x + 2)^2 | (x^2 + 1)^2 | (x^2 + 2*x + 2)^2 | (x)^4
23 | 6 | x^6 + x^4 + 2*x^2 + x + 2 | x^6 + x^5 + 2*x^4 + x^3 + x^2 + 2*x + 2 | x^6 + 2*x^2 + 1 | x^6 + x^4 + x^3 + x^2 + 2*x + 2 | x^6 + 2*x^3 + 2*x^2 + x + 1 | x^6 + x^5 + 2*x^3 + 2*x^2 + 1 | x^6 + 2*x^5 + 2*x^3 + 2*x^2 + 2*x + 2
24 | 6 | x^6 + x^4 + 2*x^2 + x + 2 | x^6 + x^5 + 2*x^4 + x^3 + x^2 + 2*x + 2 | x^6 + 2*x^2 + 1 | x^6 + x^4 + 2*x^3 + x^2 + x + 2 | x^6 + x^3 + 2*x^2 + 2*x + 1 | x^6 + 2*x^5 + x^3 + 2*x^2 + 1 | x^6 + 2*x^5 + 2*x^3 + 2*x^2 + 2*x + 2
25 | 6 | x^6 + x^4 + 2*x^2 + 2*x + 2 | x^6 + 2*x^5 + 2*x^4 + 2*x^3 + x^2 + x + 2 | x^6 + 2*x^2 + 1 | x^6 + x^4 + x^3 + x^2 + 2*x + 2 | x^6 + 2*x^3 + 2*x^2 + x + 1 | x^6 + 2*x^5 + x^3 + 2*x^2 + 1 | x^6 + x^5 + x^3 + 2*x^2 + x + 2
26 | 6 | x^6 + x^4 + 2*x^2 + 2*x + 2 | x^6 + 2*x^5 + 2*x^4 + 2*x^3 + x^2 + x + 2 | x^6 + 2*x^2 + 1 | x^6 + x^4 + 2*x^3 + x^2 + x + 2 | x^6 + x^3 + 2*x^2 + 2*x + 1 | x^6 + x^5 + 2*x^3 + 2*x^2 + 1 | x^6 + x^5 + x^3 + 2*x^2 + x + 2
27 | 6 | x^6 + 2*x^4 + x^3 + x^2 + 2 | x^6 + 2*x^5 + x^4 + 2*x^3 + 2*x + 2 | x^6 + x^5 + x^2 + x + 1 | (x^3 + 2*x^2 + 1)^2 | x^6 + 2*x^4 + 2*x^3 + x^2 + 2*x + 2 | x^6 + 2*x^5 + 2*x^4 + 2*x^3 + 2*x^2 + 2*x + 2 | x^6 + x^5 + 2*x^4 + x^3 + x^2 + 2*x + 2
28 | 6 | x^6 + 2*x^4 + x^3 + x^2 + 2 | x^6 + 2*x^5 + x^4 + 2*x^3 + 2*x + 2 | x^6 + 2*x^5 + x^2 + 2*x + 1 | (x^3 + x^2 + 2)^2 | x^6 + 2*x^4 + x^3 + x^2 + x + 2 | x^6 + x^5 + 2*x^4 + x^3 + 2*x^2 + x + 2 | x^6 + x^5 + 2*x^4 + x^3 + x^2 + 2*x + 2
29 | 6 | x^6 + 2*x^4 + 2*x^3 + x^2 + 2 | x^6 + x^5 + x^4 + x^3 + x + 2 | x^6 + x^5 + x^2 + x + 1 | (x^3 + x^2 + 2)^2 | x^6 + 2*x^4 + x^3 + x^2 + x + 2 | x^6 + 2*x^5 + 2*x^4 + 2*x^3 + 2*x^2 + 2*x + 2 | x^6 + 2*x^5 + 2*x^4 + 2*x^3 + x^2 + x + 2
30 | 6 | x^6 + 2*x^4 + 2*x^3 + x^2 + 2 | x^6 + x^5 + x^4 + x^3 + x + 2 | x^6 + 2*x^5 + x^2 + 2*x + 1 | (x^3 + 2*x^2 + 1)^2 | x^6 + 2*x^4 + 2*x^3 + x^2 + 2*x + 2 | x^6 + x^5 + 2*x^4 + x^3 + 2*x^2 + x + 2 | x^6 + 2*x^5 + 2*x^4 + 2*x^3 + x^2 + x + 2
31 | 6 | x^6 + x^5 + x + 2 | x^6 + 2*x^3 + 2*x^2 + x + 1 | x^6 + x^5 + 2*x^4 + x^3 + x^2 + 2*x + 2 | x^6 + x^5 + 2*x^4 + 2*x^3 + 1 | x^6 + 2*x^5 + 2*x^3 + 2*x^2 + 2*x + 2 | x^6 + 2*x^5 + x^3 + 1 | x^6 + 2*x^5 + x^4 + x^3 + 2*x + 1
32 | 6 | x^6 + x^5 + x + 2 | x^6 + 2*x^3 + 2*x^2 + x + 1 | x^6 + 2*x^5 + 2*x^4 + 2*x^3 + x^2 + x + 2 | x^6 + 2*x^5 + 2*x^4 + x^3 + 1 | x^6 + x^5 + x^3 + 2*x^2 + x + 2 | x^6 + x^5 + 2*x^3 + 1 | x^6 + 2*x^5 + x^4 + x^3 + 2*x + 1
33 | 6 | x^6 + 2*x^5 + 2*x + 2 | x^6 + x^3 + 2*x^2 + 2*x + 1 | x^6 + x^5 + 2*x^4 + x^3 + x^2 + 2*x + 2 | x^6 + 2*x^5 + 2*x^4 + x^3 + 1 | x^6 + x^5 + x^3 + 2*x^2 + x + 2 | x^6 + 2*x^5 + x^3 + 1 | x^6 + x^5 + x^4 + 2*x^3 + x + 1
34 | 6 | x^6 + 2*x^5 + 2*x + 2 | x^6 + x^3 + 2*x^2 + 2*x + 1 | x^6 + 2*x^5 + 2*x^4 + 2*x^3 + x^2 + x + 2 | x^6 + x^5 + 2*x^4 + 2*x^3 + 1 | x^6 + 2*x^5 + 2*x^3 + 2*x^2 + 2*x + 2 | x^6 + x^5 + 2*x^3 + 1 | x^6 + x^5 + x^4 + 2*x^3 + x + 1
35 | 8 | x^8 + x^7 + x^6 + x^5 + x^3 + x^2 + 2 | x^8 + x^6 + x^4 + x^2 + x + 2 | x^8 + 2*x^6 + x^5 + 2*x^4 + 2*x^3 + 2*x^2 + x + 2 | x^8 + x^6 + 2*x^5 + 2*x^4 + x^3 + 1 | x^8 + x^4 + 2*x^3 + 1 | x^8 + x^7 + x^6 + 2*x^3 + 2*x^2 + x + 2 | x^8 + x^7 + x^5 + x^4 + 2*x^2 + 2
36 | 8 | x^8 + x^7 + x^6 + x^5 + x^3 + x^2 + 2 | x^8 + x^6 + x^4 + x^2 + x + 2 | x^8 + 2*x^6 + 2*x^5 + 2*x^4 + x^3 + 2*x^2 + 2*x + 2 | x^8 + x^6 + x^5 + 2*x^4 + 2*x^3 + 1 | x^8 + x^4 + x^3 + 1 | x^8 + 2*x^7 + x^6 + x^3 + 2*x^2 + 2*x + 2 | x^8 + x^7 + x^5 + x^4 + 2*x^2 + 2
37 | 8 | x^8 + 2*x^7 + x^6 + 2*x^5 + 2*x^3 + x^2 + 2 | x^8 + x^6 + x^4 + x^2 + 2*x + 2 | x^8 + 2*x^6 + x^5 + 2*x^4 + 2*x^3 + 2*x^2 + x + 2 | x^8 + x^6 + x^5 + 2*x^4 + 2*x^3 + 1 | x^8 + x^4 + x^3 + 1 | x^8 + x^7 + x^6 + 2*x^3 + 2*x^2 + x + 2 | x^8 + 2*x^7 + 2*x^5 + x^4 + 2*x^2 + 2
38 | 8 | x^8 + 2*x^7 + x^6 + 2*x^5 + 2*x^3 + x^2 + 2 | x^8 + x^6 + x^4 + x^2 + 2*x + 2 | x^8 + 2*x^6 + 2*x^5 + 2*x^4 + x^3 + 2*x^2 + 2*x + 2 | x^8 + x^6 + 2*x^5 + 2*x^4 + x^3 + 1 | x^8 + x^4 + 2*x^3 + 1 | x^8 + 2*x^7 + x^6 + x^3 + 2*x^2 + 2*x + 2 | x^8 + 2*x^7 + 2*x^5 + x^4 + 2*x^2 + 2
```

*Committed before any key material opens. Offered, not self-filed; countersign gates the record. The key opens next.*
