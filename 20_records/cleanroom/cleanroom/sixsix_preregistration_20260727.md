# Six-for-six pre-registration — EVEN-icosahedral (the corner), 3-dim Sym²ρ̃ entirety certificates across ALL Doud prime-conductor fields — 2026-07-27 (~11:00Z, blind-decode session)

**Mountain line, first:** even-icosahedral, the corner. These are 3-dim **shadow** certificates — the dataset stage (queue d), not the summit. The summit remains the 2-dim even-icosahedral emission under the blind-decode seal per `session_opening_20260727T0820Z_DECISION...`. Nothing here opens any lift material.

**Status: pre-registration, lodged before any new-target computation.** Targets below have not been run. Countersign gates the result stamps; execution proceeds under the standing queue (d) as discussed at session opening.

## Instrument (rebuilt and known-answer-validated this session, before this prereg)

The certified poc2/poc3/poc4 stack, regenerated from `SCRIPTS_BUNDLE.txt`: 21/21 manifest-hashed scripts byte-identical; emission tables byte-identical (`classesX_doud1951` = a9742b02…, `classesX_corpus` = f2dd7649…, `classes_dih229` = f457d5a2…) after independently re-implementing the index-prime repair (four fixes at p = 2,7,71,137 → 3A,2A,2A,3A, exactly as RESULTS §3 documents) and recovering the emission-range convention (pmax = 16·p rounded up to the next 1000: doud 32000, corpus 75000 — this rule was not in the bundle; now scripted in `fix2.gp`); both kernel grids bit-identical (f2045292…, 82164460…). Known-answer reruns: control-1 residual 1.032e-12; Doud-1951 2.161e-14, unique blind minimum at 1951², negatives 4.1e-2/3.5e-2/1.0e-1; corpus 9.697e-15 at gauge (−1,+1,+1) unique among sixteen, unique blind minimum at 21473956. One byte-level non-match, disclosed: `poc3_results.json` (float last-ulp/BLAS formatting; all displayed quantities reproduce).

## Targets (all six Doud prime-conductor even-icosahedral fields; 1951 already certified, rerun as control)

Polynomials dual-source-fetched (arXiv math/0405534 + BYU author PDF, coefficient-identical; 1951 = known-answer transcription check passed) and **verified on this machine**: each irreducible, polgalois A₅ (order 60), signature [5,0] (totally real), fielddisc = p⁴, single prime above p with (e,f) = (5,1) — tame e = 5, type 3a. Content-keyed table (conductor: polynomial | index factorization | index primes in emission range → repair class | emission pmax):

- **2141**: x⁵−x⁴−856x³+4025x²+28501x−40877 | index 3³·43·2689 | 3→2A, 43→3A, 2689→2A | 35000
- **3701**: x⁵−x⁴−1480x³−18209x²+2191x+9683 | index 3²·89·2621 | 3→2A, 89→3A, 2621→3A | 60000
- **3821**: x⁵−x⁴−1528x³−1987x²+16629x−12281 | index 719·991 | 719→3A, 991→3A | 62000
- **8501**: x⁵−x⁴−3400x³−41825x²+671511x−966731 | index 17·8144029 | 17→2A (8144029 beyond range) | 137000
- **9461**: x⁵−x⁴−3784x³+2649x²+2960082x−2781864 | index 2·3⁵·1157327 | 2→3A, 3→2A (1157327 beyond range) | 152000

No field has a 5-cycle at an in-range index prime — the Vandermonde face-sign route applies everywhere without generator-shift. **Deviation disclosed:** 8501 is included (queue d listed four; Doud–Moore list has five remaining; six-for-six > five-for-five for the dataset claim).

## Per-field protocol (identical to the certified design; no tuning knobs)

Emission at the stated pmax with the index repair; Chebotarev soft-gate on class counts (expected fractions [1A,2A,3A,5A,5B] ≈ [1/60, 1/4, 1/3, 1/5, 1/5]). Then: gauge scan (2 ramified signs × 2 face-swaps), theta-relation residual on the certified t-grid at predicted **N = p²**; ε measured; **blind conductor scan** (same multiplier set); negative battery (face-scramble 30%, class-scramble 20%, odd-port gamma; same seeds as certified: 20260727/1951); **G_new port meter** at best gauge (expect 2 ± ~1e-13; jet fit logged).

## Pre-registered expectations and kill/report conditions

Expected per field: residual ≲ 1e-13 at a unique gauge; ε = +1 (the certified pair's precedent; a measured −1 is a reportable surprise, itemized, not silently absorbed); blind-scan unique minimum at exactly p²; negatives ≥ 9 orders above floor; G_new = 2 at ~1e-13. **KF-1** — the Doud-1951 control (rerun first in the same driver) drifts from 2.161e-14 by > 1 order → stop, fix pipeline only, never touch new-field data. **KF-2** — a field's best residual large/unstable with controls clean → report as-is with t-profile and the G_new pole-vs-corruption sign diagnostic; a pole signature at the corner is Artin-relevant data; NO tuning toward success. **KF-3** — conductor-scan minimum not at p² → claim downgraded per KP-4, reported. **KF-4** — gauge degeneracy (two sign choices at floor) → reported as measured, no adjudication by preference. Scope line, pre-committed: PASSes are numerical entirety/automorphy-consistency certificates at PoC fidelity (float64 + spline, validated floor ~1e-12, modest t-window, no rigorous tails) — evidence, not theorem; rigorization remains queue (f).

*Offered, not self-filed. The honest-bite paragraph of any results record gets written before its headline, per the standing control.*
