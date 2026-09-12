# DATA SUPPLEMENT — deposit_bundle_20260829
2026-08-30. The main bundle's scripts referenced session-local staging paths for the two input
datasets; this supplement makes the pipeline self-contained and portable:
- data/hecke_eigenvalues_doud1951_to1e5.csv, data/hecke_eigenvalues_doud2141_to1e5.csv — the
  certified eigenvalue tables (project copies; canonical originals in the Drive/project archives).
- Portable scripts (identical to the bundle's except the data paths now read data/…): run from
  this directory. Order for full replication: mackey_certificate.py (no data needed);
  coh_pipeline.py (control validation); run_1951.py; verdict_run.py; three_tier.py; twin_2141.py;
  diagonal_probe.py.
- The bundle's original scripts and their hashes remain canonical for provenance; this supplement's
  own hashes are in MANIFEST_SHA256_SUPPLEMENT.txt. sha256(main zip) =
  d0eb71fe0cad8abe88a4c62d5f314624e16656cc87226bc53574c8fed70c0bbc.
