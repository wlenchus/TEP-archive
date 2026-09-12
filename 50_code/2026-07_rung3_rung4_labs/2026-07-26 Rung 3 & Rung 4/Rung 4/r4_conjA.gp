default(parisize, 4200*1024*1024);
S = read("sat_S.bin"); Li = read("sat_Li.bin");
m = 3^24;
conjop(M) =
{
  my(d = denominator(M), e = valuation(d, 3), dp = d / 3^e);
  my(Q = lift(Mod(S, m) * Mod(d*M, m) * Mod(Li, m)));
  my(rem = vecmax(apply(x -> x % 3^(4+e), concat(Vec(Q)))));
  if(rem != 0, error("integrality fail"));
  (Q / 3^(4+e)) * lift(Mod(dp, 3^18)^(-1)) % 3^18;
}
{
  t0 = getabstime();
  T3 = conjop(read("M3_12.bin"));
  writebin("Tt3.bin", T3);
  c3 = charpoly(Mod(1,3) * T3);
  print("U3 conjugated (", (getabstime()-t0)/1000.0, " s); ordinary dim: ", 384 - valuation(c3, x), " (expect 176)");
  T7 = conjop(read("M7_12.bin"));
  writebin("Tt7.bin", T7);
  print("T7 conjugated");
}
quit;
