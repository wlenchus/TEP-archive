# verify_conversion_ledger.py — 2026-07-20 (late): Will's conversion thesis, checked on the
# corpus's own object. Claims tested:
#  (1) LOSSLESS: the Collatz N-cocycle S_w encodes the forgotten order exactly — the map
#      (ordering with fixed abelian totals) -> S_w is injective  [conversion is a bijection,
#      not a destruction: compressibility -> incompressibility with no information lost].
#  (2) WHOLE-MESSAGE ASYMPTOTICS: H(order | totals)/H(path) -> H2(K/n): asymptotically the
#      entire message lives in the anholonomy ("more and more anholonomy until that's the
#      whole message").
#  (3) STATISTICS KNOWN, ADDRESS OPAQUE: the cocycle's 2-adic valuation histogram over random
#      words matches the Bernoulli/geometric law 2^-(k+1) — the incompressible sector is
#      statistically transparent (law-determined) while pointwise unreadable.
from fractions import Fraction
from itertools import permutations
from math import comb, log2
import random
P = []
def check(name, ok):
    P.append(bool(ok)); print(("PASS " if ok else "FAIL ") + name)

def compose(word):
    # word over {'U','D'}: U: x -> 3x+1, D: x -> x/2 ; returns (a, S) with map x -> a x + S
    a, S = Fraction(1), Fraction(0)
    for c in word:
        if c == 'U':
            a, S = 3*a, 3*S + 1
        else:
            a, S = a/2, S/2
    return a, S

# (1) injectivity of order -> S at fixed abelian totals (K,C)
ok_all = True
for K, C in [(2, 3), (3, 4), (3, 6), (4, 4)]:
    words = set()
    base = 'U'*K + 'D'*C
    seen = {}
    n_dist = set()
    for perm in set(permutations(base)):
        a, S = compose(perm)
        n_dist.add(S)
    total = comb(K + C, K)
    ok = (len(n_dist) == total)
    ok_all = ok_all and ok
    print("  (K=%d, C=%d): orderings = %d, distinct S = %d  %s"
          % (K, C, total, len(n_dist), "ALL DISTINCT" if ok else "COLLISION"))
check("V1 the N-cocycle is a LOSSLESS encoding of the order at fixed abelian totals "
      "(injective on all tested (K,C); extends the record's 10/10 at K=3,C=6)", ok_all)

# (2) fraction of the path information carried by the anholonomy -> H2(K/n)
def H2(p):
    return 0.0 if p in (0, 1) else -p*log2(p) - (1-p)*log2(1-p)
print("  n     K/n    H(order)/n    H2(K/n)")
fracs = []
for n, K in [(20, 8), (60, 24), (200, 80), (1000, 400)]:
    h = log2(comb(n, K))/n
    fracs.append((h, H2(K/n)))
    print("  %4d  %.2f   %.4f        %.4f" % (n, K/n, h, H2(K/n)))
check("V2 H(order|totals)/n -> H2(K/n): the anholonomy asymptotically carries the whole "
      "per-symbol message (abelian totals carry O(log n / n) -> 0)",
      abs(fracs[-1][0] - fracs[-1][1]) < 0.01 and
      all(abs(a - b) >= abs(fracs[i+1][0] - fracs[i+1][1]) - 1e-12
          for i, (a, b) in enumerate(fracs[:-1])))

# (3) statistics of the incompressible sector: nu_2 of the integerized cocycle ~ geometric(1/2)
random.seed(5)
counts = {}
N = 20000
for _ in range(N):
    w = ''.join(random.choice('UD') for _ in range(24))
    a, S = compose(w)
    K = w.count('U'); C = w.count('D')
    Sint = S * 2**C            # clear denominators: integer cocycle
    num = int(Sint)
    if num == 0:
        continue
    k = 0
    while num % 2 == 0:
        num //= 2; k += 1
    counts[k] = counts.get(k, 0) + 1
tot = sum(counts.values())
print("  nu_2 histogram vs geometric 2^-(k+1):")
ok_geo = True
for k in range(5):
    emp = counts.get(k, 0)/tot
    thr = 2**-(k+1)
    print("   k=%d: empirical %.4f  vs  %.4f" % (k, emp, thr))
    ok_geo = ok_geo and abs(emp - thr) < 0.02
check("V3 nu_2(integer cocycle) matches the Bernoulli/geometric law to <0.02 over 20000 random "
      "words — the sector's STATISTICS are law-determined (transparent) even though its pointwise "
      "content is the whole difficulty", ok_geo)

print("\n%d/%d PASS" % (sum(P), len(P)))

# ---------- corrected forms: the failures above are recorded refutations of MY naive ensembles ----------
print("\n-- corrected ensembles --")
# V1b: admissible gap-form words U D^c1 U D^c2 ... U D^cK, c_j >= 1 (the record's ensemble: K=3,C=6 -> 10)
from itertools import combinations
def gap_words(K, C):
    # compositions of C into K parts >= 1
    for cuts in combinations(range(1, C), K - 1):
        parts = []
        prev = 0
        for c in cuts + (C,):
            parts.append(c - prev); prev = c
        yield 'U' + 'U'.join('D'*p for p in parts) if False else ''.join('U' + 'D'*p for p in parts)
ok_all = True
for K, C in [(3, 6), (3, 5), (4, 6), (4, 8)]:
    Svals = set()
    n_words = 0
    for w in gap_words(K, C):
        n_words += 1
        Svals.add(compose(w)[1])
    ok = (len(Svals) == n_words)
    ok_all = ok_all and ok
    print("  gap-form (K=%d, C=%d): words = %d, distinct S = %d  %s"
          % (K, C, n_words, len(Svals), "ALL DISTINCT" if ok else "COLLISION"))
check("V1b on the ADMISSIBLE (gap-form) ensemble the cocycle IS lossless (all distinct; reproduces "
      "the record's 10 at K=3,C=6) — losslessness is a property of the dynamics' grammar, not of "
      "the free algebra [the free-monoid collisions above are the coincidences admissibility kills]",
      ok_all)

# V3b: Terras uniformity — the CORRECT transparency statement. Accelerated map T(n) = (3n+1)/2 (odd),
# n/2 (even): the first-m parity vector is a BIJECTION of n mod 2^m.
def parity_vec(n, m):
    v = 0
    for i in range(m):
        if n % 2 == 1:
            v |= (1 << i); n = (3*n + 1)//2
        else:
            n //= 2
    return v
m = 12
vecs = {parity_vec(n, m) for n in range(2**m)}
check("V3b Terras bijection: first-%d parity vectors over n mod 2^%d are ALL 2^%d values — "
      "the anholonomy sector's statistics are EXACTLY uniform (law fully known; addresses opaque)"
      % (m, m, m), len(vecs) == 2**m)

print("\nfinal: %d/%d PASS (V1, V3 retained as recorded refutations of the naive forms)" % (sum(P), len(P)))
