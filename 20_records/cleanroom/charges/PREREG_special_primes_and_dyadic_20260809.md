# PRE-REGISTRATION — index-prime construction bits and the 2-adic γ-test — 2026-08-09

**Goal (the reviewer's named prize):** an exact algebraic algorithm for a_p at ALL unramified primes of Doud-1951, including p = 2 — closing the last two FE-resolved rows per field where the arithmetic permits.

## Standing results this rests on (all machine-verified this session, before any prediction below was tested)

1. **The "returned no rows" mystery is solved, with evidence.** The first maximal-order emitter produced γ = 0 at every prime because the qfsolve orthonormal frame of the zk Gram satisfies Σₖ bₖ = −1 *exactly* (frame-sum element = −1 ∈ 𝒪), so U·j = −j for the permutation-invariant all-ones vector j, and det(I + P_σU) = 0 identically over all 120 orderings at every prime (verified by full ordering scans at p = 3…29). The failure was **representational — a degenerate frame** — not arithmetic: Gram = field disc, BᵀGB = I, and UᵀU = I all hold exactly. Values were computed; they were all literally zero.
2. **Fix:** unimodular basis change (reversal) before orthonormalization → nondegenerate frame; 9,586/9,587 signs emitted to 10⁵ at 1951/2141 with zero double-zero skips. Frame data: isometry denominators {5, 1951} at 1951; {2141} at 2141.
3. **Sign-equivalence gate: PASSED with structure.** Against the validated power-basis gauge on all clean overlap primes: involution (2A) primes agree 2391/2391 and 2411/2411 (γ non-square in both frames — the frame-independent 2.A₅ signature); off-involution the discrepancy is EXACTLY one quadratic character per field: **d₀ = 78040 = 8·5·1951** (7195/7195 non-2A primes) and **d₀ = 12** (7176/7176) — supported precisely on the frame data, the expected spinor-norm-type frame-change law. Fit found by masked search after the full-set fit correctly failed (2A masks any character).
4. **End-to-end validation of the max gauge:** with the committed relation b_p = orient(cls)·sq·χ(p)·(−1)^(j₁₀(p) mod 2) (per crespo_seal.py line 78 / seal2141.py line 43; j₁₀ = committed ζ₁₀-exponent from the CSV, verified ≡ chilog on all 675 overlap rows), the orientation constants are CONSTANT per class in both gauges at both fields: 1951 {1A:+1, 3A:−1, 5A:−1, 5B:+1} (orientation B), 2141 {1A:+1, 3A:−1, 5A:+1, 5B:−1} (orientation A) — the max gauge additionally carrying χ_{d₀}.

## Predictions (stated NOW, before running; classes labelled per the standing convention)

| target | class | committed | prediction | label |
|---|---|---|---|---|
| p=137 @1951 (index prime) | 3A | b = −1, a = −ζ₁₀³ | **sq_max(137) = +1** | novel |
| p=43 @2141 (index prime) | 3A | b = −1, a = −ζ₁₀³ | **sq_max(43) = −1** | novel |
| p=7, 71 @1951; p=3, 2689 @2141 | 2A | a_p = 0 | **γ NON-SQUARE at all four** (frame-independent; valid even at p=3 where d₀=12 ramifies) | structural/2.A₅ |
| p=2 @1951 (the prize) | 3A | b = +1, a = +ζ₁₀⁴ (j₁₀=4) | **γ 2-adically UNRAMIFIED-INERT: v₂(γ) even AND 5·γ/2^{v₂} ≡ □ mod 8𝒪** (power gauge; χ₋₁₉₅₁(2)=+1, orient(3A)=−1, branch(4)=+1 ⟹ sq₂ = −1) | novel |
| p=2 @2141 | 5A | b = −1 | **γ 2-adically RAMIFIED** (χ₋₂₄ ramified at 2 — arithmetic obstruction, consistent) | pattern |

Component transparency, 137@1951: orient_max(3A)=−1, χ₋₁₉₅₁(137)=−1, χ₇₈₀₄₀(137)=+1, branch(j₁₀=3)=−1, b=−1 → sq = (−1)·(−1)·(−1)·(+1)·(−1) = +1. 43@2141: orient=−1, χ₋₂₄(43)=−1, χ₁₂(43)=−1, branch(3)=−1, b=−1 → sq = −1.

## Procedures (fixed before running)

- **Odd special primes — residue-embedding route.** idealprimedec at p (all unramified in 𝒪; disc = N⁴); for each prime ideal of residue degree f, the f embeddings into 𝔽_{p^m} (m = lcm f) via nfmodpr + ffembed + Frobenius powers; V₀[i,j] = embedding_i(W′_j) on the SAME tweaked basis W′ and isometry B as the gate; U = V₀·B mod p; γ = det(I+U); if 0, swap first two rows once; square test by γ^((p^m−1)/2). **Precondition (must pass before specials count):** this route reproduces the polynomial-evaluation route's sq exactly at ≥30 clean primes spanning all classes. (Ordering freedom is empirically harmless: full 120-ordering scans show sq constant on all nonvanishing orderings.)
- **p=2 — 2-adic route (power gauge, both fields).** factorpadic(P,2,K) (handles the index correctly); ℚ₂-roots from linear factors; roots of the unramified degree-m factor by independent Hensel lifts in R = ℤ₂[t]/(C_m) mod 2^K (C_m a lifted Conway polynomial), K = 60; V₀ = power Vandermonde of the five roots (2-integral); B̃ = 2^s·B_pow with s = −min v₂(entries) (assert B̃ 2-integral); D = det(2^s·I + V₀·B̃); γ = D/2^{5s}. If v₂(D) ≥ K/2 (degenerate ordering), swap two roots once. Classify: v₂(γ) odd → RAMIFIED; else u = γ/2^{v₂}: u ≡ □ mod 8𝒪 → SPLIT (+1); 5u ≡ □ mod 8𝒪 → INERT (−1); else → RAMIFIED (unit type). Squares enumerated exhaustively in (𝒪/8)ˣ (512 elements at m=3; 32768 at m=5). 5 is non-square in odd-degree unramified extensions (norm argument) and K_m(√5)/K_m is unramified — so the 5-class IS the inert class.
- **Kill conditions.** (i) Route-equivalence check fails → specials do not count, diagnose first. (ii) Any odd special prime disagrees with its prediction → transport across index primes REFUTED at that prime; record as refutation, no adjustment. (iii) γ ramified at 2@1951 → the dyadic closure at 1951 is REFUTED (χ₋₁₉₅₁ is unramified at 2; no escape hatch). (iv) γ unramified at 2@2141 → the arithmetic-obstruction reading is wrong; record loudly.

**If all pass:** the two FE-resolved rows at 1951 (p=2, 137) upgrade to construction-graded provenance; 1951's dataset becomes derivable by exact algebra at every unramified prime — the reviewer's stated completion criterion for the algebraic side. At 2141, p=43 upgrades; p=2 remains arithmetic-obstructed with the obstruction now demonstrated rather than asserted.

*Offered, not self-filed. Predictions and procedures fixed before execution; scripts maxsigns3.gp / gate_signs2.py / measure_orient2.py already run (calibration), special_nfmodpr.gp / dyadic_gamma.gp to be run next.*
