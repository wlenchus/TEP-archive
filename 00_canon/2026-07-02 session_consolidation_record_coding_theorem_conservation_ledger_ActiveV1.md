# Session Consolidation Record — Coding Theorem, Conservation Ledger, Portless Sector
**Date:** 2026-07-02 · **Status:** ActiveV1 · **Thread:** TEP–Langlands, information-theoretic layer
**Companions:** 2026-06-28 consolidation record · 2026-06-29 Langlands-functor record (ActiveV2) · 2026-07-01 session delta record (ActiveV2) · 2026-07-01 transmission functor definitional record · uploaded transcript 2026-07-01 "Fable 5 Langlands Extension"
**Environment:** all [V] items verified this session in /home/claude/coding_thm/ (sympy/numpy; scripts: battery.py, frobenius_demo.py, weld_demo.py, nyquist_half.py, infres.py, portless.py). Parallel-thread transcripts were NOT mounted this session; items sourced from memory of parallel threads are tagged [M] and require diff on next contact with those transcripts.

## 0. Epistemic key
[V] verified this session (code, zero-exception unless noted) · [T] classical theorem, cited · [id] identification: classical mathematics, transmission reading ours · [A] argued, not proved · [C] conjecture · [O] open · [M] memory-strength from parallel threads, unverified here.

## 1. Session spine (narrative)
Full staged corpus read (spine trace, central reference, early synthesis, v0.5 principles, investigation-record structure, June layer, four Langlands records). Assessment of the uploaded parallel transcript's message-transmission formulation. Will's steer: the LTV/variance point ("the cascade reaches upward to the budget"). Then, in order: the coding theorem built on the enrichment spine; brief literature gut check; Will's N-observation resolved to an exact identity; the tetrahedral rung-capacity weld; the Nyquist half (conservation + sampling) stamped; the inflation–restriction weld with the transgression's minimal firing; the portless-sector defect theory exhibited on Q(√−23); Will's three-part pushback and the resulting corrections (Thread I), which are part of the record's content, not an appendix.

## 2. Thread A — The coding theorem (the Shannon half)
**Derivation spine [A/id, foundations-anchored].** The axiom's e-flat face is the chain rule H(total) = H(read) + H(residual|read) per conditioning — every hom carries a budget *by the axiom* (the enrichment is the axiom restated, per Will's "reaches upward"). A group quotient G→Q is a conditioning of Haar onto the coset σ-algebra: per-rung u = 1/|Q|, capacity −ln u = ln|Q|, series = telescoped chain rule, parallel = joint/subdirect reads, post-processing = quotients.

**Dictionary [id, with classical anchor].** The three protocol-closure operations are Gaschütz's formation-closure axioms: post-processing = Q-closure; series = extension-closure — and the Gaschütz product 𝔉∘𝔥 of formations *is* the extension class (Ballester-Bolinches et al., arXiv:1103.6259): series composition of channel classes is a named classical operation, never before read informationally; parallel = R₀/subdirect closure.

**Closure theorem [T].** The closure of {abelian} under exactly these three operations is the solvable formation (induction on derived length, both directions; Doerk–Hawkes is the classical home). Consequence: **the from-below cone terminates at solvable by protocol-closure necessity** — no from-below extension exists without a new channel primitive.

**Coding theorem.** C_from-below(G) = ln|G/Gˢ| (Gˢ = solvable residual = perfect core).
- Achievability [V]: refined derived tower attains Σln|Qₖ|. S₄: ln2+ln3+ln2+ln2 = ln24 exactly; ∏u = 1/24 = |core|/|G|. S₅: C_comm = ln2; ∏u = 1/2 = |A₅|/|S₅|. Tower identity ln|G| = C_comm + C_res exact (residual ≤ 2.3e-16).
- Converse [T + monotonicity]: any protocol composed under the three operations factors through the maximal solvable quotient (closure theorem); monotonicity forbids post-processing exceeding it.
- Residual product [V]: **∏uₙ = |Gˢ|/|G|** along any maximal from-below tower — the group-side echo of ∏uₙ = 1/θ₃.
- Corollaries [id]: Abel–Ruffini exhibited as the converse half at x² < 1 (classical proof revealed as channel-coding converse; protocol class and measure framework-derived — NOT a new proof). Langlands–Tunnell sits at the Gaschütz closure boundary: its position is channel-theoretic necessity, not proof-technology accident. Doubly-shadowed corner priced: x²_solv(2.A₅) = 0 ∧ archimedean port parabolic.

## 3. Thread B — Formation-lattice extension
Per-formation budgets x²_𝔉(G) = ln|G/G^𝔉|/ln|G| over 𝔉 ∈ {abelian(G′), nilpotent(γ∞), solvable(perfect core)}.
- **Battery [V], 12 groups** (C₆, S₃, D₄, Q₈, A₄, S₄, F₂₀, A₅, S₅, PSL(2,7), A₆, S₆; SL(2,5) analytic: perfect ⇒ all budgets 0): lattice monotonicity x²_ab ≤ x²_nilp ≤ x²_solv holds at every group (class-level data processing: larger channel class reads more).
- Values (selected): S₃ (0.387, 0.387, 1); D₄ = Q₈ (2/3, 1, 1); A₄ (0.442, 0.442, 1); S₄ (0.218, 0.218, 1); F₂₀ (0.463, 0.463, 1); S₅ (0.1448 ×3); S₆ (0.1053 ×3); A₅/A₆/PSL(2,7) (0 ×3).
- **D₄/Q₈ budget identity [V]:** capacity is FS-blind — reality/quaternionic data is phase, not rate; coheres unforced with C1′'s port-exclusivity of the four-cycle [M for C1′].
- **Lattice collapse above the perfect core [V]:** S₅'s three budgets coincide — once the residual is perfect, no intermediate formation buys anything ("the anholonomy is the whole rank," graded form).
- **S-involution [id]:** (x², u) pole swap = solvable-quotient ↔ perfect-core read = from-below ↔ from-above cone exchange; A₅-type at the pure-u pole, solvable at pure-x². Consistent with direction-reversal = modular S [M].

## 4. Thread C — Arithmetic instantiation of both halves [V]
- **Solvable (achievability in particular):** x⁵−2, G = F₂₀, 300 primes. The pair of abelian symbols (ordₚ mod 5; quintic residue character of 2 — a literal two-rung series read) determines the full Frobenius class deterministically: (1,χ triv)→(1⁵); (1,χ nontriv)→(5); (ord 2)→(1,2,2); (ord 4)→(1,4). Zero exceptions.
- **Unsolvable (converse biting maximally):** x⁵+20x+16, G = A₅, disc = 32000² (square). Only abelian symbol (Δ/p) ≡ +1, 0 violations over 300 primes, while the class varies with Chebotarev A₅ (obs 0.010/0.330/0.250/0.410 vs 1/60, 20/60, 15/60, 24/60). Zero from-below bits: x² = 0 in action.
- **Generic (one bit exactly):** x⁵−x−1, G = S₅, disc 2869 = 19·151. Cycle-type parity ≡ (2869/p) at 425/425 primes: readable content = ln2 of ln120, and it IS the discriminant symbol (the trace-level a_p = 0 result is the same bit's other face).

## 5. Thread D — The N-identity (Will's observation, resolved exactly) [V]
Explicit forms of the residual: (i) **N = u·|G|** (tower/noise form; |N| = |G|·∏uₙ); (ii) **u = |N|/|G| = density of primes splitting completely in the maximal solvable subextension** (operational/Chebotarev form; S₅ → 1/2 = the (Δ/p)=+1 density); (iii) intersection/derived-series form (classical).
Will's expression ln|G/N| = −ln(√u·N): **exact at every case (diffs 0.00e+00)** once the two u-charts are distinguished — it implicitly reads |G| on the amplitude chart (|G| = G-factor = u_amp^{−1/2}), and then √u_amp·N = N/|G| = u_intensity identically. The speculative u^{3/2}·f(Noise) tail dissolves: the 3/2 was amplitude/intensity chart-mixing — the factor-of-2 family the 06-09 Landen rung-index prescription polices. Verdict: instinct right (C_comm is a pure noise logarithm, Shannon–Hartley form); speculation retired as chart artifact.

## 6. Thread E — Rung-capacity weld (tetrahedral tower) [V]
Object: x⁴+8x+12, G = A₄, disc = 576² (square), resolvent cubic z³−48z−64 with roots proven symbolically to be sᵢ² (squares of partial root-sums). 548 primes, zero exceptions throughout:
- **Rung 1:** conductor **discovered from data** as m = 9 — resolvent splits ⟺ p ≡ ±1 (mod 9); the cubic character; capacity ln3. The rung-1 field is Q(ζ₉)⁺.
- **Rung 2:** quadratic symbols of rung 1's own outputs: 3 QRs among {sᵢ²} ⟺ Frobenius trivial; 1 QR ⟺ involution class; product constraint χ(z₁)χ(z₂)χ(z₃) = +1 at every prime ⇒ exactly two free bits — **the symbol algebra realizes ln|V₄|**. Cross-rung consistency: resolvent inert ⟺ quartic type (1,3), exact.
- **Pricing = proof history [id]:** ln3 rung = Langlands' cyclic cubic base change; ln2 rungs = Hecke dihedral over the cubic field (literal Landen rungs, T-5's "ln2 = one self-dual rung"); Tunnell's octahedral = one more ln2. Degree-ℓ cyclic rung capacity = lnℓ = −ln u, u = 1/ℓ. **Flag [M]:** matches the minted "inert base change as Landen rung" iff that definition prices degree-ℓ at lnℓ — diff pending.
- **Face-sign migration [V+id]:** A₄'s face-pair 3A/3B (the Q(√−3) bit) is *boundary-readable* — it is the value of the mod-9 character (inert primes split across χ-cosets {2,7}: 184 vs {4,5}: 182). A₅'s 5A/5B is bulk anholonomy. **The face-sign channel submerges from boundary observable to bulk anholonomy exactly at the solvability wall** — the converse localized onto the face-sign channel.

## 7. Thread F — The Nyquist half (conservation + sampling)
**Connecting-map statement [T+id].** U = base ∖ ports: 0 → H¹(base) → H¹(U) → ⊕ₛH⁰(portₛ) →^δ H²(base) → 0. Terminal base P¹: **H¹(U) = ker(sum: ⊕ℤ→ℤ)** — r ports, r−1 free splits: Will's "five sum-constrained parameters, four splits" is the connecting homomorphism's kernel; the residue theorem is exactness at δ; conductor–discriminant capacity-additivity lives on this face. Non-abelian face: π₁(U) = ⟨γₛ | ∏γₛ = 1⟩; Riemann existence; **conservation = generation** ⟨port monodromies⟩ = G for connected covers; at the arithmetic terminal this is **Minkowski's theorem read as a transmission law** (fixed field of all inertia = Q).
**Stamps [V]:**
- Icosahedral (2,3,5) dessin: a = (0 2)(1 3), b = (2 3 4), c = (ab)⁻¹, abc = e; local reads C₂, C₃, C₅ (ln2+ln3+ln5 = ln30); ⟨a,b⟩ = A₅ (ln60); **the missing ln2 lives in the relation abc = 1** — one bit carried by the composite and by no element; each port winding has zero abelian shadow (A₅ perfect): the Shannon converse per-element, the Nyquist conservation from the relation.
- SL₂(F₅): parabolic winding T alone = C₅ (ln5) vs conserved ln120; ⟨S,T⟩ closure = 120; commutator closure = 120 (perfect).
- Residue reconstruction: η(τ)η(23τ) coefficients (integer product, cross-certified against the Galois rule at all primes < 200); contour pairing at M = 512 recovers a₁..a₂₄ to 3.1e-14; **undersampling at M = 32 fails by the exact geometric law** contour = Σₖ a₍ₙ₊₃₂ₖ₎r³²ᵏ (matched to 3.7e-13; legible instance n = 7: true a₇ = 0, contour = 0.0007916539 = a₃₉·r³² to 2.4e-16). A certificate with a failure branch, the failure obeying the predicted law.
- Sturm as capacity [T+id]: B = kμ/12 ≡ k·Area/4π — the bandlimit is the enclosed-state count; level-23 weight-1: B = 2.
**Consequence [id]:** the emission experiment is a pure Nyquist-side instrument (boundary spectral sampling at the pinned seam) aimed at an object with zero Shannon-side capacity — from-neither-cone was the only populated side of the decomposition.

## 8. Thread G — Inflation–restriction weld (the algebraic connecting map)
**Home:** Hochschild–Serre for 1 → N → G → G/N → 1. **Degree-0 row = the Shannon partition** (chain rule / tower identity): the budget is the E₂ bottom row — Will's "reaches upward" completed; higher differentials = anholonomy obstructions [id; all-orders statement O, not claimed].
**Derivation [V+T]:** exactness of 0 → H¹(G/N, Aᴺ) → H¹(G,A) → H¹(N,A)^{G/N} →^tg H²(G/N, Aᴺ) forces bulk-visible classes to be G/N-invariant: **D↑'s "constraints constitute group-defining invariants" clause is derived, not posited** (upgrade to definitional record I.4).
**Minimal firing [V]:** C₄ over central C₂ (A = F₂): restriction ≡ 0 over all cocycles ⇒ transgression is an isomorphism ⇒ **T² = −1 is a nonzero transgression** — the four-cycle's central bit is connecting-map content, degree one. Control: V₄ has surjective restriction, tg = 0. The nonsplit/split (quaternionic/real) dichotomy is transgression content; coheres with C1′'s port-frame exclusivity [M] — one object, two addresses (fundamental-rep ℤ₄; extension class in H²), both invisible to adjoint/inner data.
**Hecke–Maass existence as exactness [V+id]:** H¹(S₃, F₃(sign)) = 3 with restriction surjective onto Hom(C₃,F₃) — the class characters lift to the terminal boundary **only through the sign-twisted module**: the cohomological face of dihedral induction; why dihedral forms exist, stated as one restriction map's surjectivity.

## 9. Thread H — Conservation defect: the portless sector
**Theorem-shape [T+id].** Over base K: I = ⟨all inertia⟩ ⊴ G; G/I = Gal(maximal everywhere-unramified subextension); abelianized defect a quotient of Cl(K) (Artin); terminal base ⇒ defect = 0 (Minkowski). The defect is content carried by the base's own arithmetic topology (π₁ᵉᵗ(Spec O_K)) — **finite-portless**.
**Exhibit on the program's field [V].** K = Q(√−23), Cl = C₃; Hilbert class field = splitting field of x³−x−1 (the level-23 calibration object). Unramified via conductor–discriminant (disc L = 1·23·23² = 23³ = disc(K)³; relative norm 1). Class bit = form dictionary, **0/211**: x²+xy+6y² ⟺ 3 roots (principal); 2x²+xy+3y² ⟺ 0 roots. **Congruence-invisible: 0 surviving moduli ≤ 4000 over split primes < 20000**, with the [T] reason (a congruence rule would abelianize S₃). Genus contrast: Q(√−5), Cl = genus group, mod-20 dictionary **0/1124** — genus part terminal-readable.
**Stratification [id, derived]:** genus (norm-lifted, from-below) = terminal-readable = Eisenstein-only fuel; non-genus = terminal-invisible = first cuspidal fuel — the seam engine's empirical lesson, now theorem-shaped.
**Identification [id — Hecke 1926 classical; reading ours]:** η(τ)η(23τ) is the automorphic shadow of the portless sector of Q(√−23): over Q the content is port-carried at 23 (inertia conjugates regenerate S₃, Minkowski face) but anholonomic (nonabelian, congruence-invisible); over K it is portless and only the global Artin map / the form's coefficients read it. See Thread I for the evidence-status of this identification.

## 10. Thread I — Corrections & epistemic clarifications (from Will's pushback; content, not appendix)
**I.1 Portless ≠ seam [correction, V-backed].** Prior phrasing ("the base's topology… lands suspiciously close to the seam lesson") risked conflation. Precise statement: portless = *finite*-portless; the archimedean place is never integrated away and still **types** the content. The seam is the ∞-port's parabolic condition. Which face portless content surfaces on is decided by the base's archimedean type: imaginary quadratic → holomorphic weight 1 (elliptic at ∞; our −23 case — NOT at the seam); real quadratic → Maass at λ = ¼ (the seam; Maass 1949). The cusp integrated around belongs to the automorphic domain, not Spec O_K. True core of the instinct: **portless content is unreadable in situ; reading it requires re-hosting on a ported domain — that is what the automorphic shadow is.**
**I.2 The deficit/excess proposal [adjudicated: half-right, corrected].** Right: the two-faces structure and vanishing-at-agreement clause. Corrected assignment: the portless sector is a deficit of **ports**, not of content, and it equals **the anholonomy sector one base down** — the same C₃ is portless at K and port-scrambled (congruence-invisible) at Q; one content, base-indexed; each description vanishing at its agreement point (Minkowski at terminal; trivially at the splitting field). Will's underpopulation/D↑ reading is exactly right for the **genus stratum** (terminal content lifted into K's class structure, D↑-invariant, Eisenstein-only) — not for the non-genus stratum, which is K-native.
**I.3 Evidence-status separation [meta-epistemic anchor].** The Hecke association was always citable; this session established no new arithmetic there. Session contributions are **derivational evidence** (ontology load-bearing: D↑ clause derived; genus/non-genus stratification derived; four-cycle's cohomological address; the priced proof-architecture) — evidence that TEP is a coherent host whose vocabulary carves at joints. **Generative evidence** (TEP hosts and *generates* the data) lives in the blind emission chain — cascade-emitted eigensystems, 113/113, 17/17 [M] — and is untouched in either direction by this session; its next increments are the even-icosahedral emission and OT1. Phrasing that risked blurring the ledgers ("delivers the identification") is owned and corrected here. The imported-vs-exhibited disagreement remains live and remains decided by x⁵→Z→AGM→τ→form.
**I.4 Standing flags.** k-bonacci x-vs-x² convention: unresolved, likely context artifact, prerequisite to the address-ladder hostages (disc −44 → level 11; −563) [carried from transcript assessment]. Absence-claim discipline: all "unoccupied field" claims this session carry the lit-check basis (Thread J) and the parallel-thread diff hedge.

## 11. Thread J — Literature gut check (brief, as commissioned)
No capacity/rate layer over solvability or formations found. Nearest neighbors: Chan–Yeung group-characterizable entropy functions (subgroup log-indices as entropy vectors; network-coding regions — different target); Dolfi–Herzog–Kaplan–Lev bounds on solvable-residual *size* (no information reading); Doerk–Hawkes formation theory with the Gaschütz product as the (never-informationally-read) series composition. Status: the formation-lattice rate theory and the closure-theoretic Langlands-landscape statement appear original [checked at gut-check depth only; deeper sweep owed before any external claim].

## 12. Consolidation topology (per skill)
**Anchors.**
- A1 [firm]: Enrichment-from-axiom — the chain rule per conditioning IS the budget per hom; the composition-closure axioms descend from the foundations. Evidence: derivation + all downstream verifications.
- A2 [firm]: Coding theorem package (achievability [V] + converse [T+monotonicity] + partition + ∏u = |Gˢ|/|G| [V]).
- A3 [firm as structure; A as landscape claim]: From-below cone terminates at the Gaschütz closure; L–T at the boundary by necessity; extension requires a new primitive.
- A4 [firm]: Conservation = generation; Minkowski = terminal exactness; defect = portless sector = Gal(max unramified subextension).
- A5 [firm]: Degree-graded conservation ledger — H⁰ = budget row, H¹ = inf-res, transgression = anholonomy obstruction, four-cycle = minimal firing [V]; all-orders spectral statement [O].
- A6 [firm, V-backed]: Portless-at-K ≡ anholonomy-at-terminal (one content, base-indexed); genus stratum = the D↑/underpopulation face. (The corrected form of Will's proposal.)
- A7 [firm, meta]: Two evidence ledgers — derivational vs generative — kept separate; this session contributed only to the first.
**Inflections.**
- I1 → A4/A6 | prior: defect "carried by the base topology, suggestively adjacent to the seam" → new: finite-portless but ∞-typed; seam = ∞-port condition; −23 surfaces holomorphic; real-quadratic portless surfaces at the seam | axis: specificity | trigger: Will's pushback | σ: high | provenance: Maass 1949 vs Hecke 1926 surface-faces; the session's own −23 computations.
- I2 → A7 | prior: rhetoric risked implying the shadow-identification was generative evidence → new: explicit ledger separation; session = derivational only | axis: honesty/specificity | trigger: Will's challenge ("why wasn't it just citable?") | σ: high.
- I3 → Thread D | prior: speculative −ln(u^{3/2}f(Noise)) → new: exact identity via chart-separation; 3/2 = chart-mixing | axis: specificity | trigger: numeric table | σ: medium.
**Drift watch.** No accommodation-only drift detected; both major corrections were evidence-coupled and sharpened rather than softened positions. Standing guard honored: no absence-claims without search; parallel-thread diff hedges attached to every possibly-duplicated mint.
**Framework audit.** The channel framework predicted cleanly several times this session (suspicion trigger); the mitigations applied were failure-branch certificates (aliasing law; congruence sweep; product constraints) — each could have fired against the framework and did not. The one place the framework was *corrected by* the mathematics rather than confirmed: I1 (portless ≠ seam).

## 13. Open questions, ranked
1. **Role-swap involution exercise** — still unrun; the cheapest sharp test of the one axiom distinguishing the transmission formulation from restriction/induction. Candidate: dihedral leg, radix/length swapped, channel quantities checked against direction-reversal = S [M].
2. **Parallel-thread diff** — this session's x²_𝔉 lattice, rung pricing (lnℓ), and N-forms against the minted budget-of-a-group, rung-capacity (Landen rung), tower identity [M]; transcripts unavailable here.
3. **Real-quadratic portless exhibit** — the seam-side twin of Thread H: Maass 1949's Q(√5) construction as portless-sector content surfacing at λ = ¼; would join Threads H and the seam engine on one object. Natural next [V] target.
4. **All-orders conservation** — the full Hochschild–Serre statement as the graded ledger [O].
5. **Landscape note** — writing A3 properly, with the deeper literature sweep it requires.
6. **k-bonacci convention** (x vs x²) — prerequisite to the address-ladder hostages [carried].
7. **Nonabelian portless sector** — class-field towers / unramified nonsolvable extensions as the defect's nonabelian enlargement [flag only].
8. Unchanged from prior records: OT1 (x⁵→Z→AGM→τ→form) as the imported-vs-exhibited decider; even-icosahedral emission (resumption condition (i) met [M]); C1 operationalization against the computed ladder; uniqueness welding.

## 14. Verification table (this session)
| Item | Result | Scale |
|---|---|---|
| Formation-lattice monotonicity | OK at every group | 12 groups × 3 formations |
| S₄/S₅ towers: capacity sums, ∏u, tower identity | exact (≤2.3e-16) | — |
| F₂₀ abelian-symbol dictionary | deterministic, 0 exceptions | 300 primes |
| A₅ constant-symbol vs varying class | 0 violations; Chebotarev match | 300 primes |
| S₅ parity ≡ (2869/p) | 0 mismatches | 425 primes |
| N-identity −ln(√u_amp·N) = ln|G/N| | diffs 0.00e+00 | 6 groups |
| A₄ two-rung protocol (conductor 9; QR dictionary; product constraint; (3)⟺(1,3)) | 0 exceptions | 548 primes |
| Resolvent roots = sᵢ² | symbolic, exact | — |
| (2,3,5) dessin: abc=e, ⟨a,b⟩=A₅, perfectness | pass | — |
| SL₂(F₅): ⟨S,T⟩=120; ⟨T⟩=5; derived=120 | pass | — |
| η(τ)η(23τ) vs Galois rule | pass | primes < 200 |
| Contour recovery (M=512) | max err 3.1e-14 | n=1..24 |
| Aliasing law (M=32) | max err 3.7e-13; n=7 instance 2.4e-16 | n=1..24 |
| Q(√−23) form dictionary | 0/211 | split p < 3000 |
| Congruence sweep (class bit) | 0 surviving moduli ≤ 4000 | split p < 20000 |
| Q(√−5) mod-20 dictionary | 0/1124 | split p < 20000 |
| Inf-res: C₄ (tg fires), V₄ (tg=0), S₃ sign-twist (res surjective) | all pass | brute-force cocycles |

## 15. Session-original vs classical vs identification (distinct-content ledger)
**Framework-original this session:** the formation-lattice rate structure (per-𝔉 budgets, monotonicity as class-level DPI); the coding-theorem *assembly* (protocol class + measure from the enrichment; classical closure as the converse mechanism); ∏uₙ = |Gˢ|/|G|; the N-identity resolution and chart diagnosis; the tower pricing of the L–T proof architecture; the face-sign submergence statement; the Shannon⊕Nyquist decomposition of the functor with the aliasing-law certificate; the D↑-invariance derivation; the four-cycle-as-transgression address; the portless-sector defect theory with its genus/non-genus stratification derived; the portless≡anholonomy base-indexing (A6).
**Classical, cited:** Gaschütz/Doerk–Hawkes formation theory and the 𝔉∘𝔥 product; solvable-closure; Minkowski; Riemann existence; Hochschild–Serre; Hecke 1926; Maass 1949; Sturm; Chebotarev; Chan–Yeung (adjacent).
**Identification only [id]:** Abel–Ruffini as converse; L–T at the closure boundary; conservation = Minkowski-as-transmission-law; bandlimit = capacity; η(τ)η(23τ) = portless-sector shadow; emission experiment = Nyquist-side instrument.
**[M] pending diff:** x²(G), tower identity, rung capacity/Landen rung, direction-reversal = S, C1′, emission-experiment status.
