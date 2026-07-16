# Session Delta — OT1 decider: N=8000 excluded; conductor ladder advanced
**2026-07-04 (evening)** · tiers: [V]erified · [T]classical · [A]rgued · [C]onjecture · [O]pen · [id]entification

## One-line result
The cascade-emitted icosahedral eigensystem for x⁵+20x+16 does **not** close into
S₂(Γ₀(8000)) for **any** admissible nebentypus (all four odd quadratic χ | 40, and the
order-4 ψ-family, both √5-embeddings) — a complete, instrument-validated exclusion of
N = 8000. Combined with the prior 2000/4000 exclusions this forces the 2-adic conductor
exponent **a₂ ≥ 7**, i.e. **a₂ ≥ 8** under the evenness argument below.

## What was built and validated this session [V]
- **8000 weight-2 host generated here**: S₂(Γ₀(8000)), 1141 forms × 2401 coefficients
  (full Sturm), exact integer q-expansions. Built in memory-bounded chunks (fresh process
  per 400 forms) after the monolithic build OOM'd the ~3 GB container. Saved:
  `host8000.csv`, `host8000.npy`.
- **Independent CM control on host8000**: the weight-1 CM form of Q(√−5) (level 20 | 8000)
  built from binary-quadratic-form representation numbers with an independently coded
  E₁(χ₋₂₀), reduced against host8000 at two primes (1000003, 999983) → residual 0 both.
  Confirms the host contains the level-20 oldforms, the rref is sound, and the membership
  reduction is correct at depth 1600. The instrument works on *this* host.
- **Decoder run** (validated `decoder2.run`, reducer computed once, float-exact mod-p
  reduction): 8 quadratic candidates → REJECT (3 s each); 8 quartic candidates via the
  8-dim ℚ(ζ₈,√5) branch (`decoder3.run8`) → REJECT (18 s each).

## Why the rejection is rigorous [A]
A REJECT is an *inconsistency* of the sign-monomial linear system over the reduced host
rows: no sign/embedding assignment places f_emit·E₁(χ) in the span. Adding coefficients
(higher depth) adds constraints and cannot cure an inconsistency, so REJECT at depth 1600
⟹ REJECT at the full Sturm bound 2400. The emitted **magnitudes** (2, 0, 1, φ or 1/φ by
projective order) are forced by the trace of an order-k element in the 2-dim rep of
2.A₅ — classical [T]; the decoder exhausts the only genuine freedom (per-prime signs +
one global embedding bit). Hence: if an A₅ newform existed at N=8000 with one of these
nebentypi, the product would lie in S₂(Γ₀(8000)) [weight-lifting: S₁·M₁ ⊆ S₂, level lcm
= N] and the decoder would find it. It does not.

## Conductor ledger [A/T]
- Projective (V₄) ramification is FORCED by the quintic: v₂(disc)=6 = a₂(ρ₄), giving the
  three V₄ quadratic characters each break 1 (Swan(ρ₄)=3, cross-checked via Sym²ρ₂). [V]
- Lift to ρ₂ (inertia → Q₈, Sylow-2 of SL(2,5) is quaternion): every nontrivial subgroup
  of Q₈ contains the center, so **a₂ = 2w + 2** with w the central ramification break, and
  **a₂ is even** (the center contributes in [Q₈:Z]·dim increments; Sym²ρ₂ = the three V₄
  chars carries Swan 3 independent of w — the consistency check). [A]
- Exclusion ladder: a₂=4 (N=2000) ✗, a₂=5 (N=4000) ✗ [prior], **a₂=6 (N=8000) ✗ [this
  session]**. Evenness ⇒ a₂ ∉ {5,7}, so the next rung is **a₂=8, N=32000 = 2⁸·5³ (w=3)**;
  if one distrusts evenness, test a₂=7, N=16000 first.
- All lift ambiguity is at p=2: the Schur multiplier of A₅ is ℤ/2, so the double cover
  splits over the odd part — a₅ (conductor exponent) = 3 is fully determined, and a₅, a₂
  as Fourier coefficients are both 0 (Atkin–Lehner, since 2²|N and 5²|N: local reps
  supercuspidal). [A/T]

## Bearing on imported-vs-exhibited [A, updates the [O] disagreement]
The central break w is exactly the datum the projective quintic underdetermines. Each
exclusion is the cascade determining w by pure closure — no Khare–Wintenberger input. The
program has now *derived*, from membership alone, that w ≥ 3 (a₂ ≥ 8): the central
extension is more deeply 2-ramified than even the deepened w=2 guess. This is the cascade
doing the work K-W would otherwise supply. The exhibition has not yet landed a PASS; the
success condition is unchanged and concrete: a PASS at some rung N=2^{2w+2}·5³ pins w and
emits the full a_p, exhibiting a lift datum provably not fixed by the projective field.

## Honest caveat
Validated: the closure/membership pipeline (CM control), the emission→closure for a real
case (dihedral certificate, level 23, PASS), the E₁/Kronecker/reduction stack. NOT
independently validated at the icosahedral scale: the A₅-specific **magnitude model**
(golden-ratio traces) and the 5A/5B parity. These are [T]-classical and were cross-checked
in the 06-29 record, so the residual risk is low — but a persistent ladder of REJECTs
would eventually warrant a direct magnitude/parity audit against a known A₅ form (e.g. the
conductor-800 or -1600 icosahedral forms in the literature) before trusting "w ≥ k" for
large k.

## Handoff — next rung (your machine)
1. Generate host: `gp -q`, `default(parisizemax, <~0.75·RAM>)`, then
   `mf=mfinit([32000,2],1); B=mfbasis(mf); for(i=1,#B, print(mfcoefs(B[i], <Sturm>)))`
   → CSV. (dim S₂(Γ₀(32000)) and Sturm via `mfdim([32000,2],1)`, `mfsturm([32000,2])`;
   expect ~4600 forms, Sturm ~9600. If it OOMs, chunk with fresh processes per ~400 forms
   exactly as `chunk.gp` did for 8000 — that pattern is validated.)
2. Run `final_run8000.py` retargeted: point it at the 32000 CSV, set DEPTH to just above
   the new rank (rank + a few hundred surplus is plenty for PASS/REJECT), keep
   ram={2:None,5:None}, χ ∈ {−4,−8,−20,−40}. Add the quartic branch (`decoder3.run8`) to
   fully close the level.
3. On any PASS: the decoded {a_p} committed to `prediction_*.json` BEFORE grading; then
   grade via LMFDB or `mfeigenbasis(mfinit([32000,1,χ],0))`. On REJECT everywhere: a₂ ≥ 10
   (w ≥ 4) or the magnitude audit above.

## Files (this session)
`host8000.csv`, `host8000.npy` (validated 8000 host); `final_run8000.py` (validated runner,
reducer-cached, quadratic grid); `decoder.py`/`decoder2.py`/`decoder3.py` (kron FIXED,
gauge, quartic branch); `cm_control_8000.py` (independent host validator);
`dihedral_membership_certificate.py` (positive control); `chunk.gp` (memory-bounded host
generator pattern).
