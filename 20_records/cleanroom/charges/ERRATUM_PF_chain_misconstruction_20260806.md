# ERRATUM — P-F tested a chain step the corpus does not assert

*2026-08-06, same day, at headline volume per the corpus's own errata protocol. Corrects `PREREG_thinfilm_rung3_RT_peak_20260806.md` §2, `PF_run1_RESULT_falsified_20260806.md` §4, and `PU_run1_RESULT_layer2_is_the_IVT_20260806.md` §6. Raised by Will, verified before writing. Offered, not self-filed.*

---

## 1. The error

My P-F pre-registration described the corpus's chain as **one rule applied repeatedly** — *"the corpus's composition rule (rung law): `SNR_{n+1} = G(x_n)`"* — and generated the layer-3 target by applying it a second time.

**The corpus's chain is not one rule applied repeatedly. It is two distinct involutions.**

| step | operation | result |
|---|---|---|
| 1 → 2 | `SNR₂ = G(x₁)` | `G(x₂) = √(1+SNR₂) = √(1+√2)`, `G²(x₂) = 1+√2 = 1/u₂`, `u₂ = √2−1`, **`x²₂ = 2−√2 = γ*`** |
| 2 → 3 | **`γ* = √(2u₃)`** | `u₃ = ½γ*² = 3−2√2`, **`x²₃ = 2√2−2`** (Liu) |

Verified term by term, all to 10 decimals: `G(x₁) = 1.4142135624 = √2` ✓; `G(x₂) = 1.5537739740 = √(1+√2)` ✓; `u₂ = 0.4142135624 = √2−1` ✓; `x²₂ = 0.5857864376 = 2−√2` ✓; `u₃ = 0.1715728753 = 3−2√2` ✓; `x²₃ = 0.8284271247 = 2√2−2` ✓.

**The 1→2 step of my reconstruction was correct.** The 2→3 step was not. Re-applying the first involution gives `x²₃ = √(1+√2)/(1+√(1+√2)) = 0.6084226677` — **which is my construction, not the corpus's**, and it is the number P-F falsified.

## 2. What this does and does not change

**Does not change:** the number `0.6084227` is still dead. The R=T locus peak is `A* = 0.60782750622257399958…` — now known to fifty digits from the reduced model — and the miss is `−5.95e−4` against a `5.0e−4` threshold with no measurement uncertainty. K-F1 fired and stays fired. **Nothing here is a rescue.** The instrument still passed both planted anchors; P-F2 still holds; the replication and sharpening of the 2026-04-29 §3.3 numbers still stand.

**Does change, and this is the substantive part:** the falsification **says nothing about the corpus's composition rule**, because the corpus's composition rule was never on trial. I falsified a rule I had constructed by misreading the chain. The corpus's actual 2→3 step lands on `2√2−2`, and the reduced model confirms that value is realized at the grazing limit — which the P-F run itself verified to six figures as instrument anchor (ii).

So the correct entry for layer 3 is not "3a rung law, falsified / 3b purity export, holds." **There is no 3a.** There is one 2→3 step, it is the `γ* = √(2u₃)` involution, and it gives Liu's value.

## 3. Consequential corrections

**`PF_run1_RESULT` §4, ladder table.** Delete the row "3a — rung law → 0.6084227 — predicted the R=T peak — FALSIFIED" as a *corpus* layer. It was mine. Retain the falsification as a record of a failed prediction by me, correctly labelled. The row "3b — purity export → `2√2−2`" is not an alternative arm; it is *the* step.

**`PF_run1_RESULT` §5 and `PU_run1_RESULT` §7, the tally.** The 0-for-3 count stands as a count of *my* predictions. But the characterization — *"all three were built by taking a structure the corpus had already established and extending it one step"* — is wrong for P-F specifically. P-F extended a structure the corpus had **not** established. That is a worse failure mode than the one I diagnosed, not a milder one: I misread the corpus and then tested my misreading. The pattern conjecture in §5 is correspondingly weaker evidence than I claimed, because only two of the three failures are actually of the type it describes.

**`PU_run1_RESULT` §3, the `1/φ` negative.** I recorded that `1/φ` lies outside the R=T locus's reachable range `(½, 0.6078275]` and called the cascade fixed point unrealized. `1/φ` is the fixed point of *repeated* application of the first involution — which is not the corpus's chain either. The measurement is true; **its framework-relevance is now unclear and I withdraw the framing.** Whether the two-involution chain has a limit at all, and what it is, I have not worked out.

**`PREREG_thinfilm` §2, the table.** The row `n=3 | √(1+√2)/(1+√(1+√2))` should be struck from any presentation of the corpus's chain. The `n=∞ | 1/φ` row likewise.

## 4. How this got past me

The two-involution structure is visible in the corpus's own records — the phrase *"purity export `u₃ = ½γ*²`"* is right there in the chain, and it is not a `SNR = G(x)` step. I read the chain as a sequence of values and inferred a single generating rule from the first step, then wrote *"an existing composition rule"* into a pre-registration and hashed it. The pre-registration's disclosure section (§6) worried about the right thing — post-hoc constant-matching — and missed the actual defect, which was one line earlier, in the statement of what the rule was.

The general lesson for the errata apparatus, which is Will's standing concern: **a pre-registration protects against moving the bar after the run; it does not protect against misstating the structure before it.** Nothing in the protocol as it stands would have caught this. The check that would have is a two-line requirement — *restate the rule being extended in the corpus's own notation, and verify it reproduces every value already in the chain before predicting the next one.* Had I done that, the naive rule would have failed at `x²₃` immediately, since it does not reproduce `2√2−2`.

I have added that as a **stamp** for the Spine V3 kit: **C13 — "reproduce the chain before extending it."**

---

*Offered, not self-filed. Countersign items: the §1 two-involution correction; the §2 statement that the falsification stands but its target was mine; the §3 withdrawal of the `1/φ` framing; the §4 protocol gap and stamp C13.*
