\\ step1b_canonical.gp -- identify K4 among ALL quartic 2-adic fields; iso test P1 vs P2
read("/home/claude/p2_break/quartic_models.gp");

locembed(g, h) = {
  my(cs, fp, target = poldegree(h));
  if (g == h, return(1));
  cs = polcompositum(g, h);
  for (i = 1, #cs,
    fp = factorpadic(cs[i], 2, 120);
    for (j = 1, #fp[,1],
      if (poldegree(fp[j,1]) == target, return(1))));
  0;
}

{
print("--- all quartic extensions of Q2 with v2(disc)=6 (PARI padicfields) ---");
L = padicfields(2, [4,6], 1);
print("count with (n,d)=(4,6): ", #L);
cands = [];
for (i = 1, #L,
  my(pol = liftall(L[i][1]), e = L[i][2], f = L[i][3], d = L[i][4], au = L[i][5]);
  print(i, ": pol = ", pol, "  e=", e, " f=", f, " d=", d, " #aut=", au);
  if (e == 4, cands = concat(cands, [[pol, au]])));
print();
print("--- totally ramified (e=4, d=6) candidates: ", #cands, " ---");
for (i = 1, #cands, print("  cand ", i, ": ", cands[i][1], "  #aut=", cands[i][2]));
print();
print("--- embed/iso: P1 quartic factor vs each candidate ---");
for (i = 1, #cands,
  print("  P1-K4 == cand ", i, " ? ", locembed(cands[i][1], g1q)));
print("--- embed/iso: P2 (Buhler) quartic factor vs each candidate ---");
for (i = 1, #cands,
  print("  P2-K4 == cand ", i, " ? ", locembed(cands[i][1], g2q)));
print();
print("--- direct iso test P1-K4 vs P2-K4: ", locembed(g1q, g2q));
\\ closure-group witnesses for the matched candidate(s): global Galois group of the
\\ small canonical polynomial (upper bound for local closure) for context:
for (i = 1, #cands,
  print("  cand ", i, " polgalois (GLOBAL closure of this model): ", polgalois(cands[i][1])));
}
quit
