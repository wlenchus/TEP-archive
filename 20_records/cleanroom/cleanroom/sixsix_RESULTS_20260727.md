# Six-for-six RESULTS — EVEN-icosahedral (the corner): all six Doud prime-conductor fields certify entire+FE at 10⁻¹⁴ — with one new instrument lesson bought by two failures — 2026-07-27 (blind-decode session, ~12:30Z)

**Mountain line:** even-icosahedral, the corner; 3-dim Sym²ρ̃ **shadow** certificates. The summit (2-dim emission) remains untouched and under seal — nothing in this campaign opened lift material.

## 0. Honest bite, before the headline

Same PoC pricing as the 07-27 certificates: float64 sums with spline kernels (validated floor ~10⁻¹²), the modest certified t-window, truncation justified by kernel decay, no rigorous tails, no Turing-method zero accounting. And this campaign's specific bite: **two of the five new fields (3701, 8501) failed first** (6.8e-3 / 2.0e-2, corruption-profile per KP-3), and their certificates below were obtained **after a one-bit-per-field data repair** whose necessity was discovered through the failure. The epistemic order was: leave-one-out surgery localized the bit (the p=2 face) with the L-data in view → the *mechanism* was identified as structural (the mod-p face test is blind at p=2, where +√disc ≡ −√disc; the classifier silently defaults to 5A) → an **answer-free 2-adic decider** was built and run against pre-registered expectations, including **two blind validators** (2141, 3821 — certified with the default, so their true face at 2 is forced): it went **4/4** (validators → 5A; 3701, 8501 → 5B) with the decision sharp at mod 8 → the repaired tables were re-run through the **untouched pre-registered protocol**. What carries the weight is the decider's validator record and the post-repair blind conductor scans — not the surgery. A referee wanting stricter ordering (decide-before-any-L-contact) cannot get it from these six fields — none remain below 10⁴ — and that limit is stated here rather than papered over. KF-1 control (Doud-1951 at certified gauge) read 2.161e-14 in all three batches; no other deviation from `sixsix_preregistration_20260727.md` occurred; the 1.70·p² pseudo-dip seen mid-diagnosis (2.7e-5, nine orders above floor, inadmissible as a conductor) is recorded as what a coherent one-bit corruption looks like to this instrument.

## 1. The dataset [V]

All under the pre-registered protocol (gauge scan 2×2, predicted N = p², certified t-grid, negative battery with fixed seeds, G_new meter at best gauge). "Scan" = blind conductor scan; all six minima unique at exactly p² with ±5% neighbors at 7e-4–2e-3 (ten–eleven orders above the certified value).

| field | residual | ram sign c_p | face-swap | ε | scan min | G_new max dev |
|---|---|---|---|---|---|---|
| 1951 (control rerun) | 2.161e-14 | +1 | 1 | +1.000000 | 1951² unique | 2.7e-14 (07-27) |
| 2141 | 2.385e-14 | +1 | 1 | +1.000000 | 2141² unique | 4.1e-14 |
| 3701 (post-repair) | 2.536e-14 | +1 | 0 | +1.000000 | 3701² unique | 2.1e-14 |
| 3821 | 1.282e-14 | +1 | 0 | +1.000000 | 3821² unique | 1.5e-14 |
| 8501 (post-repair) | 3.816e-14 | +1 | 0 | +1.000000 | 8501² unique | 2.9e-14 |
| 9461 | 4.092e-14 | +1 | 1 | +1.000000 | 9461² unique | 5.5e-14 |

Negatives per field (face-scramble 30% / class-scramble 20% / odd-port): all in 8e-3–2e-1, i.e. every corruption fails by nine to thirteen orders. Chebotarev tallies on all five new emission tables sit on the A₅ fractions with zero unclassified primes. Emission tables carry the idealprimedec index-prime repair (2141: 3,43,2689; 3701: 3,89,2621; 3821: 719,991; 8501: 17; 9461: 2,3) — all 2A/3A patterns, no 5-cycle index primes anywhere in range.

**With the corpus {2,7,331} field, the certified even-icosahedral 3-dim dataset now stands at seven objects — every known even-icosahedral field of prime conductor < 10⁴, plus one composite-conductor field — a dataset, not an anecdote.**

Observation, offered at [O]: all six 5A-inertia (tame e=5) ramified ports measured **c_p = +1**; the 3A-inertia ports of the corpus field measured (−1,+1,+1). A retrodiction target for the w₂/ε-ledger instruments before the 2-dim pre-registration: predict these seven sign-sets from local data.

## 2. The dyadic face port — new standing lesson (session-ops, sibling to the index-prime lesson)

The Frobenius-orbit Vandermonde test (V ≡ +√disc ↔ 5A) is **structurally blind at p = 2**: +s ≡ −s (mod 2), so the classifier's first branch always fires and silently returns 5A whenever Frob₂ is a 5-cycle. The certified 07-27 fields were immune only by accident of arithmetic (1951: 2 is an index prime → 3A; corpus: 2 ramified → skipped). Repair instrument: `face2_decider.gp` — the same classifier computed in Z₂ (unramified quintic Z₂[y]/(y⁵+y²+1), Hensel-lifted orbit, true Frobenius ordering, V ∈ Z₂ˣ compared to ±√disc, decidable at mod 4 whenever disc is odd; all gates machine-checked). Standing rule: **any emission table for a field with a 5-cycle at 2 must take its p=2 face from the 2-adic decider, never from the mod-2 default.**

## 3. Provenance

Scripts, repaired tables, per-field result JSONs, and batch logs hashed in `PROVENANCE_MANIFEST_v4_addendum_20260727.txt`. Base toolchain reproduction (this session, before any new computation): 21/21 bundle scripts, all three certified emission tables, and both kernel grids byte-identical to the v1-v3 manifest; the one nonmatch (poc3_results.json, float last-ulp) disclosed there. Everything regenerates: poc5_emit.gp (<2 s), poc5_sixsix.py (~2 min/field), face2_decider.gp (<5 s).

## 4. Offered (countersign-gated)

(a) [V] stamps on the five new certificates and the six-for-six dataset claim (title claim: all known prime-conductor even-icosahedral fields < 10⁴ certify). (b) The dyadic-face-port lesson as standing session-ops + the decider as a named instrument. (c) The [O] sign-set observation as a pre-registered retrodiction target for the decode instruments. (d) The honest-bite framing of §0 (surgery-then-decider order; validator-carried weight) as the record's permanent scope line. (e) Erratum-grade note on the five-for-five queue item: Doud's list below 10⁴ has six fields, not five; 8501 was silently absent from the queue phrasing — six-for-six supersedes.

*Offered, not self-filed. Design and kill conditions were lodged in `sixsix_preregistration_20260727.md` before any target ran; KF-2's no-tuning path was followed through the anomaly; the bite paragraph above was written before the table.*
