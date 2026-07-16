# The TEP Archive

**The Terminal Equivalence Principle (TEP)** — a boundary-first, operationalist research program in mathematical physics: the physical content of a passive system is taken to be exhaustively characterized by its boundary response (its Dirichlet-to-Neumann operator), with the Schur complement as the fundamental operation of physical reduction. From that stance the corpus develops an information-geometric "budget" formalism, tiered-rigor theorem notes (e.g. a purity/decoherence speed limit), an experimental dictionary, and — in its current frontier — a transmission-functor bridge toward Langlands-type structures.

This repository is the **curated public record** of that program: 158 primary documents spanning August 2025 – July 2026, selected and organized from a working corpus of 2,602 files. The complete corpus — every draft, transcript, dataset, figure, and precursor-era document — is indexed in [`CATALOG.csv`](CATALOG.csv) with links to the originals.

**Honest framing, in the corpus's own words** (from the 2026-05-29 closing note): *not crankery, not a breakthrough* — a mathematically serious constraint theory of measurement geometry, developed in an unusual human–AI collaborative process, with its verified results, its retired claims, and its open questions all kept on the record. The archive preserves corrections and dead ends deliberately: the errata ledger and the assessment records are part of the point.

## How this repository is organized

```
00_canon/          the current authoritative layer (central reference, errata, corpus maps, active records)
10_papers/         publication-track standalone theorem notes
20_records/        the chronological ledger of dated session records (2026-04 … 2026-07)
30_assessments/    internal reviews, external calibration, audits
40_foundations/    v0.5 working notes + the Base Theory shelf
50_code/           decoders, validation scripts, the OT1 instrument
60_data/           DATA_MANIFEST.md — datasets stay in Drive (~1.9 GB), indexed not mirrored
90_archive/        transcripts; precursor eras indexed via CATALOG.csv
CATALOG.csv        the full 2,602-file index: dates, provenance era, status, summaries, links
```

Provenance eras: **QSF/UST precursor** (Q1 2025) → **GSR** (mid 2025) → **IFFT** (late 2025) → **TEP** (Sep 2025 – present). Original file modification dates were preserved end-to-end; the catalog carries them.

## The priority spine — a proposed reading order

### I. Foundation

1. **[v0.5 — Terminal Equivalence Principle (TEP) & Passive Holography — Working Notes .txt](40_foundations/v0.5%20%E2%80%94%20Terminal%20Equivalence%20Principle%20%28TEP%29%20%26%20Passive%20Holography%20%E2%80%94%20Working%20Notes%20.txt)** (2025-08-23) — Where TEP begins: defines the DtN/Schur boundary program, budget metric, passive holography. Documented limitations included.
2. **[Framework Reconciliation and Experimental Proposal](40_foundations/base_theory/Framework%20Reconciliation%20and%20Experimental%20Proposal.txt)** (2025-11-16) — The GSR→TEP reconciliation (Nov 2025): Rosetta Stone table; formally excises the IFFT-era Lagrangian.
3. **[Terminal Equivalence Principle (TEP): A Comprehensive Documentation](40_foundations/base_theory/Terminal%20Equivalence%20Principle%20%28TEP%29_%20A%20Comprehensive%20Documentation.txt)** (2025-12-15) — Broadest end-of-2025 synthesis (Shannon–Hartley identity, GMC correspondence, vacuum sum rule).

### II. Maturation

4. **[2-2-26 TEP Framework: Rigorous Assessment](40_foundations/base_theory/2-2-26%20TEP%20Framework_%20Rigorous%20Assessment.txt)** (2026-02-02) — Definitive Feb 2026 audit: Operationalist Pivot, Steel Frame, HBAR/Silver Ratio, Experimental Dictionary.
5. **[2026-04-19 TXT_V2_TEP_Entrodynamics_Central_Reference.txt](00_canon/2026-04-19%20TXT_V2_TEP_Entrodynamics_Central_Reference.txt)** (2026-04-19) — THE canonical tiered reference (V2, Apr 2026): Tier-1 theorems, Tier-5 retired claims, LLM failure modes, open questions.

### III. Publication-track results

6. **[tep_tier1_purity_decoherence_limit.txt](10_papers/tep_tier1_purity_decoherence_limit.txt)** (2026-04-19) — Flagship Tier-1 theorem paper: purity speed limit |dγ/dt| ≤ 4‖H‖√F with constructive saturation.
7. **[2026-05-08 purity_speed_limit_v2.txt](10_papers/2026-05-08%20purity_speed_limit_v2.txt)** (2026-05-08) — Polished v2 of the flagship paper; adds Shannon–TEP budget identity.
8. **[2026-06-18 homogeneity_closure_monotone_metrics.md](10_papers/2026-06-18%20homogeneity_closure_monotone_metrics.md)** (2026-06-18) — Publication-grade standalone theorem note (journal-style, de-TEP-ified).

### IV. Epistemic calibration

9. **[2026-05-25 External_Literature_Review_TEP_Framework.md](30_assessments/external/2026-05-25%20External_Literature_Review_TEP_Framework.md)** (2026-05-25) — The pivotal adversarial external calibration (5-25) that drove all subsequent corrections.
10. **[5-26 Review Postmortem .txt](30_assessments/external/5-26%20Review%20Postmortem%20.txt)** (2026-05-26) — Establishes the governing epistemic rule: trust derivations, distrust consolidation prose.
11. **[closing_note_reliability_and_bottom_line.md](30_assessments/internal/closing_note_reliability_and_bottom_line.md)** (2026-05-29) — The plainly-stated bottom-line reliability judgment on the corpus.
12. **[2026-06-10 consolidated_errata_and_status_revision_record.md](00_canon/2026-06-10%20consolidated_errata_and_status_revision_record.md)** (2026-06-10) — Master corrections ledger (6-10): governs read-status of many earlier documents (Liu demotion, α retirement).

### V. Verified corpus map

13. **[2026-06-07 interior_spine_trace_ActiveV11.md](00_canon/2026-06-07%20interior_spine_trace_ActiveV11.md)** (2026-06-07) — Verified trace of the entire interior corpus — the closest existing thing to this catalog.
14. **[2026-06-07 early_corpus_synthesis.md](00_canon/2026-06-07%20early_corpus_synthesis.md)** (2026-06-07) — Definitive survey of the precursor eras (QSF/GSR/IFFT); best entry point to the archive layer.
15. **[2026-06-18 assessment_delta_record.md](00_canon/2026-06-18%20assessment_delta_record.md)** (2026-06-18) — Best single synthesis of what TEP is (the subtractive-framework meta-pattern; seven deltas).
16. **[2026-06-20 delta_external_assessment_evolution.md](00_canon/2026-06-20%20delta_external_assessment_evolution.md)** (2026-06-20) — Definitive external-assessment state: validity firm, genericity open on three closable items.

### VI. Current frontier

17. **[2026-06-29 session_consolidation_record_langlands_functor_ActiveV2.md](00_canon/2026-06-29%20session_consolidation_record_langlands_functor_ActiveV2.md)** (2026-06-29) — N=4 onset resolved; dihedral functor verified end-to-end; foundations re-grounded.
18. **[2026-07-01_transmission_functor_definitional_record.md](00_canon/2026-07-01_transmission_functor_definitional_record.md)** (2026-07-01) — Definitional pin of the TEP↔Langlands transmission functor; self-described anti-regression reference.
19. **[2026-07-02 session_consolidation_record_coding_theorem_conservation_ledger_ActiveV1.md](00_canon/2026-07-02%20session_consolidation_record_coding_theorem_conservation_ledger_ActiveV1.md)** (2026-07-02) — Master consolidation threads A–J (7-02): group-quotient coding theorem, formation-lattice budgets.
20. **[2026-07-03 session_delta_record_uniqueness_tensor_twist_capacity_ActiveV5.md](00_canon/2026-07-03%20session_delta_record_uniqueness_tensor_twist_capacity_ActiveV5.md)** (2026-07-03) — Current canonical delta, threads K–U (7-03): reflection theorem, dead-channel theorem, N=389 census.
21. **[2026-07-05_ot1_delta_buhler_control_PASS.md](50_code/ot1/2026-07-05_ot1_delta_buhler_control_PASS.md)** (2026-07-16) — Validates the OT1 decoder instrument (35/35 Buhler control); corrects the conductor ladder.
22. **[2026-07-15 collatz_tep_division_of_labor_record_ActiveV1.md](00_canon/2026-07-15%20collatz_tep_division_of_labor_record_ActiveV1.md)** (2026-07-15) — Parent record of the newest thread (7-15): (A)/(B) factorization; 'dictionary, not yet guide'.
23. **[2026-07-15 faces_seam_groupoid_record_Delta2.md](00_canon/2026-07-15%20faces_seam_groupoid_record_Delta2.md)** (2026-07-15) — Most recent substantive record: Sturmian-seam theorem, transmission groupoid.

## Conventions you'll see in the documents

`ActiveVn` = current working version of a record · `ArchivalVn` = retained snapshot · `DeltaN` = incremental addendum · Tier 1–5 = the corpus's rigor ladder (Tier 1 verified theorem → Tier 5 retired claim) · `[V]` = claim with a reproducibility path (see the methods supplement in `10_papers/`).

Two documents govern how to read everything else: the **consolidated errata & status revision record (2026-06-10)** in `00_canon/`, and the **review postmortem (2026-05-26)** in `30_assessments/external/` — the latter's rule, "trust derivations, distrust consolidation prose," applies to this README too.

## Provenance & method

This archive was assembled in July 2026 from the working corpus (Google Drive) by an automated cataloging pass: recursive crawl, per-document review of the 196 most significant files, rule-based placement, byte-exact mirroring where formats allowed (Google-Docs-native files were exported as text; equations may be degraded in those exports — originals are linked in the catalog). Assembly notes and the full provenance map live in `CATALOG.csv`.

## License

No license has been granted yet; all rights reserved by the author pending a licensing decision. (A CC BY 4.0 / MIT split for documents/code is under consideration.)
