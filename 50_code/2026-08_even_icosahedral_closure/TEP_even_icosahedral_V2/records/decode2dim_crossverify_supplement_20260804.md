# Cross-verification supplement (Will's four items) — 2026-08-04

## 1. Total-positivity stdout, BOTH fields (`totpos_BOTH_stdout.txt`, script `totpos2.gp`)

Run fresh this session over ALL 120 orderings per field (the ~60 nonvanishing determinants are γ's conjugates; the vanishing coset is the improper-orthogonal branch):

```
Doud-1951: nonvanishing conjugates 60 of 120;  NEGATIVES = 0;  min = 6.609e-5   max = 13.5888
Doud-2141: nonvanishing conjugates 60 of 120;  NEGATIVES = 0;  min = 0.0024074  max = 10.5482
```

Both γ totally positive ⟹ both constructed lifts have ρ(c) = +I (untwisted parity = +I₂, as you put it). Note the epistemics: for 1951 this re-confirms the earlier run; **for 2141 it was a prediction I had inferred but not measured until now** (χ₋₂₄ odd forces it) — filed as a fresh falsifiable check, and it held. Both committed sin-type parities are therefore derived: constructed(+I) ⊗ odd-twist = committed(−I), at both fields.

## 2. Full per-prime correlation tables (`corr_table_1951.txt`, `corr_table_2141.txt`)

65 rows each, format `p : class_label : j₅ : b_committed : γ-square(±1) : b_constructed(det-1) : corr : kron(d_twist, p)` with d_twist = −1951 (field 1951) and −24 (field 2141). In both tables the last two columns agree on every row — corr(p) = χ_twist(p) exactly, 65/65. (2141's committed convention: ν order 5, odd port, orientation A: dictionary {1A: sq→+1, 3A: sq→−1, label-3 (1/φ-face): sq→+1, label-4 (φ-face): sq→−1}; det-1 transport b⁰ = b·(−1)^{j₅}.)

## 3. Twist uniqueness

Scan over **all fundamental discriminants |d| ≤ 20,000 plus the field-specific specials** (±N, ±4N, ±8N; ~24,000 candidate characters per field), agreement of corr(p) with kron(d, p) on all 65 primes:

- Field 1951: **exact matches: d = −1951 only.** Runners-up: 46/65 (d = 13313), 46/65 (−5087), 45/65 (5116), …
- Field 2141: **exact matches: d = −24 only.** Runners-up: 47/65 (7069), 44/65 (12401, 4349, −4727, −7496), …

Chance agreement is ~32/65; the extreme-order statistics of ~24,000 random draws predict a best-of-scan near 45–47 — which is exactly where the runners-up sit. The 65/65 matches stand ~19 bits beyond the entire chance tail: **one and only one character works per field**, and each is odd, as the parity closure in §1 independently requires. (Note −7804 = −4·1951 and −96/−216/−384 = −24·{4,9,16} reported earlier are the same characters as −1951 and −24; the scan above dedupes to fundamental discriminants.)

## 4. Provenance of construction-vs-decode independence

Three independent layers, strongest last:

**(a) Container mtimes** (same-machine, self-reported; full-iso):
```
2026-08-03 21:32:11  gp2/DECODE_COMMIT_bundle.json      (the committed 67-bit table)
2026-08-03 21:33:14  decode2dim_COMMIT_20260803.md      (the sealed commit record)
2026-08-04 00:32:52  decode2dim_VERIFICATION_addendum_20260804.md
2026-08-04 01:33:46  gp2/crespo.gp                      (construction script CREATED — ~4h after commit)
2026-08-04 01:33:46  gp2/crespo_signs.txt
2026-08-04 01:34:16  gp2/crespo_grade.json
2026-08-04 01:35:49  gp2/crespo_signs_2141.txt
2026-08-04 01:37:26  decode2dim_CRESPO_GRADE_20260804.md
```

**(b) Append-only manifest + server timestamps.** `PROVENANCE_MANIFEST_v6_addendum_20260803.txt` is sectioned append-only: the v6 body (lines 1–61, containing the commit bundle's sha256 `9004e181…` at line 6) closes with its own self-hash computed at the 2026-08-03 push; the Crespo artifacts enter only in the v6d section (lines 90+, `crespo.gp` = `4a6ff17d…`), appended 08-04. Independently of this container, the claude.ai project's server-side doc dates (visible to you in the project UI) show `decode2dim_COMMIT_20260803.md` and `DECODE_COMMIT_bundle_20260803.json` written on 08-03 and `decode2dim_CRESPO_GRADE_20260804.md` on 08-04, and the in-conversation tool receipts (your own transcript) fix the full ordering.

**(c) The structural argument — the strongest, because it needs no clock.** `crespo.gp`'s inputs are the quintic polynomial and nothing else: no decode output enters the construction at any point (inspect the script — it reads no summit/commit file). Its internal validation is performed on data the decode never touched: γ's non-squareness at **221 (resp. 231) involution-class primes, none of which carry committed bits**, at confidence 2⁻²²¹ — a wrong or fitted γ cannot pass it. And the comparison had full freedom to refute: 65 bits against a construction with one character of gauge freedom is a 2⁻⁶⁵-rigid test that a wrong decode fails with certainty. Timestamps say the construction came after and apart; the mathematics says it could not have been steered even if it hadn't.

*All four items regenerable from the archive (`totpos2.gp` + the grade scripts); files hashed and shipped alongside. Offered, not self-filed.*
