"""EXACT-EPSILON — integer-exact Gauss/Jacobi certificate + identification of the
Fricke root number at Doud-1951, with a zero-freedom out-of-sample test at Doud-2141.
2026-08-09 (session B), Claude (Fable 5).

PREDICTIONS (stated before run; same-session, unhashed — disclosed as such):
  E-a  Each CSV's j5 column is EXACTLY one order-5 residue character:
       chi(x) = iota(x^((N-1)/5) mod N), iota pinned by the p=2 row alone;
       consistency across all 9,591 remaining rows, both fields.
  E-b  For exactly one s in {+1,-1} (tau(chi) vs tau(chibar)) the ratio
       eps*sqrt(N)/tau_s lands on a 20th root of unity to <= 3e-9, where
       eps = -const and const is the certified 11-digit Fricke constant at 1951
       (-0.88509639889 + 0.46540774024i). Second-best candidate separated by >= 0.1.
  E-c  (deferred to exact_epsilon_confirm.py) the identified algebraic candidate
       matches a fresh dps-40 Fricke measurement to <= 1e-28.
  E-d  The SAME structural formula (same s; unit expressed through the field's own
       a_N as unit = zeta20^k0 * a_N^e for some fixed e in {0,+1,-1}), applied
       verbatim at 2141 with its own CSV-pinned chi and a_N = zeta10^8, reproduces
       the parallel session's measured const -0.00271583114 + 0.99999631212i to
       <= 1e-8.  Zero adjustable choices: 2141's measurement is never consulted
       until the comparison line.
Kill: no candidate within 3e-9 at 1951 -> report as-is, no exact-eps claim, E-d void.
Integer part is exact (python ints only); floats enter only for tau and comparisons.

AMENDMENT (post-run, disclosed): run 1 measured best = 4.524e-12 (identification
clause PASS) but the E-b second-best clause (>= 0.1) was mis-calibrated: with 40
candidate points on the unit circle the runner-up landed at 2.571e-2 — still 9.7
orders above the best. E-b is graded PASS on the identification clause and FAIL as
literally stated; the kill condition ("no candidate within 3e-9") did not trigger,
so E-d runs. The gate below now requires best <= 3e-9 AND second >= 1e6*best.
Run 1 also refuted the mu20 guess for local roots: |a_p| = 1 classes (group-element
orders 3 and 6) carry cube roots of unity — the correct closure is mu60; the check
below now measures exact multiplicative orders and asserts they divide 60."""
import csv
from mpmath import mp, mpf, mpc, exp, pi, sqrt, conj, fabs

mp.dps = 45
CSV = {
 1951: "/root/.claude/projects/-home-claude/e1c6a220-faa1-5bd1-9d10-c0c3344b96cd/tool-results/project-doc-b99b6076-631d-43e3-92a2-b1e8923dc0c4.txt",
 2141: "/root/.claude/projects/-home-claude/e1c6a220-faa1-5bd1-9d10-c0c3344b96cd/tool-results/project-doc-70dab881-3783-468e-aa79-e35a5252de13.txt"}
CONST = {1951: mpc('-0.88509639889', '0.46540774024'),
         2141: mpc('-0.00271583114', '0.99999631212')}   # certified Fricke constants (theirs)
ANEXP = {}    # a_N = zeta10^m, read from CSV ramified row

# ---------- exact Z[zeta5] arithmetic: basis (1, z, z^2, z^3), z^4 = -(1+z+z^2+z^3)
def zred(c7):
    c = list(c7) + [0]*(7-len(c7))
    for k in (5, 6): c[k-5] += c[k]; c[k] = 0
    t = c[4]
    return [c[0]-t, c[1]-t, c[2]-t, c[3]-t]
def zmul(a, b):
    c = [0]*7
    for i in range(4):
        for j in range(4): c[i+j] += a[i]*b[j]
    return zred(c)
def zconj(a):   # z -> z^-1 = z^4: exponent m -> -m mod 5
    c = [0]*7; expmap = {0:0, 1:4, 2:3, 3:2}
    for m in range(4): c[expmap[m]] += a[m]
    return zred(c)
def zscal(s, a): return [s*x for x in a]
def zeval(a):   # float value at zeta5 = e^(2 pi i/5)
    z = exp(mpc(0, 2)*pi/5)
    return a[0] + a[1]*z + a[2]*z**2 + a[3]*z**3
def vec_from_counts(n):  # sum n_m zeta^m -> basis vector
    return [n[0]-n[4], n[1]-n[4], n[2]-n[4], n[3]-n[4]]

def zeta20(k): return exp(mpc(0, 2)*pi*k/20)

field = {}
for N in (1951, 2141):
    print(f"\n================ N = {N} ================")
    j5 = {}
    with open(CSV[N]) as f:
        for row in csv.DictReader(f):
            p = int(row['p'])
            if row['j5'].strip() == '-':
                s = row['a_p_exact'].strip(); assert s.startswith('zeta10^')
                ANEXP[N] = int(s[7:]); continue
            j5[p] = int(row['j5'])
    e5 = (N-1)//5
    # pin iota by p=2 alone
    t0 = pow(2, e5, N); j0 = j5[2]
    mu5 = {}; iota = {}
    for k in range(5):
        elt = pow(t0, k, N)
        assert elt not in iota, "t0 does not generate mu5"
        iota[elt] = (k*j0) % 5
    assert len(iota) == 5
    # jarr for all residues
    jarr = [None]*N
    for x in range(1, N):
        jarr[x] = iota[pow(x, e5, N)]
    # E-a: full-table verification
    mism = [p for p, j in j5.items() if jarr[p % N] != j]
    print(f"E-a: chi := order-5 character with chi(2) = zeta5^{j0}; "
          f"verified {len(j5)-len(mism)}/{len(j5)} CSV rows"
          + ("" if not mism else f"  MISMATCH at {mism[:10]}"))
    print(f"     chi(-1) = zeta5^{jarr[N-1]} (must be 0: even character); a_N = zeta10^{ANEXP[N]}")
    # exact Jacobi sums
    Js = []
    for (a, b) in [(1,1), (1,2), (1,3)]:
        n = [0]*5
        for x in range(2, N):
            n[(a*jarr[x] + b*jarr[(1-x) % N]) % 5] += 1
        J = vec_from_counts(n); Js.append(J)
        nrm = zmul(J, zconj(J))
        print(f"     J(chi^{a},chi^{b}) = {J}   |J|^2 = {nrm}  "
              + ("OK(=N)" if nrm == [N,0,0,0] else "NORM FAIL"))
    tau5 = zscal(N, zmul(zmul(Js[0], Js[1]), Js[2]))
    print(f"     tau(chi)^5 = N*J1*J2*J3 = {tau5}   (exact, Z[zeta5])")
    # float tau + cross-check
    z5 = exp(mpc(0,2)*pi/5); eN = exp(mpc(0,2)*pi/N)
    tau = mpc(0)
    for x in range(1, N):
        tau += z5**jarr[x] * eN**x
    print(f"     float tau = {complex(tau):.6f};  ||tau|^2 - N| = {float(fabs(abs(tau)**2 - N)):.2e}")
    dev = fabs(tau**5 - zeval(tau5))/fabs(tau**5)
    print(f"     cross-check tau^5 float vs exact vector: rel dev = {float(dev):.2e}")
    field[N] = dict(tau=tau, jarr=jarr, tau5=tau5)

# ---------- E-b: candidate identification at 1951
print("\n================ E-b: identification at 1951 ================")
N = 1951; tau = field[N]['tau']
eps_meas = -CONST[N]
cands = []
for s, ts, lab in [(1, tau, "tau(chi)"), (-1, conj(tau), "tau(chibar)")]:
    r = eps_meas*sqrt(N)/ts
    for k in range(20):
        cands.append((float(fabs(r - zeta20(k))), s, k, lab))
cands.sort()
best, second = cands[0], cands[1]
print(f"best:   eps = zeta20^{best[2]} * {best[3]} / sqrt(N)   dist = {best[0]:.3e}")
print(f"second: eps = zeta20^{second[2]} * {second[3]} / sqrt(N) dist = {second[0]:.3e}")
ok_Eb = best[0] <= 3e-9 and second[0] >= 1e6*best[0]
print(f"E-b (as literally stated, second >= 0.1): {'PASS' if best[0] <= 3e-9 and second[0] >= 0.1 else 'FAIL'}")
print(f"E-b (identification clause + amended separation, second/best = {second[0]/best[0]:.1e}): "
      f"{'PASS' if ok_Eb else 'FAIL/KILL'}")

if ok_Eb:
    s1, k1 = best[1], best[2]
    m1 = ANEXP[1951]           # a_N = zeta10^m1 = zeta20^(2 m1)
    print(f"\nunit structure at 1951: unit = zeta20^{k1}; a_N = zeta20^{2*m1}")
    for e in (0, 1, -1):
        k0 = (k1 - e*2*m1) % 20
        print(f"   e={e:+d}:  unit = zeta20^{k0} * a_N^{e}")
    # cleanest direct form: const = -eps ?= tau/(sqrt(N)*a_N)  (Atkin-Li shape, no sign)
    dAL = float(fabs(CONST[1951] - tau/(sqrt(N)*exp(mpc(0,1)*pi*m1/5))))
    print(f"   direct check: |const_meas - tau(chi)/(sqrt(N)*a_N)| = {dAL:.3e}")
    # ---------- E-d: verbatim transfer to 2141
    print("\n================ E-d: out-of-sample at 2141 (zero freedoms) ================")
    N2 = 2141; tau2 = field[N2]['tau']; m2 = ANEXP[N2]
    t2 = tau2 if s1 == 1 else conj(tau2)
    eps2_meas = -CONST[N2]
    verdicts = []
    for e in (0, 1, -1):
        k0 = (k1 - e*2*m1) % 20
        pred = zeta20((k0 + e*2*m2) % 20) * t2 / sqrt(N2)
        d = float(fabs(pred - eps2_meas))
        verdicts.append((d, e, k0, complex(pred)))
        print(f"   e={e:+d} (unit = zeta20^{k0}*a_N^{e}):  predicted eps = {complex(pred):.9f}   "
              f"|pred - eps_meas| = {d:.3e}   {'PASS' if d <= 1e-8 else 'no'}")
    hits = [v for v in verdicts if v[0] <= 1e-8]
    print("E-d:", f"PASS with e={hits[0][1]:+d}" if len(hits) == 1 else
          ("MULTIPLE-PASS (underdetermined)" if hits else "FAIL"))

# ---------- Theorem-A support: local roots are in mu20 (per (a_p, chi_p) class)
print("\n================ local Frobenius roots: unit-circle / mu20 check (1951) ================")
import re
phi_f = (1 + sqrt(5))/2
def parse_apex(sst):
    sst = sst.strip()
    if sst == "0": return mpc(0)
    sg = mpf(1)
    if sst[0] == '+': sst = sst[1:]
    elif sst[0] == '-': sg = mpf(-1); sst = sst[1:]
    fac = mpf(1)
    if sst.endswith("*1/phi"): fac = 1/phi_f; sst = sst[:-6]
    elif sst.endswith("*phi"): fac = phi_f; sst = sst[:-4]
    elif sst.endswith("*2"): fac = mpf(2); sst = sst[:-2]
    assert sst.startswith("zeta10^"), sst
    return sg * fac * exp(mpc(0,1)*pi*int(sst[7:])/5)
classes = set()
with open(CSV[1951]) as f:
    for row in csv.DictReader(f):
        if row['j5'].strip() == '-': continue
        classes.add((row['a_p_exact'].strip(), row['chi_p_exact'].strip()))
worst_abs = 0.0; worst_mu60 = 0.0; orders = set()
divs60 = [d for d in range(1, 61) if 60 % d == 0]
for (astr, cstr) in sorted(classes):
    a = parse_apex(astr)
    c = exp(mpc(0,2)*pi*int(cstr[6:])/5)
    disc = (a*a - 4*c)**mpf('0.5')
    for r in ((a+disc)/2, (a-disc)/2):
        worst_abs = max(worst_abs, float(fabs(abs(r)-1)))
        worst_mu60 = max(worst_mu60, float(fabs(r**60 - 1)))
        o = next((d for d in divs60 if fabs(r**d - 1) < mpf('1e-20')), None)
        assert o is not None, f"root of class {astr},{cstr} not in mu60"
        orders.add(o)
print(f"{len(classes)} distinct (a_p, chi_p) classes; worst ||root|-1| = {worst_abs:.2e}; "
      f"worst |root^60 - 1| = {worst_mu60:.2e}")
print(f"exact multiplicative orders observed: {sorted(orders)}  (all divide 60)")
print("=> every local Frobenius root is a 60th root of unity; |c_n| <= d(n) follows")
