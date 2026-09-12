"""LAMBDA RUN 1, part 3 — complete the zero census: deepen refinement (tol 1e-15)
on all 17 candidate minima, fine-scan the four wide gaps for the 17th zero.
2026-08-10, Claude (Fable 5), session B.

Companion to lambda_instrument_run1.py (instrument + ray-Fricke) and
lambda_zeros_run1.py (grid-independence, first scan, winding count).
Outcome of record: 18 zeros total, ALL on the critical line at rel depth <= 2.0e-15;
winding W = 17.000 over the box [-0.4,1.4] x [0.5,15] = the on-line census inside it;
the 17th/18th form a close pair (14.5349 / 14.5585, gap 0.0236) found only because the
winding surplus forced an edge-window hunt -- the census-vs-winding discipline working."""
import pickle, time
from mpmath import mp, mpf, mpc, sqrt, exp, pi, conj, fabs, log, nstr, arg, gamma

mp.dps = 28
N = 1951
with open('/home/claude/lam_cache.pkl','rb') as fh:
    C = pickle.load(fh)
nodes  = [mpf(x) for x in C['nodes']]
weights= [mpf(x) for x in C['weights']]
Hvec   = [mpc(a, b) for a, b in zip(C['Hre'], C['Him'])]
omega  = mpc(C['omega'])
sqrtyH = [sqrt(y)*h for y, h in zip(nodes, Hvec)]
sqrtyHc= [conj(v) for v in sqrtyH]
logy   = [log(y) for y in nodes]
def Q_up(s, cj=False):
    tot = mpc(0); sph = s + mpf('0.5')
    vec = sqrtyHc if cj else sqrtyH
    for ly, w, v in zip(logy, weights, vec):
        tot += w*v*exp(sph*ly)
    return tot
def Lam(s): return N**(s/2)*Q_up(s) + omega*N**((1-s)/2)*Q_up(1-s, cj=True)
half = mpf('0.5')
def mag(t): return fabs(Lam(mpc(half, t)))

# fine scan of the four wide gaps (step 0.01)
print("== gap scans (step 0.01) ==")
t0 = time.time()
gaps = [(1.71, 3.40), (4.01, 5.50), (10.31, 11.59), (13.34, 14.52)]
extra = []
for (ga, gb) in gaps:
    tt = ga
    vals = []
    while tt <= gb + 1e-9:
        vals.append((tt, float(mag(mpf(str(round(tt,4)))))))
        tt += 0.01
    for i in range(1, len(vals)-1):
        if vals[i][1] < vals[i-1][1] and vals[i][1] < vals[i+1][1]:
            sc = max(vals[max(0,i-3)][1], vals[min(len(vals)-1,i+3)][1])
            if vals[i][1] < 0.5*sc:
                extra.append(vals[i][0])
                print(f"   new candidate minimum in gap ({ga},{gb}): t ~ {vals[i][0]:.2f}"
                      f"  |Lam| = {vals[i][1]:.2e} (nbhd scale {sc:.2e})")
print(f"gap scans done [{time.time()-t0:.0f}s]")

cand = [0.4253, 1.6963, 3.4135, 3.9968, 5.5093, 6.1216, 6.8805, 7.4998,
        8.4185, 8.8951, 9.8087, 10.2992, 11.6030, 11.8747, 12.6285, 13.3238,
        14.5349] + extra
cand = sorted(cand)

def refine(tc):
    tl, tr = mpf(str(tc)) - mpf('0.02'), mpf(str(tc)) + mpf('0.02')
    for _ in range(90):
        tm1 = tl + (tr-tl)*mpf('0.381966'); tm2 = tl + (tr-tl)*mpf('0.618034')
        if mag(tm1) < mag(tm2): tr = tm2
        else: tl = tm1
        if tr - tl < mpf('1e-15'): break
    tz = (tl+tr)/2
    return tz, mag(tz)

print("\n== deep refinement (tol 1e-15) ==")
t0 = time.time()
rows = []
for tc in cand:
    tz, d = refine(tc)
    sc = mag(tz + mpf('0.05')) + mag(tz - mpf('0.05'))
    rows.append((tz, d, float(d/sc)))
print(f"[{time.time()-t0:.0f}s]")
print(f"{'t (zero ordinate)':>22s}  {'|Lambda|':>10s}  {'rel depth':>10s}")
nz_in_box = 0
for tz, d, rel in rows:
    onl = rel < 1e-13
    if onl and 0.5 < float(tz) < 15.0: nz_in_box += 1
    print(f"{nstr(tz, 14):>22s}  {float(d):10.1e}  {rel:10.1e}   "
          f"{'ZERO' if onl else 'not resolved as zero'}")
print(f"\nzeros resolved inside the winding box (0.5, 15): {nz_in_box}  "
      f"(winding said 17)")
print("full census (incl. below box): " +
      ", ".join(nstr(tz, 11) for tz, d, rel in rows if rel < 1e-13))
