#!/usr/bin/env python3
"""Extended exact a_p tables from the trace-form construction, p <= LIMIT.
Provenance per row: construction | FE-resolved | 2A-trivial."""
import json, csv, numpy as np
PHI = (1+np.sqrt(5))/2
Z10 = np.exp(1j*np.pi/5)
LIMIT = 100000

def kron(D, p):
    if D % p == 0: return 0
    return 1 if pow(D % p, (p-1)//2, p) == 1 else -1

def build(field, fullfn, clsfile, bitsfile, orient, D, out):
    F = {}
    for line in open(fullfn):
        p, c, s, j = line.strip().split(':')
        F[int(p)] = (int(c), int(s), int(j))
    cls0 = {}
    for line in open(clsfile):
        p, c = line.strip().split(':'); cls0[int(p)] = int(c)
    bits = {int(p): v for p, v in json.load(open(bitsfile))['bits'].items()}
    if orient == 'B':
        MS = {0:('2',2.0), 1:('0',0.0), 2:('1',1.0), 3:('phi',PHI), 4:('1/phi',1/PHI)}
        SG = {0:(1,-1), 2:(-1,1), 3:(-1,1), 4:(1,-1)}
    else:
        MS = {0:('2',2.0), 1:('0',0.0), 2:('1',1.0), 3:('1/phi',1/PHI), 4:('phi',PHI)}
        SG = {0:(1,-1), 2:(-1,1), 3:(1,-1), 4:(-1,1)}
    CN = {0:'1A', 1:'2A', 2:'3A', 3:'5A', 4:'5B'}
    rows = []; unresolved = []
    for p in sorted(F):
        if p > LIMIT or p == field: continue
        c, s, j = F[p]
        if c < 0:                      # construction-blind: fall back
            c = cls0.get(p)
            if c is None: unresolved.append(p); continue
            if c == 1:
                b, prov = 0, '2A-trivial'
            elif p in bits:
                b, prov = bits[p], 'FE-resolved'
            else:
                unresolved.append(p); continue
        elif c == 1:
            b, prov = 0, '2A-trivial'
        else:
            b = SG[c][0] if s == 1 else SG[c][1]
            b = b * kron(D, p) * (-1)**(j % 2)
            prov = 'construction'
        msym, mval = MS[c]
        if c == 1:
            asym, aval = '0', 0j
        else:
            sgn = '+' if b > 0 else '-'
            asym = f"{sgn}zeta10^{j}*{msym}" if msym != '1' else f"{sgn}zeta10^{j}"
            aval = b * Z10**j * mval
        chi = np.exp(2j*np.pi*j/5)
        rows.append({'p':p, 'proj_class':CN[c], 'j5':j, 'b_p':b, 'abs_a_p':msym,
                     'a_p_exact':asym, 'Re_a_p':f"{aval.real:.15f}", 'Im_a_p':f"{aval.imag:.15f}",
                     'chi_p_exact':f"zeta5^{j}", 'Re_chi':f"{chi.real:.15f}", 'Im_chi':f"{chi.imag:.15f}",
                     'provenance':prov})
    with open(out,'w',newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    import collections
    pv = collections.Counter(r['provenance'] for r in rows)
    print(f"{out}: {len(rows)} primes to {LIMIT}  provenance {dict(pv)}  unresolved {unresolved}")
    # cross-check against the committed decode
    mis = [p for p in bits if any(r['p']==p for r in rows)
           and next(r for r in rows if r['p']==p)['b_p'] != bits[p]]
    print(f"   committed-bit agreement: {len(bits)-len(mis)}/{len(bits)}  mismatches {mis[:5]}")

build(1951,'full_1951.txt','../gp/classesX_doud1951.txt','summit_base_oddGS.json','B',-1951,
      'hecke_eigenvalues_doud1951_to1e5.csv')
build(2141,'full_2141.txt','classesX_2141.txt','summit2141_nu5_odd_A.json','A',-24,
      'hecke_eigenvalues_doud2141_to1e5.csv')
