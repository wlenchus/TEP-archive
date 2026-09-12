# P-F run 1 — RESULT: **FALSIFIED.** K-F1 fires. (And the instrument passed, which makes it worse.)

*2026-08-06, following `PREREG_thinfilm_rung3_RT_peak_20260806.md`, sha256 `b6396eeeeb3dcb243e7106a72a3e060f255dbcd53db0f65ac5719e66e4424dcd`, hashed before the calculation was written. Script `thinfilm.py`. Offered, not self-filed.*

---

## 1. Verdict

**P-F1 is falsified.**

| | value |
|---|---|
| prediction (chain rung 3) | `√(1+√2)/(1+√(1+√2))` = **0.60842267** |
| measured R=T locus peak | **0.60783146**, kd-spread 5.3e−5 |
| difference | **−5.91e−4** |
| K-F1 threshold | 5.0e−4 |

The miss is 18% past my own threshold — which is the kind of margin that invites a rescue. The rescue is not available, and not only because §5 forbade it: **the measurement is sharper than the threshold.** The peak is kd-universal to 5.3e−5 across four decades, so the prediction sits ≈ 11 spreads away. It is not marginally wrong; it is decisively wrong, and my 5e−4 threshold was too generous rather than too tight.

**P-F2 (kd-universality) HOLDS** — 5.3e−5 against a 1e−3 bar. The predicted *object* exists and is sharp. Its *value* is not the chain's.

**P-F3** (`A* > ½`) confirmed and explicitly costless, as labelled.

## 2. The instrument passed both planted anchors

This matters, because it removes the escape route.

- **Anchor (i), classical matched sheet:** max `A = 0.500000` at `(R,T) = (0.249983, 0.250017)`, `α = σ_n·kd/2 = 0.9999`. The classical 50% limit and its `(¼,¼,½)` split reproduced to 2e−5.
- **Anchor (ii), Liu's grazing limit:** at `σ_n cos²θ = 1`, `cos θ ≪ kd ≪ 1`, six independent (kd, cos θ) combinations all give `R = 0.171573`, `T < 1e−6`, `A = 0.828427` — i.e. `3−2√2` and `2√2−2` to six figures.

Neither anchor is a TEP value; both are fixed by classical physics and by Liu respectively, exactly as K-F3 required after the 2026-02-01 Colab precedent. So the instrument that refuted the prediction is the same one that reproduces the two values the corpus cares most about. I cannot blame the tool.

## 3. What the run did produce

**A replication.** The 2026-04-29 Luo-pairwise §3.3 numbers are independently reproduced by a from-scratch direct-interface implementation: `A_peak ≈ 0.6078` ✓, `R = T ≈ 0.196` ✓, and the geometric location `ρ = cos θ_peak/kd → 0.76419` against that session's recorded *"cos θ_peak/kd ~ 0.77 (kd-universal)"* ✓. That session's result stands, replicated by different code.

**A sharpening.** The corpus recorded `A_peak = 0.6078 ± 0.001`. It is now

  **A_peak = 0.6078315 ± 0.00005**,  `R = T = 0.1960890`,  at `ρ = cos θ/kd = 0.76419`, converged for `kd ≤ 1e−4`.

Two decimal orders sharper. Both previously-entertained candidates are now dead by wide margins: **3/5 is 148 spreads away**; **the rung-3 value is 11 spreads away**. The corpus's *"algebraically unidentified"* flag on this number **stands, and is now much harder to satisfy** — any future candidate must match six figures.

**I am not going to fit it.** The corpus's own 07-25 TSP tombstone prices this exact temptation: *"distinguished constants are dense in (0,1) at 1e−3 tolerance… the chance of some 2×1e−3 graze is order one-half."* Fishing for an algebraic form immediately after a falsification, on a number I have just pinned, is the post-hoc mode at its worst. The number is recorded; identifying it requires a mechanism first and a match second.

## 4. What this does to the structure

The three-layer thin-film ladder, restated with the correction:

| layer | value | thin-film realization | status |
|---|---|---|---|
| 1 — self-dual seed `x² = u = ½` | 0.5000000 | classical limit, `(¼,¼,½)`, matched sheet | **holds** (classical, not TEP's) |
| 2 — `2−√2` | 0.5857864 | kd-universal passage on the R=T locus | holds, per 2026-04-29 §5 (not re-tested here) |
| 3a — **rung law** → 0.6084227 | — | **predicted the R=T peak** | **FALSIFIED** |
| 3b — purity export → `2√2−2` | 0.8284271 | Liu's grazing maximum, `T = 0` | holds (replicated §2 above) |

So the **purity-export arm survives and the rung-law arm dies** at layer 3. The fork I described as "the structural content" resolves: only one continuation off layer 2 has a physical realization here, and it is the one that was already known. The rung law's own fixed point (`1/φ = 0.618034`) is 1.9e−2 above the measured peak and is not realized at this locus either.

The honest reading: **layers 1 and 3b are the classical limit and Liu's limit, neither of which TEP predicted** — layer 1 is Woltersdorff 1934 and layer 3b is Liu 2026, with public priority zero per the 07-21 closure. Layer 2's realization (2026-04-29 §5) remains the one genuinely TEP-shaped item in the ladder, and it was not tested in this run. **That is now the single load-bearing empirical claim of the whole thin-film correspondence**, and it deserves the same five-digit treatment this run gave the peak — which I have not done.

## 5. Tally, and a base-rate note against myself

Three predictions lodged in this session: **P-H inconclusive** (failed its own coverage bar), **P-R falsified**, **P-F falsified**. The corpus's predictive column is **0 for 3**.

I want to record the pattern rather than the individual results. All three were built by taking a structure the corpus had *already* established and extending it one step — the port reading extended to a locus, the budget extended to a balance condition, the rung law extended to a layer. All three extensions failed. That is a consistent signal about this mode of prediction-generation, and it is worth more than any of the three results: **the corpus's structures describe what they were built on and do not, so far, extrapolate.** Whether that is a fact about the structures or about my extensions of them is not settled by three trials — but it is the hypothesis I would now bet on, and the way to test it is to lodge a prediction that does *not* come from extending an existing corpus result one rung.

---

*Offered, not self-filed. Countersign items: the FALSIFIED verdict; the sharpened value `A_peak = 0.6078315 ± 0.00005` with the refusal to fit it; the §4 resolution of the fork against the rung-law arm; the §5 pattern claim, which is a conjecture about the corpus and should be treated as one.*
