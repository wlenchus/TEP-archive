# OT1 full-width instrument — session artifacts (2026-07-20 → 07-22)
Companion to "2026-07-22 ot1_delta_EXHIBITION_GRADED_conductor_4000.md". Suggested repo home: 50_code/ot1/full_width_2026-07/.

## Pipeline (run order)
- decoder.py — v1 PRIMITIVES subset (transcribed from Drive 'Untitled document.txt', kron FIXED; Q(sqrt5,i) arithmetic, cycle_type, parity5, E1).
- decoder2.py — v2 membership decoder (de-escaped from repo 50_code copy; unmodified).
- build3.gp / build16000.gp / build4000.gp — PARI host builders (full-Sturm cuspidal S2 export; 16000: 2321×4801; 4000: 561×1201). GP gotcha: single-line for-loops; apply needs x->Str(x) lambda.
- ot1_fast.py — normal-equations projector: M = H H^T mod p, M^-1 checkpointed (H_p1/Minv_p1.npy); full-width bisection control (theta-difference CM × independent E1 → residual 0 = host validated). Float64 BLAS exact below 2^53.
- minv_p2c.py — second-prime factor build, checkpoint/resume pattern (p2_state.npz).
- cm_full2.py — full-width CM decoder control. Recorded: free=0, a2=-1, a5=+1, 314/314 genus. (Width-2701 comparison: free=244 — the SOLVED-NO-GAUGE artifact.)
- sweep_full.py / sweep_p2.py — 8-config icosahedral sweep at p1/p2, rank-preserving ±1 row sketch, per-config JSON checkpoints (sweep_results_full.json, sweep_p2_results.json). Recorded: chi_-8/-40 REJECT; chi_-4/-20 NON-REJECT free=7, identical at both primes.
- gauge_fast.py — sketch solve + EXACT unsketched verification of solution/null space + 2^free gauge search. Recorded: 8 all-±1 multiplicative points (chi_-4 e0).
- cross_check.py — cross-prime pattern comparison (recorded: 8/8 identical). NOTE: its "unanimous interior" print is the session's catalogued false PASS line (E-b); honest unanimity 49/474 = joint quadratic kernel.
- twist_character_match.py — orbit structure: sol_j = sol_0 ⊗ chi_D, all seven D | 40 exact; branches disjoint.
- fe_control.py / fe_grade.py / fe_scan.py — functional-equation grader: validated on CM20 (drift 4e-16 at N=20); decoded series passes at N=4000 (drift 7e-16, |eps|=1); N-scan + a2/a5-mode scan + small-prime negative control.
- autopsy4000.py — N=4000 rerun, fixed vs RECONSTRUCTED 07-04 kron bug (even-exponent skip before p|D check). Recorded: fixed → form family present (free=3, 4 gauge pts); buggy → clean REJECT. False-negative attribution by demonstration.

## Data artifacts included
sweep_results_full.json, sweep_p2_results.json, gauge_solution_*.npy,
2026-07-22_ot1_16000_PREREGISTERED_prediction.json (md5 7fdd69c80d6fa0c35ff45b56d6a2d0e2 — committed before table access).
Hosts and M^-1 factors are NOT included (large); regenerate with the .gp builders (16000: ~10 min; 4000: ~1 min) and ot1_fast.py/minv_p2c.py.
