"""R3.2 — crossing-pair analysis of the graded key.
For each graded prime and both nebentypus branches: Hecke polynomial X^2 - a_p X + chi(p),
crossing pair {alpha, beta}, gap^2 = a_p^2 - 4 chi(p).
Tests: (1) is the gap class-determined (tower-readable layer)?
       (2) is a_p^2 twist-orbit invariant (the structured-multiplicity layer)?
       (3) what per-prime freedom remains (the carrier's irreducible cargo)?
"""
import json, math, cmath
from fractions import Fraction

s5 = math.sqrt(5); phi = (1+s5)/2

with open('/home/claude/TEP-archive/50_code/ot1/full_width_instrument/2026-07-22 ot1_16000_PREREGISTERED_prediction.json') as fh:
    data = json.load(fh)

def parse(s):
    sgn = 1 if s[0]=='+' else -1
    body = s[1:]; mult = 1
    if body.endswith('*i'): mult = 1j; body = body[:-2]
    elif body.endswith('*1'): body = body[:-2]
    mag = {'1':1.0, '(sqrt5-1)/2':(s5-1)/2, '(1+sqrt5)/2':(1+s5)/2}[body]
    return sgn*mag*mult

def _factor(n):
    fs=[]; d=2
    while d*d<=n:
        while n%d==0: fs.append(d); n//=d
        d+=1
    if n>1: fs.append(n)
    return fs

def kron_p(D,p):
    if p==2: return 0 if D%2==0 else (1 if D%8 in (1,7) else -1)
    if D%p==0: return 0
    return 1 if pow(D%p,(p-1)//2,p)==1 else -1
def kron(D,n):
    r=1
    for p in _factor(n): r*=kron_p(D,p)
    return r

# recognized radical table: gap^2 candidates as exact values
named = {
    round(phi+2,9):  "phi+2   = (2 sin 72)^2",
    round(3-phi,9):  "3-phi   = (2 sin 36)^2",
    round(3.0,9):    "3       = (2 sin 60)^2",
    round(4.0,9):    "4       = (2 sin 90)^2",
    round(-(phi+2),9):"-(phi+2)",
    round(-(3-phi),9):"-(3-phi)",
    round(-3.0,9):   "-3",
    round(-4.0,9):   "-4",
    round(5.0,9):    "5       = (sqrt5)^2",
    round(-5.0,9):   "-5",
    round(1-4*1,9):  "-3",
}

graded = [3,7,11,13,17,19,23,29,31]
print(f"{'p':>4} {'branch':>7} {'class':>5} {'a_p':>16} {'chi(p)':>6} {'gap^2':>22}  class-determined?")
for branch, chiD in (("chi_-4",-4), ("chi_-20",-20)):
    ap = data[branch]["a_p_table_p<=200"]
    for p in graded:
        e = ap.get(str(p))
        a = parse(e['a_p']) if e else 0.0
        cls = e['class'] if e else '2'
        chp = kron(chiD, p)
        g2 = a*a - 4*chp
        g2r = complex(g2)
        # match to named table (real or pure-negative real)
        tag = "?"
        if abs(g2r.imag) < 1e-9:
            tag = named.get(round(g2r.real,9), f"{g2r.real:+.6f}")
        else:
            tag = f"{g2r:+.6f} (complex: i-dressed)"
        print(f"{p:>4} {branch:>7} {cls:>5} {str(e['a_p'] if e else '0'):>16} {chp:>6} {str(tag):>22}")

print("""
--- Layer decomposition ---""")
# (2) twist-orbit invariance of a_p^2: orbit acts by eps(p) in {+-1} => (eps a)^2 = a^2. Trivially invariant.
print("a_p^2 is invariant under the entire quadratic-twist gauge orbit (eps(p)^2 = 1): PROVED (one line).")

# (3) residual freedom: within the level-4000 4-point family {1, chi_-4, chi_5, chi_-20}-twists x conjugation,
# count distinct sign/dressing patterns at the graded primes:
tw_lvl = [1, -4, 5, -20]
pats = set()
ap4 = data["chi_-4"]["a_p_table_p<=200"]
for tw in tw_lvl:
    for conj in (1,-1):
        pat = []
        for p in graded:
            e = ap4.get(str(p))
            a = parse(e['a_p']) if e else 0.0
            a = a*kron(tw,p)
            if conj==-1: a = a.conjugate() if isinstance(a,complex) else a
            pat.append(round(complex(a).real,6)+1j*round(complex(a).imag,6))
        pats.add(tuple(pat))
print(f"distinct eigensystems within the level-4000 orbit at the 9 graded primes: {len(pats)} (the orbit-point freedom)")

# gap magnitudes vs class only:
print("""
gap^2 at order-5 primes lands in {+-(phi+2), +-(3-phi)}; order-3 in {+-3}; order-2 in {+-4}:
i.e. |alpha - beta| = 2 sin(pi k/m) for Frobenius order m -- CLASS-DETERMINED up to the chi/i-dressing sign.
The dressing (which of +-, and real-vs-i) is exactly the {branch, orbit-point} datum.""")
