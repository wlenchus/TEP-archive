# PRE-REGISTRATION — Crouzeix healing-exponent universality (Charge 1, prediction P-H)

*Filed 2026-08-06 **before any computation of the quantities below**. Claude (Opus 5). This is the corpus's first prediction about a fork it can lose that is not a prediction about its own instrument's reading. Offered, not self-filed. Bars are not moved after this filing.*

---

## 0. Why this, and why the corpus has not done this before

The 08-06 adjudication proposed a three-part bar for external-leverage claims — reproduce / yield-new / **predict-and-test** — and found the third column empty across every external charge. It is empty for a structural reason worth stating: **the corpus's protocol is optimised for not-fooling-itself, which is a different objective from generating exposure.** Pre-registration with kill conditions prevents overclaiming; it does not put the framework at risk. Every prediction the corpus has lodged (parity ports, orientation, nebentypus order, the Crespo twist character) is a prediction about *what its own instrument will read*. Those are calibration predictions, and the corpus is very good at them. None of them exposes TEP.

A prediction exposes the framework only where **TEP's reading and the default reading disagree**. This one does.

## 1. The fork

Charge 1 established that the interference functional `I` goes negative below the summit ("creases") and heals as `c → c*`. Two incompatible readings of *what a crease is* are already on the record:

**(TEP-port reading.)** Delta 2.3 and Delta 5 §1: the reflected channel is a **port** object. On a disk it collapses to the single number `f(z₀)`; the Naimark dilation *is* the port construction; the crease is destructive interference between the direct read and the one reflected read at the seam. A port is a boundary structure. **This reading predicts the healing law is blind to the interior — in particular, to Jordan block size.**

**(Spectral/fold reading.)** Delta 1.1: the violation engine is constructive multi-sheet phase-stacking, because `f = z^{n−1}` on `J_n` wraps `∂W` n−1 times; crease behaviour is then governed by fold multiplicity, which is an interior spectral datum that **grows with n**. This reading predicts the healing law moves with dimension.

Both are live in the brief. They have never been separated by measurement.

## 2. Definitions (fixed here, not adjustable later)

- `A_n` := the n×n nilpotent with constant superdiagonal `1/cos(π/(n+1))`, so `W(A_n)` = the closed unit disk exactly. `Ω` := the closed unit disk. `z₀ = 0`.
- `I` computed by the Delta 5 disk reduction, `I = Re[conj(f(0))·⟨f(A)x,x⟩]`, exactly — no quadrature.
- `f` ranges over finite Blaschke products of degree ≤ 4 (`|f| ≡ 1` on `∂Ω` by construction).
- `c*_n` := the summit, `max ‖f(A_n)‖` over that family, computed by the same optimiser.
- **Crease depth** `D_n(θ) := −min{ I : c ≥ θ·c*_n }`, reported only when ≥ 20 restarts are feasible at that level.
- **Healing exponent** `p_n` := the ordinary-least-squares slope of `log D_n` against `log(1−θ)` over the ladder `θ ∈ {0.90, 0.95, 0.98, 0.99}`, when all four levels yield creases.

## 3. The prediction

**P-H1 [novel — the load-bearing claim].** `p_n` is **independent of n**: `p_3, p_4, p_5, p_6` agree within the tolerance of K-H1 below. *TEP-port predicts this. The fold reading predicts drift with n.*

**P-H2 [novel, weaker — [C]].** `p = 2` exactly. Sketch, offered as motivation not derivation: for `J₂` the exact form `I = |x₂|²|a₀|²(1+α)` gives `I ~ |a₀|²`, and expanding the Schwarz-extremal `c` at small `|a₀|` gives `c* − c ≈ (3/2)|a₀|²`, so the *positive* floor is first-order in `(c*−c)`. A crease in n ≥ 3 requires one additional vanishing factor from the reflected channel; if that factor is itself first-order in the same small parameter, `p = 2`. My own Delta 5 J₃ measurement gave log-log slopes 2.29, 2.32, 1.40 — consistent with 2 and not well determined, which is why this is the weaker claim.

**P-H3 [pattern, costless — labelled so].** Creases exist at some θ ≥ 0.90 for every n ≥ 3. Evidence is 1/1 (n = 3). This is not a test of anything; it is stated so that its confirmation is not later miscounted as support.

**Explicitly no prediction is made** about: the sign or size of `c*_n − 2`; whether `p_n` exceeds or falls below 2 if P-H2 fails; the off-disk case (not in scope here).

## 4. Kill conditions

- **K-H1 (the fork).** If `max p_n − min p_n > 0.5` across n ∈ {3,4,5,6} — i.e. > ~25% of the predicted value — **P-H1 is FALSIFIED and the TEP-port reading of the crease is falsified with it**; the fold/spectral reading is favoured, and Delta 2.3's "the Naimark dilation *is* the port construction" must be re-scoped as an identity of construction that does not govern crease behaviour.
- **K-H2 (coverage).** For any n, if fewer than 20 restarts are feasible at a level, that level is reported as **coverage failure, not a null**, and is excluded from the fit. If fewer than three levels survive for any n, no `p_n` is issued for that n.
- **K-H3 (optimiser limit).** If doubling the restart budget moves any `p_n` by more than 15%, the measurement is optimiser-limited and **no verdict is issued on P-H1 at all** — the run is reported as inconclusive rather than as support.
- **K-H4 (premise).** If no crease is found for any n ≥ 4 at any level with adequate coverage, P-H3 fails, and the whole exponent question is void for those n.

**No rescue is permitted.** If K-H1 fires I do not get to argue that the port reading survives in a weakened form; the record will say the fork resolved against TEP.

## 5. What each outcome buys, priced now

- **P-H1 holds:** the crease is a boundary/port phenomenon, blind to interior structure. This is the first measurement in this corpus that could have gone against a TEP reading and did not. It is *one* fork in *one* register — it is not a validation of the framework, and I will not let it be reported as one.
- **P-H1 fails:** the port reading of the crease is wrong, Delta 2.3's identification narrows, and the brief's own fold picture is vindicated against it. That is a real cost and it is the point of filing.
- **P-H2 holds:** a specific constant predicted from a two-line argument. Worth more than P-H1 if it lands, worth little if it fails alone.

## 6. Disclosures

**Training-prior.** I know of no literature measuring a "healing exponent" for the Crouzeix interference functional; the functional is this corpus's construction (2026-08-01) and Delta 5's exact evaluation is four days old. There is nothing here I could be recalling. Berger, Okubo–Ando and Schwarz–Pick are weights-knowledge and are used only through Delta 5's already-filed results.

**What I have already computed and what I have not.** Already on record from Delta 5: `c*_3 = 1.990165663`, and the J₃ crease ladder (−7.20e−3, −1.47e−3, −1.75e−4, −6.66e−5 at θ = 0.900/0.950/0.980/0.990). So `p_3` is **partially determined by data that predates this filing** — that is a real weakness of this pre-registration and I am stating it rather than hiding it: only `p_4, p_5, p_6` are fully blind. The fork is nonetheless live, because P-H1 is a claim about *agreement across n*, and three of the four values are unmeasured.

**Nothing about A₄, A₅, A₆ has been computed at the time of filing** — not their summits, not their profiles, not a single value of `I`.

---

*Offered, not self-filed. Countersign items: the prediction-class labels in §3; the kill conditions in §4 as binding; the §6 disclosure that `p_3` is not blind.*
