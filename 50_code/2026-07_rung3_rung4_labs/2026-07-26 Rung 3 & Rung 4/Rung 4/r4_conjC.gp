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
mf = mfinit([12000, 2, 12], 0);
todo = eval(getenv("PRIMES"));
{
  foreach(todo, l,
    my(t0 = getabstime());
    my(Tl = conjop(mfheckemat(mf, l)));
    writebin(Str("Tt", l, ".bin"), Tl);
    print("T", l, " conjugated (", round((getabstime()-t0)/1000.0), " s)"));
}
quit;
