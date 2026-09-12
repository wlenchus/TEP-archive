# P-H run 1 — RESULT: INCONCLUSIVE under K-H2. No verdict issued.

*2026-08-06, immediately following the pre-registration `PREREG_healing_exponent_universality_20260806.md`, sha256 `a7ab639b72927a0796182ad121b03ad701546a11e8429b9cb15b75508cc0d59e`, which was written and hashed before any of the quantities below were computed. Script `ph_test.py`, seed 80683. Offered, not self-filed.*

---

## 1. Outcome

**No exponent was issued for any n. P-H1 is neither supported nor falsified by this run.** Every level at every n failed the pre-registered coverage requirement K-H2 (≥ 20 feasible restarts): the feasible counts were 1, 1, 1, 5 (n=3); 2, 1, 1, 1 (n=4); 1, 0, 0, 0 (n=5), out of 24 descents each.

Per K-H2 as written, these are **coverage failures, not nulls**. They say nothing about whether creases exist at those levels — Delta 5 already established that they do at n = 3 — and nothing about the exponent.

## 2. What I am not doing

The obvious move is to lower K-H2 from 20 to, say, 5, at which point n=3's θ=0.99 row would qualify and the run would start producing numbers. **That is forbidden by §4 of the pre-registration ("no rescue is permitted") and I am not doing it.** A coverage bar relaxed after seeing which rows fail it is not a bar.

I also note, because it is the kind of thing that gets quietly forgotten: had the run *succeeded*, I would have reported it as support for a TEP reading. Failing to report the failure at the same volume is the asymmetry the corpus's own "same-day errata at headline volume" convention exists to prevent.

## 3. Diagnosed cause — a defect in my method, not in the prediction

The descent phase used a **penalty** formulation, `min I(f) + 10⁵·max(0, c_min − c(f))²`, seeded from points already satisfying `c ≥ c_min`. Nelder–Mead then walks out of the feasible set: near the summit the constraint surface is extremely narrow (the whole point of the region — `c` is near its maximum, so the feasible set is a thin shell), the penalty gradient is not felt until the walker is already outside, and the returned optimum sits below `c_min` and is discarded. Hence 1-of-24 rather than 24-of-24.

Two corrections for run 2, neither of which touches a bar:
1. **Replace the penalty with a hard constraint** — SLSQP or trust-constr with `c(f) − c_min ≥ 0` as an explicit inequality, or an exact-penalty method with a feasibility restoration step.
2. **Reparametrise to make the constraint structural** — search on the level set directly by fixing the Blaschke parameters that control `c` and varying only the remaining freedom, so every trial point is feasible by construction.

Option 2 is better and is what I would run: it turns a 1/24 feasibility rate into 24/24 and removes the failure mode rather than penalising it.

## 4. One incidental measurement, priced as a search yield

Not predicted, not part of P-H, reported because it was measured: the summit `c*_n` over degree-3 Blaschke products on the unit-disk-normalised nilpotent family is **not monotone in n**.

| n | ‖A_n‖ = 1/cos(π/(n+1)) | c*_n (deg-3 search) |
|---|---|---|
| 2 | 2.000000 | 1.980315 |
| 3 | 1.414214 | **1.990166** |
| 4 | 1.236068 | 1.888544 |
| 5 | 1.154701 | 1.615696 |

`c*` peaks at n = 3 and falls thereafter, while `‖A_n‖` falls monotonically from n = 2. **This is degree-limited**: the search family was fixed at degree 3, and higher-degree Blaschke products may well raise `c*` for larger n — the n = 3 summit itself is attained at degree 3 and exceeds `‖A₃‖` by 0.576, so degree matters a great deal here. Treat the table as a search yield at fixed degree, not as a property of the family.

## 5. Standing after run 1

- **P-H1, P-H2, P-H3: all open.** Nothing was learned about the fork.
- **The pre-registration stands unmodified** and is the binding document for run 2. Its §6 disclosure — that `p_3` is partially determined by pre-filing Delta 5 data — still applies and still weakens it.
- **What the run does establish** is a methodological point I will carry: near-summit constrained search over Blaschke families needs a feasibility-preserving parametrisation, not a penalty. Delta 5's stage-C figures were obtained with the same penalty method and 7–10 feasible restarts out of 45; they are therefore **also** thinner than they looked, and while they exceed K-H2's bar at those levels, their crease depths should be read as upper bounds on |I_min| that a better-covered search would likely deepen further.

That last sentence is a self-correction against my own Delta 5 §5, and it cuts against the direction I would prefer: it means the corrected J₃ profile I reported yesterday is itself probably still understating crease depth.

---

*Offered, not self-filed. Countersign items: the INCONCLUSIVE verdict; the refusal to relax K-H2; the §5 self-correction against Delta 5 §5's coverage.*
