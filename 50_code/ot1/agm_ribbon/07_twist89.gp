\\ AGM ribbon - addendum: can the 89^2 conductor junk be cleared by twisting by the
\\ split-prime generators 13 +/- 4*sqrt5 (N = 89)?  Probes whether the twist-minimal
\\ conductor of E_(j+) has support exactly {2, sqrt5}.
default(parisize, 512*1024*1024);
K = nfinit(t^2 - 5);
{
  my(j = Mod(10400 - 4640*t, t^2-5), E = ellinit(ellfromj(j), K));
  my(eps = Mod((1+t)/2, t^2-5), pi1 = Mod(13+4*t, t^2-5), pi2 = Mod(13-4*t, t^2-5));
  my(cands = List());
  foreach([1,-1], s1, foreach([1, eps, -eps], u, foreach([1, pi1, pi2, pi1*pi2], pi,
    foreach([1, 2, 3, 6, Mod(t,t^2-5)], r, listput(cands, s1*u*pi*r)))));
  my(best = idealnorm(K, ellglobalred(E)[1]), bestd = 1);
  print("base (ellfromj) conductor norm: ", best, " = ", factor(best));
  for(i = 1, #cands,
    my(d = cands[i], Et, nt);
    iferr(
      Et = ellinit(elltwist(E, d), K);
      nt = idealnorm(K, ellglobalred(Et)[1]);
      if(nt < best, best = nt; bestd = d),
      err, ));
  print("best twist found: d = ", bestd, "  conductor norm = ", best, " = ", factor(best));
  my(Eb = if(bestd == 1, E, ellinit(elltwist(E, bestd), K)));
  my(fac = idealfactor(K, ellglobalred(Eb)[1]));
  for(r = 1, #fac[,1],
    my(pr = fac[r,1]);
    print("   prime over p=", pr.p, " (f=", pr.f, ", e=", pr.e, "): exponent ", fac[r,2]));
}
quit;
