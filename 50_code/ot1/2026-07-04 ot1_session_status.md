# OT1 Decoder Session — Status, Exclusion Ledger, Handoff
**2026-07-04 (evening session)** · instrument: weight-lifting membership decoder v2/v3

## Instrument validation [V]
1. **Synthetic ground truth** (planted-form recovery on the uploaded 2000 host): recovered
   all 34 real-locus signs exactly; the 44 "misses" decoded to 0 at precisely the
   {χ(p) = −1} primes with free-dim exactly 1 — the complex-conjugation gauge (f vs f̄),
   as it must be. Assembly + solver validated.
2. **True-positive control** — the CM form of Q(√−5) (S₁(Γ₀(20), χ₋₂₀), living old in the
   uploaded host): **PASS, unique (free = 0)**. Decoded from pure membership:
   a₂ = −1 (nonprincipal ramified class), a₅ = +1 (principal), and the genus character
   across all 52 split primes ≤ 600 — every value matching the independent ideal-count
   construction. The builder (E₁ + Hecke model + host reduction) validated end-to-end.
3. **Bisection method**: independent zero-shared-code construction of the CM product,
   reduced against the host at two primes (residual 0) — isolates host vs builder faults.

## Bug log (caught & fixed)
**Kronecker composite-argument error** in `kron(D, n)`: the even-exponent skip ran
*before* the p | D check, so χ(4), χ(16), χ(25), χ(100)… returned ±1 instead of 0,
corrupting E₁ divisor sums for every even-D character. Level 23 passed because
`kron_m23` checked ramification first. **Third Kronecker-symbol bug in program history**
(contour engine caught two 2-rule errors). Post-fix: kron(−20, ·) matches the truth
table on 1..200; CM control flipped REJECT → PASS. Methodological note for the record:
*synthetic controls share the builder and cannot see builder bugs; only true-positive
controls (external ground truth) validate the builder.* 

## Structural constraint derived [T-derived]
det ρ restricted to inertia factors through I^ab. With I₅ = D₅ (D₅^ab = C₂) and
I₂ = V₄ lifting into Q₈ (Q₈^ab = C₂×C₂, exponent 2): **the nebentypus is quadratic at
both places** ⟹ χ ∈ {χ₋₄, χ₋₈, χ₋₂₀, χ₋₄₀} is the COMPLETE candidate set (odd, cond | 40).
Order-4 branches (ψ-family mod 5, ξ₁₆-family, mod-25 quartics) are excluded a priori.
(The 8 quartic runs were executed anyway: all REJECT — consistent.)

## Exclusion ledger [V, given validated instrument; spot-checked at a 2nd prime]
| host / levels covered | configs | verdict |
|---|---|---|
| M₂(Γ₀(2000)) ⊇ all N | 2000 (incl. 400, 500-old, …) | 4 χ × 2 emb, a₂=a₅=0 | REJECT ×8 |
| same, ramified-PS at 2 (u₂ ∈ {1, i}) — closes v₂-matching divisor levels | ×16 | REJECT |
| a₅ ≠ 0 variants | — | illegal: v₅(cond ρ) ≥ 2 > 1 = v₅(cond χ) |
| M₂(Γ₀(800)), Sturm 240 | ×8 | REJECT |
| M₂(Γ₀(1600)), Sturm 480 | ×8 | REJECT |
| M₂(Γ₀(4000)), Sturm 1200 | ×8 | REJECT |
| quartic χ at 2000 (8-dim algebra) | ×8 | REJECT (forced, see above) |

**Consequence:** conductor is forced to **N = 8000 = 2⁶5³** (or the a₂ = 7 tails
3200 = 2⁷5², 16000 = 2⁷5³). The naive Swan estimate a₂ = 4 is off by ≥ 2: the lift's
central 2-wildness is real and now *quantified* by exclusion. a₅ = 3 stands.

## Remaining runs (your machine — same job as your 2000 host, scaled)
1. Generate the universal host (contains the whole grid as divisors):
   `gp -q -s 2000000000` then
   `mf=mfinit([8000,2],4); B=mfbasis(mf); for(i=1,#B, print(mfcoefs(B[i],2400)))` → CSV
   (strip brackets; 1260 rows × 2401 cols).
2. Run (shipped modules): load host mod p=1000003, `D2.run(host, D2.pdata_quintic(2400),
   chiD, emb, 2400, ram={2:None,5:None}, p)` over chiD ∈ {−4,−8,−20,−40}, emb ∈ {0,1}.
3. **On PASS**: the decoded {a_p : p ≤ 200} is the pre-registered prediction — write it
   to file (commit) BEFORE any grading; then grade via LMFDB or
   `mfeigenbasis(mfinit([8000,1,chi],0))`. Expect free = 1 (conjugation) iff some
   χ(p) = −1 in the sign support; both gauge choices are the conjugate pair.
4. If 8000 rejects: tails 3200/16000; then the audit order is (i) 2-adic lift filtration
   done properly (central C₂ tracked), (ii) dimension-locator (mfdim weight 1 — dims
   only, no coefficients, R0-compatible), (iii) magnitude-model audit (low risk: golden
   traces are [T]-classical and cross-checked in the 06-29 record).

## Files
`decoder.py` (kron FIXED), `decoder2.py` (v2: ram unknowns, gauge, generic depth),
`decoder3.py` (8-dim quartic branch, kept for completeness), `dihedral_membership_certificate.py`,
`cm_control.py` (the true-positive harness — run it first on any new setup).
