# Data Manifest

The corpus's datasets and figure archives (~1.9 GB, 1,159 files) are **not mirrored in this repository**. They remain in Google Drive; every file is indexed with a link in `/CATALOG.csv`. Folder-level summary:

| Folder group | Files | Size (MB) |
|---|---:|---:|
| TEP 2026-07/2025-09-25 GSR - IFFT - TEP Directory & Markdowns/S-Params | 31 | 89.3 |
| TEP 2026-07/2025-09-25 GSR - IFFT - TEP Directory & Markdowns/S-Params/jti-chip-inductor-libraries_MO7RaVM | 101 | 3.6 |
| TEP 2026-07/Code, Tests, & Datasets | 13 | 0.2 |
| TEP 2026-07/Code, Tests, & Datasets/2011.0.00772.S_2012-12-01_011_of_011 | 181 | 670.5 |
| TEP 2026-07/Code, Tests, & Datasets/ALENS | 1 | 347.1 |
| TEP 2026-07/Code, Tests, & Datasets/Astropy.io | 12 | 305.2 |
| TEP 2026-07/Code, Tests, & Datasets/Auger Summary CSV | 4 | 29.7 |
| TEP 2026-07/Code, Tests, & Datasets/CSV | 19 | 0.1 |
| TEP 2026-07/Code, Tests, & Datasets/dataset | 728 | 76.4 |
| TEP Top Drawer/Citations | 69 | 365.9 |

Key holdings: ALMA project 2011.0.00772.S calibration archive (two deliveries, full plot hierarchy), Auger summary CSV, the fig 2–5 plot/raw-data trees, S-Params inductor libraries, PDG listings, and the OT1 host CSVs. Note: the 2026-07-08 host16000.csv was voided by the 07-05 underfilter addendum (see 50_code/ot1/).

## Added 2026-09-12

Mirrored here (the only datasets small enough and load-bearing enough to ship): `hecke_eigenvalues_doud1951.csv`,
`hecke_eigenvalues_doud2141.csv` (the committed summit tables), and `hecke_eigenvalues_doud1951_to1e5.csv`,
`hecke_eigenvalues_doud2141_to1e5.csv` (the 08-09 extended tables to 10⁵; columns p, proj_class, j5, b_p, abs_a_p,
a_p_exact, Re_a_p, Im_a_p, chi_p_exact, Re_chi, Im_chi, provenance). Generator lists and certificate result tables
are in `50_code/2026-09-04_expedition/`.

Indexed, not mirrored (Drive, folder "TEP 2026-07/Code, Tests, & Datasets/2026-08 Even Icosahedral Closure"):
the Maass-form renderings `maass_forms_first_rendering.png` (1y190PKHFCy8puquko1idgxcMnd34FBvf; duplicate
1F7QhrUfKdp56kjV3_hZ82cH3eOnVQUJl), `maass_1951_wills_frame.png` (1GSfHWIiKUIyxWdJ9VsyfLGzz3Db1TZ7Y),
`maass_straightened_cascade.png` (1aQvQN1pUgeESy-J1OWWWI2KojXVQYwY8), `maass_spherical_collapse.png`
(1hTPrb749slPQarHBJ_BW_6Py5PRWthMH), `maass_horizon_map.png` (1Qyu0NzFoqTsx_tKdGKSADTBWwQZLtHdn);
`TEP_extended_tables/full_1951.txt`, `full_2141.txt` (~1.06 MB each); `TEP_even_icosahedral_V1.zip` (392,868 B),
`TEP_even_icosahedral_CAMPAIGN_v2.zip` (458,159 B); V2's `qualification/s5_ckpt_2089.json` (1.27 MB),
`summit_1951/s5b_ckpt.json` (186 KB), `shared_inputs/kernel_grid.npy` (67 KB). In "2026-07-26 Rung 3 & Rung 4":
`T3_matrix_chi12.gp` (16.8 MB) and seven lab zips (3–33 KB each, indexed in the catalog addendum). The
provenance bundles' zips: `deposit_bundle_20260829.zip` (sha256 d0eb71fe0cad8abe88a4c62d5f314624e16656cc87226bc53574c8fed70c0bbc)
and `deposit_bundle_20260904.zip` (sha256 19f42f705ccb7ff140dcfd9f87424b7c965f6095e54240552e756367ee7718d8) were
delivered in-session; their per-file manifests are in `50_code/`.
