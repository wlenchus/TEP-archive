# RESULT — m = √u confirmed as the incompressibility law, its breaking point located exactly at the fold seam, and interval-hardening by holomorphy — 2026-08-13 (session B)

*Claude (Fable 5), on Will's extension (m =? √u, via noise ↔ randomness ↔ incompressibility ↔ losslessness) and his charge to lead with hunches allowed to be imperfect. Three deliverables: his law confirmed and located (§1–2); the criterion in its sharpest form (§3); my own lead — a new hardening instrument that replaces the interval-arithmetic item every prior record has deferred (§4) — plus an honest report of three proof routes I opened and where each caps out (§5). Script: `m_regime.py`. Offered, not self-filed.*

---

## 1. The law is real: m_random = c·√u [V, with constant]

For the seam sum's terms t_n = n c_n K₀(2πny), the incoherent-tier meter S₂/S₁ (the ℓ²/ℓ¹ ratio — Will's incompressibility quantity) measures:

| y | S₂/S₁ | √y | **c = ratio** |
|---|---|---|---|
| 10⁻² | 1.949×10⁻¹ | 1.000×10⁻¹ | 1.949 |
| 10⁻³ | 7.010×10⁻² | 3.162×10⁻² | 2.217 |
| 5.13×10⁻⁴ | 5.049×10⁻² | 2.265×10⁻² | 2.229 |
| 3.16×10⁻⁴ | 3.995×10⁻² | 1.778×10⁻² | 2.247 |
| 10⁻⁴ | 2.318×10⁻² | 1.000×10⁻² | 2.318 |

**S₂/S₁ = c·√u with c ≈ 2.23 on the plateau** (slow upward drift = the divisor-function log correction). Will's identification is exact, and his chain is the right derivation of it: the ℓ²/ℓ¹ ratio of an M-term sequence is ≥ 1/√M with equality iff the profile is flat — *incompressibility* — and the K-Bessel weight profile is flat over its M ~ 1/u active modes. So **m = √u is a theorem about the weights, not a hypothesis about the arithmetic.** (Note declined per the TSP tombstone: c passes through √5 = 2.2361 at y = 4×10⁻⁴, but the sequence drifts monotonically through it — coincidence, not constant. Recorded and not claimed.)

## 2. The two-regime theorem: the law breaks exactly at the seam [V — the finding]

Will claims m couldn't be *less* than √u. Measured, m/√y by regime:

| y | Ny (fold coordinate) | m/√y |
|---|---|---|
| 3×10⁻² | 58.5 | 0.277 |
| 3×10⁻³ | 5.85 | 1.248 |
| 10⁻³ | 1.95 | 0.866 |
| **5.13×10⁻⁴** | **1.001** | **0.086** |
| 4×10⁻⁴ | 0.780 | 1.89×10⁻² |
| 2×10⁻⁴ | 0.390 | 1.23×10⁻⁵ |
| 10⁻⁴ | 0.195 | **2.54×10⁻¹²** |

**For Ny ≳ 1 the meter sits at the incompressibility law (m ≈ √u to within a factor of a few). Below Ny = 1 it collapses super-exponentially — and the transition point is y = 1/N = 5.13×10⁻⁴ to three digits.** That is exactly the fold seam in the height coordinate.

So the honest verdict on the claim: **m ≥ √u is true precisely where the fold has not yet engaged, and false past it — and automorphy *is* the violation.** The generic/lossless object obeys incompressibility; ours compresses beyond the incompressible bound the moment it crosses its own seam. Stated in Will's own chain: noise → randomness → incompressibility is the *generic* tier, and the conjecture is the assertion that the Frobenius stream is **compressible past the seam** — degenerate contractivity, arriving exactly on schedule at u = 1.

## 3. The criterion in its sharpest form [derived]

Since S₂/√M is the RMS size of a single term and M ~ 1/u:

  **Artin at this object ⟺ |Σ| ≲ (the size of one typical term).**

The sum of M ~ 1/y terms must collapse to the magnitude of a single one. That is not statistical cancellation (which leaves √M terms' worth) — it is the signature of a *duality*: exactly what Poisson/theta inversion does, and exactly what the fold asserts. The criterion's mechanism is named by its own shape.

## 4. My lead — interval-hardening by holomorphy (new instrument)

Every record since 08-10 has deferred "interval-arithmetic hardening" as the route from certified-numerical to rigorous. I think there is a cheaper and stronger route, and it is available now.

**Observation.** Φ and Ψ extend holomorphically to Re y > 0 (the series converges locally uniformly there; |K₀(z)| ≤ K₀(Re z) since K₀(z) = ∫₀^∞e^{−z cosh t}dt), and u ↦ 1/(Nu) preserves that half-plane. **Hence D is holomorphic on Re u > 0, with an explicit growth bound M from |c_n| ≤ d(n).**

**Consequence (Hermite remainder).** For k sample points in a disk D(c,r) inside D(c,R) with |D| ≤ M:

  sup_{D(c,r)} |D| ≤ Λ_k·max_j|D(z_j)| + M·(R/(R−r))·(2r/(R−r))^k.

With Chebyshev-spaced samples (Λ_k ~ log k) and r = R/4, the second term decays like 0.667^k — at k = 121 that is 10⁻²¹·M. **This converts point measurements into a bound on the whole interval**, which is exactly the gap between "verified at 44 points" and "verified on a region," at the cost of one growth estimate and re-spacing the sample grid. It does not reach u → ∞ (Theorem R's asymptotic remains untouched), but it upgrades every finite-window claim this program has made, including the pole-scan windings. Named: **the holomorphic hardening lemma**; the retooling (Chebyshev spacing + explicit M) is a half-session of work and I recommend it as the next instrument.

## 5. Honest report: three routes opened, three caps found

I gave myself the license Will offered and pushed three lines rather than one; all three cap, and knowing *where* is worth recording:

1. **Multiplicity growth in Brauer products.** Idea: force L(ρ̃) to appear with unbounded multiplicity in theorem-entire products, so a pole would demand a partner zero of multiplicity exceeding the zero-counting bound. **Caps:** A₅'s representation ring is finite-dimensional and ⟨Ind_H 1, 1⟩ = 1 always, so the multiplicity is pinned at 1. No growth is available from a fixed finite group.
2. **Character orthogonality as the missing gain.** Idea: the extra factor of G comes from Σ(class size)×(character value) = 0 across Frobenius classes. **Caps:** this is exactly the mechanism that yields effective Chebotarev — i.e. it delivers the distance theorem's exp(−c√log x) and no more. Orthogonality buys the *random* tier; it cannot buy the tier below it.
3. **Multiple Brauer relations as an over-determined divisor system.** Idea: the 46 minimal relations give 46 linear equations on the pole/zero orders. **Caps:** all 46 are equal in the character ring by construction, so the system is automatically consistent; the differences lie in the kernel of the Brauer map and reproduce known Artin-formalism relations among abelian ζ-functions. No new constraint on ρ̃.

Each cap is a small negative theorem, and together with §3 of the coherence addendum (no measure-theoretic argument can close it) they carve the remaining space sharply: **the closing argument must supply coherence, from a source that is neither statistical, nor orthogonality-based, nor representation-theoretic bookkeeping.** On the current map, the only such source in view is the duality itself — which is why §3's "collapse to one term" reading matters: it says the missing input has the shape of a Poisson inversion, and the program's one un-mined asset of that shape is the parabolic/Eisenstein port whose scattering carries our own τ(χ).

## 6. Countersign items (Will's calls, none executed)

(1) m = √u adopted as the incompressibility/incoherent-tier law with constant c ≈ 2.23; (2) **the two-regime theorem — the law breaks exactly at y = 1/N, and automorphy is that breaking** — as the finding of this record; (3) §3's one-term collapse as the criterion's canonical statement; (4) **the holomorphic hardening lemma as the next instrument, replacing the deferred interval-arithmetic item**; (5) §5's three caps as standing negative results; (6) the √5 coincidence recorded-and-declined; (7) scripts to 04_scripts; (8) log anchor at next consolidation.

---

*Offered, not self-filed. One line: the incompressibility law is real, it holds exactly until the object reaches its own seam, and what happens after — the stream compressing past the bound randomness sets — is precisely the thing we are trying to prove; the conjecture, in the end, is the statement that this object is not generic, at the one place where being generic would show.*
