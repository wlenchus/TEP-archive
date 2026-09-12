#!/usr/bin/env python3
"""Emit the citable Hecke-eigenvalue datasets for both even-icosahedral 2-dim lifts.
a_p = b_p * zeta10^{j5(p)} * m_p ; nebentypus chi(p) = zeta5^{j5(p)} ; Euler factor 1 - a_p T + chi(p) T^2."""
import json, numpy as np, csv
PHI = (1+np.sqrt(5))/2
Z10 = np.exp(1j*np.pi/5)

def emit(field, clsfile, jlfile, bitsfile, orient, outfile):
    cls = {}
    for line in open(clsfile):
        p, c = line.strip().split(':'); cls[int(p)] = int(c)
    jl = {}
    for line in open(jlfile):
        p, j = line.strip().split(':'); jl[int(p)] = int(j) % 5
    bits = {int(p): v for p, v in json.load(open(bitsfile))['bits'].items()}
    if orient == 'B':
        MS = {0: ('2', 2.0), 1: ('0', 0.0), 2: ('1', 1.0), 3: ('phi', PHI), 4: ('1/phi', 1/PHI)}
    else:
        MS = {0: ('2', 2.0), 1: ('0', 0.0), 2: ('1', 1.0), 3: ('1/phi', 1/PHI), 4: ('phi', PHI)}
    CN = {0: '1A', 1: '2A', 2: '3A', 3: '5A/5B', 4: '5B/5A'}
    X = max(bits)
    rows = []
    for p in sorted(cls):
        if p > X or p == field or p not in jl:
            continue
        c = cls[p]; j = jl[p]; msym, mval = MS[c]
        if c == 1:
            b = 0; asym = '0'; aval = 0j
        else:
            b = bits.get(p)
            if b is None: continue
            sgn = '+' if b > 0 else '-'
            asym = f"{sgn}zeta10^{j}*{msym}" if msym != '1' else f"{sgn}zeta10^{j}"
            aval = b * Z10**j * mval
        chi = np.exp(2j*np.pi*j/5)
        rows.append({'p': p, 'proj_class': CN[c], 'raw_label': c, 'j5': j, 'b_p': b,
                     'abs_a_p': msym, 'a_p_exact': asym,
                     'Re_a_p': f"{aval.real:.12f}", 'Im_a_p': f"{aval.imag:.12f}",
                     'chi_p_exact': f"zeta5^{j}", 'Re_chi': f"{chi.real:.12f}", 'Im_chi': f"{chi.imag:.12f}"})
    with open(outfile, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    nb = sum(1 for r in rows if r['b_p'] != 0)
    print(f"{outfile}: {len(rows)} primes (p <= {X}), {nb} carrying decoded sign-bits, orientation {orient}")

emit(1951, '../gp/classesX_doud1951.txt', 'chilog_1951.txt', 'summit_base_oddGS.json', 'B',
     'hecke_eigenvalues_doud1951.csv')
emit(2141, 'classesX_2141.txt', 'chilog_2141.txt', 'summit2141_nu5_odd_A.json', 'A',
     'hecke_eigenvalues_doud2141.csv')
