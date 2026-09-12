# PRE-REGISTRATION — is the A = 2−√2 passage on the R=T locus content, or is it the intermediate value theorem? (P-U)

*Filed 2026-08-06, **before writing the control code**. Claude (Opus 5). Offered, not self-filed. Bars are not moved after this filing.*

**This is a prediction against the corpus.** P-U predicts that the corpus's own 2026-04-29 §5 finding — described there as *"the most substantive intermediate-structure finding of the session"* — has no predictive content. I am lodging it in the same form and under the same rules as the three predictions I lodged *for* the framework earlier today, so that it costs the same to be wrong.

---

## 1. Why this and not the two things I was asked for

Will asked for (a) the thin-film **interference** analogue of the grazing case, with *"an analogously privileged gamma\*-like prediction"*, and (b) a **d=4** extrapolation with nested/cascaded conditions. Both are live and I intend to get to them. Neither goes first, for two reasons.

**First, the map is already drawn and it says the interference-side prediction was lodged in April.** Will's grazing/interference contrast is exactly the corpus's own ladder, restated:

| Will's case | channel structure | locus | corpus layer | value | whose result |
|---|---|---|---|---|---|
| **interference**, unconstrained | all three live | matched sheet, `α = 1` | 1 | `(¼,¼,½)` | Woltersdorff 1934 — classical |
| **interference**, with the R=T balance imposed | all three live, R and T locked equal | the R=T locus | **2** | `A = 2−√2` passage | **the corpus's, 2026-04-29 §5** |
| **grazing** | T → 0, two-term budget | `σcos²θ = ωε₀` | 3b | `(3−2√2, 0, 2√2−2)` | Liu 2026 / Garg–Mermin 1987 |

So the "analogously privileged γ\*-like prediction for the interference case" is not missing. It is layer 2, it is `2−√2` = `γ\*`, and it has been on the books for three months. Lodging a *second* one before auditing the first would be building a fourth storey on the only plank in the structure nobody has load-tested.

**Second, I said this morning that I would stop doing the thing that has gone 0-for-3.** From the P-F record, §5, written before I knew what I would do next: *"All three were built by taking a structure the corpus had already established and extending it one step… the way to test it is to lodge a prediction that does not come from extending an existing corpus result one rung."* Both of Will's branches are one-rung extensions — the interference γ\* is layer 2 re-lodged, and d=4 is layer 3a's failure re-attempted in a wider space. P-U is not an extension. It is a **planted-control audit of an existing corpus finding**, which is the corpus's own qualification method (GATE-M, K-F3's anchors, the 2026-02-01 Colab post-mortem) turned inward for the first time.

**Third, and decisive: after this morning, layer 2 is the whole correspondence.** Layer 1 is classical and layer 3b is Liu's, both at public priority zero per the 07-21 closure; layer 3a was falsified at 05:10 today. If layer 2 does not carry content, the thin-film correspondence consists of two results TEP did not obtain and one that failed — and that is a fact Will should have before deciding where to push, not after.

## 2. The claim under audit, verbatim

From `session_findings_luo_pairwise`, 2026-04-29, §5 and §11:

> *"The R=T locus passes through the n=1 framework absorption value A = 2 − sqrt(2) at a specific configuration. At this passage: R = T = (sqrt(2) − 1)/2 = 0.20711 exactly (this is tautological given R = T and A = 2 − sqrt(2)). Geometric parameters at the passage are kd-universal: rho = cos theta/kd = 0.62821(1), xi = sigma\*kd\*cos theta = 1.14987(1), sigma\*kd^2 = 1.83038(1). Universality confirmed across kd from 1e−5 to 1e−3 to ~1e−4 precision. There are two passages: a rising-branch passage at rho ~ 0.628 and a falling-branch passage at rho ~ 1.083."*
>
> *"This finding sharpens the framework's predictive content: the iterative-sequence absorption value A = 2 − sqrt(2) IS realized at a kd-universal configuration along the R=T pairwise self-dual locus. The framework's intermediate-structure prediction is therefore real, not just an endpoint statement."*

Note the internal consistency check that lets me replicate exactly: `ξ/(σ_n kd²) = cosθ/kd = ρ`, and `1.14987/1.83038 = 0.62821` ✓. So that session's `σ` is my dimensionless `σ_n = σ/(ωε₀)` and the parameterizations agree.

## 3. The hypothesis I am predicting is true

**H-null.** §5's finding is an artifact of two facts, neither of which is TEP's:

1. In the thin-film limit, `A` along the R=T locus is a **kd-universal function of the single reduced parameter** `ρ = cosθ/kd`. (Established independently: §3.3, and re-measured this morning at the peak to 5.3e−5 across four decades of kd.)
2. That function **rises from below `2−√2`, peaks at `A* = 0.6078315`, and falls.** (Measured this morning to seven figures.)

Given 1 and 2, the intermediate value theorem gives **two crossings of every level in the range**, and the universality of the curve makes **every one of those crossing locations kd-universal automatically.** `2−√2 = 0.5857864` is in the range. Therefore its crossing exists, is doubled, and is kd-universal — and *so is 0.55's, and 0.57's, and 3/5's.* On this account §5 measured a property of the curve and attributed it to the level.

## 4. The predictions

**P-U1 [control — load-bearing].** Three non-TEP levels in the open range `(A(ρ→0), A*)` — **L1 = 0.5500000, L2 = 0.5700000, L3 = 0.6000000** (the last being 3/5, the corpus's own named non-TEP alternative from §3.3) — each have rising- and falling-branch crossings on the R=T locus whose `ρ` and `ξ` are **kd-universal to at least 1e−4 relative** across `kd ∈ {1e−2, 1e−3, 1e−4, 1e−5}` — i.e. to at least the precision §5 claims for `2−√2`.

**P-U2 [the sharp one].** The kd-universality of the `2−√2` crossing is **not better than the controls'**. Operationally: `spread(2−√2) ≥ (1/3)·median{spread(L1), spread(L2), spread(L3)}`, on relative kd-spread of `ρ_rising`.

**P-U3 [distinguished-location check].** `ρ_rising(2−√2) = 0.62821` does **not** coincide, to 1e−3 relative, with any feature the curve defines by itself: the inflection point of `A(ρ)`; `ρ = 1` (the `cosθ = kd` physical crossover identified in that session's own §2.2); the half-max point; or `ρ*` scaled by any of `φ⁻¹`, `√2−1`, `(1+√2)^(−1/2)`.

**P-U4 [instrument replication — a check on me, not on TEP].** My implementation reproduces §5's own numbers: `ρ_rising = 0.62821`, `ξ_rising = 1.14987`, `σ_n kd² = 1.83038`, `ρ_falling ≈ 1.083`, each to 1e−3 relative.

**Explicitly no prediction** is made about: the algebraic identity of `A*` (I refused to fit it this morning and that refusal stands); the layer-2 claim's *status in other geometries* (Salisbury screen, §8.3 — untested); or anything about `d=4`.

## 5. Kill conditions

- **K-U1.** If **any** control level fails kd-universality at 1e−4 relative while `2−√2` passes it, **H-null is falsified** — the universality would then be a property of the level, not the curve, and §5's finding survives with real content. I would report that as the framework scoring, and it would be the first time today.
- **K-U2.** If `spread(2−√2)` is smaller than **every** control's by a factor ≥ 10, that is a real anomaly and H-null fails even if K-U1 does not fire.
- **K-U3.** If `ρ_rising(2−√2)` lands on a curve-intrinsic feature (inflection, `ρ = 1`, half-max) to within 1e−3 relative, H-null is weakened at that point and I record the hit at full weight.
- **K-U0 (instrument qualification, must pass first — same anchors as this morning).** The implementation must reproduce (i) the classical matched-sheet point `(¼,¼,½)` at `α = 1` and (ii) Liu's grazing limit `(3−2√2, 0, 2√2−2)`, each to 1e−3, **and** P-U4 must hold. If P-U4 fails, **no verdict is issued** — the disagreement is then between my code and April's, and that has to be resolved before anything is concluded about the framework.

**No rescue in either direction.** If H-null survives, I do not get to say "but the value is still suggestive." If H-null dies, I do not get to say "but it's only one bit."

## 6. The one bit I concede in advance

There is a residual claim in §5 that is *not* killed by H-null, and I want it on the record before the run rather than conceded after:

**The R=T locus reaching above `2−√2` at all was not guaranteed.** `A*` could have come out at 0.55 and the passage would not exist. That is a genuine, falsifiable, TEP-shaped claim, and it is confirmed. It is worth **exactly one bit** — and it is a bit whose confirmation comes from a peak value (`0.6078315`) that the framework does not predict and this morning failed to predict. It is also not independent of the classical layer-1 result, which already puts the curve's reachable range above `½`.

So the best case for §5, if H-null holds, is: *one confirmed bit, resting on an unpredicted number.* The worst case is: *zero.* Neither is *"the framework's predictive content includes intermediate trajectory passages."*

## 7. Disclosures

**Prediction class.** P-U1/P-U2 are **forced-if-H-null** in the corpus's D-2 sense — that is the point. Their evidential value is not in confirming H-null (cheap) but in the fact that **K-U1 and K-U2 could fire and would cost me the argument.** I have not computed any control crossing before this filing.

**What I already know.** I know `A* = 0.6078315` and `ρ* = 0.76419` from this morning's run. I know §5's four numbers from reading the April record ten minutes ago. I have **not** computed `A(ρ)` away from its peak, have not located any crossing, and have not run the inflection test. The controls are blind.

**Conflict of interest, stated.** I am the author of three predictions that failed today. An audit that finds a fourth corpus claim empty is *convenient* for the pattern conjecture I filed in the P-F record, which makes me exactly the wrong person to grade it leniently in that direction. K-U1 and K-U2 are written to fire against my own thesis, and I will report them firing if they do.

**Method.** `thinfilm.py`, the same direct-interface implementation qualified this morning under K-F3 on both planted anchors. Re-qualified in-script so the audit is self-contained.

---

*Offered, not self-filed. Countersign items: the §3 statement of H-null; K-U1/K-U2 as the conditions under which the framework scores; the §6 concession of the one bit; the §7 conflict-of-interest disclosure.*
