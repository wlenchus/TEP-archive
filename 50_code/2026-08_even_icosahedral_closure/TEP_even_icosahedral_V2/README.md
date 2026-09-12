# The even-icosahedral summit campaign — COMPLETE ARCHIVE v2 (2026-08-03/04)

Supersedes the v1 archive (`TEP_even_icosahedral_20260803-04.zip`), which was cut immediately after the
Crespo grade and therefore lacks the cross-verification supplement, the errata, the citable datasets,
the Klein/budget dictionary, the session-C script bundle, and the final starter.

**What this is.** First Hecke-eigenvalue data for even icosahedral 2-dimensional Galois representations,
at the two minimal prime conductors (Doud-1951 and Doud-2141) — decoded blind from Sym²-shadow emission
plus functional-equation constraints under commit-before-keys discipline, adversarially verified, and
independently confirmed by an open Crespo-genre trace-form construction.

## Verdict chain (each link has its own record and scripts here)

pre-registration → KD-1 instrument controls (floors 1.6–3.2e-15; complex-nebentypus control matching the
exact Gauss-sum ε to 2.3e-16) → GATE-M solver qualification on planted rungs (beam + exhaustive-prefix
families pass; single-path families fail — recorded, not hidden) → **Doud-1951**: 67 bits (58 visible),
cert-residual 8.957e-15, conductor blind-selected at exactly 1951, parity measured **sin-type**
(ρ̃(c) = −I; representation still even, det ρ̃(c) = +1), orientation B, ε = +0.885096 − 0.465408i, port
meter G_new = 2 to 2.2e-14 → **sealed COMMIT** (SHA-256 before any lift literature) → five verification
avenues: 30-dps recomputation (7.2e-15), Gauss-sum ε/u lock (2.6e-10 onto μ₁₀), disjoint-grid hold-out
re-decode (67/67), no-1-flip-repair (53/58 unrepairable; 5 boundary bits re-tiered e-12-grade), det-1
battery (honest null, structural) → **Doud-2141 on demand** (~40 min): 8 live cells, unique winner
(ν-order 5, odd port, orientation A) at 4.057e-15, ε-lock 7.2e-16, and a new measured fact — nebentypus
**order 5 selected where order 10 was equally admissible** → **CRESPO CONSTRUCTION GRADE: PASS, both
fields** — 65/65 agreement modulo exactly one quadratic character per field (χ₋₁₉₅₁, χ₋₂₄; each unique
among ~24,000 fundamental candidates), γ non-square at all 221/231 involution-class primes (2.A₅
signature, 2⁻²²¹), FE-seals resolving the index-denominator bits to the committed values and reproducing
the committed residuals to the last digit (8.957e-15; 4.854e-15).

**Read the parity claim precisely** (see `records/erratum_totpos_framing_20260804.md`): det(I + U) ≥ 0 is
an *identity* for U ∈ SO(5), so total positivity of γ carries no information; constructed lifts are
cos-type by identity, and the measured sin-type partners rest wholly on the **measured oddness of the
twist characters**.

## Layout

- `records/` — every pre-registration, the sealed commit, both RESULTS docs, the verification addendum,
  the cross-verification supplement (with the full per-prime correlation tables and twist-uniqueness
  scans), both errata, the Crespo grade, session logs C and D (D carries the foundations arc: the
  A0–T4 axiomatization program, thesis-positioning, the dual-face refinements, the standing overclaim
  stamps), the countersign ledger, the final starter, and the SHA-256 manifest (v6–v6e).
- `datasets/` — **`hecke_eigenvalues_doud1951.csv`, `hecke_eigenvalues_doud2141.csv`**: the citable
  artifact. Per prime: projective class, j₅, decoded sign bit, |a_p| symbol, a_p in exact form
  (b·ζ₁₀^{j₅}·m), numeric real/imaginary parts, and the nebentypus value χ(p). Euler factor is
  1 − a_p·p^{−s} + χ(p)·p^{−2s}. `verify_dataset.py` rebuilds the L-series *from the CSV alone* and
  re-certifies: 2.2e-12 (1951) and 4.1e-13 (2141) — the floors set by the CSV's 12-decimal rounding,
  confirming faithfulness; exact values are recoverable from the symbolic column.
- `instrument/`, `qualification/`, `summit_1951/`, `verification/`, `summit_2141/`, `crespo_grade/` —
  the pipeline as run: exact-Bessel kernels and controls; planted ladders and every solver family
  (including the failures); decode drivers and cell outputs; the five verification avenues; the 2141
  emission rebuild with its validated p-adic face decider; the open construction and both grades.
- `klein_budget/` — `klein_budget.gp`: machine verification of Klein's icosahedral syzygy
  (T² = 1728f⁵ − H³, exact) and the modular twin (E₄³ − E₆² = 1728Δ), plus the budget chart they force
  (u = 1728/j; seam at z = i, the Fricke fixed point). Companion record in `records/`.
- `bundles/` — `SCRIPTS_BUNDLE_C_20260804.txt` (sha256 66332155…): all session-C scripts concatenated,
  the single-file regeneration source.
- `shared_inputs/` — certified session-A inputs reused (Doud-1951 emission table, dihedral-229 control
  table, degree-3 kernel grid).

## Reproduction

PARI/GP ≥ 2.15; Python 3 with numpy/scipy/mpmath. Deterministic, fixed seeds. Order: `run_controls.py`
→ `qualify4.py 2089 S2` → `summit_base.py` → verification scripts → `emit2141.gp` / `decider2.gp` /
`rho3_2141.py` / `summit2141.py 0..7` → `crespo.gp` + `crespo_seal.py` (+ 2141 twins) → `make_dataset.py`
+ `verify_dataset.py`. Per-file digests in `records/PROVENANCE_MANIFEST_v6_addendum_20260803.txt`.

## Status language

All results are offered-not-self-filed at PoC numerical fidelity, countersign-gated. Open and named:
rigorization (Turing-method; Palojärvi–Zhao 2508.03023), the eigenfunction itself, Artin holomorphy
(untouched by numerics), the 1951 mid-band and the ramified eigenvalue u ∈ {ζ₁₀³, ζ₁₀⁸} pending the
odd-port Atkin–Li constant, the Crespo-formula literature citation pin, and the four remaining Doud
fields. — Compiled 2026-08-04/05.
