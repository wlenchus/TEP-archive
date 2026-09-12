# DEPOSIT RECORD — the TEP Archive on Zenodo, version 0.1.0 — 2026-09-12

*Claude (orchestrator, claude-fable-5-1). The deposit itself was made by Will (William C. Lenchus) through the Zenodo–GitHub integration; the orchestrator prepared the metadata and verified the record afterwards. Offered, not self-filed.*

## 1. The record

- **Version DOI:** 10.5281/zenodo.22727505 — the snapshot of 2026-09-12, version 0.1.0.
- **Concept DOI (all versions):** 10.5281/zenodo.22727504 — verified to resolve (HTTP 302) to the v0.1.0 record; it will resolve to the latest version as versions are added. This is the DOI for the statement's §2(iv) and for `CITATION.cff`.
- **Title (from `.zenodo.json`):** "The TEP Archive (August 2025 – September 2026): working records of the Terminal Equivalence Principle program, with Hecke eigenvalue tables, candidate Maass forms and numerical automorphy tests for the even icosahedral Artin representations of conductors 1951 and 2141."
- **Creator:** Lenchus, William C. **Resource type:** Other. **License on the record:** CC BY 4.0 (documents, records, data); MIT for source code per `LICENSE-MIT`. **Publication date:** 2026-09-12.
- **File archived:** `wlenchus/TEP-archive-v0.1.0.zip`, 11.1 MB — GitHub's source archive of the release `v0.1.0`, cut from `main` at fe456c5 (merge of PR #4), whose tree equals commit 24bb451.
- **Mechanism:** GitHub release → Zenodo webhook → record built from `.zenodo.json`, published automatically. Releases only are archived; later commits to `main` enter the record only at the next release.

## 2. What the snapshot contains, and what it is for

The repository as of PR #4: the July 2026 layer (CATALOG.csv and the 08-05 delta), the 2026-07-25 → 2026-09-12 layer (655 files by catalog addendum, SHA-256 and provenance per file), the licenses, `.zenodo.json`, `CITATION.cff`, and the four 2026-09-12 records — including the deposit statement **draft v2, offered and not countersigned**, and the RESULT record carrying the exact Heilbronn certificate, the errata to the 09-04 generator record, and the citation cards. Version 0.1.0 is a **timestamping deposit**: it fixes a public date for the archive's contents and claims nothing beyond what the README's "Honest framing" and not-claimed box say. Version 1.0.0 of this record is reserved for the release in which the statement is countersigned. The even-icosahedral **replication kit** is a separate repository and a separate record with its own DOI; that record, not this one, is the presentation object for readers outside the collaboration.

## 3. Consequences recorded in the repository (branch `doi-recorded-2026-09-12`)

README: the clause "None of this has been refereed or deposited" becomes "None of this has been refereed," followed by the deposit facts and the note that a deposit is a timestamp, not a review; DOI badge under the title; the State section's "not yet made" replaced by the deposit line; the arXiv half and the kit remain open. Status index: the deposit item updated, dated. `CITATION.cff`: concept DOI as `doi`, version DOI under `identifiers`. Statement draft v3 (working copy): §2(iv) carries both DOIs.

## 4. Standing

Next: Will reads statement v3 and returns counters; the kit is assembled (relative paths, the generator-deduplication script, the completed 34-digit pass, the 228-row script or its single-implementation marking, expected outputs, two license files) in its own repository; on countersign, this record's version 1.0.0 and the kit's first release follow. Zenodo metadata is editable in place: once the kit has a DOI, this record's description should gain a pointer to it.
