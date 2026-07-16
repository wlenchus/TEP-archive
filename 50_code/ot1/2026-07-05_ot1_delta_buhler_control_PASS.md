# Session Delta — OT1: icosahedral true-positive control PASS; ladder corrected
**2026-07-05** · tiers: [V]erified · [T]classical · [A]rgued · [C]onjecture · [O]pen

## Headline
The weight-lifting membership decoder, fed only cascade-emission data (cycle types,
5A/5B √disc-orbit parity, golden-trace magnitudes, per-prime sign bits), **decoded the
Buhler icosahedral form** (x⁵+10x³−10x²+35x−18, N=800, nebentypus Conrey 100.91, order 10)
**from pure membership in M₂(Γ₀(800))** — recovering all 35 sign bits (35/35 vs PARI
ground truth), the ramified port a₅ = +ζ₅², the embedding bit, and the correct
nebentypus slot. The A₅-specific components of the instrument (golden magnitudes and
parity separator — the last unvalidated pieces) are now [V] against external ground
truth. The x⁵+20x+16 exclusion ladder is therefore fully load-bearing.

## Specificity record [V]
- (j₅, emb) sweep at the true character: 19/20 slots REJECT; the unique consistent slot
  (j₅=8, emb=0) is exactly where ground truth sits.
- Wrong Galois orbit (Conrey 100.79, dim_new = 0): 20/20 REJECT.
- Complete quadratic grid and quartic ψ-family at 800: REJECT — exactly matching PARI's
  dimension data (only dihedral types 6/8/40 live there). The instrument rejects
  precisely where forms do not exist and passes precisely where they do.
- Gauge structure: free-dim = 1, resolving to exactly TWO all-±1 solutions = the
  Galois-conjugate eigenform pair (dim_new = 2); the two differ exactly on the σ-flip
  set {p : ord_ζ₂₀-exponent of χ(p) ≡ 2 mod 4} under σ: ζ₂₀ ↦ ζ₂₀¹¹ (fixes ζ₁₀, √5).
  Predicted and observed identical. Hecke field ℚ(ζ₂₀) [V: mfparams y²−ζ₁₀ over Φ₁₀].

## Model audit (per-prime, vs numeric mfembed truth) [V]
a_p = s_p·√χ(p)·t_p with t ∈ {±2, 0, ±1, ±φ, ±1/φ} by projective class: every prime
≤ 240 matches (35 sign primes; all class-2 primes give a_p = 0; a₉ = a₃²−χ(3) = 0 and
a₂₇ = −χ(3)a₃ confirm the Euler recursion; a₂ = 0 confirms the supercuspidal rule).

## Diagnosis ledger for the control's earlier failures (all resolved)
1. First rejection wave: **grid miss** — Buhler's nebentypus has an order-5 component of
   conductor 25 (his I₅ = C₅ is abelian, so the local rep at 5 is reducible and
   twist-minimizable to a₅-exponent 2 with a ramified order-10 character). Located via
   the R0-compatible dimension/Galois-type scan: the A₅ slot at 800 is (order 10,
   cond 100), type −60, dim 2.
2. Second wave: **wrong orbit** — two odd order-10 cond-100 orbits exist mod 100
   (Conrey 79 and 91); the first table grab took 79 (the empty slot). Fixed to 91.
3. "Still rejecting" report: **premature poll** (run had only reached j₅=6) + an
   over-strict PASS flag (no gauge resolution at free=1). decoder4 now gauge-resolves.
No assembly bug existed: the truth-signs product reduces to residual 0 in my own stack.

## Structural corollary for x⁵+20x+16 [A/T]
The Buhler comparison sharpens, not weakens, our χ-grid completeness: his order-10
nebentypus is *enabled by* abelian I₅ = C₅; our I₅ = D₅ (nonabelian, forced by the
non-integral C₅ break: 4(u+1) = 6) makes the local rep at 5 irreducible/supercuspidal,
capping the 5-part of det at order ≤ 2 (D₅^ab = C₂) — likewise Q₈^ab (exponent 2) at 2.
So χ ∈ {χ₋₄, χ₋₈, χ₋₂₀, χ₋₄₀} remains COMPLETE for our quintic, with a₂ = a₅ = 0.

## Evenness RETRACTION and corrected ladder [A; falsified by [V] data]
Buhler's quintic has the SAME 2-adic shape as ours ([4,1]+[1,1] ⟹ I₂ = V₄ → Q₈) yet
conductor 2⁵: **a₂ = 5 is odd**, falsifying my a₂ = 2w+2 evenness claim (Hasse–Arf
integrality misapplied to the nonabelian Q₈). Correct bookkeeping: G₀ = G₁ = Q₈,
G₂..G_b = Z (forced: V₄-breaks at 1 pin G_{≥2} ⊆ Z), giving Swan = 2 + (b−1)/2 and
**a₂ = 4 + (b−1)/2 with b odd** (oddness from integrality of the Artin conductor).
Buhler realizes b = 3. Our exclusions (a₂ ∈ {4,5,6}) kill b ∈ {1,3,5}:
**b ≥ 7 ⟹ a₂ ≥ 7 ⟹ next rungs N = 16000 = 2⁷·5³, then 32000 = 2⁸·5³** (16000
REINSTATED — the earlier "skip to 32000" instruction is void).

## Imported-vs-exhibited update [A on the standing [O]]
Two independent advances: (i) the cascade emission + closure has now *decoded a known
icosahedral eigensystem in full* from membership alone — the exhibition mechanism works
at icosahedral complexity, on ground truth; (ii) for our quintic it has *derived* b ≥ 7
— a central-extension ramification datum invisible to the projective field — with no
Khare–Wintenberger input. The success condition stands: a PASS at some rung pins b and
emits the full eigensystem, completing OT1 toward "exhibited."

## Handoff (your machine)
1. Host: `mfinit([16000,2],1)` → mfbasis → mfcoefs to Sturm (mfsturm([16000,2])),
   chunked per ~400 forms exactly as chunk.gp (validated pattern), CSV.
2. Runner: final_run8000.py retargeted (host file, DEPTH ≳ rank + 300; χ ∈ {−4,−8,−20,−40},
   ram={2:None,5:None}, both embeddings); decoder4 not needed for our quintic (quadratic
   χ) but shipped, gauge-patched, for any richer-character contingency.
3. On PASS: commit prediction JSON before grading (LMFDB / mfeigenbasis). On REJECT:
   b ≥ 9, rung 32000; the magnitude-model escape hatch is now CLOSED (validated), so
   rejections bear full weight.

## Shipped
decoder4.py (ℚ(ζ₂₀) branch, gauge-patched), buhler_control2.py, chartable.txt (Conrey
100.91 values), buhler_an.txt (ground-truth coefficients), this record; prior bundle
(hosts, runners, decoder/2/3, controls, chunk.gp) unchanged in outputs.
