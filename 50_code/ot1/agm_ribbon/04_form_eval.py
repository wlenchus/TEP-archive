#!/usr/bin/env python3
"""
AGM ribbon - LINKS 4-5 (GAP as recorded; reviewer interpolations, explicitly labeled).
Record sentence (06-29 Open #2): "... -> tau -> evaluate the candidate weight-1 form
-> check its a_p against the golden cascade-Frobenius sequence (one prime suffices)".

GAP documentation executed here:
 (G4a) The chain supplies no q-expansion for "the candidate weight-1 form"; the
       coefficients below are the 07-22/LMFDB GROUND TRUTH (4000.1.b.a, embedding
       nu = i*phi) -- an import, labeled as such. (Machine-computed evaluation;
       operator knows the target; the evaluation itself is contamination-robust.)
 (G4b) tau from j-inversion is defined only mod PSL(2,Z); a level-4000 weight-1 form
       is not PSL(2,Z)-invariant.  We evaluate F at tau and at Gamma(1)-translates
       to demonstrate the value is representative-dependent (not a function of the
       chain's data as recorded).
 (G5)  No recorded procedure extracts a_p from a point value; we print the values
       and (compute-then-grade) scan them for golden structure afterwards.
"""
import mpmath as mp
mp.mp.dps = 60

phi = (1 + mp.sqrt(5))/2
I = mp.mpc(0, 1)

# ground-truth a_p for 4000.1.b.a at nu = i*phi  [IMPORT: 07-22 record / LMFDB]
ap = {2: mp.mpf(0), 5: mp.mpf(0),
      3: -I/phi, 7: I, 11: I, 13: 1/phi, 17: mp.mpf(-1), 19: I/phi,
      23: mp.mpf(0), 29: mp.mpf(-1), 31: I*phi}
def chi(n):  # chi_{-4}
    n = n % 4
    return 0 if n % 2 == 0 else (1 if n == 1 else -1)

NMAX = 36
a = {1: mp.mpc(1)}
import sympy
for n in range(2, NMAX+1):
    f = sympy.factorint(n)
    if len(f) == 1:
        p, k = list(f.items())[0]
        if p not in ap:
            a[n] = None; continue
        if k == 1:
            a[n] = ap[p]
        else:
            if 4000 % p == 0:
                a[n] = ap[p]**k
            else:
                am1 = a[p**(k-1)]; am2 = a[p**(k-2)]
                a[n] = ap[p]*am1 - chi(p)*am2 if (am1 is not None and am2 is not None) else None
    else:
        val = mp.mpc(1); good = True
        for p, k in f.items():
            c = a.get(p**k)
            if c is None: good = False; break
            val *= c
        a[n] = val if good else None

print("q-expansion coefficients a_n (n<=%d), embedding nu=i*phi [GROUND-TRUTH IMPORT]:" % NMAX)
for n in range(1, NMAX+1):
    if a.get(n) is not None and abs(a[n]) > 1e-50:
        print("  a_%d = %s" % (n, mp.nstr(a[n], 12)))

def F(tau):
    q = mp.e**(2*mp.pi*I*tau)
    s = mp.mpc(0)
    for n in range(1, NMAX+1):
        if a.get(n) is not None:
            s += a[n]*q**n
    return s

taus = {}
with open("tau_values.txt") as f:
    lines = f.read().split("\n")
taup = eval(lines[0], {"mpc": mp.mpc, "mpf": mp.mpf})
taum = eval(lines[1], {"mpc": mp.mpc, "mpf": mp.mpf})

print("\n== (G4b) Evaluation of F at tau and PSL(2,Z)-translates ==")
for name, tau in [("tau(+)", taup), ("tau(-)", taum)]:
    print(f"--- {name} = {mp.nstr(tau, 30)} ---")
    tr = {"tau": tau, "tau+1": tau+1, "-1/tau": -1/tau, "tau+2": tau+2,
          "(tau)/(tau+1)... rep": tau/(tau+1)}
    for lab, t in tr.items():
        if mp.im(t) <= 0: continue
        v = F(t)
        print(f"   F({lab:>18s}) = {mp.nstr(v, 25)}   |F| = {mp.nstr(abs(v), 18)}")
    # reviewer exploration: 5-isogeny-adjacent points (Open #8 territory), labeled
    for lab, t in [("5*tau", 5*tau), ("tau/5", tau/5)]:
        if mp.im(t) <= 0: continue
        v = F(t)
        print(f"   F({lab:>18s}) = {mp.nstr(v, 25)}   |F| = {mp.nstr(abs(v), 18)}  [exploration]")

print("\n== (G5) Post-print scan (grading happens in the report, not here) ==")
print("golden reference magnitudes: phi =", mp.nstr(phi, 25), " 1/phi =", mp.nstr(1/phi, 25))
print("|a_3| =", mp.nstr(abs(ap[3]), 25), " (= 1/phi, ground truth)")
