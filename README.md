# The TEP Archive

**The Terminal Equivalence Principle (TEP)** — a boundary-first, operationalist research program in mathematical physics: the physical content of a passive system is taken to be exhaustively characterized by its boundary response (its Dirichlet-to-Neumann operator), with the Schur complement as the fundamental operation of physical reduction. From that stance the corpus develops an information-geometric "budget" formalism, tiered-rigor theorem notes (e.g. a purity/decoherence speed limit), an experimental dictionary, a transmission-functor bridge toward Langlands-type structures, and — from late July 2026 — a seam-constraint decoding instrument that produced, and saw constructor-confirmed, the first Hecke-eigenvalue data for even icosahedral 2-dimensional Galois representations (Doud-1951 and Doud-2141), followed by an attempt, still open, to close the Artin conjecture for those two representations.

This repository is the **curated public record** of that program. It now holds roughly 800 primary documents, scripts, and data files spanning August 2025 – September 2026, selected and organized from a working corpus of 2,600+ Drive files plus a sealed project shelf. The July 2026 layer is indexed in [`CATALOG.csv`](CATALOG.csv) (through 2026-07-16) and [`2026-08-05 catalog_delta_master_ActiveV1_1.csv`](2026-08-05%20catalog_delta_master_ActiveV1_1.csv) (2026-07-16 → 08-05); the layer added on 2026-09-12 is indexed file-by-file, with SHA-256 hashes and provenance, in [`CATALOG_ADDENDUM_2026-07-25_to_2026-09-12.csv`](CATALOG_ADDENDUM_2026-07-25_to_2026-09-12.csv).

## Honest framing

The corpus's character judgment of record (the 2026-05-29 closing note, restamped two-sidedly on 2026-08-06): *not crankery* — strengthened by a falsification record kept at headline volume — and *methodologically exemplary* in its pre-registration / sealed-commit / solver-qualification / countersign protocol; no longer summarizable as "a reorganization with modest verified content," because the even-icosahedral Hecke datasets are first-of-their-kind arithmetic data, constructor-confirmed 65/65 per field modulo one pre-declared quadratic twist, with no prior numerical treatment found (E0(ii) sweep, five disclosed coverage gaps). Foundations are stated as forced at the metric-space level modulo three named lemmas (canon A7; Foundations Status block v2, `00_canon/2026-07-25 correctness_patch_bundle_ActiveV1.md`, appendix).

On the Artin conjecture itself the record is unambiguous, and the September 2026 council handshake made it unanimous: **not closed, and not equipped to close it decisively**; equipped to state it exactly, certify the object, and deposit. The Heilbronn coin of 2026-09-04 names the missing inequality and shows that no subgroup of 2.A₅ supplies it; every certificate in the record (pointwise automorphy at 10⁻²⁴, Fricke covariance at 10⁻²⁶, the 326- and 358-generator certificates) is an instrument reading of the conjecture's content, not a proof of it — Fricke covariance is equivalent to entirety, hence to the conjecture.

**None of this has been refereed or deposited.** That clause is the operative one and gates every campaign (direction memo 2026-07-25; adjudication 2026-08-06; council orientation 2026-08-26). The Zenodo/arXiv deposit is the program's own stated first priority and has not yet been made.

### The not-claimed box
Strong Artin for the even icosahedral representations at conductors 1951 and 2141 is not claimed. Entirety of L(ρ̃) is not claimed; entirety of ζ_{K₅}/ζ (Dedekind's conjecture at the A₅ quintic) is not claimed (erratum 2026-09-04). Automorphy of the constructed Maass candidates is not claimed — it is measured at finite precision. No result in this archive has been re-run by a person outside the collaboration. The framework's effectiveness is demonstrated on the readability side (parity read, explicit derivation, certified constants, exact moments) and on machine-checked identities; on the proof side it is undemonstrated by the record's own ledger.

## Who wrote what

The program is Will Copeland's; he directs it, decides what is countersigned, and holds the only decision rights over claims. The records since 2026-07-27 were written by Claude models — named in each record's header (Claude Fable 5 through 2026-08, Claude Fable 5.1 from 2026-09-04; from 2026-08-26 in a "council" configuration of charter-bound seats with an orchestrator) — and are **offered, not self-filed**: every stamp in them awaits Will's countersign (see `20_records/cleanroom/cleanroom/countersign_ledger_20260803.md` and the 2026-08-26 rulings on countersign and attribution). Will's own notes are marked as his (e.g. the two d_eff notes of 2026-08-29, archived verbatim with provenance headers). Session transcripts (`90_archive/transcripts/`, `TRANSCRIPT_` prefix) are verbatim exports of Will+model sessions; ingested third-party material carries the `SOURCE_` prefix.

The commits that assembled this repository were made by Claude models at Will's direction and are attributed as such in the git history. Nothing in this repository poses as Will; where the council represents him, it identifies itself. The corpus's language rule since 2026-09-04: checks run inside the collaboration are "same-family, separate implementation," never "independent."

## Where the corpus lives (four shelves)

1. **This repository** — curated mirror; pushes 2026-07-16, 2026-07-23/24, 2026-09-12.
2. **Google Drive** (`TEP 2026-07/…`) — the working tree: dated records, staging folders, instruments and data, the 2026-08-17 closure-campaign pack, and the provenance bundles of 2026-08-29 and 2026-09-04 (hash manifests; the 09-04 folder also holds the files, byte-verified).
3. **The claude.ai project "2026-07-26"** — the sealed record set of 2026-07-27 → 2026-09-04 (142 documents: pre-registrations, commits, results, verifications, errata, the council records, the September stack). Mirrored 1:1, byte-exact, at `20_records/cleanroom/`.
4. **Hash-pinned bundles** delivered in-session (e.g. `deposit_bundle_20260829.zip`, sha256 d0eb71fe…; `deposit_bundle_20260904.zip`, sha256 19f42f70…), whose per-file manifests are in `50_code/`.

## How this repository is organized

```
00_canon/          the current authoritative layer: central reference (ActiveV3), the errata line
                   (06-10 → 07-21 ledger patches ActiveV2 → 07-25 correctness patch bundle with the
                   Foundations Status block v2 → 2026-09-12 errata & status index), corpus maps, the
                   repository-architecture and spine records (08-05/08-09), the ratified council
                   orientation (08-26), the deposit skeleton (08-27)
10_papers/         publication-track standalone theorem notes (unchanged since July; see errata index §G)
20_records/        the chronological ledger: 2026-04 … 2026-08 dated records;
   cleanroom/      1:1 byte-exact mirror of the project "2026-07-26" (cleanroom/, charges/, arch/,
                   assessments/ — 142 files, filenames preserved, dates in the suffixes)
   2026-08/        the 2026-08-01 archaeology bundle and the 2026-08-17 closure-campaign pack, each
                   kept intact as a unit, plus the Drive-only dated records of August
30_assessments/    internal reviews, external calibration, audits — now with the 07-20 → 08-01 review
                   ledger (each review WITH its addenda) and council/ (charters, protocols, seat
                   reports, mailboxes, the 2026-09-04 handshake primaries)
40_foundations/    v0.5 working notes + the Base Theory shelf (unchanged)
50_code/           decoders, verify/ scripts, the OT1 instrument, the rung-3/4 labs, the 2026-08
                   even-icosahedral closure shelf (scripts, READMEs, provenance manifests), the
                   2026-08-29 deposit scripts, the 2026-09-04 expedition scripts and outputs
60_data/           the certified Hecke-eigenvalue tables (both conductors, to 10⁵) + DATA_MANIFEST.md;
                   large artifacts stay in Drive, indexed not mirrored
90_archive/        transcripts; precursor eras indexed via CATALOG.csv
```

Provenance eras: **QSF/UST precursor** (Q1 2025) → **GSR** (mid 2025) → **IFFT** (late 2025) → **TEP** (Sep 2025 – present). Within TEP, the reliability gradient the council adopted 2026-08-26 applies: documents before the V2 Central Reference (2026-04-19) are read with their errata; V2 → early June with caution; the clean-room era (2026-07-27 onward) carries its own SHA-256 manifests and countersign ledger.

## The priority spine — reading order (Spine V4, 2026-08-09, extended to September)

*Spine V4 (`00_canon/2026-08-09 spine_V4_canon_first_mode_priced_DraftV1.md`) was offered for countersign and is used here as the reading order because its companion assessor review found the earlier order fed a stranger the most-corrected stratum before the correction apparatus. A new reader follows it as printed; an assessor additionally executes the 2026-08-08 onboarding read order first.*

**Gate 0 — the correction apparatus (read first, ~45 min).** `00_canon/2026-06-10 consolidated_errata…` (everything pre-June is read with this in hand) → `00_canon/2026-07-21 ledger_patches_proposed_ActiveV2.md` (in-file header still says ActiveV1 — C16) → `00_canon/2026-07-25 correctness_patch_bundle_ActiveV1.md` with its appendix, the Foundations Status block v2 → **`00_canon/2026-09-12 errata_and_status_index_2026-07-25_to_2026-09-12.md`** (the council-era errata line, 37 items) → `20_records/cleanroom/cleanroom/ONBOARDING_assessor_grounding_20260808.md` §3 (the regression-trap card T1–T12). The reader's rule, six clauses: no document is current below its latest stamp; consolidation prose is trusted less than derivation records; "verbs are claims"; reproduce a chain before extending it (C13); verify that an open problem is open (C14); date-check every assessment against the errata that postdate it.

**Stratum 1 — the framework as it stands (definitional canon first).** `2026-07-01_transmission_functor_definitional_record` (I.5 first) → `2026-06-29 …langlands_functor_ActiveV2` (canon A7) → the 06-25 delta (the three W's) → Foundations Status block v2 → the Central Reference ActiveV3, *rebilled* as the tiered claims-and-retirements ledger (it contains none of the instrument era) → `interior_spine_trace_ActiveV12` → the live frontier pair `STARTER_next_session_20260812B.md` + `STARTER_PROMPT_TEP_grounding_and_thread_diff_20260815.md` (project mirror) → the countersign ledger → the character frame read two-sided (5-29 closing note with the 08-06 adjudication) → **the council orientation** `00_canon/2026-08-26 COUNCIL_general_priority_and_orientation.md` and the **deposit skeleton** `00_canon/2026-08-27 DEPOSIT_SKELETON_DraftV1.md`.

**Stratum 2 — current evidence, priced by mode (datasets and derivations, then audits, then the falsified-predictions ledger as first-class content).**
Band A, the datasets and certificates: the even-icosahedral campaign README (`50_code/2026-08_even_icosahedral_closure/TEP_even_icosahedral_V2/`), `decode2dim_COMMIT_20260803` + `RESULTS`, `decode2141_RESULTS_20260804`, the five-avenue `VERIFICATION_addendum`, the Crespo grade (+ the same-day totpos erratum), `STATUS_KD2_20260727` (read before trusting the commit), the 08-09 articulation of the Maass forms (`EXACT_articulation_maass_1951_20260809B`; `RESULT_maass_live`; the replication record), the 08-10/11 instrument records, and the 2026-09-04 certificates (`RESULT_complete_generator_certificate_1951_20260904`; `RESULT_unipotent_seam_and_adjoint_RS_constant_20260904` for L(1, Ad ρ̃) at both conductors).
Band B, derivations and theorem notes: the closure campaign's instrument layer (`20_records/2026-08/2026-08-17 1951_closure_campaign/` — read `00_START_HERE_MANIFEST.md` and `03_verification/` first; the manifest's canonical-values table wins), the Crouzeix corner read through `charge1_REASSESSMENT` **and** the 2026-08-26 status notice, the thin-film close-out `PU_run1_RESULT`, the 2026-09-04 Heilbronn coin (`PROPOSAL_port_definition_and_heilbronn_coin_20260904`), and the publication-track notes in `10_papers/`.
Band C, the prediction ledger: `PF_run1_RESULT_falsified` + `ERRATUM_PF_chain_misconstruction`, `PR_run1_RESULT_falsified`, `PH_run1_RESULT_inconclusive`, `RESULT_Pt1_FALSIFIED_rapidity_sampling_20260811B`, the black-hat tombstone — kept at full volume (the tally predictions 0/3, audits 1/1, derivations 2/2 is the finding).

**Stratum 3 — the instrument and method.** `decode2dim_RESUMPTION_preregistration_20260803` §§1, 3 · `portseam_reconsidered_20260727` · the prereg amendments · the Crespo-grade method · the PROVENANCE_MANIFEST files and SCRIPTS_BUNDLE files (the SHA-256 spine; regenerability) · the 2026-09-04 scripts (`50_code/2026-09-04_expedition/`).

**Stratum 4 — how we know (the assessment ledger).** `30_assessments/external/`: the 07-20 corpus review, the 07-22 OT1 review and QC pass, the 07-24 third review, the 07-25 fourth review with Addenda 1–2, the period review, the direction memo; the 08-01 archaeology report ActiveV2 and its correction record (`20_records/2026-08/2026-08-01 tep_archaeology_appendices/`); the 08-09 assessor review of the architecture (`00_canon/`); the council's own ledger (`30_assessments/council/` — the convening record, the deep-grounding addendum, the pack read with its assessor grade, the 2026-09-04 handshake: five seat primaries and the synthesis `COUNCIL_handshake_equipment_question_20260904`). The practice layer (`asides_consolidation_log_entry_*`) is load-bearing for the provenance of positions.

**Stratum 5 — historical strata (provenance, not doctrine; read only through Gate 0).** The June maps; the May calibration; the 2-2-26 Rigorous Assessment (historical specimen — graded FAIL-as-assessment by the council, with an eight-item confabulation catalog); the foundation era (v0.5, Framework Reconciliation, Comprehensive Documentation); the precursor eras at zero evidential weight.

**Fast path (one sitting):** Gate 0's reader's rule and trap card → TF I.5 → Foundations Status v2 → the campaign README → the 08-03 COMMIT → the Crespo grade → the 08-17 manifest §§3–5 → the 2026-09-04 handshake synthesis §1 → the errata & status index.

## Conventions you'll see in the documents

`ActiveVn` = current working version · `ArchivalVn` = retained snapshot · `DraftVn` = working draft · `DeltaN` = incremental addendum · Tier 1–5 = the rigor ladder (Tier 1 verified theorem → Tier 5 retired claim) · `[V]` = claim with a reproducibility path (every [V] record ends with "Scripts archived at:") · `[T]` machine-checked / proved in-record · `[T-v]` proved by a prover session and verified with named repairs · `[T-cited]` a cited theorem whose hypotheses were checked at the point of use · `[Tsk]` skeleton-grade · `[CN]` certified-numerical · `[cal]` calibrated against controls · `[id]` an identification/relabeling, never load-bearing · `[R]` reading/dictionary layer · `[C]` conjectural identification · `[O]`/`[open]` named open statement · `[recalled]` rests on memory of a standard result, unpinned · **offered** = offered-not-self-filed, awaiting Will's countersign (the default state of every record since 2026-07-27) · **countersigned** = adjudicated stamp on record. Campaign records carry parity qualifiers ("odd-icosahedral (calibration)" vs "even-icosahedral (the corner)") and prediction-class labels (forced / pattern / no-prediction / novel). Council records label obstructions (M) method-relative, (L) language-invariant, or (A) audit findings (2026-09-04).

Four documents govern how to read everything else: the consolidated errata record (2026-06-10) with its successors (ledger patches ActiveV2; correctness patch bundle; the 2026-09-12 index); the review postmortem (2026-05-26) — "trust derivations, distrust consolidation prose," a rule that applies to this README; the countersign ledger for everything offered; and, for the closure campaign, the 2026-08-17 manifest (the precedence document: where a parent and a correction disagree, the correction wins; where anything disagrees with its canonical-values table, the table wins).

## State of the repository (2026-09-12)

This push adds the layer 2026-07-25 → 2026-09-12 (about 640 files): the review ledger and rung-3/4 records of July 24–27; the 1:1 project mirror (clean-room era, charges, council, the September stack); the archaeology bundle; the closure-campaign pack; the council apparatus; the even-icosahedral code shelf; the deposit bundles' scripts and manifests; the certified eigenvalue tables. It executes the repository architecture proposed 2026-08-05 (`00_canon/2026-08-05 TEP_Repository_Arch_ActiveV2.md` §3: the cleanroom mirror, the 2026-08 records, the review ledger, the code shelves) and the README regeneration the 08-09 assessor review asked for (F6), and replaces the 08-05 README draft (`00_canon/2026-08-05 README_ActiveV2 (superseded…).md`). Five commits made in an 08-05/06 session were reported as unpushed (spine V4 §E.2) and never reached this remote; their intended content is re-assembled here from the project and Drive.

Still open, as the records left them: the Zenodo/arXiv deposit (the program's #1); referee submission #1 (the homogeneity-closure note); the Anandan–Aharonov patch to the purity papers (P-B); the OT1 V6 headline rewrite (C12); the master Asides Log pointer index; the coin's literature check (Foote TAMS 321 (1990)); a real assessor pass over the 08-29 AUDIT and WORKS records (ungraded); the external loop (no step yet re-run by a human outside the collaboration); and the rotation of a personal access token exposed in an 08-05 transcript. Datasets and images larger than ~150 KB remain in Drive and are indexed in `60_data/DATA_MANIFEST.md`.

## Provenance & method

The July 2026 layer was assembled from the Drive corpus by an automated cataloging pass with per-document review (see the 07-16 and 08-05 catalogs). The September 2026 layer was assembled as follows. Project documents were mirrored byte-exactly from the claude.ai project and checked against the clean-room SHA-256 manifests where they list them (11/11 matching) and against the 2026-08-29 bundle manifest. Drive files were fetched through the Drive connector: as base64 with byte-length verification against Drive's file size (and zip CRC where applicable), and where a second, independently transcribed copy existed, cross-checked against it modulo whitespace; Google-Docs-native records were exported as text/markdown and are marked as exports in the catalog addendum (no byte-exact form exists for them). Every added file carries its SHA-256 and its source (project path, Drive file id, or session bundle) in `CATALOG_ADDENDUM_2026-07-25_to_2026-09-12.csv`. The clean-room layer's own integrity spine — append-only PROVENANCE_MANIFEST files (v1–v7) and the two deposit-bundle manifests — is mirrored unchanged; a single external timestamp on those manifests would pin the whole layer.

## License

No license has been granted yet; all rights reserved by the author pending a licensing decision. (A CC BY 4.0 / MIT split for documents/code is under consideration.)
