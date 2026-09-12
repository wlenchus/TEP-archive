#!/usr/bin/env python3
"""Per-arm TRUE-BITS lint for the twist-enriched rung: every arm must certify with the true assignment."""
import numpy as np, sys
sys.path.insert(0, '.')
from qualify2 import build, TW, FACP, FACN, FACI
from instr2 import sieve

D = int(sys.argv[1])
arms, bitp, truth, cands, fixed, cls = build(D)
kr = {}
for line in open(f'kron_{D}.txt'):
    parts = line.strip().split(':')
    kr[int(parts[0])] = {TW[i]: int(parts[i+1]) for i in range(len(TW))}

labels = ['base'] + [f'tw{d}' for d in TW]
for ai, arm in enumerate(arms):
    d = None if ai == 0 else TW[ai-1]
    def tf(p):
        c = cls.get(p)
        if c is None: return None
        if d is None:
            return {'P': FACP, 'N': FACN, 'I': FACI, 'R': [1.0, -1.0]}[c]
        kd = kr.get(p, {}).get(d, None)
        if kd is None or kd == 0: return None
        if c == 'P': return [1.0, -2.0*kd, 1.0]
        if c == 'N': return [1.0, 1.0*kd, 1.0]
        if c == 'I': return FACI
        return [1.0, -1.0*kd]
    arm.set_a(sieve(arm.X, tf))
    r, eps = arm.residual()
    print(f"{labels[ai]:6s} N={arm.N:>10.0f} port={arm.port} X={arm.X:>5d}: TRUE-bits residual {r:.3e}  eps {eps:.4f}")
