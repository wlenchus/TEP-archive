# MANIFEST — the 1951 closure campaign, curated pack — sessions of the C lineage, 2026-08-15 → 08-17

*Assembled 2026-08-17 by the session that ran the campaign, on Will's charge to keep only what should survive and to leave no conflicting reports behind. **This manifest is the precedence document.** Where a parent record and a correction disagree, the correction wins; where anything disagrees with the canonical-values table in §3, the table wins. Every record here is offered, not self-filed; countersign is Will's alone.*

---

## 1. What this is

A 25-file pack covering one campaign: the attempt to close the Artin conjecture for the even icosahedral representation ρ̃ at conductor 1951 (Doud–Moore), together with the framework work that surrounded it. Nothing here claims the conjecture. What it does claim, and what survives adversarial verification, is stated in §5.

The pack is self-contained. It deliberately does **not** include Will's own corpus records (v0.5, the Central Reference, the consolidations, the III record); those are canon and live in their own place. Quotations from them appear inside these records with attribution.

## 2. Reading order

1. `01_map/CONSOLIDATED_closure_campaign_countersign_ready_20260817.md` — the map of every record with tiers, correction layers, honest distance, and the **countersign block (§9)**: the six calls that are Will's.
2. `03_verification/` — the corrections layer. Read this **before** any instrument record. `STAMP_adversarial_verification_closure_20260816.md` carries the night's three repairs and one refutation; `verify_cap_and_seam_blind.py` is the blind replication script (separate implementation, written from filed prose only) that reproduces the pincer's numbers independently.
3. `02_instruments/` — the exact computations at (Γ₀(1951), χ). Each parent that was corrected carries a **CORRECTION HEADER** at its top; those headers are the reconciled state.
4. `04_structural/` — the 08-17 layer: the equivalent dresses of the throat, the attempt records (positive and negative), the framework syllogism, and the entangled register.
5. `05_origin/` — the session's origin charge (thread diff) and its running log.

## 3. Canonical values — the table that wins

| quantity | canonical | superseded values that appear in drafts |
|---|---|---|
| B at window X = 3.496 | **276.46** → cap **≤ 276** (margin 0.54) | 276.08, 276.1 (undoubled elliptic) |
| B at window 1 (X = 1.9248) | **946.68** → cap ≤ 946 | 946.3, 946.26, 946.62, 946.67 |
| identity term at L = 0.4812 | **960.67184** | 960.6240 (refuted — two method-independent deciders) |
| elliptic term, total | **(4/(3√3))∫h·cosh(πr/3)/cosh(πr)dr** | (2/(3√3))∫… (ν₃ = 1 packaging) |
| cap ladder, X = 5/6/7/8/10 | **129 / 86 / 61 / 45 / 26** | — |
| golden-geodesic weight prefactor | **1.721632** = 2·(4logφ)/√5 | 1.72176 (prose typo) |
| ℓ(trace 3) | **1.9248473** = 4logφ | — |
| ℓ(ramified disc 4·1951) | **164.2045** | — |
| seam value w = φ_∞0(½) | **−0.7614484884 + 0.6482254233i**, \|w\| = 1 | — |
| E[\|a_p\|] | **(11+6√5)/30 = 0.81388** | — |
| E[\|a_p\|²] | **1 exactly** (Schur orthogonality) | — |
| Cl(L₅), quintic resolvent | **ℤ/30**, Cl⁺ = ℤ/30 × ℤ/2 (PARI `bnfcertify`) | — |
| ord ζ_K if L(ρ̃) has a pole | **≥ 4** (Heilbronn LP, integer certificates) | ≥ 2 (Stark, weaker) |
| Γ̄₀(1951) | **F₃₂₅ ∗ C₃ ∗ C₃** → **326** obstruction functions | — |

## 4. Correction ledger — everything that changed, and who caught it

| # | claim as first filed | corrected to | caught by |
|---|---|---|---|
| 1 | elliptic term (2/(3√3))∫ | **doubled**: (4/(3√3))∫ — each of ν₃ = 2 points gives both rotation classes | adversarial verifier (scattering/trace) |
| 2 | −2g(0)log2 convention flagged, worst case ±1.7 | **pinned** to Booker–Strömbergsson (per-cusp −g(0)log2) — which is what lets the corrected cap be stated at all | same verifier |
| 3 | "mod-q-closed family" (winding record) | **false**; pairing routes through the contragredient into modulus qN — (W) and T\* carry q₀N | adversarial verifier (winding) |
| 4 | "dihedral determinants have even order" | **false in general** (explicit order-5 counterexample); conclusion salvaged at 1951 by conductor arithmetic | adversarial verifier (packets) |
| 5 | converse-step cites Weil 1967 | **Jacquet–Langlands 1970** — the looseness originates in Booker 2003 itself (holomorphic converse cited for an even/Maass case) | adversarial verifier (winding) |
| 6 | τ\* = max(A,0) unrestricted | **scoped** to the operative window τ ∈ (0,1) | adversarial verifier |
| 7 | "window-1 identity is 960.6240" (a *verifier's* correction) | **refuted** — 960.67184 by exact decomposition and by 600k-node Simpson | commissioning session |
| 8 | Booker-pair hypotheses as glossed in the sweep | qualifying pair is the **det-1 twist at level 1951², trivial nebentypus** | packet verification |
| 9 | "cascade" used for within-layer transfer composition | corrected to the framework's sense (**threshold-transgressing DtN/Schur**); the corpus-sense cascade is the scattering block | **Will** |
| 10 | family↔term associations treated as facts to settle | **orbit-valued** per the automorphism–bijectivity dichotomy; only discrete/continuous is forced | **Will** |
| 11 | (P3)'s "virtual port" negativity treated as intrinsic | **chart-dependent** — an artifact of the induced-abelian presentation | **Will** (methodological charge) |

Two provenance notes kept deliberately: corrections ran **both** directions (verifiers corrected the parents; the commissioning session then refuted a verifier's over-correction, item 7), and three of the eleven were Will's. One near-miss that was checked and cleared: the constant (11+6√5)/30 in the T-A…T-D record is attached to a *first*-moment statement and is correct as filed — the confusion was in a later charge, not in the record.

## 5. Status, stated once

**Not closed.** Strong Artin at 1951 is open, and nothing in this pack asserts otherwise.

**What is proved and verified:** the exact scattering matrix Φ(s) at (Γ₀(1951), χ) with its forced ±1 seam involution (τ(χ)'s phase in the eigenvectors); the exact Selberg identity with every term priced; the multiplicity cap ladder down to **≤ 26**; the single-object winding reduction (strong Artin ⟺ one zero-set inclusion) and the magnitude-free halting detector (failure is semi-decidable, unconditionally); uniform no-Siegel and packet multiplicity 1; the finite presentation of the obstruction (**326** explicit Bessel-series functions) and the rank-one uniqueness of the candidate; the boundary-Poisson/Smirnov equivalence; the vacuity proof for central-sign forcing (a general theorem about Selberg zetas, not a local failure); and, in the entangled register, the cross-spin tensor identity χ₂χ₂′ = 4-dim with the conductor-one Hecke character it produces — whose prediction 15 | h⁺(L₅) landed against a certified class-group computation.

**What is open:** COH, (W), Δ(T₀) — and their equivalent dresses (T1), ζ_K-simplicity, N⁺-membership, δ(γ,K), Missing Lemma A\*. Every one is a location/ordering/multiplicity statement. The measure level is saturated; that is the campaign's single most robust structural finding, arrived at independently from seven charts.

## 6. What was excluded, and why

- **Working notes** (`NOTES_workspace.md`): scratch, containing superseded thread-map hypotheses that would conflict with the corrected map.
- **Agent working scripts** (the ledger and closure run directories): unverified provenance, and one of them produced the figure refuted in item 7. The one script included (`verify_cap_and_seam_blind.py`) is the independently-written replication that survived.
- **Mirrors of Will's corpus records**: canon, not deliverables of this campaign.
- **Nothing was excluded for being negative.** The refutations (q-positivity on asymmetric domains, the seam-parity vacuity, the amplified-Kuznetsov failure margins, the Fredholm route's pricing) are load-bearing and are all here.

## 7. Tier legend

**[T]** proved this campaign and adversarially verified · **[T-v]** proved by a prover session, verified independently with named repairs applied · **[Tsk]** skeleton-grade (structure re-derived, some steps cited) · **[CN]** certified-numerical · **[cal]** calibrated against controls, not re-derived · **[R]** reading/dictionary — ontology layer, never load-bearing · **[open]** named open statement · **[recalled]** rests on memory of a standard result, unpinned.

*Offered, not self-filed. 2026-08-17.*
