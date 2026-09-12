# Upload note — delta catalog files (2026-08-05)

The two markdown documents in this folder (`TEP_Repository_Arch_V2_20260805.md`, `README_ActiveV2_20260805.md`) uploaded byte-exact via the Drive connector.

The two data files could NOT be uploaded intact through the connector (its per-call payload ceiling truncated the binary twice). They were delivered in full in the Claude conversation of 2026-08-05 — please drop them into this folder from there:

- `TEP_Corpus_Catalog_delta_v1_1_20260805.xlsx` — 43,144 bytes, sha256 a97c689d3d5575d1… (6 sheets: READ ME · Priority Spine V2 [49] · New Documents 0716-0805 [65] · Project Cleanroom Index [49] · Version & Status Events [36] · Hygiene Punch List V2 [20])
- `catalog_delta_master_20260805.csv` — 33,483 bytes, sha256 30d47615811a9d62… (machine-readable merge of the New Documents + Cleanroom sheets)

**Please delete the two truncated artifacts this attempt left behind** (the connector cannot delete files): the copies of `TEP_Corpus_Catalog_delta_v1_1_20260805.xlsx` at 14,379 bytes (id 1m11Tcqi3Ohf7p4O_BU9Y8TWDPs9bVeQE) and 28,761 bytes (id 1346VIBWYudn24HPPWT554E_9KVI5mZ4q) — both are unopenable partial zips. The correct file is the 43,144-byte one from the conversation.

Verification after drop-in: file size must read exactly 43,144 bytes (xlsx) and 33,483 bytes (csv).

— Claude, 2026-08-05, per the Repository Arch V2 package.