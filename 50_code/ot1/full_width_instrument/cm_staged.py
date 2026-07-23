"""Staged CM read at depth 2800, per the corpus's recoverability principle
(A4 Addendum1: solvable => two-read recovery; read the abelian quotient first).
After the flat solve, compute PINNED coordinates (fixed across the entire
solution space) and check pinned singleton signs against the independent
genus character. Benign gauge = singletons pinned, composites floating."""
import sys, time, numpy as np
sys.path.insert(0,'/home/claude/ot1_16000')
import decoder as D, decoder2 as D2
from fractions import Fraction

DEPTH = 2800; NCOL = DEPTH+1; P = 1000003
def fast_E1(chiD, depth):
    m = abs(chiD)
    B1 = Fraction(sum(D.kron(chiD,a)*a for a in range(1,m)), m)
    c = [0]*depth
    for d in range(1, depth):
        cd = D.kron(chiD, d)
        if cd:
            for n in range(d, depth, d): c[n] += cd
    return [-B1/2] + [Fraction(x) for x in c[1:]]
D.DEPTH = DEPTH; D.E1_series = lambda chiD: fast_E1(chiD, DEPTH)

def genus(p):
    y = 0
    while 5*y*y <= p:
        r = p - 5*y*y; x = int(r**0.5)
        for xx in (x-1,x,x+1):
            if xx>=0 and xx*xx==r: return +1
        y += 1
    return -1

host = np.zeros((2321, NCOL), dtype=np.int64)
for i, line in enumerate(open('host16000_local.csv')):
    parts = line.rstrip('\n').split(',')[:NCOL]
    for j, t in enumerate(parts):
        if t != '0': host[i,j] = int(t) % P
print("host loaded", host.shape)

# flat solve pieces (mirrors decoder2.run but keeps the augmented system)
pd = D2.pdata_cm20(DEPTH)
F = D2.build_f2(pd, -20, 0, DEPTH, {2: D.ONE, 5: D.ONE})
E = D.E1_series(-20)[:DEPTH]
Emod = np.array([(int(e.numerator)%P)*pow(int(e.denominator)%P, P-2, P)%P for e in E], dtype=np.int64)
blocks = {}
for m_, d in F.items():
    if m_ > DEPTH: continue
    for T, v in d.items():
        for c in range(4):
            x = v[c]
            if x == 0: continue
            if T not in blocks: blocks[T] = np.zeros((4, NCOL), dtype=np.int64)
            xm = (int(x.numerator)%P)*pow(int(x.denominator)%P, P-2, P)%P
            L = min(len(E), NCOL-m_)
            blocks[T][c, m_:m_+L] = (blocks[T][c, m_:m_+L] + xm*Emod[:L]) % P
t0=time.time(); red, hrank = D2.make_reducer.__wrapped__(host, P) if hasattr(D2.make_reducer,'__wrapped__') else D2.make_reducer(host, P)
print(f"reducer: rank={hrank} ({time.time()-t0:.0f}s), codim={NCOL-hrank}")
Ts=[]; cols=[]; b=None
for T, arr in blocks.items():
    flat = np.concatenate([red(arr[c]) for c in range(4)])
    if T == frozenset(): b = (-flat) % P
    else: Ts.append(T); cols.append(flat)
A = np.stack(cols, axis=1) % P
Aug = np.concatenate([A, b.reshape(-1,1)], axis=1)
R, piv = D2.rref_modp(Aug, P)
nT = len(Ts)
print(f"monomials={nT}, constraint rows={A.shape[0]}, aug rank={len(piv)}, inconsistent={nT in piv}")
if nT not in piv:
    free = [c for c in range(nT) if c not in piv]
    print(f"free={len(free)}")
    # nullspace basis; pinned coordinate = zero in every null vector
    pinned = np.ones(nT, dtype=bool)
    for fcol in free:
        v = np.zeros(nT, dtype=np.int64); v[fcol] = 1
        for i,c in enumerate(piv): v[c] = (-R[i,fcol]) % P
        pinned &= (v == 0)
    sol = np.zeros(nT, dtype=np.int64)
    for i,c in enumerate(piv): sol[c] = R[i,nT]
    sing = [(k, next(iter(Ts[k]))) for k in range(nT) if len(Ts[k])==1]
    pinned_sing = [(q, int(sol[k])) for k,q in sing if pinned[k]]
    print(f"singletons={len(sing)}, PINNED singletons={len(pinned_sing)}")
    ok = bad = notpm = 0
    for q, v in pinned_sing:
        if v not in (1, P-1): notpm += 1; continue
        s = 1 if v==1 else -1
        if q in (2,5): print(f"  ram a_{q} pinned sign = {s} (record: a2=-1, a5=+1)"); continue
        if s == genus(q): ok += 1
        else: bad += 1
    print(f"pinned split-prime signs vs independent genus character: {ok} match, {bad} mismatch, {notpm} non-pm")
    # ---- invariant-sector read (down-flow resolvent recovery + global integration) ----
    # per 06-29 M / 07-15 faces_seam 5: what per-prime (abelian) reads scramble may be
    # pinned in the gauge-invariant sector: composite monomials mu_T = prod s_p and their
    # multiplicative-consistency 'loops'. A pinned mu_T outside {±1} or a pinned loop
    # violation is a REJECT certificate even at large free-dim.
    comp = [(k, Ts[k]) for k in range(nT) if len(Ts[k]) > 1]
    pinned_comp = [(T, int(sol[k])) for k, T in comp if pinned[k]]
    non_pm_comp = [(T, v) for T, v in pinned_comp if v not in (1, P-1)]
    print(f"composite monomials={len(comp)}, PINNED composites={len(pinned_comp)}, pinned-non-pm={len(non_pm_comp)}")
    if non_pm_comp[:5]: print("  sample non-pm pinned composites:", [(sorted(T), v) for T, v in non_pm_comp[:5]])
    # loop consistency: where {p},{q},{p,q} all pinned, check mu_pq = s_p s_q
    sing_pin = {q: int(sol[k]) for k, q in sing if pinned[k]}
    loops_ok = loops_bad = 0
    for T, v in pinned_comp:
        Tl = sorted(T)
        if len(Tl) == 2 and all(q in sing_pin for q in Tl):
            prod = (sing_pin[Tl[0]] * sing_pin[Tl[1]]) % P
            if prod == v: loops_ok += 1
            else: loops_bad += 1
    print(f"pinned 2-loops (mu_pq vs s_p*s_q): {loops_ok} consistent, {loops_bad} violated")
    verdict_bad = bad or notpm or non_pm_comp or loops_bad
    print("STAGED READ:", "REJECT CERTIFICATE in invariant sector" if (non_pm_comp or loops_bad) else
          ("gauge BENIGN — invariant sector recovered, consistent" if not verdict_bad and (len(pinned_sing)+len(pinned_comp))>10
           else "indeterminate — invariant sector too thin; escalate to AL-sector projection"))
