default(parisize, 4200*1024*1024);
mf = mfinit([12000, 2, 12], 0);
{
  C = mfcoefs(mf, 2500);
  A = denominator(C) * C;   \\ integral (B+1) x 384
  Li = matid(384); t = 0;
  while(1,
    my(Ac = A * Li);
    my(mn = 99); for(j = 1, 384, for(i = 1, matsize(Ac)[1], my(c = Ac[i,j]); if(c != 0, mn = min(mn, valuation(c, 3)); if(mn < t, break(2)))));
    if(mn < t, print("INVARIANT FAIL"); break);
    my(Bm = Ac / 3^t);
    my(k = matker(Mod(1,3) * Bm));
    print("round t = ", t, ": rank = ", 384 - #k, "  kernel dim = ", #k);
    if(#k == 0, break);
    Li = mathnf(concat(3 * Li, Li * lift(k)));
    t++;
    if(t > 12, print("TOO DEEP"); break);
  );
  print("saturation done at t = ", t);
  dt = matdet(Li);
  print("v3(det Li) = ", valuation(dt, 3), " ; det pure 3-power: ", abs(dt) == 3^valuation(dt,3));
  R = Li^(-1);
  adjLi = dt * R;
  print("adj integral: ", denominator(adjLi) == 1);
  writebin("sat_Li.bin", Li); writebin("sat_adj.bin", adjLi); writebin("sat_det.bin", dt);
}
quit;
