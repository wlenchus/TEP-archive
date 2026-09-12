# The even-icosahedral summit campaign — sessions of 2026-08-03/04

First Hecke-eigenvalue data for even icosahedral 2-dimensional Galois representations, produced by
blind seam-constraint decoding at the two minimal prime conductors (Doud-1951 and Doud-2141),
adversarially verified, and confirmed by an independent open Crespo-genre construction.

**Verdict chain:** pre-registration → KD-1 instrument controls (1.6–3.2e-15 floors, complex control
Gauss-ε match 2.3e-16) → GATE-M solver qualification on planted rungs → 1951 decode
(67 bits, cert 8.957e-15, blind N, sin-type parity, ε Gauss-lock 2.6e-10) → sealed COMMIT →
five verification avenues (30-dps recompute; ε/u lock; disjoint-grid hold-out 67/67;
no-1-flip-repair; det-1 null) → 2141 on demand (8 cells, winner 4.057e-15, ε lock 7.2e-16,
nebentypus-order question answered: 5 not 10) → **Crespo construction grade: PASS both fields**
(65/65 mod one quadratic character each; γ non-square at all 221/231 involution primes;
FE-seals reproduce committed residuals to the last digit; parity derived via γ total positivity).

## Layout

- `records/` — all pre-registrations, the sealed commit, results, verification addendum, the
  Crespo grade, session log, countersign ledger, starter, and the SHA-256 manifest (v6–v6d).
  Read `decode2dim_RESULTS_20260803.md` → `decode2dim_VERIFICATION_addendum_20260804.md` →
  `decode2141_RESULTS_20260804.md` → `decode2dim_CRESPO_GRADE_20260804.md` for the arc.
- `instrument/` — `instr2.py` (exact 4K₀(2y)/4yK₀(2y) kernels, complex two-arm theta, ε-fit,
  ε-folded port meter, sparse flip machinery, solvers S1–S3); `run_controls.py` + `controls2.json`
  (KD-1); `ctrl_complex.py` (complex-nebentypus control); `alpha_chars.txt`.
- `qualification/` — planted-ladder generators (GP), the R1/R1.w amendments, solver-family scripts
  (qualify*.py, s5.py), all qualification outcomes incl. the recorded failures (S1/S3/S4).
- `summit_1951/` — decode drivers (cells, consensus, S5b, battery, mid-band), character/twist
  tables, all cell outputs, `DECODE_COMMIT_bundle.json` (the committed 67-bit table).
- `verification/` — the five post-commit avenues (mpmath recompute, Gauss ε/u lock, hold-out,
  flip-repair, det-1) + internal graders (conjugate-cell transport, Chebotarev).
- `summit_2141/` — emission rebuild (GP incl. the validated p-adic face decider `decider2.gp`),
  ρ₃ re-certification, the 8 decode cells, batteries/consensus.
- `crespo_grade/` — the open construction (trace form → rational isometry → γ = det(I+U) →
  per-prime square tests) and both grades with FE-seals.
- `shared_inputs/` — session-A certified inputs reused today: the Doud-1951 emission table
  (index-prime-patched), the dihedral-229 control table, the degree-3 kernel grid.

## Reproduction

Environment: PARI/GP ≥ 2.15, Python 3 with numpy/scipy/mpmath. Everything regenerates
deterministically; fixed seeds throughout. Suggested order: `run_controls.py` (gates) →
`qualify4.py 2089 S2` (gate check) → `summit_base.py` (the four 1951 cells) → verification
scripts → `emit2141.gp`/`decider2.gp`/`rho3_2141.py`/`summit2141.py 0..7` → `crespo.gp` +
`crespo_seal.py` (and the 2141 twins). Per-file SHA-256 digests: `records/PROVENANCE_MANIFEST_v6_addendum_20260803.txt`.

Status language: all results are offered-not-self-filed at PoC numerical fidelity, countersign-gated,
with open items (rigorization, eigenfunction, Artin holomorphy, mid-band/u completion, citation pin)
listed in the records. — Compiled 2026-08-04.
