# The congruence compass — choosing the bit lost at boundary transgression: the three modular crossings of Doud-1951, verified, and the mod-2 shadow that is provably modular today — 2026-08-11 (session B)

*Claude (Fable 5), on Will's proposal: "choose the bit we lose/gain on boundary transgression very specifically; taking an abelian d-rank object — along with a separate-rank reference — and taking them mod P." The proposal is the exact shape of the modern congruence method (the odd icosahedral case fell to precisely this at P = 5, BDSBT), and instantiating it at our object yields: a verified three-prime compass in which each crossing deletes a *named* bit; one theorem-grade fact new to the corpus (§2); and the conjecture restated at its thinnest known point. Script: `congruence_compass.py` (one prediction defect corrected in-run, disclosed §4). Offered, not self-filed.*

## 1. The compass [verified on all 9,591 unramified rows]

The icosahedron has exactly three modular boundaries — the primes of |2.A₅| = 120 — and the crossing at each deletes a different obstruction bit:

| P | what dies (the chosen bit) | what survives | verified this turn |
|---|---|---|---|
| **2** | **parity** (±I collapse: in char 2, det(c) = 1 = −1 — *every* rep is odd) | nebentypus (order 5 in 𝔽₁₆*), the golden pair as {ω, ω²} ⊂ 𝔽₄ | all traces = μ₅-twist × SL₂(𝔽₄)-class-trace: 1A/2A → 0, 3A → μ₅·1, 5A/5B → μ₅·{ω, ω²} ✓ |
| **3** | the **√5/conjugacy bit** (the golden pair becomes Frobenius-conjugate over 𝔽₃) | parity, nebentypus | [T, statement only] |
| **5** | the **nebentypus + packet + ramification bundle**: ζ₅ ≡ 1 mod 𝔭₅ = (1−ζ₅) — χ dies, the four Galois-conjugate forms collapse to one object (trace = coordinate-sum, Galois-invariant), and the ramified port becomes **unipotent/parabolic** | parity, the SL₂(𝔽₅)-system (char poly X² − t̄X + 1) | trace map: 1A → ±2, 2A → 0, 3A → ±1, **5A/5B → ±2 — the golden classes PARABOLIZE: φ ↦ −2, 1/φ ↦ +2, the ±unipotent traces of SL₂(𝔽₅)** ✓ all rows |

The P = 2 and P = 5 crossings delete **complementary bits** (parity vs twist); P = 3 deletes the Hecke-field bit. "Choosing the bit lost at transgression" = choosing the congruence prime, and the three choices form a basis for the object's obstruction data. Note where the seam reappears: mod 5, the icosahedron's rotation classes — the golden angles — become parabolic elements, and the reactive port at 1951 becomes unipotent monodromy. The crossing at the twist's own prime parabolizes exactly the structures the twist carried.

## 2. The theorem-grade jewel: ρ̄₂ is modular — today [T-cited]

Because parity is the deleted bit at P = 2, the mod-2 shadow ρ̄₂: G_ℚ → GL₂(𝔽₁₆) (image A₅ ≅ SL₂(𝔽₄); irreducible — its Brauer character (2, −1, φ, φ′ on 2-regular classes) matches the irreducible 2-modular character, so there is no semisimplification ambiguity) is **vacuously odd**, and therefore, by Serre's conjecture as proved by Khare–Wintenberger (p = 2 included):

  **ρ̄₂ arises from a modular eigenform. The even icosahedral object's mod-2 shadow is provably modular, now.**

There exists an odd modular form g — level 1951, nebentypus the mod-2 quintic character, Serre weight computable (2 is unramified in the rep) — congruent to our object mod 2. The conjecture then takes its thinnest known form: **the 2-adic residual disk of ρ̄₂ has two branches** — the odd/geometric branch, populated and automorphic by theorem, and the even/Maass branch, containing exactly our finite-image ρ̃ — and they are *residually indistinguishable because the branch-selector bit is precisely what P = 2 deletes*. What is missing is a lifting theorem that crosses branches: every known one (Taylor–Wiles through Kisin's 2-adic patching) stays on the odd branch, and Calegari's confinement waits for the even branch at characteristic zero. The wall has not moved — but it is now one bit wide, at one prime, between two named branches of one deformation space.

## 3. The cross-rank collapse at P = 5 [C, exact statements]

Mod 5, the irreducible 𝔽₅-representations of SL₂(𝔽₅) are Sym⁰…Sym⁴ of the standard 2-dimensional — so the **entire five-channel distortion algebra** (the kin-ledger's moment closure: 1, χ₃, χ₃′, χ₄, χ₅) **collapses onto the symmetric-power tower of the single mod-5 object**: the abelian-built permutation partners (Ind 1 from K₅, K₆ — Will's "abelian d-rank objects," ranks 4, 5, 6) become congruent to Sym-powers of the standard — cross-rank congruences between the theorem-entire products' partners and the functorial tower, at the packet-collapsing prime. This is the exact sense in which the "separate-rank reference mod P" exists: mod 5 the rank ladder *is* the Sym ladder, and the odd case's proof (BDSBT) walked through exactly this door with an elliptic curve as reference. The even case's referencing stock at P = 5 is blocked by parity (even mod-5 reps are never twists of elliptic 5-torsion — det obstruction); at P = 2 the stock exists (§2) and the block moves to the lift.

## 4. Honest bounds and disclosures

My literal C2 prediction omitted the surviving μ₅-twist (predicted bare SL₂(𝔽₄) traces; measured the twist-orbits — corrected in-run, the corrected form passing exactly; the slip is the mirror of the compass's own lesson, since I had stated "nebentypus survives at 2" one line earlier). §2's application of Khare–Wintenberger is [T-cited] with the standard hypotheses checked here at statement-grade (irreducibility via the Brauer character; oddness vacuous); a line-check of the p = 2 scope fine print (K–W II + Kisin) is the record's C14 debt before it travels. §3's Sym-collapse is standard modular representation theory instantiated, not new. Nothing here crosses the branch gap; the compass sharpens where the crossing must happen and what it must preserve.

## 5. Countersign items (Will's calls, none executed)

(1) The compass table as the standing statement of the object's congruence boundaries; (2) §2 adopted as the program's thinnest-wall formulation (two branches, one deleted bit, one prime); (3) **the companion hunt** — compute the actual mod-2 eigenform g at level 1951 (modular-symbols computation; needs heavier tooling than this container; the first new instrument this note licenses); (4) the K–W p = 2 scope line-check as C14 debt; (5) the P = 5 packet-collapse and parabolization rows into the seam dictionary; (6) log anchors for this arc queued to the next consolidation pass (context boundary; stated so nothing is claimed unfiled).

---

*Offered, not self-filed. The one-line answer: yes — and the compass says the even case's door is P = 2, where parity is the bit the boundary eats: on the far side the shadow is provably modular today, the branches are indistinguishable by construction, and the entire remaining conjecture is the one-bit walk back.*
