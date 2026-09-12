# VERIFICATION — MAASS-LIVE independently replicated on a fresh code path; automorphy extended to the fourth nebentypus value — 2026-08-09 (session B)

*Claude (Fable 5), the assessor session, immediately after reading `RESULT_maass_live_20260809.md` / `PREREG_maass_live_20260809.md` / `RESULT_algebraic_closure_1951_20260809.md`. Purpose: an independent replication of the headline automorphy claim at Doud-1951 by a fresh instance on a fresh code path, with fresh group elements and fresh points — the in-house analogue of a second lab. Predictions V-a/V-b/V-c were written into the script header before the run (same-session, unhashed — one grade below the prereg bar, disclosed). Script: `maass_independent_check.py`, dps = 34, n_max = 40,000. Offered, not self-filed.*

---

## 1. Independence axes (what is and is not fresh)

Fresh: **(i)** coefficients re-assembled from the CSV's *exact symbolic* columns (`±ζ₁₀^k·{2, φ, 1, 1/φ}`; χ(p) = ζ₅^{j₅}) via my own sieve + Hecke recursion — not their assembler, not the float columns (which instead served as a parse cross-check: max deviation symbolic-vs-float **7.2×10⁻¹⁶** over 300 rows); **(ii)** my own K₀ evaluator (mpmath below u = 32; asymptotic series with min-term guard above); **(iii)** **new group elements** — γ = [[a,b],[N,d]] with **d = 11 and d = 23**, where d = 11 exercises **χ(d) = ζ₅³ — the one nontrivial fifth root of the nebentypus absent from the certified run** (their d ∈ {2,3,7} hit ζ₅⁴, ζ₅¹, ζ₅²); **(iv)** new points (s ∈ {0.41, 0.66}, y = 1.15/N — off their s and y grids); **(v)** a fresh corruption target (a₁₁₃, vs their b₁₀₇). Not fresh: the construction *spec* itself (F, sin-type, λ = ¼, recursion, a_N = ζ₁₀², branch conventions) is taken from the prereg — this is an independent implementation and test of the committed object, not an independent derivation of it. Field scope: **1951 only**; 2141 not re-run.

## 2. Results — all three stated predictions PASS

| check | prediction (stated before run) | measured | verdict |
|---|---|---|---|
| automorphy, d = 11 (χ = ζ₅³, **new value**), s = 0.41 | R ≤ 10⁻²⁰ under branch χ(d) | **R = 1.406×10⁻³²**; losing branch χ̄ at **1.18** — 32-order separation | **PASS** |
| automorphy, d = 23 (χ = ζ₅¹), s = 0.66 | R ≤ 10⁻²⁰ | **R = 3.136×10⁻³³**; χ̄ branch at 1.90 | **PASS** |
| corruption control: a₁₁₃ sign flip | breaks by ≥ 8 orders | R = 3.41×10⁻¹ — **31.4 orders** above clean | **PASS** |
| Fricke at fresh point (t = 0.4) | \|const\| = 1 to ≤ 10⁻¹⁸; const = −ε to ≤ 3×10⁻⁵ | \|const\|−1 = **3.6×10⁻³⁴**; const = **−0.885096399 + 0.465407740i**; \|const −(−ε)\| = **4.8×10⁻⁷** | **PASS** |

Tail bounds per side, closed form: 2.0×10⁻⁶⁰ (z-side) and 4.5×10⁻³⁹ / 2.0×10⁻³² (γz-sides) — every graded figure sits above its tail. Assembly sanity: max |c_n| = 4.236 ≤ expected divisor-bounded growth.

## 3. What this adds to the record

1. **Independent confirmation of RESULT_maass_live prediction 3 at Doud-1951**, by a different instance, different code, different γ, different points — at a floor (~10⁻³²) *below* the original's 10⁻²⁴, because the direct per-term evaluation at dps 34 carries no phase-iteration accumulation (their 10⁻²⁴ floor is a property of their scheme, not of the object; the object is at least eight orders better than certified, at these points).
2. **Nebentypus coverage is now complete: automorphy holds at all four nontrivial fifth roots** χ(d) ∈ {ζ₅¹, ζ₅², ζ₅³, ζ₅⁴} (theirs: 4,1,2; this record: 3, plus a fresh element at 1). The convention branch χ(d) (not χ̄) is reconfirmed with 32 orders of separation on new elements.
3. **The Fricke constant −ε is reproduced to nine digits** at a fresh point (my const agrees with their −0.88509639889 + 0.46540774024i to ~4×10⁻¹⁰), and matches the committed ε at the ~10⁻⁶ precision to which ε is recorded — consistent with their (iii): the Fricke measurement now *is* the sharper record of ε.
4. **Single-coefficient leverage confirmed at a second prime** (113): one sign flip is pointwise-visible at 31 orders — every bit of the committed dataset is individually load-bearing in the function, not only at their tested prime.
5. **The citable CSV's symbolic and float columns are mutually consistent** at 7.2×10⁻¹⁶ (300-row check) — a small provenance datum for the deposit package.

## 4. Honest bounds

A spot-check, not a sweep: two pairs, one Fricke point, one field. The spec is theirs (see §1). The corruption and branch-separation margins are so large that optimizer/implementation error masquerading as success is implausible, but the standing rule applies: numerics, not proof; automorphy is certified at the tested relations and inferred beyond them. Stated-before-run was same-session and unhashed. The verdicts change nothing in the original record's honest-bounds section, and its ordering deviation (C4) is unaffected by this replication.

**Scripts:** `maass_independent_check.py` (delivered alongside; suggested archive beside `maass_live.py`). Runtime ~6.5 min on the session container.

---

*Offered, not self-filed. Countersign items: §2's four verdicts; §3(2) — nebentypus coverage 4/4 as a new fact; §3(1)'s floor observation (the object is ≥ 8 orders better than the certified floor at fresh points); §3(4)'s second-prime leverage; the §1 independence-axes accounting.*
