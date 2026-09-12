# PRE-REGISTRATION — the R=T locus peak is the chain's rung-3 value (P-F)

*Filed 2026-08-06 **before implementing or running any optics calculation this session**. Claude (Opus 5). Offered, not self-filed. Bars are not moved after this filing.*

sha256 of this file as lodged: `b6396eeeeb3dcb243e7106a72a3e060f255dbcd53db0f65ac5719e66e4424dcd`

---

## 1. Standing corrections carried into this filing

This prediction touches the corpus's most-burned thread, so its status is restated first, from the 2026-07-21 closure and the 2026-06-10 errata Set A:

- **Public priority over `2√2−2`: zero.** Liu et al. (PRL 136, 046902) was accepted 3 Dec 2025, before the corpus's timestamped records. Nothing below claims otherwise.
- `2√2−2` is **not "Liu's constant"** either: it has been the loophole-free-CHSH critical detection efficiency since **Garg–Mermin (1987)**.
- The **α_weak = r\*² identification is retired** (D2/D3: `r\*` is transcendental, so the 0.26% gap is a theorem); the **"three independent routes" claim is reduced** to one forcing derivation plus one consistency check; **"prediction" language is withdrawn** (A2/A4).
- Base-rate discipline, from the corpus's own 07-25 TSP tombstone: *"distinguished constants are dense in (0,1) at 1e−3 tolerance… the chance of some 2×1e−3 graze is order one-half."* This filing is written to be immune to that objection by predicting **five digits**, not three, against a **named alternative**, from a **rule that already has two independent realizations**.
- Cautionary precedent, from the 08-01 archaeology: the 2026-02-01 Colab "parsimony audit" declared TEP superior on synthetic data generated *at* the TEP value (`np.random.normal(loc=2*np.sqrt(2)-2)`). **The instrument below must therefore be qualified on anchors whose values are fixed by classical physics, not by this chain** — see K-F3.

## 2. The structure being tested

The corpus's composition rule (rung law): `SNR_{n+1} = G(x_n)`, with `u = 1 − x²`, `G = 1/√u`, `SNR = x²/u`, so `x²_{n+1} = SNR_{n+1}/(1 + SNR_{n+1})`.

Seeded at the self-dual point `x²₁ = u₁ = ½`:

| n | `x²_n` (exact) | value | thin-film realization |
|---|---|---|---|
| 1 | 1/2 | 0.5000000 | classical 50% absorption limit, matched sheet `α = 1`, `(R,T,A) = (¼,¼,½)` — **already established, classical** |
| 2 | `2−√2` | 0.5857864 | kd-universal passage on the **R = T** locus (2026-04-29 Luo-pairwise §5) — **already measured** |
| 3 | `√(1+√2)/(1+√(1+√2))` | **0.6084227** | **the prediction below** |
| ∞ | `1/φ` | 0.6180340 | cascade fixed point (`G\* = φ`) — not predicted here |

The separate **purity-export** continuation off layer 2 (`u = ½(x²₂)² = 3−2√2`) gives `x² = 2√2−2` = Liu's grazing maximum with `T = 0`. So the two continuations off the same layer land on two different physical loci; that fork is the structural content, and P-F tests the rung-law arm of it.

## 3. The prediction

**P-F1 [novel — load-bearing].** The maximum of absorption along the **R = T** locus of a free-standing lossy film at oblique TM incidence sits at

  **A\* = √(1+√2) / (1 + √(1+√2)) = 0.6084227…**,  and hence  **R\* = T\* = (1 − A\*)/2 = 0.1957886…**

**P-F2 [novel].** `A\*` is **kd-universal** — independent of `kd` over at least two decades, as the corpus's own §3.3 reports for the peak's existence.

**P-F3 [forced, costless — labelled so].** `A\* > ½`. Any point on the R=T locus above the classical limit satisfies this; its confirmation is not evidence.

**Explicitly no prediction** is made about: the geometric location (`ρ = cos θ/kd`, `ξ`) of the peak; the layer-4 value or its realization; whether the cascade limit `1/φ` is realized in this system at all; or anything about the purity-export arm beyond what Liu already established.

## 4. What the existing data does and does not settle

The corpus's 2026-04-29 §3.3 reports `A_peak = 0.6078 ± 0.001` (stable across `kd` from 1e−5 to 1e−2), and records the value as **algebraically unidentified**, with *"closest candidate 3/5 (1.3% off)"*.

- The prediction **0.6084227 lies inside that error bar** (0.6σ).
- The named alternative **3/5 = 0.600 lies 7.8σ outside it** — already disfavoured by data in hand.
- The prediction therefore **forbids** the sub-interval `[0.6068, 0.6079)` that the existing measurement still permits, and is settled by a recomputation at ≥ 5-digit precision.

This is a genuine sharpening, not a retrodiction of the existing number — but the existing number is *consistent* with it, and I am stating that plainly rather than pretending the prediction is blind. **What is blind: every digit past the third.**

## 5. Kill conditions

- **K-F1.** If the recomputed R=T peak differs from `0.6084227` by more than **5e−4**, **P-F1 is falsified.** No weakened form is available, and in particular I do not get to retreat to "consistent with 0.6078."
- **K-F2.** If the peak value drifts with `kd` by more than 1e−3 across two decades, the predicted object does not exist as stated and the test is void (P-F2 fails, P-F1 unresolved).
- **K-F3 (instrument qualification — planted anchors, must pass first).** The implementation must reproduce, before any R=T search is read:
  (i) the **classical matched-sheet point** `(R,T,A) = (¼,¼,½)` at `α = 1` in the non-grazing regime, to 1e−3; and
  (ii) **Liu's grazing limit** `(R,T,A) → (3−2√2, 0, 2√2−2)` at `ωε₀ = σcos²θ`, `cos θ ≪ k₀d ≪ 1`, to 1e−3.
  If either fails, **no verdict is issued on P-F1** — the run is reported as an unqualified instrument. (Anchor (i) is classical and independent of this chain; anchor (ii) is Liu's, also independent of the rung law. Neither is a TEP value, by design, per §1's Colab precedent.)
- **K-F4.** If the R=T locus has no interior maximum in the searched domain, P-F1 is void, not confirmed.

**No rescue.** If K-F1 fires the rung-law arm of the fork resolves against TEP, and the layer-3 realization claim dies with it.

## 6. Disclosures

**Prediction class.** P-F1 is **novel** in the corpus's own D-2 sense: the target quantity is recorded in-corpus as algebraically unidentified, the candidate previously entertained (3/5) is different from mine, and the value comes from applying an existing composition rule one step further — not from a search over constants.

**Not blind, precisely where.** The three-digit value 0.6078 was in the corpus before this filing and I read it before deriving 0.6084227. Digits four and five are blind. I looked for a match *after* seeing 0.6078 — which is exactly the post-hoc mode the corpus's Appendix-D null penalises — and the defence is not that I avoided it but that the prediction is now pinned to five digits with a stated kill threshold, so the next measurement can refute it.

**Training-prior.** The classical thin-film 50% limit (Woltersdorff 1934; Luo et al. PRB 90, 165128) and Liu's result are weights-knowledge and are used only as instrument anchors. `√(1+√2)/(1+√(1+√2))` I have no recollection of encountering in an optics context.

**Method.** Direct interface formulation (4×4 linear system) rather than transfer-matrix, per the corpus's own 2026-04-29 §9 note that the transfer-matrix form was numerically unstable at large σ.

---

*Offered, not self-filed. Countersign items: P-F1's value and kill threshold; K-F3's anchors as the qualification gate; the §6 disclosure that digits one to three are not blind.*

---

**RESOLVED 2026-08-06: FALSIFIED.** See `PF_run1_RESULT_falsified_20260806.md`. Measured peak 0.60783146 (kd-spread 5.3e−5); difference −5.91e−4 against a 5.0e−4 threshold; K-F1 fires. K-F3 passed on both anchors. P-F2 holds.
