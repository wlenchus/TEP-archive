#!/usr/bin/env python3
"""
AGM ribbon - addendum: makes "one prime suffices" quantitative at the computed tau.
At tau(-) = 1.57635974...i (|q| ~ 5e-5), the identity
    a_3 = (F(tau) - q) / q^3 + O(q^4)
determines a_3 to ~26 digits from ONE point value of the form.  This demonstrates
the check semantics the chain WOULD have -- and its circularity as recorded: the
only available producer of the number F(tau) is the form's own q-expansion
(ground-truth import).  No cascade-side evaluator exists in the records (Open #8
'unbuilt' is the record's own locator for the missing machinery).
"""
import mpmath as mp
mp.mp.dps = 60
phi = (1 + mp.sqrt(5))/2
I = mp.mpc(0, 1)
with open("tau_values.txt") as f:
    lines = f.read().split("\n")
taum = eval(lines[1], {"mpc": mp.mpc, "mpf": mp.mpf})

# rebuild F exactly as in 04 (import: ground truth)
ap = {2: mp.mpf(0), 5: mp.mpf(0), 3: -I/phi, 7: I, 11: I, 13: 1/phi, 17: mp.mpf(-1),
      19: I/phi, 23: mp.mpf(0), 29: mp.mpf(-1), 31: I*phi}
def chi(n):
    n = n % 4
    return 0 if n % 2 == 0 else (1 if n == 1 else -1)
import sympy
NMAX = 36
a = {1: mp.mpc(1)}
for n in range(2, NMAX+1):
    f = sympy.factorint(n)
    if len(f) == 1:
        p, k = list(f.items())[0]
        if p not in ap: a[n] = None; continue
        a[n] = ap[p] if k == 1 else (ap[p]**k if 4000 % p == 0 else ap[p]*a[p**(k-1)] - chi(p)*a[p**(k-2)])
    else:
        val = mp.mpc(1); good = True
        for p, k in f.items():
            c = a.get(p**k)
            if c is None: good = False; break
            val *= c
        a[n] = val if good else None

q = mp.e**(2*mp.pi*I*taum)
Fv = sum(a[n]*q**n for n in range(1, NMAX+1) if a.get(n) is not None)
a3_extracted = (Fv - q)/q**3
print("tau(-)        =", mp.nstr(taum, 40))
print("q             =", mp.nstr(q, 30))
print("F(tau)        =", mp.nstr(Fv, 30))
print("(F - q)/q^3   =", mp.nstr(a3_extracted, 30))
print("true a_3      =", mp.nstr(ap[3], 30))
print("|extracted - true a_3| =", mp.nstr(abs(a3_extracted - ap[3]), 8),
      "  (next-order term a_7 q^4 ~", mp.nstr(abs(I*q**4), 8), ")")
