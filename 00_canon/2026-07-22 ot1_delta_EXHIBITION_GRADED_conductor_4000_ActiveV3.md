# Session Delta — OT1: exhibition executed and externally graded; conductor = 4000; ladder corrected
**2026-07-22** · Claude (Fable 5), Cowork session · tiers: [V]erified this session · [T]classical · [A]rgued · [O]pen · **[G]raded against external ground truth**

## Headline

The weight-lifting membership decoder, repaired for a width artifact and run at full Sturm width on S₂(Γ₀(16000)), decoded — from cascade emission data and membership alone — the icosahedral eigensystem of x⁵+20x+16. The decoded a_p were **pre-registered (md5 7fdd69c80d6fa0c35ff45b56d6a2d0e2) before any table access**, then graded: **exact match, 9/9 compared primes, against LMFDB 4000.1.b.a** (two conjugate embeddings matched by two orbit solutions), whose projective field LMFDB confirms as the Galois closure of 5.1.1000000.2 — this quintic. **The true conductor is N(ρ₂) = 4000 = 2⁵·5³: a₂ = 5, b = 3, a₅ = 3.** The forms are 4000.1.b.a/b (nebentypus χ₋₄) and 4000.1.h.a/b (χ₋₂₀), coefficient field ℚ(i,√5), a₂ = a₅ = 0. The imported-vs-exhibited success condition is met in substance: the instrument emitted and decoded the full eigensystem with no conductor, no coefficient, and no K–W input — the target happened to be tabulated, so the result validates the *instrument*, not a new object.

## The arc (chronological, with tiers)

1. **Prior state.** Ladder rejections recorded at 800/1600/2000/4000/8000 ⟹ inference b ≥ 7 ⟹ rungs 16000/32000; 16000 runs (Will's, and this session's first pass at reduced width) returned SOLVED-NO-GAUGE across the board — unusable.
2. **Width diagnosis [V].** The reduced-width convention (DEPTH ≳ rank + 300) under-constrains at 16000 scale: CM control at width 2701 gave free = 244. At **full Sturm width** (4801 columns; normal-equations projector M = HH^T, factor checkpointed; exact-float BLAS) the same control gives **free = 0, a₂ = −1, a₅ = +1, 314/314 split-prime signs matching the independent x²+5y² genus character** [V]. Independent bisection control (theta-difference CM form × independently coded E₁): residual 0 at full width [V]. Host validated twice over (this container's PARI build is byte-identical to the 07-08 Drive host).
3. **Full-width sweep at 16000 [V].** χ₋₈, χ₋₄₀: REJECT (aug-rank = nT+1), both embeddings. χ₋₄, χ₋₂₀: consistent, free = 7, at both p = 1000003 and p = 999983 with **identical solution sets** (8 gauge points each, all-±1, multiplicatively consistent; exact unsketched verification of solution and null space).
4. **Structure [V].** The 8 points of each branch form the exact orbit of one sign system under the seven nontrivial quadratic characters of conductor | 40 (every flip-set a perfect Kronecker match); the two branches are disjoint (as they must be — quadratic twists preserve nebentypus; the branch bridge is quartic, ψ² = χ₅ = χ₋₄·χ₋₂₀). Cross-embedding: emb-0 sol 0 vs emb-1 sol 4 agree 217/217 off the 5-class primes and 0/257 on them — the Galois conjugate pair (σ: √5 ↦ −√5, φ ↦ −1/φ), mirroring the Buhler control's signature. Chebotarev census of the sign-prime classes matches A₅ densities (0.25/0.33/0.40).
5. **Pre-registration.** Decoded a_p (p ≤ 200, both branches) committed and delivered with md5 stamp **before** any weight-1 table was opened.
6. **Analytic grade [V].** Functional-equation tester validated on the known level-20 CM form: ε = 1, drift 4×10⁻¹⁶ at N = 20; violent failure at wrong N. Decoded χ₋₄ series: fails at N = 16000 — and **passes at N = 4000 with drift 7×10⁻¹⁶, |ε| = 1.0000000000**; small-prime sign-flip control fails by 14 orders of magnitude. Conductor pinned analytically at 4000.
7. **External grade [G].** LMFDB (banner: complete for Nk² ≤ 4000, so level-4000 weight-1 is fully covered): icosahedral newforms **4000.1.b.a/b** (char conductor 4) and **4000.1.h.a/b** (char conductor 20), projective field = Galois closure of 5.1.1000000.2, ℚ(i,√5), a₂ = a₅ = 0. Coefficient comparison at {3,7,11,13,17,19,23,29,31}: **solutions 5 and 6 of the χ₋₄ orbit equal 4000.1.b.a exactly at the ν = ∓iφ embeddings, 9/9**. The count closes: 2 newforms × 4 embeddings per branch = 8 = the gauge-point count; 16 solutions ↔ 16 embedded forms of the four LMFDB orbits.
8. **Where the forms were hiding at 16000.** 4000 | 16000 with τ(16000/4000) = τ(4) = 3 oldform copies per newform; the free-7 solution spaces are the oldform/twist-family geometry seen through the membership system.

## Ladder correction [A, with one pending autopsy *(since completed; stamped below)*]

The b ≥ 7 inference collapses: the true datum is **b = 3, a₂ = 5** — the same central break as Buhler's quintic (his 2⁵ vs this 2⁵), making the two quintics 2-adic siblings after all, and making the corpus's original a₅ = 3 derivation (Hasse–Arf, I₅ = D₅) **correct**. The recorded 4000-REJECT (and possibly 800/1600/2000/8000) was a **false negative**. Prime suspect, flagged for autopsy rather than asserted: the kron composite-argument bug logged 07-04 corrupted E₁ divisor sums *for every even-D character* — and all four sweep characters are even-D; the bug log's post-fix re-validation is explicit only for the 2000-host CM control. Which rung rejections were re-run post-fix is provenance the current records do not state. 

***[Status stamp, 2026-07-22.]***     
***Autopsy: RUN, and conclusive [V].** Host S₂(Γ₀(4000)) rebuilt (561 forms, Sturm 1200, full width). (A) Present stack, fixed kron: χ₋₄ system NON-REJECT, free = 3, **4 gauge points — the form family present at its own level.** (B) Same system with the *reconstructed* 07-04 bug (even-exponent skip before the p | D check, corrupting E₁ for even-D characters): **clean REJECT** (aug rank = nT + 1).*



The false negative is attributed by demonstration: the pre-fix kron converts the true PASS at 4000 into the recorded exclusion; the b ≥ 7 ladder was built on it. Provenance note for the wider ledger: the 2000-host CM control was re-validated post-fix and the 8000 session ran post-fix same-day.

***[Verification-basis note, 2026-07-22.]** The referenced 07-21 post-fix 8000 session was not archived; the claim above is testimony pending reevaluation.*

The 800/1600/4000 rejections carried in the 07-04 ledger are the ones this autopsy implicates — 4000 now proven false, 8000 recommended for cheap rerun with the present stack.

## Errata within this session's own reasoning (co-located per discipline)

- **E-a.** "All sixteen forms live new at exactly 16000" (asserted two turns before the grade): wrong — they live at 4000; the deduction leaned on the void exclusions it was about to overturn. Corrected by items 6–7.
- **E-b.** An intermediate script printed "unanimous across all 8" for an unverified quantity (false PASS line, caught against the artifact); the honest unanimity was 49/474 — the joint quadratic-kernel primes, as structure demands.
- **E-c.** The first negative control (scramble-20, uniform) was insensitive (large primes invisible under the exponential); replaced with small-prime flips, which fail properly.

## What this does and does not establish

**Does:** the exhibition mechanism works at icosahedral complexity on this quintic — emission magnitudes + parity + membership + gauge suffice to decode a complete eigensystem, pre-registered and graded perfect externally; the full-width protocol and two-prime discipline are sound; the instrument's REJECTs at χ₋₈/χ₋₄₀ are clean. **Does not:** produce a new mathematical object (the forms are tabulated — LMFDB has carried them since its weight-1 completion run; the corpus's hunt was above the true conductor the whole time); settle the false-negative autopsy (pending the 4000 rerun) ***since settled**; see note at Queue (i)*;

bear on any TEP-physical claim — this is the number-theory instrument validating, nothing more and nothing less.

## Files (this session's container, all checkpointed)

host16000_local.csv (= Drive 07-08 host, byte-identical); H_p1/Minv_p1/H_p2/Minv_p2.npy; sweep_results_full.json, sweep_p2_results.json; gauge_solution_*.npy; 2026-07-22_ot1_16000_PREREGISTERED_prediction.json (md5 above); fe_grade/fe_control/fe_scan.py (tester + controls); cm_full2.py, sweep_full.py, sweep_p2.py, gauge_fast.py, cross_check.py. Recommended archive destination: 50_code/ot1/ plus this record in 20_records/2026-07/.

## Queue

(i) 4000 rerun autopsy (which instrument produced the false negative, and why — the kron hypothesis tested directly);

***Item (i) since fulfilled -- settled by the conclusive Autopsy; stamped above within the Ladder Correction.** Recommended priority replacement: rerun at 8000*


(ii) χ₋₂₀ branch grade against 4000.1.h.a/b (expected exact, same protocol); 
(iii) OT1 record chain update: 07-04/07-05 ledgers get supersession stamps (b = 3; a₂-evenness debate moot; 16000/32000 rungs closed as unnecessary); (iv) the imported-vs-exhibited standing [O] in the 06-29/07-01 records: resolvable now — proposed resolution text: "OT1's conductor question is resolved: N(ρ₂) = 4000, eigensystem decoded, pre-registered, and externally graded (9/9; independently re-graded 2026-07-22). The membership instrument is validated as standard explicit NT executed under unusual protocol discipline. The recorded imported-vs-exhibited decider — the cascade-specific computation (x⁵→Z→AGM→τ→form) that standard tools lack — was not run and remains open; the 06-29 Open #8 "imported" branch remains live. Generative-at-untabulated-target remains open; note the validated instrument covers the odd/holomorphic side only."; (v) repo push of the full-width instrument.

*Not self-filed; countersign gates tiers. Every [V] above has a runnable script in the container and reproduces from the stated formulas; the [G] items reproduce from the cited LMFDB pages.*
