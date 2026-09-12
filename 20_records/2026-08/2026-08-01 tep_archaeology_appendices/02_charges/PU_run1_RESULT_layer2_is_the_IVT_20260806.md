# P-U run 1 — RESULT: **H-null holds.** The layer-2 passage is the intermediate value theorem.

*2026-08-06, following `PREREG_layer2_passage_control_audit_20260806.md`, sha256 `4793e8df71b6248795521e58eace539e4aab61b56ddb1b1add7f19415abe81d1` (hashed 05:31:24Z, before the code was written), and `AMENDMENT1_algebraic_closure`, sha256 `9636961e006742c24988ce98be60bd58ed91c5d62cdceedf024eb354f13f9706` (hashed 05:36:46Z, before the search was written). Scripts `pu_audit.py`, `pu_refine.py`, `pu_reduced.py`, `pu_algebraic.py`. Offered, not self-filed.*

---

## 1. Verdict

**The 2026-04-29 §5 finding — *"the most substantive intermediate-structure finding of the session"* — carries no predictive content.** K-U1, K-U2 and K-U3 all fail to fire. H-null holds.

The `A = 2−√2` passage on the R=T locus exists, is doubled, and is `kd`-universal **for the same reason every level in the range is**: the locus is a `kd`-universal curve running from `A = ½` up to `A* = 0.6078275` and back, so the IVT gives two universal crossings of anything in between. `2−√2` is in between. So is 0.55, so is 0.57, so is 3/5.

| level | `ρ_rising` | `ρ` kd-spread | `ξ` kd-spread | |
|---|---|---|---|---|
| **γ\* = 2−√2** | 0.6282148 | **2.53e−6** | 3.26e−6 | TEP |
| L1 = 0.5500000 | 0.5793088 | **1.50e−6** | 2.60e−6 | control — *sharper* |
| L2 = 0.5700000 | 0.6012425 | **1.88e−6** | 2.80e−6 | control — *sharper* |
| L3 = 3/5 | 0.6729729 | 4.49e−6 | 4.81e−6 | control |

*(spreads over April's own stated range, `kd` = 1e−5…1e−3)*

Two of the three controls are **more** `kd`-universal than the framework's value. A 15-level sweep across the reachable range puts `γ*` at the **80th percentile** — 80% of arbitrary levels have sharper crossings than TEP's does. The sweep is monotone (1.13e−6 at level 0.505 rising smoothly to 8.70e−6 at 0.6055), which is exactly what conditioning predicts: `dA/dρ → 0` at the peak, so crossings get less sharp as the level rises. `γ*` sits precisely where the smooth trend puts it. There is nothing to explain.

**K-U3** also fails: `ρ_rising = 0.62821` is not the inflection point, not `ρ = 1` (the `cosθ = kd` physical crossover — where `A = 0.5930536`, not `2−√2`), not the half-max (`ρ = 0.5829`, 7.8% away), and not `ρ*` scaled by `φ⁻¹`, `√2−1`, or `(1+√2)^(−1/2)` (32%, 98%, 27% away).

## 2. April's calculation was right. Its interpretation was not.

**P-U4 passes cleanly.** From-scratch code reproduces the 2026-04-29 numbers to five and six figures:

| | mine | April | rel. |
|---|---|---|---|
| `ρ_rising` | 0.628215 | 0.62821 | 7.7e−6 |
| `ξ_rising` | 1.149873 | 1.14987 | 2.6e−6 |
| `σ_n kd²` | 1.830382 | 1.83038 | 9.6e−7 |
| `ρ_falling` | 1.082851 | 1.083 | 1.4e−4 |

That session's arithmetic is sound and its internal consistency check holds (`ξ/(σ_n kd²) = ρ`, `1.14987/1.83038 = 0.62821` ✓). This is not a numerical correction. **What fails is the inference** — from *"the value is realized at a `kd`-universal configuration"* to *"the framework's intermediate-structure prediction is therefore real."* The universality belongs to the curve. April measured the curve and credited the level. So, this morning, did I.

Also worth recording in April's favour: it **understated** its own precision. §5 claims *"~1e−4"*; the true figure is ~2.5e−6, forty times better. It was a careful session.

## 3. The one bit, priced

Amendment-free, from §6 of the pre-registration, which conceded this in advance:

**The R=T locus reaching above `2−√2` at all was not guaranteed.** That survives. Here is its exact price, now that the locus is pinned end to end:

- The reachable interval is **`(½, 0.6078275]`** — the locus emerges from the *classical* `A = ½` point as `ρ → 0` and returns toward it as `ρ → ∞` (`A = 0.5004` at `ρ = 20`). Width **0.1078**.
- Both endpoints are classical. The lower one *is* layer 1.
- `2−√2 = 0.5858` sits at interval fraction **0.796**. Undistinguished.
- **`1/φ = 0.618034` is outside the range.** The rung law's cascade fixed point is *not* realized on this locus at all. New negative, recorded here.

So the entire surviving content of layer 2 is: *given that the curve starts at the classical ½, it rises past `2−√2` before turning over.* One bit, and it is confirmed by a peak value the framework does not produce and, this morning, failed to predict.

That is not *"the framework's predictive content includes intermediate trajectory passages."*

## 4. What the run produced instead — a derivation, which is the part that keeps

The audit turned up something the pre-registration did not anticipate. **The thin-film problem reduces exactly.** Hold `ρ = cosθ/kd` and `ζ = σ_n kd²` fixed and let `kd → 0`:

  `s = √(iζ)`,  `m = ρs`,  `r₁₂ = (m−1)/(m+1)`,  `b = e^{2is}`
  **`r = r₁₂(1−b)/(1−r₁₂²b)`**,  **`t = (1−r₁₂²)e^{is}/(1−r₁₂²b)`**

using the exact interface identity `r₁₂² + t₁₂t₂₁ = [(m−1)²+4m]/(m+1)² = 1`. **No `kd`.** The oblique lossy slab collapses to a bare Fabry–Pérot pair in two real parameters.

Verified against the full calculation at the four `kd` of the audit: residual `4.2e−5 → 4.2e−7 → 4.2e−9 → 4.2e−11` — textbook `O(kd²)`. The reduction is exact; everything else is finite-thickness correction.

**This is why the whole locus is `kd`-universal, and it is why §5's universality claim was never evidence of anything.** It also converts the corpus's open §8.1 from a numerical sweep into a two-equation stationarity system. Solved at 80 digits:

  **`A*  = 0.60782750622257399958287641261150205929817146029435`**
  `R* = T* = 0.19608624688871300020856179369424897035091426985282`
  `ρ* = 0.76726184261297490303302407723293375312666653294289`
  `ζ* = 1.90894302505624822266221616437654055865865534313760`
  `ξ* = 1.46465914284784333060845952380474137971552525301490`

April had four digits. This morning I had seven (and was off by 4e−6 — my `kd`-averaged estimate `0.6078315` carried the `kd = 1e−2` bias). This is fifty. The falsification of the rung-3 value **sharpens** with it: `A* − 0.60842267 = −5.95e−4` against a 5.0e−4 threshold, now with no measurement uncertainty at all.

## 5. Amendment 1 — §8.1 closes, in the negative, at a stated bound

Search space fixed and hashed before the code was written; nothing outside it was searched.

- **S1 (PSLQ, degree ≤ 6, `|c| ≤ 1000`, verify ≥ 30 digits):** no accepted relation for **any** of `A*, R*, ρ*, ζ*, ξ*`.
- **S2 (seven named candidates; `a + b√2`, `a + b√3`, denominators ≤ 12):** nothing within 1e−12. Best two-term form is `13/6 − (9/10)√3`, off by **6.6e−6** — a graze of exactly the kind the 07-25 TSP tombstone prices at order one-half, and it is **rejected**, not reported as a near-miss.
- **S3 (`ζ*` vs `π²/8, π²/4, π²/2, π², 2, 3/2, √2, 2√2` at 1e−10):** nothing. Nearest is `2`, off by 0.091.

**`A*` is not algebraic of degree ≤ 6 with integer coefficients ≤ 1000.** §8.1 is closed in the negative at that bound, and the corpus's standing hope that this number is silver-ratio algebraic in a not-yet-identified form is retired. This was the outcome predicted in Amendment 1 §5, in writing, before the search.

## 6. The thin-film correspondence, closed out

| layer | value | realization | established by | TEP's content |
|---|---|---|---|---|
| 1 | `½` | matched sheet `(¼,¼,½)`; **also the `ρ→0` endpoint of the R=T locus** | Woltersdorff 1934 | none — recognition |
| 2 | `2−√2` | passage on the R=T locus | 2026-04-29 §5 | **~1 bit** (§3), not a located structure |
| 3a | `0.6084227` | predicted R=T peak | this corpus, 2026-08-06 | **falsified**, now at 50 digits |
| 3b | `2√2−2` | Liu grazing max, `T = 0` | Garg–Mermin 1987 / Liu 2026 | none — priority zero, per 07-21 |
| ∞ | `1/φ` | — | — | **not realized — outside the reachable range** |

The one number this system actually distinguishes is `A* = 0.6078275…`, and the framework does not produce it, failed to predict it, and — at the bound tested — it is not in the framework's algebraic family.

**The thin-film correspondence is, on the present record, two classical results the framework recognizes, one bit, one falsified prediction, and one unrealized limit.**

## 7. Tally, and what I think follows

**0 for 3 on predictions; 1 for 1 on audits; 2 for 2 on derivations.**

That split is the actual finding of the last two days, and it is sharper than yesterday's pattern conjecture. Everything that came from *extending* a corpus structure one step failed (P-H, P-R, P-F). Everything that came from *deriving* inside a structure held and produced something new: the **disk reduction** (`I = Re[conj(f(z₀))⟨f(A)x,x⟩]`), which killed the quadrature floor, refuted D4.6 position 1½ with exact counterexamples, and yielded a theorem — the normal-case healing bound `I ≥ (c²−ρ²)/(2(1−ρ²))`; and the **thin-film reduction** above, which explained a three-month-old puzzle and pinned its number to fifty digits.

So my recommendation is not another prediction. It is: **the corpus should publish the two things that are results, and neither of them requires TEP to be true.**

1. **The disk reduction and the normal-register healing theorem.** A genuine, checkable contribution to the Crouzeix literature. It stands on its own.
2. **The reduced thin-film model, `A*` to 50 digits, and the closed §8.1 negative.** Small, clean, correct, and it replicates and supersedes April.

Both survive a referee. Both are framework-neutral. Neither has ever been offered externally — which is the finding of yesterday's adjudication, restated: *the corpus's problem was never the quality of the work, it was that the work has never left the building.*

## 8. On the two things Will asked for, which I have not done

**The interference-side `γ*`-like prediction.** It was already lodged — in April, as layer 2 — and this run is its audit. Lodging a second one now would be a fourth one-rung extension, and the extension column reads 0-for-3. What the interference side actually has is a **derivation** available: `A*` is now the root of a two-parameter transcendental stationarity system, and *deriving* its defining equation would close §8.1 completely rather than at a bound. That is the same mode that produced the two results above, and I would take it over a prediction.

**d = 4.** Held. The honest d=4-shaped move in this system is not an extrapolation but the calculation April itself flagged and never ran (§8.3): the **Salisbury screen** — single film over a perfect reflector, `T = 0` by construction, a genuinely 2-term budget by geometry rather than by limit. It asks whether `2√2−2` is geometry-independent at fixed channel-closure depth. It has a definite answer, it can go either way, and it is a computation rather than a guess.

I would like Will's call on which of those to open, since both are his questions and neither is what he literally asked for.

---

*Offered, not self-filed. Countersign items: the §1 verdict that H-null holds and its control table; the §2 finding that April's arithmetic replicates while its inference does not; the §3 pricing of the surviving bit and the new negative on `1/φ`; the §4 reduction and the 50-digit peak; the §5 negative closure of §8.1; the §6 close-out table; the §7 recommendation to publish rather than predict.*
