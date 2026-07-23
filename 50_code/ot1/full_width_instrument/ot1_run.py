"""OT1 N=16000 independent replication runner — 2026-07-21, Claude (Fable 5), Cowork.

Pipeline (mirrors the corpus's validated final_run8000 pattern, reconstructed
from the 07-04/07-05 records' API descriptions):
  1. Load host CSV (mine: PARI mfinit([16000,2],1) built in this container;
     cross-checked against the head of Will's 2026-07-08 host16000.csv).
  2. CM true-positive control: Q(sqrt(-5)) weight-1 CM form, level 20 | 16000,
     chi_{-20}, ram={2,5} sign-bit unknowns -> expect PASS; decoded genus
     character independently validated against x^2+5y^2 representability.
  3. Icosahedral sweep: pdata_quintic, chi in {-4,-8,-20,-40} x emb {0,1},
     ram={2:None,5:None} -> corpus reports REJECT x8 (a2 >= 8 consequence).
  4. Any non-REJECT re-checked at a second prime.
"""
import sys, time, json
import numpy as np
from fractions import Fraction
sys.path.insert(0, '/home/claude/ot1_16000')
import decoder as D
import decoder2 as D2

DEPTH = 2700          # > rank(2321) + 300 surplus, per the handoff rule
NCOL  = DEPTH + 1
P1, P2 = 1000003, 999983

# ---- fast E1 (sieve; v1's O(n^2) divisor scan is too slow at depth 2700) ----
def fast_E1(chiD, depth):
    m = abs(chiD)
    B1 = Fraction(sum(D.kron(chiD, a) * a for a in range(1, m)), m)
    coef = [0] * depth
    for d in range(1, depth):
        cd = D.kron(chiD, d)
        if cd:
            for n in range(d, depth, d):
                coef[n] += cd
    out = [-B1 / 2] + [Fraction(c) for c in coef[1:]]
    return out

def selftest_E1():
    D.DEPTH = 120
    for chiD in (-4, -8, -20, -40):
        slow = D.E1_series(chiD)
        fast = fast_E1(chiD, 120)
        assert slow == fast, f"E1 mismatch chi={chiD}"
    print("[selftest] fast_E1 == v1 E1_series at depth 120 for all four chi")

# ---- reducer cache (records: "validated runner, reducer-cached") ----
_red_cache = {}
_orig_make_reducer = D2.make_reducer
def cached_make_reducer(host, p):
    key = (id(host), p)
    if key not in _red_cache:
        t0 = time.time()
        _red_cache[key] = _orig_make_reducer(host, p)
        print(f"[reducer] built for p={p} in {time.time()-t0:.1f}s, rank={_red_cache[key][1]}")
    return _red_cache[key]
D2.make_reducer = cached_make_reducer

def load_host(path, p, ncol):
    rows = []
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            rows.append(line.split(','))
    M = np.zeros((len(rows), ncol), dtype=np.int64)
    for i, parts in enumerate(rows):
        for j in range(min(ncol, len(parts))):
            t = parts[j]
            if t == '0':
                continue
            if '/' in t:
                a, b = t.split('/')
                M[i, j] = (int(a) % p) * pow(int(b) % p, p - 2, p) % p
            else:
                M[i, j] = int(t) % p
    return M

def genus_char_indep(p):
    """+1 iff p = x^2 + 5y^2 (principal), -1 iff 2x^2+2xy+3y^2 class. Independent of decoder."""
    y = 0
    while 5 * y * y <= p:
        r = p - 5 * y * y
        x = int(r ** 0.5)
        for xx in (x - 1, x, x + 1):
            if xx >= 0 and xx * xx == r:
                return +1
        y += 1
    return -1

def cm_control(host, p):
    print(f"\n=== CM CONTROL (chi_-20, level 20 | 16000) at p={p} ===")
    D.DEPTH = DEPTH
    D.E1_series = lambda chiD: fast_E1(chiD, DEPTH)
    t0 = time.time()
    res = D2.run(host, D2.pdata_cm20(DEPTH), -20, 0, DEPTH, {2: D.ONE, 5: D.ONE}, p)
    print(f"[cm] status={res.get('status')} free={res.get('free')} ({time.time()-t0:.1f}s)")
    if res.get('status') == 'PASS':
        signs = res['signs']
        print(f"[cm] decoded a_2 sign = {signs.get(2)}, a_5 sign = {signs.get(5)} (record: -1, +1)")
        split = sorted(q for q in signs if q not in (2, 5))
        bad = [q for q in split if signs[q] != genus_char_indep(q)]
        conj = [q for q in split if signs[q] != -genus_char_indep(q)]
        exact = len(split) - len(bad)
        print(f"[cm] genus-character check on {len(split)} split primes: "
              f"{exact} exact matches; {len(split)-len(conj)} matches under global flip")
        ok = (len(bad) == 0) or (len(conj) == 0)  # conjugation gauge allows a global flip
        print(f"[cm] VERDICT: {'PASS - instrument validated on this host' if ok else 'MISMATCH - investigate'}")
        return ok
    print("[cm] VERDICT: control did not PASS - host or pipeline fault; halt before sweep")
    return False

def sweep(host, p):
    print(f"\n=== ICOSAHEDRAL SWEEP x^5+20x+16 at p={p}, depth={DEPTH} ===")
    D.DEPTH = DEPTH
    D.E1_series = lambda chiD: fast_E1(chiD, DEPTH)
    t0 = time.time()
    pd = D2.pdata_quintic(DEPTH)
    from collections import Counter
    print(f"[pdata] census: {Counter(c for c,_ in pd.values())} ({time.time()-t0:.1f}s)")
    results = {}
    for chiD in (-4, -8, -20, -40):
        for emb in (0, 1):
            t1 = time.time()
            res = D2.run(host, pd, chiD, emb, DEPTH, {2: None, 5: None}, p)
            results[(chiD, emb)] = res.get('status')
            print(f"[sweep] chi={chiD:+d} emb={emb}: {res.get('status')} "
                  f"(rank={res.get('rank','-')}, free={res.get('free','-')}) {time.time()-t1:.1f}s")
    return results

def main():
    selftest_E1()
    host_path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/ot1_16000/host16000_local.csv'
    print(f"loading host {host_path} at p={P1} ...")
    t0 = time.time()
    host = load_host(host_path, P1, NCOL)
    print(f"host: {host.shape[0]} rows x {host.shape[1]} cols ({time.time()-t0:.1f}s)")
    if host.shape[0] != 2321:
        print(f"WARNING: expected 2321 rows (dim S2(G0(16000)) cuspidal), got {host.shape[0]}")
    if not cm_control(host, P1):
        print("HALT: CM control failed; sweep results would be uninterpretable.")
        return
    results = sweep(host, P1)
    nonreject = [k for k, v in results.items() if v != 'REJECT']
    if nonreject:
        print(f"\nnon-REJECT configs {nonreject} -> re-checking at second prime {P2}")
        host2 = load_host(host_path, P2, NCOL)
        if cm_control(host2, P2):
            for (chiD, emb) in nonreject:
                res = D2.run(host2, D2.pdata_quintic(DEPTH), chiD, emb, DEPTH, {2: None, 5: None}, P2)
                print(f"[p2] chi={chiD:+d} emb={emb}: {res.get('status')}")
    verdict = 'REJECT x8 - replicates the corpus exclusion; a2>=8 ladder consequence stands' \
        if not nonreject else f'NON-REJECT at {nonreject} - DIVERGES from corpus report'
    print(f"\n==== OT1 N=16000 REPLICATION VERDICT: {verdict} ====")
    json.dump({str(k): v for k, v in results.items()},
              open('/home/claude/ot1_16000/sweep_results.json', 'w'), indent=1)

if __name__ == '__main__':
    main()
