# 50_code — Instruments

Decoder lineage (v1/v2), validation scripts, and analysis code. `ot1/` holds the OT1 icosahedral-decoder instrument records: session status, the N8000 exclusion delta, the Buhler control PASS (which retracted the a₂-evenness claim), and the underfilter addendum that voided the first N=16000 host.

Colab notebooks are indexed in /CATALOG.csv but not mirrored (Colab-format export was unreliable at assembly time).

**Added 2026-09-12.** `2026-07_rung3_rung4_labs/` — the Code/Tests folders of the carrier campaign (rung-3
ribbon/AGM/p2 labs and rung-4 census scripts; the 07-25 session bundle zip). `2026-08_even_icosahedral_closure/`
— the even-icosahedral closure shelf as it stands in Drive: the V1 and V2 campaign archives (READMEs, scripts,
qualification and summit logs; the hash-pinned zips and >150 KB artifacts are indexed in `60_data/DATA_MANIFEST.md`,
not mirrored), the 08-09 dyadic-closure and MAASS_LIVE folders, the even_icosahedral/ and tomography/ script sets,
and the PROVENANCE_MANIFEST v7 addenda. `2026-08_crouzeix/` — the 08-01 Crouzeix strike and ledger scripts
(Google-Docs exports). `2026-08-29_deposit_scripts/` — the council deposit bundle's scripts (Mackey certificate,
COH pipeline, deep reading, three-tier, twin, diagonal probe), its README and SHA-256 manifest, and the 08-30
portable supplement. `2026-09-04_expedition/` — the Heilbronn-coin script and output, the adjoint L-function
scripts (Python + PARI/GP) with outputs for both conductors, the complete-generator certificate sweeps with
their TSV results, the 34-digit mpmath pass (results as of 2026-09-12: 5 of 24 sampled generators, all at the
truncation floor), the PARI generator scripts and raw generator lists, and the bundle README and manifest.
The clean-room script bundles (`SCRIPTS_BUNDLE.txt`, `SCRIPTS_BUNDLE_C_20260804.txt`, `DECODE_COMMIT_bundle_20260803.json`)
live with their records in `20_records/cleanroom/cleanroom/`; each is a concatenation with `==== FILE:` headers.
