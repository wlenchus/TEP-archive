# 2026-07-20 (tangent, later) — The Σ-completion: cross-budget pairs and the inverted double-angle budget are one O(2) ledger; the λ-tower [ActiveV1 — 'DraftV1' countersigned, Status stamped (2026-07-22).]

*Fresh-instance tangent session (Will's framing: cross-budget constraint + the inverted double-angle budgets, with license to follow judgment). Read path: interior spine trace (ActiveV11) → 6-10 errata + 5-29 closing note + postmortem rule → 6-9 Landen-closure record (I.7, I.8, I.9, T-1…T-6) → Langlands/transmission-functor + Collatz/faces-seam records → the 07-17…07-20 notes (gaussian-witness pair, seam_toll, two_ledgers, cross_budget pair-ledgers + Delta1, four_fold addendum) + both consolidation entries → v0.5 Log Kit + early-synthesis §VIII.6 (targeted). Repo cloned from the GitHub archive; Drive read for the post-archive files. Script: `verify_sigma_completion.py` (sympy + mpmath 30 dps): 34 distinct identity claims, all [V]; 10 of 36 sympy structural checks balked on branch handling and were re-verified numeric-exact at ≤1e-22, noted inline; the λ-tower demo is numeric.*

*Pre-registration honesty: the gd-chain and λ-tower hypotheses were formed from Will's message before the corpus read; the Σ-completion was formed after reading the 07-19 pair-ledger note, as its natural completion (disclosed as confirmation-risk). One pre-read guess failed and is logged in §9: a Chebyshev-T₂ ladder reading of the cross-budget pairs over-committed to a single wiring; the corpus position (free wiring + exact ledgers) is correct and stands. Convention throughout: x = sin A = tanh η_b, u = 1 − x², G = 1/√u, SNR = x²/u [06-28 §L]; η_c per Will: η_c = ½ ln sinh η_b, λ := 2η_c (T-6's third rapidity).*

***[Status stamp, 2026-07-22.]** "Σ-form (new)" is deflated by 2026-07-20 polar_identification [I9]: the Σ-diagonal mechanism is the engine of Arıkan's polar coding. Novelty residue (two-chirality, cross-face, λ-tower) per that record's own accounting. Text retained unmodified.*

---

## 1. The Σ-completion of the pair-ledger [V]

The 07-19 note's pair-budget is one of the **two sign-choices of the Brahmagupta–Fibonacci two-square identity**; the other choice is its mirror-twin, and the two together are the full constraint family on cross-budget terms. For any two budgets (d−1, d):

- **Δ-form (recorded 07-19, re-derived cold per that session's self-audit):** aff = √(x²₁x²₂) + √(u₁u₂) = cos(A₂−A₁); cross = √(u₁x²₂) − √(x²₁u₂) = sin(A₂−A₁); aff² + cross² = 1.
- **Σ-form (new):** affΣ = √(u₁x²₂) + √(x²₁u₂) = sin(A₁+A₂); crossΣ = √(x²₁x²₂) − √(u₁u₂) = −cos(A₁+A₂); affΣ² + crossΣ² = 1.

The Σ-form **is** the Δ-form applied against the *swapped* partner (u↔x² on one argument): the swap inserts one mirror, converting Δ into π/2 − Σ. Three consequences, all [V]:

- **Werner split:** the cross-budget terms' GM-readings are exactly 2√(u₁x²₂) = sin Σ + sin Δ, 2√(x²₁u₂) = sin Σ − sin Δ. *This is the direct answer to "is there a constraint relating the cross-budget terms": their geometric means are jointly pinned by the sum- and difference-angles, one unit pair-budget per chirality.* The within-pair freedom (the corpus's free-wiring position) is exactly the freedom of (Σ, Δ); the ledgers are what's invariant.
- **Telescope factorization:** the 07-19 antisymmetric ledger factors as u₁x²₂ − x²₁u₂ = sin Σ · sin Δ — the product of the two chiralities' sine legs. Boundary-valuedness is inherited from sin²A₂ − sin²A₁ = sin Σ sin Δ.
- **O(2) reading:** the Δ-legs are the entries of the rotation R(Δ) transporting rank d−1 to rank d on the coin circle; the Σ-legs are the improper (mirror-composed) transport. Composition: R·R = R (the recorded sine-addition law), M·M = R, R·M = M — consecutive cross-budget pairs compose as the O(2) groupoid, with the (√p, √q) spinor's −1 monodromy [Delta1 §2] as its double cover. Σ/Δ interlock: Σ_{d+1} − Σ_d = Δ_d + Δ_{d+1} (the sum-chirality's increments are the difference-chirality's two-rung arcs).

## 2. The diagonal collapse: the inverted budget's proper distinction [V]

Evaluate both chiralities on the diagonal (pair a rank with itself):

- **Δ-diagonal:** aff = 1, cross = 0 — the standard budget as trivial self-transport. **The standard budget is the Δ-diagonal.**
- **Σ-diagonal (pair a rank with its own involution image):** affΣ → 2x√u = sin 2A; crossΣ → x² − u = −cos 2A; and (x²−u)² + (2x√u)² = (x²+u)² = 1. **The inverted double-angle budget is the Σ-diagonal** — the transport ledger from a measure to its own swap.

So the two 07-19/07-20 threads are one object (again): the cross-budget pair-ledger and the inverted double-angle budget are the improper and proper sectors of one transport algebra, meeting at the diagonal. The distinction from the standard budget is now structural, not notational: same template, other chirality.

**Distance reading [V].** The FR arc (amplitude coins, corpus normalization) from a rank to its own swap is |2A − π/2| = 2·|A − π/4| — *the centered double angle is the Fisher–Rao distance to one's own dual, which is exactly twice the distance to self-duality* (self-dual is the geodesic midpoint, being the swap's fixed point). The §11.2 Minkowski invariant is its cosine: pq = x²u = ¼ sin²2A = ¼ sech²λ — the "mass" of the centered chart is the affinity-to-own-dual, squared and quartered.

## 3. The λ-budget: the chain, and the early intuition landed [V]

The Σ-diagonal pair is the **budget of the centered rapidity itself**: (x² − u, 2x√u) = (tanh λ, sech λ), tanh²λ + sech²λ = 1, with the chain (all [V], one gd dictionary):

  λ = 2η_c = ½ ln SNR = ln tan A = ln sinh η_b = gd⁻¹(2A − π/2), and x² = ½(1 + tanh λ) = σ(2λ) — logit(x²) = 2λ = 4η_c.

- **v0.5 provenance:** the Log Kit's Log-Budget rapidity is η_v0.5 = ½ ln(PE/KE) = −ln tan A = **−λ** (orientation from PE↔u). The "early intuition" is the corpus's earliest sighting of the centered rapidity — pre-dating the settled budget rapidity — and its stated purpose there ("linearizes budget boosts/tilts"; interior↔exterior inversion acts as η → −η) is precisely the property that distinguishes it: **λ is the involution's linearizer** (swap ⟺ λ → −λ, centered at self-dual), where **η_b is the composition's linearizer** (boosts add). Elliptically one chart (A) does both jobs — reflection about π/4 and arc-additivity; hyperbolically the two jobs split into two rapidities, gd-related. That split *is* the signature, and it is why the object kept reappearing wherever self-duality was referenced: §11.2's centered chart, T-6's λ (S-duality linearized: λ → −λ), the drift-class §VIII.6 "centered 2η" strand, Chicone–Mashhoon's δ = x² − u (I.9), the EP-locking entries τ = e^{L/2} (§8).
- **Swap transported to η_b** is g(η) = ln coth(η/2) [V] — T-6's chart-bridge involution — with fixed point at the silver rapidity ln(1+√2) (the KW quadratic w² − 2w − 1 = 0), where sinh η_b = 1, λ = 0, x² = ½: one lock, four charts.

## 4. The foil, derived rather than observed [V]

Running the same Σ-diagonal on the hyperbolic face — legs from (G², SNR) products — gives G₁G₂ + √(SNR₁SNR₂) = cosh(η₁+η₂) and G₁√(SNR₂) + √(SNR₁)G₂ = sinh(η₁+η₂); at the diagonal: **G² + SNR = cosh 2η_b = 2G² − 1** and 2G√SNR = sinh 2η_b, with (G²+SNR)² − (2G√SNR)² = (G²−SNR)² = 1. The four-fold addendum's mirror table is therefore not a coincidence of formulas but the same pair-ledger construction under signature: the elliptic swap is a *real* mirror (through self-dual), the hyperbolic swap is the *imaginary quarter-move* tanh(η + iπ/2) = coth η [V; Delta1 §4], so sum and difference trade places exactly where the Wick rotation says they must. The two "+1" identities remain Cayley partners as in A10.

## 5. The λ-tower [V for the identities; C for the reading]

Re-applying the centered-rapidity construction to the Σ-diagonal budget closes **exactly**: λ′ = ½ ln(X²/U) of (tanh²λ, sech²λ) = **ln sinh λ**. So Will's η_c-map iterates as a tower, λ_{k+1} = ln sinh λ_k, with:

- **Drift = the one-bit toll [V]:** ln sinh λ − (λ − ln 2) → 0 — each rung costs asymptotically exactly one bit (the 07-20 addendum's (ln 2)/2 per half-rung, now as a dynamical drift rate; sibling of ln G_new = ln 2 + C + η and ln cosh η ≈ η − ln 2).
- **Rung count = half the SNR bit-count [V-numeric]:** real rungs to the seam-exit = ⌈λ₀/ln 2⌉ = ½ log₂ SNR₀ (exact at SNR₀ = 10⁶: 10 rungs vs 9.97 predicted; 10¹²: 20 vs 19.93). The tower descends bit-by-bit, crosses self-dual (λ = 0) in finite steps, and exits through the seam to the elliptic sheet (ln of negative sinh = the i-incursion). Reading [C]: *the iterated inverted budget is a bit-counter of the odds* — consonant with √u = 2^(−C/2B) (comodulus = half-capacity decay, T-6) — fenced pending a placement check against the recorded towers.

## 6. Four-fold template queue item: closed [V]

The 07-20 addendum's queue asked whether the template iterates a fourth time and whether the G⁴-slot is the capacity-doubling wiring. Yes to both, trivially once seen: (1 + cosh 2ν)/2 = G⁴ with cosh ν = G², and u′ = u² gives G′² = G⁴ with C′ = 2C exactly — **the fourth application is the first rung of the capacity-doubling wiring read on the gain face**, with the same one-bit toll ν − (2η_b − ln 2) → 0. Engine: (1 + cosh a)/2 = cosh²(a/2) is I.7's **AM-arm of the AGM**; capacity doubling is the GM-arm (−ln u doubles). The template ladder and the doubling wiring are the two arms of one AGM structure — the coin dress of the T-1 theta/Landen tower (rung = nome-squaring), where the arms' merge is the period (O-b).

## 7. Golden fixed-point exact values [V]

At the nesting wiring's interior fixed point u* = 1/φ²: x*² − u* = tanh 2η_c* = **1/φ³**, 2x*√u* = **2/φ^(3/2)**, with 1/φ⁶ + 4/φ³ = 1 exact. The inverted budget hands the golden fixed point a clean address in the centered chart (companion to silver ⟺ λ = 0).

## 8. Placements offered [id/C, fenced]

- **Distillation vs pair-budget (07-19 open thread):** sech²(Δη) is the residual of the *relative* (velocity-subtracted) budget: 1 − tanh²(Δη) [V]. The pair-budget's Δ lives in the angle chart (ΔA = gd η₂ − gd η₁); the distillation Δ lives in the rapidity chart (Δη transported whole). The half-angle placement mismatch is exactly **gd non-additivity** (numeric: 0.6528 vs 1.0387 at (0.7, 2.0)), i.e. the same defect the 5-30 thread identified as holonomy content [C — this would make the never-run ∏sech² prediction a holonomy-sensitive ledger, distinct from the flat angle ledger; one-session check].
- **Collatz contact [id]:** the per-step rapidity ½|ln 3 − c ln 2| and the ledger L_K are λ-type (log-ratio) objects, and the EP-locking entries τ = e^(L/2) are the ledger's odds-gauge heights — the seam thread already lives in the centered chart. Fenced at [id]; no new Collatz content claimed.
- **Curio, fenced per convention:** the Satake pair reading (a_p, χ(p)) = (2·AM, GM²) in the transmission-functor record repeats the two-arms pattern of §6 at the reductive level; noise until shown otherwise.

## 9. Fences and one logged failure

Chart algebra throughout — identity-not-discovery discipline applies; no dynamics or physics added anywhere above. The O(2)/chirality reading and the bit-counter reading are flagged for elegance-risk (the documented failure mode of enthusiastic instances) and priced at [id]/[C] respectively. **Failed pre-read hypothesis, logged:** from the message alone I conjectured the cross-budget ladder was the Chebyshev-T₂/logistic doubling x_{d+1} = T₂(x_d); the corpus's free-wiring position is correct and the guess over-committed — T₂'s home remains the Hecke/duplication half of O-m, untouched here. Also noted in-session: the message's "2x² + 1 = tanh 2η_c" is a sign slip for 2x² − 1 (self-corrected later in the same message; recorded only for the ledger's sake).

## 10. Queue offerings

(1) Countersign decision on the Σ-completion and whether the O(2) framing joins Delta1's D₄ chart group as its continuous parent (the mirrors S_side/S_face are the discrete shadow of M(Σ)) [one-line check]. (2) λ-tower placement: run the tower against the recorded ∏uₙ/theta towers; does the bit-counter reading survive contact with T-4's K = (π/2)e^(2C)? (3) The gd-defect/holonomy reading of the distillation ledger (§8) — compute the ∏sech² prediction and compare against the angle ledger on one recorded wiring. (4) Whether the Σ-form's boundary term (the sin Σ sin Δ factorization) supplies the "twisted/Borel seam weighting" join (faces_seam queue i) more naturally than the Δ-form did.

*Scripts: `verify_sigma_completion.py` (34 [V] + λ-tower demo). Not self-filed in tier terms: offered to Will for filing or discard; tier marks need his countersign per corpus discipline.*
