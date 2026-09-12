# ERRATUM — "the parabolic port measured empty" is withdrawn: mode 0 is not the port, and the port is not empty — 2026-08-13 (session B)

*Claude (Fable 5), at headline volume per the corpus's errata convention. Raised by Will ("the port is not empty, it's active at rank/depth = 1 mod 2; the ports are indices — factors"), verified before writing. Corrects `charges/RESULT_horocycle_fourier_parabolic_port_20260813B.md` §1(i), §2 headline, §4, and its closing line. Offered, not self-filed.*

---

## 1. The error, stated plainly

I identified mode 0 of the horocycle transform with "the parabolic/Eisenstein component," and its vanishing with cuspidality-hence-entirety. **Both identifications are wrong, and they are wrong in two separate ways.**

**(a) Category error — ports are places, not Fourier modes.** In the corpus's own ledger, *ports are indices: places, Euler factors*. The parabolic port is the rank-1 (GL₁) channel — the Eisenstein family induced from the parabolic's Levi, whose scattering entries are ratios of abelian L-functions and whose cross-cusp coupling carries τ(χ). **That port is active, and it is active exactly at rank/depth 1** — it is where the entire abelian ledger lives. Calling a Fourier mode "the port" conflated an index-structure concept with a coefficient of one expansion. Will's phrasing is the correction: the ports are the factors.

**(b) The measurement does not mean what I said.** For an odd (sin-type) form, F(−conj z) = −F(z), and one checks w(−x) = −conj(w(x)) for w(x) = −1/(N(x+iy)) — so **F|W is odd in x unconditionally, by parity alone.** Combined with 1-periodicity, that forces mode 0 = 0 identically. So the vanishing I measured is *not* evidence of an absent Eisenstein component; the constant term of an odd form vanishes structurally, at every cusp, always.

## 2. What the measurement does test (the salvage, correctly labelled)

Periodicity of F|W in x is *not* automatic without automorphy: F|W(x+1) = F|W(x) ⟺ F is invariant under W⁻¹TW = [[1,0],[−N,1]] — **the parabolic generator at the cusp 0**, a genuine element of Γ₀(N). So:

> **Mode 0 ≈ 0 tests the parabolic generator at cusp 0, given oddness.** It is a real automorphy test at one group element — a useful one, and new (no prior test used the lower-unipotent generator) — but it is *necessary, not sufficient*, and it says nothing about the Eisenstein channel's occupancy.

**§4 downgraded.** The identity c₀(y) = Σ_n c_n I_n(y) with I_n arithmetic-free stands as an identity. But its billing as "⟺ the strong Artin conjecture" is **withdrawn**: it is one automorphy relation among the generators of Γ₀(N), not the whole conjecture. The kernel-orthogonality framing survives only as *a* necessary condition with a clean separation of arithmetic from analysis — which is still worth having, and the "compute I_n in closed form" target is still worth pursuing, but it is not the conjecture in one line, and I said it was.

## 3. What survives unchanged

- **The mode-matching at n ≥ 1**: modes 1–3 (1951) and 1–5 (2141) equal const·√y·c̄_n·K₀(2πny) to every computed digit, with const the certified Fricke constant. Not forced by parity; a genuine test.
- **The must-be-zero band**: modes 6–255 vanishing at median 2×10⁻¹⁵ is not a parity consequence — it is the fold's prediction that only ~3 modes survive. ~250 real simultaneous tests.
- **The collapse**: 10⁵ K-Bessel terms per evaluation → 3 nonzero Fourier modes. Unaffected by the erratum, and still the clearest exhibition of the duality mechanism this program has produced.
- Lemma H (holomorphic hardening) is independent of all of the above and stands.

## 4. The correct next probe, per the correction

If the parabolic port is active at rank 1, the way to read it is to **compute the rank-1 channel directly**: the scattering matrix Φ(s) for Γ₀(1951) with primitive nebentypus χ. For primitive χ at prime level the scattering matrix is purely off-diagonal, and its entry carries **τ(χ)/√N — the seam unit already derived and certified**. That computation is the parabolic-seam note's countersign item (3), still unexecuted, and it is now the named next instrument: it would measure the port's *actual* occupancy (its rank-1 content), rather than a coefficient that parity zeroes for free.

## 5. Grade of the miss, for the drift record

Same-day, self-corrected on Will's flag, verified before writing. Class: **over-interpretation of a structural zero** — I measured a quantity that vanishes for a reason I had not checked, and read the vanishing as evidence for a claim it cannot support. Closest prior instance: the E-b separation clause (a bar mis-set against a structural fact). Distinct from the week's numerical slips in that this one reached the headline of a record and would have travelled. The instrument itself is sound; the label was not. **Countersign:** (1) this erratum against the parent record at headline volume; (2) §2's parabolic-generator test as the salvaged, correctly-billed finding; (3) §4's scattering-matrix computation as the next instrument; (4) the parent record's §4 marked downgraded, not withdrawn.

---

*Offered, not self-filed. One line: the port is a place, not a mode; it is active, not empty; and what I actually measured was the lower-unipotent generator behaving itself — worth having, worth naming correctly, and not worth the headline I gave it.*
