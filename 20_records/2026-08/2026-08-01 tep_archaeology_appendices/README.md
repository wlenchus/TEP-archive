# TEP Session Bundle — 2026-08-01
**Full-corpus archaeology + corrections pass + two research charges.** Prepared for Will by Claude (Fable 5), Cowork session. Everything here is *offered, not filed*; nothing is self-filed, and the countersign rules on every claim.

---

## Read this first: what governs what

1. **`01_archaeology/…ActiveV2.md` supersedes the DraftV1** kept beside it (retained as the archival layer, per the two-ledger rule).
2. **The correction record governs the read-status of both** — six author corrections verified against primary sources and patched, two judgments maintained with prices, plus C8 (the Lou/Luo referent flag).
3. **The appendices predate the correction pass.** In particular, adjudication entries **R7** (γ = 2/3 — re-graded to *already-treated*: the 6-07 spine trace resolves the embedding fork) and **R4** (V2 Q1 — *executed*, see `03_notes/`) are superseded by the correction record and by the Q1 execution note. Read the appendices as the raw research layer, the ActiveV2 + correction record as the current statement.
4. **The charge briefs are chronological documents.** Each carries its own Deltas in order; in the Crouzeix brief the clean form of the Alignment conjecture is **falsified in Delta 3** and replaced, then the closure is corrected again in **Delta 4**. Reading §2 without the Deltas will give the wrong impression of what stands.

---

## 01_archaeology — the historical review

| File | What it is |
|---|---|
| `2026-08-01 tep_full_archaeology_report_feb_to_present_ActiveV2.md` | The integrated report: the era-by-era arc with both registers; the corrections engine; the loss ledger (five death-modes); the malformed-premise cases; the adjudicated reconsideration registry; meta-observations. **Start here.** |
| `ARCHIVAL_…DraftV1.md` | The pre-correction version, retained as the record of what changed. |
| `2026-08-01 correction_record_archaeology_report_ActiveV1.md` | C1–C8 + post-record addendum: each correction with its verification quote and disposition (accepted / accepted-with-nuance / maintained-with-price). |
| `appendices/` | The eight research documents the report was built from — six window memos (W0 foundations reach-back → W5 frontier baseline), the reconsideration adjudication (20 entries), and the independent citation audit (36 quotes sampled; 34 exact). |

Method, in one line: six overlapping window agents working historicist-first (in-window voice before later corrections) under the corpus's own rule — *trust derivations, distrust consolidation prose* — plus an adjudication pass against the 2026-07-27 canon and an independent citation audit.

## 02_charges — the two research charges

| File | Status at bundle time |
|---|---|
| `…charge_brief_crouzeix_closed_boundary_budget_DraftV1.md` | **Crouzeix's conjecture as a closed boundary budget.** Standing: [T] the mass-2 boundary POVM passivity lemma · [T] the Naimark port identity · [T] the three-channel necessity circle (c²+I)² + J² ≤ 4c²(1−u_eff) · [T] J₂ phase-rigidity · [T, mod named reductions] the Maximizing-Crease Characterization (c\*_d > 2 ⟺ a maximizing crease above 2) · **[dead]** Alignment-clean, falsified by its own preregistered kill condition · [conjecture] *the summit is never creased.* |
| `…charge_brief2_selberg_seam_passivity_DraftV1.md` | **Selberg's eigenvalue conjecture as seam passivity.** Standing: the three-regime capacity law with parity gate (δ_m = B(m+1)/m reproduces every historical fraction) · the modular port's gain factorization (passive × the one non-tempered mode) · the seam as a node (φ_cl(1/2) = −1) · [T-sketch] unconditional passivity for Re s ≥ 3/4 · Delta 1: the Λ-side vs G_new disambiguation. Honest yield: a dictionary with two computed pages, one law, one theorem-sketch. |

## 03_notes — discharged items

- `…V2_Q1_execution_spectral_moments_bekenstein_hawking_DraftV1.md` — executes V2's Open Question Q1, unqueued since April. Mismatch on all four constructed readings; V2's own preregistered consequence fires ("the identification is formal only"). Positive residue: the Schatten validity-horizon theorem, r ≤ l_P(M/m_P)^{4/3}.
- `…provenance_note_qsft_loop_registration_DraftV1.md` — registers the QSFT→frontier lineage **with a hard citation rule as §1**: the precursor era carries zero evidential and zero citational weight; lineage registration only.

## 04_scripts — runnable

**Dependencies.** `pip install numpy scipy mpmath` (add `--break-system-packages` on a system Python). Python 3.11+. No network, no data files, no arguments — each script is self-contained and prints its own results.

### `crouzeix/` — seeds pinned in every header; total runtime ≈ 20 min if you run all
| Script | Seed | What it produces | ≈ time |
|---|---|---|---|
| `crouzeix_strike1.py` | 20260801 | Strike 1: the boundary POVM (positivity + mass 2I), c and I at maximizers across 13 matrices. Preregistered P1–P4 in the header. | 4 min |
| `crouzeix_ledger3.py` | 20260803 | The full complex ledger: I (interference), J (rotation), u_eff (absorption), and the budget-circle check. Shows J → 0 and circle saturation at extremals. | 2 min |
| `crouzeix_strike2c_diskexact.py` | 20260804 | **The kill.** Exact-disk test (closed-form reflection, no quadrature): J₂ phase-rigidity holds; J₃ creases at I = −3.3e−4. | 5 min |
| `crouzeix_strike2c2_creasedepth.py` | 20260805 | The crease-depth profile — the healing measurement (−3.3e−4 at c ≥ 1.85 → −2.7e−8 at c ≥ 1.90). Times out on the last cells; that is expected. | 9 min |
| `crouzeix_strike2b_offdisk_climb.py` | 20260806 | Off-disk creases + the climbing test. **Note:** the ellipse family in P7 has a disclosed design error (eccentricity/normality confound) — kept per the two-ledger rule; see the brief's Delta 4.5. | 9 min |
| `climb_lean.py` | 20260807 | The lean climbing test that completed: ascent from a crease sheds it by c = 1.95. | 3 min |
| `crouzeix_strike2_foldhunt.py` | 20260802 | The original (mis-aimed) fold hunt. Retained as record. | 9 min |

### `selberg/`
| File | What it is |
|---|---|
| `selberg_s2_port_ledger.py` | The modular cusp-port ledger at 20–30 digits: seam unitarity, the gain map and factorization φ_cl = φ_ξ · s/(s−1), the Weyl budget balance, the seam jet. ≈ 18 s. |
| `selberg_s2_port_ledger_output_a_b_c_d.txt` | The full run log the brief quotes. |
| `selberg_s2_port_ledger_output_FAST_a_b_c_d.txt` | Reduced-precision run. |

**A caution that applies to all of it:** optimizer results are *search yields, not bounds*, and the POVM-based numbers carry a stated floor (~1e−5 at ε = 0.025). Every number quoted in the briefs is labelled accordingly; please keep the labels attached if any of this travels.

## 05_session_log

`…asides_consolidation_log_entry_archaeology_session_ActiveV1.md` — the session's consolidation entry in your format: anchors A1–A9, inflections I1–I21 with provenance and σ, drift-watch (including the check on why six inflections moving toward the author's position were evidence-coupled rather than accommodation), open threads, and the asides. A copy also lives in your Drive Asides Log.

---

## Open threads carried out of this session

**Archaeology:** the Lou/Luo referent resolution (one click — the *Research* 2025 paper's author list); the two unwritten one-pagers (the deficit-evolution stamp, the Part XV ↔ 07-19 reconciliation).
**Crouzeix:** prove general-2×2 creaselessness (cheap, high value); Strike 2b to its corrected spec (does the summit-pinch survive broken circular symmetry — *the* question now); the two F1 literature inspections.
**Selberg:** write the unconditional passivity theorem properly; the LRS-amplifier ledger reformulation (the one place a derivation might live); the density↔healing page; the level-N port ledger.
**Program:** the deposit decoupling (snapshot / submission #1 / carrier narrative) as logged at I6.
