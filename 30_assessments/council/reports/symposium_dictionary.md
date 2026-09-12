# DICTIONARY — symposium findings (Feb–June sweep, my slice)
*2026-08-26. [dv-Drive] = read this round (ID given) · [pv] = peer (mailbox, seat named) · [run] = machine-checked. Era-gradient applied: flags, not inheritance. Offered, not self-filed.*

## 1. ★purity_speed_limit_v2 (1uGESTEa…) — FULL READ + tier-audit start

**Ship verdict: viable, gated on three repairs; the Gamma herring did NOT propagate into it.**

1. **[AUDIT-CRITICAL] The Lemma's displayed proof has two soft/broken steps** — (i) "‖[ρ_SE, ρ_S⊗I]‖₁ = Σ_{a≠c}|λ_a−λ_c|σ_ac" is an upper bound, not the stated equality ([run]: spectrum (0.5,0.3,0.2) gives block-sum 0.394 vs 2√F = 0.250); (ii) the "second factor ≤ √2" Cauchy–Schwarz split holds only at d_S = 2 (at Schmidt purification the ratio-sum is d(d−1)). **The theorem itself stands** — repair route: trace-norm convexity ⟹ extremal ρ_SE are purifications ⟹ commutator reduces to the wedge B, and rank-2-ness forces ‖B‖_nuc = √2‖B‖_F = 2√F exactly; Gamma_testing independently machine-verified EXACT at d = 2–5. ~3-line fix; sent to domain-anchor.
   **[CONSOLIDATED, post-cross-talk]** Domain-anchor's ping (their 02-14 audit): that doc's gap is the *H-optimization* step (op-norm = Frobenius, valid only d ≤ 3); v2's gap is the *commutator-trace-norm* step (√2 aggregation, valid only d = 2) — same disease, different limb. **Answer to their gating question: v2 STATES the rank-2 lemma (§3.2 property (iii), "the structural fact at the heart of the bound") and uses it for the §4 saturator, but never runs it in the §3.3 bound proof.** One consolidated repair fixes both documents, using v2's own §3.2: convexity → Schmidt purification → the commutator IS the wedge B ([run]: (v∧u)_ac = √(λ_aλ_c)(λ_c−λ_a)), rank 2, singular pair (√F, √F) ⟹ ‖·‖₁ = 2√F at every d → Hölder → 4√F; sharpness inherits domain-anchor's independent re-proof. Ship-gate wording: *"after consolidated Lemma repair (dictionary + domain-anchor) + verification-grid reconciliation."* Replied via their mailbox (no-cycle rule; ping budget still unused).
2. **[CLEAR] §11.2 budget-form is clean** — works entirely in the spectral pair (γ²/p₃, F/p₃), never asserts the Liu match from it; γ\* appears nowhere. The Gamma_testing slot-conflation is quarantined to that one working note.
3. **[EXEMPLARY] §9.1 prior-art positioning** is C14-before-C14: "Theorem 1 is Hamazaki's general inequality applied to the moment observable… Calling it 'new' overstates; calling it 'an MT corollary' understates… this should be the headline framing." The doc carries its own guiding context (self-corrects against its draft) — the era's correction layer working inside one manuscript.
4. **[RECONCILE] Verification-grid inconsistency**: §4.3 lists (2,2),(2,3),(3,3),(3,4); Lemma-check grid adds (4,4); §12 claims "verified numerically at d_S = 3, 4, 5." One table of actually-run grids needed before ship; adding d_S = 4,5 saturator runs is an afternoon.
5. **[NEEDS WILL] §12.5 additivity-gap conjecture** ("minimum-output-entropy additivity gap bounded by 2√2−2… predictive statement predates Luo… documented in a separate note"): the separate note is UNLOCATED; units/bridge unstated — D7-risk. Keep-or-retire is Will's call; locating the note is a registry task. **§12.4 composition-law companion doc**: also unlocated — flag.
6. **Needs-Will's-errata list (for the gated ship)**: Lemma repair countersign; grid reconciliation; §12.5 decision + note location; §12.4 companion location; venue/authorship (Q10); post-May C14 refresh (Hamazaki/Rosal positions re-verified — [tp] currently).

## 2. ★Silver/Pell OUTPUT HUNT — FOUND (Q13 overturned, archivist's catalog-negative rider'd)

**`2026-02-05 TEP_Silver_Ratio_Findings.md`** — TWO copies (1DSfftDgova4…, 1WDGWJS1B9…) [dv-Drive]. The run WAS executed:
- **Metric product corrected in-era**: script predicted δ_S⁴/16; findings prove **g_B × g_P = δ_S⁶/16** via γ\*² = 2σ² ([run]-checked algebra: 1−2σ = σ² in Z[√2]).
- **Honest statistics**: golden/Fibonacci balance advantage ~11%, **p = 0.04**; silver/Pell ~10%, **p = 0.12 (trending, not significant)**. "The effect is real but modest."
- Companion-Pell 7 among optimal sizes; δ_S^n = H_n + P_n√2 both-sequence structure; 24-fold speculation (pun-watch).
- **Consequence for the revival**: the January arc-review's dramatic split (0.85–0.95 vs 0.50–0.60) and the Feb ensemble-mean test (~10%, mixed significance) are **different observables** (state-resolved near-critical states vs all-eigenstate means). The prereg revival must first reconcile protocols, then power the test — not "replicate the split." Pathfinder's dating rule adopted: post-06-25 silver derivations are re-derivations unless they predate (these do — Feb).

## 3. Thin-film Feb-origin records — mapped [dv-Drive, metadata+snippets]

01-27: Liu txt + Galiffi CPA (2410.16426) ingested · 01-31: `TEP Grazing parsimony.ipynb` (the planted-anchor precedent's subject; not attempted per Colab rule) · 02-01: 71vr-lb26 gdoc conversions + `2-1-26 Colab HBAR Testing` (1q1vjpVkv…) · 02-02/04: Untitled80/83 (Colabs, not attempted) · 02-05: Liu PDFs + **arXiv 1405.6475 "A unified theory for perfect absorption in ultra-thin absorptive films"** (the classical 50%-limit theory) + alam-sm (ITO/ENZ). **Yield: the classical antecedent was in the SOURCE folder from 02-05** — strengthens the thin-film note's C14 genealogy (my round-2 finding that the (β,γ)-chart is Liu-supplement-classical has a Feb-era sibling: the corpus ingested the classical unified theory the same week it began).

## 4. Era physics-register map (Feb–June)

| register | era arc | correction event INSIDE the era | status |
|---|---|---|---|
| **Purity/QI** | tier-1 pair (Feb) → D-dim bound (02-14) → **v2 manuscript (05-08)** → Gamma_testing (05-18) → kinetic_cascade (05-29) [pv pathfinder: Petz-entrywise invariance, O-5/O-6] → O-b closure (06-10) [pv exegete: theta-tower exact-Gaussian; harmonic-channel repair] | v2 §9.1 self-repositioning; Central-Ref V1→V3 lineage [pv exegete] | ship candidate (gated §1) |
| **Thin-film** | ingestion (01-27→02-05, incl. classical antecedent) → parsimony Colab (02-01, K-F3 precedent) → Maxwell session (04-29) → reviews (5-25/26/29) → provenance (6-1) → Set A (06-10) | 06-10 Set A demotions | note results-complete (Phase A) |
| **Metallic/AA** | golden arc (01-25) → script + **FINDINGS (02-05)** → dormant | findings correct script's δ⁴→δ⁶ | revival re-scoped (§2) |
| **HBAR/bimetric** | Dec–Jan origin → Colab HBAR Testing (02-01) → δ_S⁶/16 identity | narrowed by V1 Tier 5.1 [pv exegete: DFF = pre-V1 stratum] | mechanism ledger entry (deep-dive F2, now with exact product) |
| **GMC/theta-tower** | → O-b closure 06-10 [pv exegete] | Gaussian-fixed-point degeneration; question upgraded | pathfinder/exegete lanes |

**Era-gradient verdict from my slice: every physics register carries a correction event inside the era** — the "V2-lineage = the era's own correction layer" rule is confirmed; flag-not-inherit works because the era mostly flagged itself.

## 5. Cross-talk log

**Received**: archivist (catalog-negative → now overturned by §2; charge-brief location + **second brief `charge_brief2_selberg_seam_passivity_DraftV1` (08-01)** — new to council, flagged for pathfinder's native-route file); exegete (O-b GMC closure + harmonic-channel repair + DFF stratum — folded into §4); pathfinder (kinetic-cascade Petz-invariance → my Petz entry gains the O-6 "is the rank-2 curvature the W wedge?" question; silver-dating rule → adopted §2; theta-tower → §4). **Sent (mailbox)**: archivist (findings-doc discovery + Feb timeline); assessor (Gamma-herring pinpoint + v2-§11.2-clean + ship-gate wording); domain-anchor (Lemma proof gap + counterexample + repair route). **Pings**: none used.

## 6. Strike-outs

None — slice covered as given; the findings-doc discovery absorbed the motivation the strike-out license would have spent.

## 7. Failed reads

None technical. Not attempted (per protocol's Colab rule, zero-of-one attempts used): Grazing parsimony.ipynb, Untitled80/83, 2-1-26 Colab HBAR Testing (gdoc — readable in principle; deferred as adjacent, not starred). Unlocated despite search: §12.5's "separate note" (additivity-gap provenance) and §12.4's companion doc — both flagged for archivist's still-unread list.

*Offered, not self-filed.*
