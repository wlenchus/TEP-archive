# The TEP Repository Architecture — V2 (ActiveV2)

*Prepared 2026-08-05 by Claude at Will Copeland's direction. Supersedes the 2026-07-16 Repository_Arch_ActiveV1 layer (`TEP_Archive_Proposal.md` + `TEP_Corpus_Catalog_v1.xlsx` + `catalog_master.csv`), which remains the index of record for everything on or before 2026-07-16 and should be retitled `…_ArchivalV1` at Will's convenience (the Drive connector cannot rename folders). Companion: `TEP_Corpus_Catalog_delta_v1_1_20260805.xlsx` (the delta catalog), `README_ActiveV2_20260805.md` (the refreshed repo README), `catalog_delta_master_20260805.csv`. This document was ordered, in effect, by the corpus itself: the third external review (07-24 §0) declared the Arch layer stale and the spine refresh was repeatedly re-ordered thereafter (fourth review, period review, direction memo).*

*Method note: prepared from a full re-crawl of Drive (every file created or modified after 2026-07-16, paginated to exhaustion, ~450 objects), a complete read of catalog v1 (all six sheets), full reads of the review layer (07-20 → 08-01), and complete reads/digests of all 49 project cleanroom docs. Everything below is offered, not self-filed, per the standing convention.*

---

## 1. What changed since V1 — the short version

V1 catalogued a **single-shelf, pre-summit corpus**: 2,602 files in Drive, frontier at the 07-15 Collatz cluster, archive repo proposed but not yet built. Nineteen days later the picture is qualitatively different in four ways:

1. **The corpus became multi-shelf.** The claude.ai project **"2026-07-26"** (`cleanroom/` namespace, 49 docs) is now a first-class corpus location — it holds the *primary* records of 2026-07-27 → 2026-08-04, under SHA-256 manifests, with script bundles from which a fresh container regenerates everything deterministically. The GitHub repo (**tep-archive**) went live and received pushes through ~07-24. Hash-pinned zip archives delivered in-conversation (e.g. `TEP_even_icosahedral_20260803-04.zip`, sha256 260512aa…) are a fourth, provenance-bearing shelf.
2. **The frontier moved twice.** First the OT1 resolution (07-22/23: true conductor 4000, ladder closed by execution) and the carrier campaign (rungs 1–4, 07-23 → 07-26, ending in weight-1 icosahedral lift data read blind from a weight-2 census, both branches, K2 discharged). Then the cleanroom era (07-27 → 08-04): rung-4 blind-replicated by a fresh instance; first-ever numerical entirety certificates for even-icosahedral Artin L-functions (all six Doud fields plus the corpus field); an honestly failed summit campaign (KD-2) whose planted control voided its own floors; and finally the **conductor-minimal retarget and the summit read** — committed Hecke data at Doud-1951 and Doud-2141, five adversarial verification avenues, and the open Crespo-genre construction grading both decodes **PASS** (65/65 modulo exactly one odd quadratic twist each). These are, per the E0(ii) sweep, the only such datasets in existence — offered-not-self-filed, countersign-gated, unpublished.
3. **The assessment layer became an instrument.** Six external-review documents (07-20, 07-22, 07-24, 07-25 ×2 waves, 08-01 archaeology) now form a self-correcting ledger: reviews carry their own errata, correct *each other* (Addendum1 caught three successive reviews re-citing a closed question; Addendum2 then corrected Addendum1), and produced the two governing patch sets (`ledger_patches_proposed_ActiveV1`, `correctness_patch_bundle`) plus the **Foundations Status block v2** — the canonical statement that the budget is derived twice, the metric is forced, and the residue is three named lemmas. The 5-26 rule ("trust derivations, distrust consolidation prose") is now demonstrated to bind the review stratum too. Read every review together with its errata.
4. **The hygiene program V1 proposed was substantially executed** — by the corpus, within a week: `Transcripts/` and `External Reference Papers/` shelves created (07-21); `SOURCE_` vs `TRANSCRIPT_` prefixes adopted into the README (07-23); the Gamma* flag closed at read-status level; the OT1 16000-host flag overtaken entirely; canon re-versioned (Central Reference → **ActiveV3**, interior spine trace → **ActiveV12**, early corpus synthesis → ActiveV2, three more ActiveV2s) via the `2026-07-22 Batched Edits & Updates` staging folder. V1's remaining flags and the new ones are graded in the delta catalog's **Hygiene Punch List V2** (20 items: 3 closed/resolved, 2 partial, 15 open — most of them one-touch).

## 2. Corpus state, by the numbers (2026-08-05)

Drive: the v1 baseline (2,602 files) plus ~150 substantive new documents and instrument files in the TEP tree (plus the 07-16 normalization re-uploads catalogued in v1). Project: 49 cleanroom docs. Repo: 158 curated docs at last known push (head ~07-24 per the third review §0); everything later is Drive/project-only. Live canon pointers as of today:

| Layer | Live edition | Location |
|---|---|---|
| Central reference | `2026-04-19 TXT_V2_TEP_Entrodynamics_Central_Reference_ActiveV3.txt` (2026-07-23) | Drive: Batched Edits & Updates · repo `00_canon/` |
| Corpus self-trace | `2026-06-07 interior_spine_trace_ActiveV12.md` (2026-07-23) | same |
| Errata line | 06-10 consolidated errata → 07-21 `ledger_patches_proposed_ActiveV1` → 07-25 `correctness_patch_bundle` (P-A…P-G) → 08-01 archaeology corrections | Dated layer / R34 folder |
| Foundations | **Foundations Status block v2** (appendix of the correctness patch bundle; queued for Central Reference + README) | R34 folder |
| Frontier statement | `cleanroom/STARTER_next_session_20260804.md` | project |
| Gating ledger | `cleanroom/countersign_ledger_20260803.md` + C-additions + D-1…D-6 | project |
| Instrument-era resolution | `ot1_delta_EXHIBITION_GRADED_conductor_4000_ActiveV5` + 07-23 ladder closure | Batched Uploads · repo `50_code/ot1/` |
| Summit packaging | `TEP even-icosahedral campaign 2026-08-03_04 — README + archive pointer` | Drive: Code, Tests, & Datasets |

## 3. The repository tree — V2 (retained, with two additions)

V1's tree survives contact with three weeks of heavy use; the corpus's own staging practice (Batched Edits / Batched Uploads → push) validates it. I am deliberately **not** reorganizing what works. Two additions and one promotion:

```
tep-archive/
├── README.md                  ← replace with README_ActiveV2 (this package)
├── CATALOG.csv                ← v1 index + catalog_delta_master_20260805.csv until a full v2 crawl
├── 00_canon/                  ← ActiveV3 central reference, ActiveV12 spine trace, errata line,
│                                 Foundations Status block v2 (NEW — paste as always-visible header)
├── 10_papers/                 ← unchanged (homogeneity-closure note = referee submission #1)
├── 20_records/                ← the dated ledger, + 2026-08/
│   └── cleanroom/             ← NEW: 1:1 mirror of the project cleanroom/ set, kept intact as a unit
│                                 (preregs, commits, results, verification, Crespo grade, manifests,
│                                  script bundles; the manifests' self-hashes are the integrity spine)
├── 30_assessments/            ← + external/ gains the 07-20→08-01 review ledger (reviews WITH their errata)
├── 40_foundations/            ← unchanged
├── 50_code/                   ← + ot1/full_width_instrument/ (36 files), verify/ (07-19/20 scripts),
│                                 gp2/ (bundle C), rung-3/4 labs
├── 60_data/                   ← unchanged (DATA_MANIFEST pattern; hosts/M⁻¹ regenerable, not shipped)
└── 90_archive/                ← + precursors/ gains the percolation orphan (P-D); superseded/ grows
```

**Promotion:** the practice layer (asides/consolidation entries — `asides_log_entry_*`, the root consolidation gdocs, the project log entries) is corpus, not exhaust. It stays filed beside the records it narrates (no new top-level directory), but the delta catalog now types it (`practice`) so it is indexable, and punch item 13 proposes the master Asides Log doc become a pointer index into the dated entries. That is the lightest structure that stops the current fragmentation.

**Location as a first-class column.** Every delta-catalog row carries its shelf (drive / project / repo / conversation-zip). Any future full catalog v2 should keep this — the single-shelf assumption is the one structural thing V1 got wrong in hindsight.

## 4. The priority spine — V2

Full table with links in the delta catalog (`Priority Spine V2` sheet). Phases I–V are **retained from V1 unchanged** (16 docs — they were right) with exactly two pointer updates: **#5** now reads the Central Reference in its ActiveV3 edition, and **#13** reads the spine trace at ActiveV12. Phase VI is updated; VII–IX are new.

- **I. Foundation** (1–3): v0.5 Working Notes; Framework Reconciliation; Comprehensive Documentation.
- **II. Maturation** (4–5): 2-2-26 Rigorous Assessment *(historical specimen — P1 rebilling stands)*; **V2 Central Reference, ActiveV3 edition**.
- **III. Publication-track** (6–8): purity/decoherence limit; purity_speed_limit_v2; homogeneity-closure note *(= referee submission #1 per the direction memo)*.
- **IV. Epistemic calibration** (9–12): 5-25 external review; 5-26 postmortem; 5-29 closing note; 6-10 consolidated errata.
- **V. Verified corpus map** (13–16): spine trace **ActiveV12**; early corpus synthesis (ActiveV2); 6-18 assessment delta; 6-20 external-assessment evolution.
- **VI. Langlands instrument era** (17–24): 06-29 functor record; 07-01 transmission-functor pin *(which specifies-and-parks the even experiment that becomes IX)*; 07-02 threads A–J; 07-03 threads K–U; 07-15 Collatz division-of-labor; 07-15 faces/seam groupoid; **07-22 OT1 EXHIBITION ActiveV5** *(replaces v1's #21; read the 07-04/05 OT1 ledgers only through it)*; **07-23 ladder-provenance closure**.
- **VII. The assessment ledger** (25–31): 07-20 corpus review ActiveV3; 07-21 ledger patches P1–P7; 07-22 QC pass; 07-25 fourth review + Addenda 1–2 *(the review layer correcting itself, twice)*; 07-25 period review *(the propagation-layer diagnosis)*; 07-25 correctness patch bundle *(appendix = Foundations Status block v2)*; 07-25 direction memo *(discharge-before-mint at program level)*.
- **VIII. Carrier campaign & rung 4** (32–37): campaign opening + rungs 1–2; rung-3 R3.4 SUCCESS (Deltas 1–9); **b=3 CLOSED** *(the countersigned-stamp exemplar)*; ε-Ledger prereg + results; rung-4 χ₆₀ SUCCESS with K2 discharged (with χ₁₂ GRADED + committed census + Stage 1); O-a Rung 3 (Route S).
- **IX. Cleanroom & the summit** (38–49, all in the project): r4 blind replication; Rung E PoC ("the corner reads"); six-for-six; E0(ii) NO/NO; **KD-2** *(the honest failure that makes the success legible)*; the 08-03 retarget prereg; **the COMMIT + RESULTS** (67 bits at N=1951); 2141 on demand; the five-avenue verification; **the Crespo grade PASS** (+ totpos erratum); the countersign ledger; **STARTER_next_session_20260804** *(the live frontier)*.

**Fast path (≈ one sitting), for a reader who must triage:** #5 (ActiveV3 central reference) → #30's appendix (Foundations Status v2) → #12 + #26 (errata line) → #11 (closing note) → the even-icosahedral campaign README (Drive) → #44 → #47 → #49. Marked ★ in the catalog sheet.

## 5. Supersession chains — additions since V1

V1 §4's chains all stand. New chains the metadata layer should carry (full ledger: delta catalog, `Version & Status Events` sheet, 36 events):

- **OT1 resolution:** 07-04 N8000-excluded + 07-05 buhler/underfilter → **07-22 EXHIBITION (…→ActiveV5)** → 07-23 8000-rerun ActiveV1 (ladder closed; the 07-04 REJECT×8 falsified *by execution*; 800/1600/2000 REJECTs confirmed). V6 headline rewrite still queued.
- **Canon refresh (07-23):** Central Reference → ActiveV3; spine trace V11 → V12; early corpus synthesis → ActiveV2; scale_shape, manifold_existence, bures_fisher supplement → ActiveV2.
- **The 07-19 block re-versioning (07-22):** four records retitled ArchivalV1 in place with new ActiveV2 instances issued (gaussian-witness pair, two_ledgers, hbar_c) — the pattern V1 predicted, running live.
- **Foundations vocabulary:** fourth review §4 → Addendum1 E1 → Addendum2 E2 (retires "metric selection" / "forced-vs-chosen floor") → foundations_status_block DraftV1 → **v2 (patch-bundle appendix)**.
- **Decode chain:** B-prereg + Amendments 1–4 → KD-2 (floors voided) → 08-03 RESUMPTION retarget (conductor-minimal) → COMMIT (P1 refuted in print; orientation erratum) → 2141 (orientation per-field) → VERIFICATION addendum (V4 re-tiering; V5 erratum-let) → CRESPO grade PASS → totpos erratum (same-day). Starters: 07-27 → 08-03 → **08-04 (live)**.
- **Black-hat doc:** §1 countersigned via b=3 CLOSED; §§2–3 falsified by the μ-floor test (kept with tombstone); Weil-route inspection resolves the census-free [C] negative and *strengthens* the stamp.
- **Practice-layer self-corrections:** cleanroom entry's "nothing touches even icosahedral" → corrected (lexical summit-drift named); archaeology report DraftV1 → ActiveV2 with six corrections ("verbs are claims").

## 6. Conventions now standing (V1 §"status vocabulary" + what July added)

Everything in v1's vocabulary, plus: `DraftVn`; `countersigned`; `offered` (offered-not-self-filed — the default state of every cleanroom record, gated by the countersign ledger); prereg/commit/results/grade roles; manifest/bundle; `practice`. Process rules now standing (sources in the delta catalog): pre-register with kill conditions before tests; amendments may add axes, never relax bars; commit-with-SHA-256 before graders; training-prior disclosure before answer-adjacent computation; parity qualifiers in titles; content-keyed references; inspect-before-cite with own-eyes reads for load-bearing docs; live cells for every inherited discrete gauge; dictionary lint + planted benchmarks before reading optimizer floors; same-day errata at headline volume; prediction-class labels (forced / pattern / no-prediction / novel); "verbs are claims"; sweep-first symmetric on "established" *and* "still open"; every [V] ends with "Scripts archived at:"; stamps are two-sided (demotion + surviving claim); when stamps accrete, rewrite with the original moved to the errata block.

## 7. What is genuinely open (so the next Arch pass doesn't have to rediscover it)

The program-level queue, consolidated from STARTER_20260804, the countersign ledger, and the direction memo — in the direction memo's own priority order: **(1)** countersign backlog (sessions deep; open with the ledger); **(2)** the Zenodo/arXiv **deposit** — the provenance instrument (only public anchor is the 07-16 repo commit) — and referee submission #1 (homogeneity-closure note), both gating under discharge-before-mint; **(3)** the decision menu: countersign+referee / killer test at Doud-3701 (prediction-classes pre-declared, incl. the novel Crespo-twist-character prediction) / A0–T4 formalization; **(4)** u-closure, 1951 mid-band, GATE-B/wall map, det-1 battery; **(5)** rigorization (Palojärvi–Zhao), Artin holomorphy untouched by numerics; **(6)** Magma/Sage replication; **(7)** repo return + next push incl. the cleanroom mirror; **(8)** the 20-item hygiene punch list. Master Asides Log load step: owed 4× — punch item 13 is the fix.

## 8. Honest bite

Two things this pass could not do, and one caution. It could not verify the GitHub repo's current contents (no repo access from this session; "head ~07-24" is the third review's dated observation, not a live check). It could not locate the 08-01 archaeology report + appendices in Drive (conversation-side per its consolidation entry; punch item 12) — so their six corrections are carried here from the entry, not from the report. And the caution this document applies to itself: it is consolidation prose. Where it disagrees with a derivation record, the record wins — file the erratum against *this*.

*— Offered, not self-filed. Suggested countersign items: adoption of the V2 spine (§4), the two canon-pointer updates (#5, #13), the cleanroom-mirror repo path (§3), and the punch-list dispositions (delta catalog sheet 5).*
