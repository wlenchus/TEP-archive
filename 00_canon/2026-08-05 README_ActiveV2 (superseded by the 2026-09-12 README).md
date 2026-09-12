# The TEP Archive

*(README ActiveV2, 2026-08-05 — supersedes the 2026-07-23 README.md. Drop-in replacement for the repo root; also filed in Drive at `Dated TEP Documents ~2026/2026-08-05 Repository_Arch_ActiveV2/`.)*

**The Terminal Equivalence Principle (TEP)** — a boundary-first, operationalist research program in mathematical physics: the physical content of a passive system is taken to be exhaustively characterized by its boundary response (its Dirichlet-to-Neumann operator), with the Schur complement as the fundamental operation of physical reduction. From that stance the corpus develops an information-geometric "budget" formalism, tiered-rigor theorem notes (e.g. a purity/decoherence speed limit), an experimental dictionary, and — in its current frontier — a seam-constraint decoding instrument that in August 2026 produced, and saw constructor-confirmed, the first Hecke-eigenvalue data for even icosahedral 2-dimensional Galois representations (Doud-1951 and Doud-2141).

This repository is the **curated public record** of that program: 158 primary documents at the last push (spanning August 2025 – July 2026), selected and organized from a working corpus of 2,602+ files, with the July–August layer staged for the next push. The complete corpus is indexed in [`CATALOG.csv`](CATALOG.csv) (through 2026-07-16) plus [`catalog_delta_master_20260805.csv`](catalog_delta_master_20260805.csv) (2026-07-16 → 2026-08-05); the full delta review lives in `TEP_Corpus_Catalog_delta_v1_1_20260805.xlsx`.

**Honest framing, in the corpus's own words** (from the 2026-05-29 closing note): *not crankery, not a breakthrough* — a mathematically serious constraint theory of measurement geometry, developed in an unusual human–AI collaborative process, with its verified results, its retired claims, and its open questions all kept on the record. The archive preserves corrections and dead ends deliberately: the errata ledger and the assessment records are part of the point. The August 2026 summit results are stated precisely in that spirit: two committed 67-bit datasets, blind-selected conductors, five adversarial verification avenues, and an open Crespo-genre construction agreeing 65/65 modulo one pre-declared quadratic-twist freedom per field — **offered-not-self-filed, countersign-gated, unpublished and unrefereed**. The deposit and a human referee remain the program's own stated top priority (2026-07-25 direction memo).

## Where the corpus lives (four shelves)

1. **This repo** — curated mirror; last known push 2026-07-24.
2. **Google Drive** — the working tree (`TEP 2026-07/…`): dated records, staging folders (`2026-07-22 Batched Edits & Updates`, `2026-07-24 Batched Uploads`), instruments and data.
3. **The claude.ai project "2026-07-26"**, `cleanroom/` — the sealed-campaign record set (2026-07-27 → 2026-08-04): pre-registrations, commits, results, verification, the Crespo grade, SHA-256 manifests, and script bundles from which a fresh container regenerates everything. Mirror target: `20_records/cleanroom/`.
4. **Hash-pinned zip archives** delivered in-conversation (e.g. `TEP_even_icosahedral_20260803-04.zip`, sha256 260512aa…).

## How this repository is organized

```
00_canon/          the current authoritative layer — central reference (ActiveV3, 2026-07-23),
                   errata line, corpus maps (spine trace ActiveV12), active records,
                   Foundations Status block v2 (always-visible header)
10_papers/         publication-track standalone theorem notes (homogeneity-closure = submission #1)
20_records/        the chronological ledger of dated session records (2026-04 … 2026-08)
  cleanroom/       1:1 mirror of the project cleanroom set, kept intact as a unit
30_assessments/    internal reviews, external calibration, audits — now including the
                   2026-07-20 → 08-01 review ledger; read every review WITH its errata
40_foundations/    v0.5 working notes + the Base Theory shelf
50_code/           decoders, verify/ scripts, ot1/ full-width instrument, gp2/ (bundle C), labs
60_data/           DATA_MANIFEST.md — datasets stay in Drive (~1.9 GB), indexed not mirrored;
                   large regenerable artifacts (hosts, M⁻¹ factors) are never shipped
90_archive/        transcripts; precursor eras; superseded material with pointers to successors
CATALOG.csv        the 2,602-file index (≤ 2026-07-16) — dates, era, status, summaries, links
```

Provenance eras: **QSF/UST precursor** (Q1 2025) → **GSR** (mid 2025) → **IFFT** (late 2025) → **TEP** (Sep 2025 – present). Original file modification dates were preserved end-to-end; the catalogs carry them (with a composed-vs-filed dateline where they differ).

## The priority spine — a proposed reading order (V2)

Forty-nine documents in nine phases; the full table with links is the delta catalog's *Priority Spine V2* sheet. **Fast path** for one sitting: ActiveV3 central reference → Foundations Status block v2 → the errata line (6-10 + 07-21 ledger patches) → the 5-29 closing note → the even-icosahedral campaign README → the 08-03 COMMIT → the Crespo grade (+ its same-day totpos erratum) → `STARTER_next_session_20260804`.

**Phase I — Foundation (Aug–Dec 2025).** ① *v0.5 Working Notes* (DtN/Schur program, budget metric, passive holography — documented limitations included). ② *Framework Reconciliation* (the GSR→TEP rosetta stone; excises the IFFT Lagrangian). ③ *TEP: A Comprehensive Documentation*.

**Phase II — Maturation.** ④ *2-2-26 Rigorous Assessment* — **historical specimen, read with care**: the February era's most confident synthesis, on the spine for its narratives, its claims read through V2 Tiers 4–5. ⑤ **V2 Entrodynamics Central Reference — ActiveV3 edition** (2026-07-23; the 2026-04-19 text is its archival basis).

**Phase III — Publication-track results.** ⑥ *purity_decoherence_limit* ⑦ *purity_speed_limit_v2* ⑧ *homogeneity_closure_monotone_metrics* (journal-style; referee submission #1).

**Phase IV — Epistemic calibration (May–June 2026).** ⑨ *External Literature Review (5-25)* → ⑩ *Review Postmortem (5-26)* — "trust derivations, distrust consolidation prose," a rule the July reviews proved applies to reviews too → ⑪ *closing_note_reliability_and_bottom_line* → ⑫ *consolidated errata (6-10)*.

**Phase V — The verified corpus map (June 2026).** ⑬ *interior_spine_trace* — **ActiveV12** → ⑭ *early_corpus_synthesis* (ActiveV2) → ⑮ *assessment_delta_record (6-18)* → ⑯ *delta_external_assessment_evolution (6-20)*.

**Phase VI — The Langlands instrument era (late June – 23 July).** ⑰ *langlands_functor_ActiveV2 (6-29)* → ⑱ *transmission_functor_definitional_record (7-01)* — which specifies-and-parks the even-emission experiment that Phase IX executes → ⑲ *7-02 threads A–J* → ⑳ *7-03 threads K–U (ActiveV5)* → ㉑ *7-15 Collatz division-of-labor* → ㉒ *7-15 faces/seam groupoid Delta2* → ㉓ **OT1 EXHIBITION GRADED, conductor 4000 (ActiveV5, 7-22)** — the OT1 resolution; the 07-04/05 OT1 ledgers are read only through it → ㉔ *8000-rerun ladder-provenance closure (7-23)*.

**Phase VII — The assessment ledger (20–25 July).** ㉕ *external review of corpus + recent layer (ActiveV3)* → ㉖ *ledger patches P1–P7* → ㉗ *QC pass of the dated layer* → ㉘ *fourth review + Addenda 1–2* (the review layer correcting itself, twice — the metric-selection vocabulary retired) → ㉙ *period review, mid-May → present* (the propagation-layer diagnosis) → ㉚ *correctness patch bundle* (its appendix is the **Foundations Status block v2**) → ㉛ *direction memo* (discharge-before-mint at program level).

**Phase VIII — Carrier campaign & rung 4 (23–26 July).** ㉜ *campaign opening + rungs 1–2* → ㉝ *rung-3 R3.4 SUCCESS (ActiveV2-Delta4; Deltas 1–9)* → ㉞ **b = 3 CLOSED** (the countersigned-stamp exemplar) → ㉟ *ε-Ledger prereg + results* (root numbers from the marking ledger; the π/4 phase reads the twist bit) → ㊱ *Rung 4 — χ₆₀ SUCCESS, K2 discharged, both branches* (with χ₁₂ GRADED + committed census + Stage 1) → ㊲ *O-a Rung 3 (Route S)*.

**Phase IX — Cleanroom & the summit (27 July – 4 Aug; project `cleanroom/`).** ㊳ *r4 blind replication GRADED SUCCESS* → ㊴ *Rung E PoC RESULTS* ("the corner reads") → ㊵ *six-for-six RESULTS* → ㊶ *E0(ii) sweep* (NO/NO priority verdicts) → ㊷ **STATUS KD-2** — the honest failed campaign whose planted control voided its own floors; read it before ㊹ → ㊸ *RESUMPTION preregistration (08-03)* — the conductor-minimal retarget → ㊹ **COMMIT + RESULTS (08-03)** — 67 bits at N=1951, blind, sin-type, 8.957e-15 → ㊺ *decode2141 RESULTS (08-04)* → ㊻ *VERIFICATION addendum* (five adversarial avenues) → ㊼ **CRESPO GRADE — PASS** (+ crossverify supplement + the same-day totpos erratum) → ㊽ *countersign ledger* → ㊾ **STARTER_next_session_20260804** — the live frontier statement and decision menu.

## Conventions you'll see in the documents

`ActiveVn` = current working version · `ArchivalVn` = retained snapshot · `DraftVn` = working draft · `DeltaN` = incremental addendum · Tier 1–5 = the rigor ladder (Tier 1 verified theorem → Tier 5 retired claim) · `[V]` = claim with a reproducibility path (every [V] record ends with "Scripts archived at:") · `[C]` = conjectural identification · `[O]` = open question · **offered** = offered-not-self-filed, awaiting Will's countersign (see `countersign_ledger_20260803` — the default state of all cleanroom records) · **countersigned** = adjudicated stamp on record.

Files prefixed `TRANSCRIPT_` are session transcripts (verbatim exports of Will+model working sessions). Ingested third-party material uses `SOURCE_` instead. Campaign records carry mandatory parity qualifiers — "odd-icosahedral (calibration)" vs "even-icosahedral (the corner)" — and pre-registrations carry prediction-class labels (forced / pattern / no-prediction / novel).

Three documents govern how to read everything else: the **consolidated errata & status revision record (2026-06-10)** with its July successors (**ledger patches ActiveV1**, **correctness patch bundle**); the **review postmortem (2026-05-26)** — whose rule applies to this README too; and the **countersign ledger** for everything offered-not-self-filed. When a stamp-accreted headline argues with itself, the sanctioned fix is a full rewrite with the original moved to the errata block.

## State of the repository (2026-08-05)

Last known push 2026-07-24 (third review §0). Staged and pending: the rung-4 Google-Doc records, the cleanroom mirror, the summit records, and this Arch V2 package. Known punch-list items live in the delta catalog (sheet 5; 20 items — headline ones: rung-3 Deltas 2–3 missing from Drive, the archaeology report not yet filed, the even-icosahedral zip not yet in Drive, the V6 rewrite of the OT1 headline, the master Asides Log pointer index, and the deposit itself). The **Zenodo/arXiv deposit is the provenance instrument** — the only public anchor date is currently the 07-16 repo commit — and the direction memo makes it gating: no new campaign until the deposit and referee submission #1 are out.

## Provenance & method

Assembled July–August 2026 from the working corpus by automated cataloging passes with per-document review (196 documents individually reviewed for v1; ~150 more for the 08-05 delta), rule-based placement, and byte-exact mirroring where formats allowed. The cleanroom layer carries its own integrity spine: append-only SHA-256 manifests (v1–v6e) whose self-hashes (32c44d14…, 976eb06c…) are designed to be pinned by a single external timestamp. Assembly notes and the full provenance map live in the catalogs.

## License

No license has been granted yet; all rights reserved by the author pending a licensing decision. (A CC BY 4.0 / MIT split for documents/code is under consideration.)
