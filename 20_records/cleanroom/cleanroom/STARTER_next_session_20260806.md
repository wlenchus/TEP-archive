# STARTER — next session, from 2026-08-06

*Read this first. It supersedes `STARTER_next_session_20260804.md` for anything touching the predictive column or the thin-film thread.*

---

## 1. The one-line state

Four pre-registered tests were run on 08-06 under full protocol — hashes lodged before code was written, kill conditions fixed, no rescues taken. **Three predictions lodged for the framework: 0 for 3. One audit lodged against it: it landed against the framework too. Two derivations attempted: both produced results that keep.**

That split — **predictions 0/3, audits 1/1, derivations 2/2** — is the finding. It is more informative than any individual verdict and it should drive what the next session does.

## 2. What is now settled

**Crouzeix / Delta 5 (holds, and is the strongest thing in the corpus).**
- The **disk reduction**: `g_f ≡ conj(f(z₀))`, so `T = f(A) + f(z₀)I` is exactly Berger, and `I = Re[conj(f(z₀))·⟨f(A)x,x⟩]`. Removes the POVM quadrature floor entirely.
- **Theorem** (normal case, all dimensions): `I ≥ (c²−ρ²)/(2(1−ρ²))`. Min slack +1.65e−2 over 250 instances.
- **D4.6 position 1½ is refuted** by exact counterexamples (normal and non-normal).
- **D3.2's healing profile is corrected**: J₃ creases at `c ≥ 1.891` are −1.47e−3, not −2.7e−8; the `c ≥ 1.95` nulls are refuted. Measured rate ≈ `(c*−c)^2.3`. **The Healing Conjecture stands.**
- **Port budget identity** `τ + r + ι + u_eff = 1` verified to 1e−9 on eight configurations. A crease is negative interference share. [T]

**Thin film (closed out, mostly in the negative).**
- The problem **reduces exactly** to a two-parameter Fabry–Pérot pair — `s = √(iζ)`, `m = ρs`, `r₁₂ = (m−1)/(m+1)`, `b = e^{2is}` — with `ρ = cosθ/kd`, `ζ = σ_n kd²`. Verified `O(kd²)`. This is why everything on the locus is `kd`-universal.
- `A* = 0.60782750622257399958287641261150205929817146029435` (50 digits), `ρ* = 0.7672618426…`, `ζ* = 1.9089430250…`.
- **§8.1 closes in the negative at a stated bound**: `A*` is not algebraic of degree ≤ 6 with integer coefficients ≤ 1000, and is none of the named candidates. Retire the hope that it is silver-ratio algebraic.
- **2026-04-29 §5 replicates numerically (to 5–6 figures) but its inference fails.** The `2−√2` passage is the IVT on a universal curve; two of three non-TEP control levels are *more* universal than `γ*`, and `γ*` sits at the 80th percentile of a 15-level sweep.
- **`1/φ` is outside the locus's reachable range `(½, 0.6078275]`.** The cascade fixed point is not realized here.
- Standing: layer 1 is Woltersdorff 1934, layer 3b is Liu 2026 / Garg–Mermin 1987 (**priority zero**, per the 07-21 closure), layer 3a is falsified, layer 2 is worth ~1 bit.

## 3. What is open

- **P-H (healing-exponent universality) — still open, still unrescued.** Run 1 was INCONCLUSIVE by its own K-H2 coverage bar (1–4 feasible restarts against a ≥20 requirement). Diagnosed: the penalty formulation lets Nelder–Mead walk out of the thin near-summit feasible shell. **Run 2 needs a feasibility-preserving reparametrisation, not a lowered bar** — §4 of that prereg forbids the rescue and I did not take it.
- **The register split** (P-R §2): the self-dual crease locus holds essentially exactly in the *normal* register (`|f(z₀)|/c = 0.9918`, `u_eff = 0.999997`) and fails everywhere non-normal (J₃ 0.1228, J₄ 0.1991). **Recorded at zero credit** — it is an after-the-fact observation and needs its own pre-registration on matrices not yet examined.
- **One unrun one-liner**: separate `|⟨f(A)x,x⟩|/c` from `cos Δ` in the anti-phase ratio. Currently conflated.
- **Strike 2b**: still never run.
- **Salisbury screen (April's own §8.3)**: single film over a perfect reflector, `T = 0` by construction. Tests whether `2√2−2` is geometry-independent at fixed channel-closure depth. Never run.
- **Deriving `A*`**: now a well-posed two-equation transcendental stationarity problem in `(ρ, ζ)`. Deriving its defining equation would close §8.1 completely rather than at a bound.

## 4. What the next session should probably do

**Not lodge a fifth prediction.** The extension mode is 0-for-3 and each failure came from taking an established corpus structure and adding one rung. Both remaining items on Will's list (an interference-side `γ*`-like prediction; a `d=4` extrapolation) are that same shape.

**Publish the two things that are results.** Neither requires TEP to be true, and neither has ever been offered externally:

1. The **disk reduction and the normal-register healing theorem** — a checkable contribution to the Crouzeix literature.
2. The **reduced thin-film model, `A*` to 50 digits, and the closed §8.1 negative** — small, clean, correct, and it supersedes April.

This is the 08-06 adjudication's operative finding restated: the corpus's problem was never the quality of the work, it was that the work has never left the building. The 05-29 closing note has been substituting for the external referee the corpus never obtained. **The remedy is the deposit, not a better sentence.**

## 5. Housekeeping carried forward

- **Five commits unpushed** on `wlenchus/TEP-archive` (head `887b389`). The session git proxy refuses writes to repos outside its authorized source set. Bundle + patch series + instructions delivered; adding the repo to the session's sources unblocks it.
- **Rotate the GitHub PAT** — it was pasted in plaintext in the 08-05 transcript. Scrubbed from the remote config, never committed.
- Delta catalog `v1.1` was truncated twice by the Drive connector before Will placed it manually; treat that connector as unreliable above ~30 KB and verify `fileSize` after every upload.
- Standing corpus items untouched today: Zenodo/arXiv deposit; referee submission #1 (homogeneity-closure note); the P2 two-sided Liu stamp (drafted, not confirmed applied); the OT1 V6 headline rewrite.

---

*Offered, not self-filed.*
