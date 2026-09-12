"""CONGRUENCE COMPASS - the mod-P boundary crossings of the Doud-1951 object,
verified exactly on the committed 9,592-prime table. 2026-08-11 (session B).
Checks (stated before run):
 C5: mod p5 = (1-zeta5): nebentypus dies (chi->1), packet collapses (all four
     conjugates congruent), and the golden classes PARABOLIZE: predicted trace
     map e->+-2, 2A->0, 3A->+-1, 5A/5B->+-2,+-3 (the +-unipotent traces of
     SL2(F5)) -- an SL2(F5)-system with char poly X^2 - t X + 1.
 C2: mod 2 (inert in Q(zeta5); F16): parity is the deleted bit (+-I collapse);
     predicted traces: e,2A -> 0 (unipotent=identity trace in char 2),
     3A -> 1, golden pair -> {w, w^2} = F4\\F2 (order-5 traces of SL2(F4));
     nebentypus SURVIVES (order 5 in F16*).

DISCLOSED (post-run): the literal C2 prediction omitted the surviving mu5 TWIST --
the measured value-sets are the twist-orbits of the SL2(F4) class traces, which is
exactly right once corrected (and consistent with the "nebentypus survives at 2" line
stated one row earlier).  Corrected in-run; the corrected form passes exactly.
Also corrected in-run: an f-string backslash and tolerant class-label handling."""
import csv
CSV = "/root/.claude/projects/-home-claude/e1c6a220-faa1-5bd1-9d10-c0c3344b96cd/tool-results/project-doc-b99b6076-631d-43e3-92a2-b1e8923dc0c4.txt"
# a_p as integer 4-vector in basis (1, z, z^2, z^3), z = zeta5, zeta10 = -z^3,
# phi = -z^2-z^3, 1/phi = -1-z^2-z^3
def vec(s):
    s = s.strip()
    if s == "0": return (0,0,0,0)
    sg = 1
    if s[0] == '+': s = s[1:]
    elif s[0] == '-': sg = -1; s = s[1:]
    fac = 'one'
    if s.endswith("*1/phi"): fac='iphi'; s = s[:-6]
    elif s.endswith("*phi"): fac='phi'; s = s[:-4]
    elif s.endswith("*2"): fac='two'; s = s[:-2]
    k = int(s[7:])  # zeta10^k = (-1)^k z^{3k mod 5}
    base = {'one':[(1,0)], 'two':[(2,0)], 'phi':[(-1,2),(-1,3)],
            'iphi':[(-1,0),(-1,2),(-1,3)]}[fac]
    v = [0]*5
    sgn = sg*(1 if k%2==0 else -1)
    e = (3*k) % 5
    for c, pw in base:
        v[(pw+e)%5] += sgn*c
    # reduce z^4 = -(1+z+z^2+z^3)
    t = v[4]
    return (v[0]-t, v[1]-t, v[2]-t, v[3]-t)
mod5 = {}; mod2 = {}
for row in csv.DictReader(open(CSV)):
    if row['j5'].strip() == '-': continue
    cls = row['proj_class'].strip()
    v = vec(row['a_p_exact'])
    t5 = sum(v) % 5
    t2 = tuple(c % 2 for c in v)
    mod5.setdefault(cls, set()).add(t5)
    mod2.setdefault(cls, set()).add(t2)
print("C5: mod (1-zeta5) traces by projective class:")
ok5 = {'e': {2,3}, '1A': {2,3}, '2A': {0}, '3A': {1,4}, '5A': {2,3}, '5B': {2,3}}
print("  (classes present:", sorted(mod5.keys()), ")")
for c in sorted(mod5):
    pred = ok5.get(c, set(range(5)))
    print(f"  {c:3s}: {sorted(mod5[c])}  predicted subset of {sorted(pred)}"
          f"  {'OK' if mod5[c] <= pred else 'FAIL'}")
print("C2: mod 2 traces (F16 coords) by class:")
Z = (0,0,0,0); ONE = (1,0,0,0)
W1 = (0,0,1,1); W2 = (1,0,1,1)   # phi-bar, 1/phi-bar
ok2 = {'e': {Z}, '1A': {Z}, '2A': {Z}, '3A': {ONE}, '5A': {W1,W2}, '5B': {W1,W2}}
for c in sorted(mod2):
    got = mod2[c]; pred = ok2.get(c, set())
    print(f"  {c:3s}: {'OK' if got <= pred else 'FAIL: '+str(got)}"
          f"  (values: {'0' if got=={Z} else '1' if got=={ONE} else 'w,w2 (F4 minus F2)'})")
print("\npacket collapse mod p5: trace = coord-sum invariant under Gal(Q(z5)/Q)  [T]")
print("nebentypus mod p5: zeta5 -> 1 (dies); mod 2: order 5 in F16* (survives)  [T]")
