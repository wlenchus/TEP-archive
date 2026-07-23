#!/usr/bin/env python3
"""Emit gp script that lindep-identifies bridge coefficients over Q(zeta20)."""
lines_out = []
for tag in ("p", "m"):
    with open(f"/home/claude/tower5/bridge_cands_{tag}.txt") as f:
        raw = f.read().strip().split("\n")
    i = 0
    idx = 0
    while i < len(raw):
        assert raw[i].startswith("P ")
        perm = raw[i].split()[1]
        coeffs = []
        for k in range(6):
            i += 1
            re, im = raw[i].split()
            coeffs.append((re, im))
        i += 1
        cs = ",".join(f"({re})+({im})*I" for (re, im) in coeffs)
        lines_out.append(f'cand["{tag}",{idx}] = [{perm}, [{cs}]];')
        idx += 1

with open("/home/claude/tower5/13c_identify.gp", "w") as f:
    f.write("""\\\\ TOWER5 - 13c: identify bridge coefficients in Q(zeta20) via lindep
default(realprecision, 95);
z = exp(2*Pi*I/20);
B = vector(8, k, z^(k-1));
cand = Map();
""")
    f.write("\n".join(lines_out).replace('cand["', 'mapput(cand, ["').replace('] = [', '], [').replace(']];', ']]);'))
    f.write("""

\\\\ for each candidate: lindep each coefficient against [x, B...]; score
best = Map();
{
for (t = 1, 2,
  tag = if (t == 1, "p", "m");
  bestscore = 1e99; bestidx = -1; bestperm = 0; bestexpr = 0;
  for (idx = 0, 119,
    v = mapget(cand, [tag, idx]);
    perm = v[1]; cf = v[2];
    ok = 1; score = 0; exprs = vector(6);
    for (k = 1, 6,
      x = cf[k];
      rel = lindep(concat([x], B), 80);
      if (rel[1] == 0, ok = 0; break);
      \\\\ reconstructed value
      val = -sum(m = 1, 8, rel[m+1]*B[m])/rel[1];
      err = abs(val - x);
      hgt = vecmax(abs(rel));
      if (err > 1e-60 || hgt > 1e25, ok = 0; break);
      score += log(hgt + 2);
      exprs[k] = rel;
    );
    if (ok && score < bestscore,
      bestscore = score; bestidx = idx; bestperm = perm; bestexpr = exprs;
    );
  );
  print("=== branch ", tag, " ===");
  if (bestidx < 0,
    print("   NO pairing identified over Q(zeta20) at height<1e25, err<1e-60"),
    print("   best pairing perm = ", bestperm, "  (u_c -> x_{perm[c]}), score = ", bestscore);
    print("   coefficient relations (m0*x + sum m_i z^(i-1) = 0), coefficients a,b,c,d,e,f:");
    for (k = 1, 6, print("     ", bestexpr[k]));
  );
);
}
quit
""")
print("13c_identify.gp written")
