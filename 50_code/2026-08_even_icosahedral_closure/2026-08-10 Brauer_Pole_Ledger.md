"""BRAUER POLE LEDGER — exact monomial resolution of the 2-dimensional character

of 2.A5 \= SL(2,5), entirely in Q(sqrt5) integer/rational arithmetic (no floats).

2026-08-10, Claude (Fable 5), session B.

&nbsp;

Purpose: make the pole obstruction for strong Artin at Doud-1951 explicit.

By Brauer, theta2 (the faithful 2-dim character, \= our rho0 before the

nu-twist) is a Z-combination of characters induced from LINEAR characters of

subgroups; each such induced piece is a Hecke L-function of the corresponding

fixed field (solvable/monomial \=\> automorphic, entire by Hecke). Negative

coefficients form the DENOMINATOR: the only possible pole locations of

L(rho,s) are zeros of those named abelian L-functions.

&nbsp;

EXPECTATION (stated before run; a computation of a fixed algebraic fact, not a

graded experiment): a |n|\<=1 solution over inductions from C10, C6, C4 with

dimension bookkeeping 12 \+ 20 \- 30 \= 2; C2 and Q8 not needed (Q8 has no linear

character with lambda(z) \= \-1, so it cannot appear for a faithful character).

Kill: if no solution with |n\_i| \<= 3 exists over {C10, C6, C4, C2}, report

as-is and widen the subgroup set.

&nbsp;

Self-validation: the hardcoded character table is verified by full first

orthogonality (all 45 pairs, exact); induction multiplicities must be

non-negative integers; the winning combination is re-verified as a class

function on all 9 classes exactly.

&nbsp;

AMENDMENT (post-run-1, disclosed): the C6 cosine table evaluated cos(2pi\*jk/3)

instead of cos(pi\*jk/3); the built-in kill caught it (an all-zero C6 row is

impossible for a z-odd induction: total induced dimension 20 must land in the

faithful irreps). One-line fix; nothing else changed; run 2 found the expected

minimal identity and verified it exactly."""

from fractions import Fraction as Fr

from itertools import product

&nbsp;

\# \---------- exact Q(sqrt5): x \= (a, b) means a \+ b\*sqrt5

def q5(a, b=0): return (Fr(a), Fr(b))

def add(x, y): return (x\[0\]+y\[0\], x\[1\]+y\[1\])

def sub(x, y): return (x\[0\]-y\[0\], x\[1\]-y\[1\])

def mul(x, y): return (x\[0\]\*y\[0\] \+ 5\*x\[1\]\*y\[1\], x\[0\]\*y\[1\] \+ x\[1\]\*y\[0\])

def smul(s, x): return (s\*x\[0\], s\*x\[1\])

ZERO, ONE \= q5(0), q5(1)

PHI  \= q5(Fr(1,2), Fr(1,2))          \# golden ratio

PHM1 \= sub(PHI, ONE)                  \# 1/phi \= phi \- 1

NPHI, PHIP \= smul(-1, PHI), sub(ONE, PHI)   \# \-phi ; phi' \= 1 \- phi \= \-1/phi

&nbsp;

\# cos(pi\*t/5), t mod 10  (exact in Q(sqrt5))

C5T \= {0: ONE, 1: smul(Fr(1,2), PHI), 2: smul(Fr(1,2), PHM1),

       3: smul(-Fr(1,2), PHM1), 4: smul(-Fr(1,2), PHI), 5: smul(-1, ONE)}

def cos\_pi\_t\_over\_5(t):

    t %= 10

    return C5T\[t if t \<= 5 else 10 \- t\]

def cos\_2pi\_jk\_over(m, jk):    \# cos(2\*pi\*jk/m) for m in {10,6,4,2}

    if m \== 10: return cos\_pi\_t\_over\_5(jk % 10\)

    if m \== 6:

        r \= jk % 6              \# cos(2\*pi\*jk/6) \= cos(pi\*r/3)

        r \= r if r \<= 3 else 6 \- r

        return {0: ONE, 1: q5(Fr(1,2)), 2: q5(-Fr(1,2)), 3: smul(-1, ONE)}\[r\]

    if m \== 4: return {0: ONE, 1: ZERO, 2: smul(-1, ONE), 3: ZERO}\[jk % 4\]

    if m \== 2: return ONE if jk % 2 \== 0 else smul(-1, ONE)

&nbsp;

\# \---------- SL(2,5): 9 classes; character table (values in Q(sqrt5), all real)

CL \= \['1', 'z', 'o4', 'o3', 'o6', '5A', '5B', '10A', '10B'\]

SZ \= \[1, 1, 30, 20, 20, 12, 12, 12, 12\]

G \= 120

T \= {

 '1' : \[ONE\]\*9,

 '3a': \[q5(3), q5(3), q5(-1), ZERO, ZERO, PHI, PHIP, PHIP, PHI\],

 '3b': \[q5(3), q5(3), q5(-1), ZERO, ZERO, PHIP, PHI, PHI, PHIP\],

 '4a': \[q5(4), q5(4), ZERO, ONE, ONE, q5(-1), q5(-1), q5(-1), q5(-1)\],

 '5' : \[q5(5), q5(5), ONE, q5(-1), q5(-1), ZERO, ZERO, ZERO, ZERO\],

 '2a': \[q5(2), q5(-2), ZERO, q5(-1), ONE, PHM1, NPHI, PHI, PHIP\],

 '2b': \[q5(2), q5(-2), ZERO, q5(-1), ONE, NPHI, PHM1, PHIP, PHI\],

 '4b': \[q5(4), q5(-4), ZERO, ONE, q5(-1), q5(-1), q5(-1), ONE, ONE\],

 '6' : \[q5(6), q5(-6), ZERO, ZERO, ZERO, ONE, ONE, q5(-1), q5(-1)\],

}

\# first orthogonality, exact, all pairs

names \= list(T)

for i, a in enumerate(names):

    for b in names\[i:\]:

        s \= ZERO

        for c in range(9):

            s \= add(s, smul(Fr(SZ\[c\]), mul(T\[a\]\[c\], T\[b\]\[c\])))

        want \= q5(G) if a \== b else ZERO

        assert s \== want, (a, b, s)

print("character table: 45/45 orthogonality relations hold exactly")

&nbsp;

\# \---------- subgroups, fusion of powers of a generator into G-classes

SUB \= {

 ('C10', 10): \['1','10A','5A','10B','5B','z','5B','10B','5A','10A'\],

 ('C6', 6):  \['1','o6','o3','z','o3','o6'\],

 ('C4', 4):  \['1','o4','z','o4'\],

 ('C2', 2):  \['1','z'\],

}

CLI \= {c: i for i, c in enumerate(CL)}

&nbsp;

\# columns: (subgroup, j) with lambda(z) \= \-1 (faithful side), up to conjugation j \~ \-j

COLS \= \[(('C10',10), j) for j in (1,3,5)\] \+ \[(('C6',6), j) for j in (1,3)\] \\

     \+ \[(('C4',4), 1)\] \+ \[(('C2',2), 1)\]

&nbsp;

FAITH \= \['2a', '2b', '4b', '6'\]

\# multiplicities \<Ind lambda, chi\> \= \<lambda, Res chi\>  (Frobenius reciprocity), exact

M \= {}   \# M\[(col, chi)\] \= integer

for col in COLS:

    (hname, m), j \= col

    fus \= SUB\[(hname, m)\]

    for chi in FAITH:

        s \= ZERO

        for k in range(m):

            s \= add(s, mul(cos\_2pi\_jk\_over(m, j\*k), T\[chi\]\[CLI\[fus\[k\]\]\]))

        s \= (s\[0\]/m, s\[1\]/m)

        assert s\[1\] \== 0 and s\[0\].denominator \== 1 and s\[0\] \>= 0, (col, chi, s)

        M\[(col, chi)\] \= int(s\[0\])

print("\\ninduction multiplicities (rows \= columns of the search):")

print(f"{'piece':\>14s}  dim  " \+ "  ".join(f"{c:\>3s}" for c in FAITH))

for col in COLS:

    (h, m), j \= col

    dim \= G//m

    print(f"Ind\_{h}(l^{j})".rjust(14) \+ f"  {dim:3d}  "

          \+ "  ".join(f"{M\[(col,chi)\]:3d}" for chi in FAITH))

&nbsp;

\# \---------- solve: sum n\_col \* M\[col\] \= e\_{2a} over the faithful irreps

target \= {chi: (1 if chi \== '2a' else 0\) for chi in FAITH}

sols \= \[\]

for n in product(range(-3, 4), repeat=len(COLS)):

    if all(sum(ni\*M\[(col, chi)\] for ni, col in zip(n, COLS)) \== target\[chi\]

           for chi in FAITH):

        sols.append(n)

sols.sort(key=lambda n: (sum(map(abs, n)), n))

assert sols, "KILL: no |n|\<=3 solution over {C10,C6,C4,C2} — widen subgroup set"

print(f"\\ninteger solutions with |n\_i| \<= 3: {len(sols)}; minimal-L1 solution:")

best \= sols\[0\]

terms \= \[(ni, col) for ni, col in zip(best, COLS) if ni \!= 0\]

for ni, ((h, m), j) in terms:

    print(f"   {ni:+d} \* Ind\_{h}(lambda^{j})   \[dim {G//m}\]")

&nbsp;

\# \---------- exact verification of the winner as a class function on all 9 classes

def ind\_value(col, c):

    (hname, m), j \= col

    fus \= SUB\[(hname, m)\]

    hits \= \[k for k in range(m) if fus\[k\] \== CL\[c\]\]

    s \= ZERO

    for k in hits:

        s \= add(s, cos\_2pi\_jk\_over(m, j\*k))

    return smul(Fr(G, m\*SZ\[c\]), s)

for c in range(9):

    tot \= ZERO

    for ni, col in zip(best, COLS):

        if ni: tot \= add(tot, smul(Fr(ni), ind\_value(col, c)))

    assert tot \== T\['2a'\]\[c\], (CL\[c\], tot, T\['2a'\]\[c\])

print("verified: the combination equals theta2 \= chi\_2a EXACTLY on all 9 classes")

&nbsp;

\# \---------- the ledger, spelled out

print("""

LEDGER (before the nu-twist; twisting by nu multiplies every lambda by nu|\_H

and shifts conductors into 1951-powers — the shape is unchanged):

  L(rho0, s) \* \[denominator pieces\] \= \[numerator pieces\]

Numerator / denominator per the signs above; each piece is a Hecke L-function

of the fixed field of the inducing subgroup (degrees \= 120/|H|), automorphic

and entire by Hecke \+ solvability (all subgroups of 2.A5 are solvable).

\=\> poles of L(rho0 (x) anything abelian) occur ONLY at zeros of the

   denominator Hecke L-function(s) not cancelled by the numerator.""")

n\_by\_dim \= \[(ni, 120//m, h, j) for ni, ((h, m), j) in zip(best, COLS) if ni\]

num \= \[f"L\_{d}(s; {h}, l^{j})^{ni}" for ni, d, h, j in n\_by\_dim if ni \> 0\]

den \= \[f"L\_{d}(s; {h}, l^{j})^{-ni}" for ni, d, h, j in n\_by\_dim if ni \< 0\]

print("  L(rho0,s) \=", " \* ".join(num), "/", " \* ".join(den) if den else "1")

print("\\nAlso reporting ALL minimal solutions (structure of the solution set):")

for n in sols\[:6\]:

    tt \= \[f"{ni:+d}\*{h}^l{j}" for ni, ((h, m), j) in zip(n, COLS) if ni\]

    print("   ", "  ".join(tt))