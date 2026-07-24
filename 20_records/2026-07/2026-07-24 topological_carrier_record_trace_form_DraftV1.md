# Session Record — the topological carrier test: the class-half of the lift datum is trace-form-readable; the two quintics' trace forms are isometric; the i is the splitting field of the obstruction
**2026-07-24** · Claude (Fable 5), Cowork session; computed inline (PARI 2.15.4), two minutes · tiers: [V]erified · [T]classical · [A]rgued · [id] · pre-registered split conjecture fixed before execution (form carries extension-class/signs; not depth)

## The data [V]
Trace forms q_E(x) = Tr_{E/ℚ}(x²) on integral bases, diagonalized over ℚ:
- **E₁ = x⁵+20x+16:** ⟨5, 15, −5, −15, 1⟩ · signature (3,2) · disc class **1** · Hasse ε₂ = **−1**, ε₃ = +1, ε₅ = **+1**, ε_∞ = **−1**, all other places trivial · product formula +1 ✓.
- **E₂ = Buhler, x⁵+10x³−10x²+35x−18:** ⟨5, −5, 1, 2, −2⟩ · signature (3,2) · disc class **1** · ε₂ = **−1**, ε₅ = **+1**, ε_∞ = **−1** · product +1 ✓.
- Reference class **(−1,−1)** (Hamilton quaternions): ε₂ = −1, ε₅ = +1, ε_∞ = −1.

Since rank, disc, signature, and all Hasse invariants agree, **q_{E₁} ≅ q_{E₂} as rational quadratic forms**, and their common anisotropic content is the Hamilton quaternion class — **ramified at exactly {2, ∞}, trivial at 5 and everywhere else.**

## What this establishes
1. **The class-half of the lift datum is topological and cheap.** One 5×5 rational symmetric matrix, computed from the quintic with no lifts, no local fields, no forms, already carries: the obstruction-class profile, its exact ramification set {2, ∞}, and — via the product formula — the **forced-sign reciprocity statement made concrete: ε₂ is determined by ε_∞** (all other places trivial; both quintics realize it). The 07-23 local finding (no SL(2,3) octic over ℚ₂ — spin lift locally obstructed at 2) and the classical archimedean fact (involutions lift to order 4 in 2.A₅ — the odd place obstructs) are the two local faces of this one global class; three independent computations (local census, archimedean lifting, trace form) agree on {2, ∞}.
2. **[id, one normalization pin pending] Why the i:** ℚ(i) is precisely a splitting field of (−1,−1). Under Serre's trace-form theorem (the exact w₂-vs-Hasse normalization was not pinned from the literature in-session — flagged for countersign; the interpretation is corroborated by both independent local computations), the spin (det-1) embedding is obstructed by exactly this class, and adjoining i — the C₄∘ thickening Result 1 found locally, the entry port [id-2] located in the tower — is its resolution. **The tower said where the i enters; the trace form says why: it splits the quaternionic obstruction.** χ₋₄ ↔ ℚ(i) ↔ the place-pair {2,∞} ↔ oddness-plus-2-wildness, one object in four registers.
3. **The split conjecture confirms, in a sharpened form.** The form sees the class and nothing finer: it is *isometric* for E₁ and E₂ despite their genuinely different determinant structures (χ₋₄-quadratic family vs order-10 nebentypus) and different 5-adic shapes (I₅ = D₅ nonabelian vs C₅ abelian — invisible: ε₅ = +1 for both). Depth b is invisible a fortiori (a finite Witt invariant cannot grade an unbounded break). **The lift datum is now itemized in three layers with three instruments: topological class (trace form — one matrix), local class-field structure (the 16T60 census — Result 1), wild depth (slopes — ramification filtrations).** Only the first layer was ever "shape-data being asked for in arithmetic form"; the deeper two are genuinely residual arithmetic.

## Consequence for L4 and the ledger
The carrier rule's cargo is fully itemized: class (trace-form-readable, global, topological), determinant refinement at 5 (local CFT, not form-readable), depth b (local CFT, wild). Outcome vs pre-registration: **(i) confirmed, sharpened** — with the bonus isometry q_{E₁} ≅ q_{E₂} making the "2-adic siblings" of 07-22/07-23 a three-way identity (same local quartic field, same trace-form class, same a₂). The reciprocity ledger over places — the corpus's capacity-additivity instinct — has a rigorous cousin demonstrated on live data: the archimedean place buys the 2-adic sign.

## Files
50_code/ot1/trace_form/tf.gp (+ output log). Runtime ~2 min; every number reproduces from the script.

*Offered, not self-filed; countersign gates tiers — including the one flagged normalization pin (Serre 1984, exact w₂ convention), which is the single outstanding check on §2's interpretive sentence. The invariant tables, the isometry, and the reciprocity forcing are convention-free.*
