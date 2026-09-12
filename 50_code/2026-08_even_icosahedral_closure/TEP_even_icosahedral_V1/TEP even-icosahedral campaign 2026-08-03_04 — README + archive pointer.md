THE EVEN-ICOSAHEDRAL SUMMIT CAMPAIGN — 2026-08-03/04 (sessions C \+ verification \+ 2141 \+ Crespo grade)

&nbsp;

Full archive: TEP\_even\_icosahedral\_20260803-04.zip (118 files, 393 KB), delivered in the Claude conversation of 2026-08-04.

sha256: 260512aa3092e0aedfd8f47496cc8294dd6fcb58901ba3b5a8820e9adcd91132

All records also live in the claude.ai project "2026-07-26" under cleanroom/ (manifest v6-v6d).

&nbsp;

WHAT THIS IS

First Hecke-eigenvalue data for even icosahedral 2-dimensional Galois representations, produced by blind seam-constraint decoding at the two minimal prime conductors (Doud-1951 and Doud-2141), adversarially verified, and confirmed by an independent open Crespo-genre construction.

&nbsp;

VERDICT CHAIN

Pre-registration \-\> KD-1 instrument controls (1.6-3.2e-15 floors; complex-nebentypus control with Gauss-sum epsilon match 2.3e-16) \-\> GATE-M solver qualification on planted rungs (beam \+ list families pass; single-path families fail, recorded) \-\> Doud-1951 decode: 67 bits (58 visible), cert-residual 8.957e-15, conductor blind-selected at exactly 1951, parity measured sin-type (rho(c) \= \-I), orientation B, eps \= \+0.885096 \- 0.465408i, port meter G\_new \= 2 to 2.2e-14 \-\> sealed COMMIT (SHA-256 before any lift literature) \-\> five verification avenues: 30-digit recomputation (7.2e-15); Gauss-sum eps/u lock (2.6e-10 onto mu10); disjoint-grid hold-out re-decode 67/67; no-1-flip-repair (53/58 unrepairable, 5 boundary bits e-12-grade); det-1 battery honest null \-\> Doud-2141 on demand (\~40 min): 8 live cells, unique winner (nu-order 5, odd port, orientation A) at 4.057e-15, eps lock 7.2e-16, new arithmetic: nebentypus order 5 selected over admissible order 10 \-\> CRESPO CONSTRUCTION GRADE: PASS both fields. Constructed spin lift agrees 65/65 with committed bits modulo one global quadratic character per field (chi\_-1951; chi\_-24) — the pre-declared twist-family freedom; gamma non-square at all 221/231 involution-class primes (2.A5 unique-involution signature, confidence 2^-221); gamma totally positive at 1951, deriving the measured sin-type parity via the odd twist; FE-seals resolve the index-denominator bits to exactly the committed values, reproducing committed residuals to the last digit (8.957e-15; 4.854e-15).

&nbsp;

ARCHIVE LAYOUT

records/ (pre-registrations, commit, results, verification addendum, Crespo grade, session log, countersign ledger, starter, SHA-256 manifest) ; instrument/ (instr2.py kernels+theta+meter+solvers; controls) ; qualification/ (planted ladder, amendments R1/R1.w, solver families incl. recorded failures) ; summit\_1951/ (decode drivers, cell outputs, committed 67-bit bundle) ; verification/ (five avenues \+ internal graders) ; summit\_2141/ (emission rebuild incl. validated p-adic face decider, rho3 re-certification, 8 cells, batteries) ; crespo\_grade/ (construction \+ both grades) ; shared\_inputs/ (certified session-A tables).

&nbsp;

REPRODUCTION

PARI/GP \>= 2.15; Python 3 \+ numpy/scipy/mpmath. Deterministic, fixed seeds. Order: run\_controls.py \-\> qualify4.py 2089 S2 \-\> summit\_base.py \-\> verification scripts \-\> emit2141.gp / decider2.gp / rho3\_2141.py / summit2141.py 0..7 \-\> crespo.gp \+ crespo\_seal.py (+ 2141 twins).

&nbsp;

STATUS

All results offered-not-self-filed at PoC numerical fidelity, countersign-gated (see countersign\_ledger). Open: rigorization (Turing-method), the eigenfunction itself, Artin holomorphy (theorem-level, untouched by numerics), 1951 mid-band/u completion, Crespo-formula literature citation pin, remaining Doud fields (3701, 3821, 8501, 9461).

&nbsp;

— Compiled by Claude at Will Copeland's direction, 2026-08-04.