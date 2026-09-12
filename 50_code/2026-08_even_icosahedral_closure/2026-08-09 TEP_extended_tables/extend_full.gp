\\ Extended exact a_p tables via the trace-form construction. Emits p:class:sq:j5 per prime.
\\ class 0=1A 1=2A 2=3A 3/4=golden faces (Vandermonde vs sqrt(disc)); sq = gamma square-test (+1/-1); j5 = ind_g(p) mod 5.
\\ Roots computed ONCE per prime and reused for both the face and the gamma test.
default(parisize, 2000000000);
orth(GG) = {my(n = matsize(GG)[1]); if(n == 0, return(matrix(0,0))); if(n == 1, my(c = GG[1,1], s); if(!issquare(c, &s), error("nonsq")); return(Mat(1/s))); my(H = matconcat([GG, matrix(n,1); matrix(1,n), Mat(-1)])); my(v = qfsolve(H)); my(w = v[1..n], t = v[n+1]); my(v1 = w/t); my(K = matker(Mat((GG*v1)~))); my(B2 = orth(K~*GG*K)); matconcat([Mat(v1), K*B2]);}
run(P, NN, lo, hi, fn) = {
  my(ps = polsym(P, 8), G = matrix(5,5,i,j, ps[i+j-1]));
  my(B = orth(G));
  my(den = lcm(apply(denominator, Vec(matconcat(Vec(B))))));
  my(sd = sqrtint(poldisc(P)));
  my(g0 = znprimroot(NN));
  my(cnt = 0, t0 = getwalltime());
  forprime(p = lo, hi,
    if(p == NN, next);
    my(FF = factormod(P, p));
    my(degs = vecsort([poldegree(FF[i,1]) | i <- [1..matsize(FF)[1]]]));
    my(m = if(degs == [1,1,1,1,1], 1, degs == [1,2,2], 2, degs == [1,1,3], 3, degs == [5], 5, 0));
    if(m == 0, write(fn, Str(p, ":-1:0:", lift(znlog(Mod(p,NN), g0))%5)); next);          \\ ramified/index-anomalous: flag
    \\ p=2 flagged: char-2 square test is VACUOUS (every element of F_{2^m} is a square)
    if(p == 2 || den % p == 0, write(fn, Str(p, ":-2:0:", lift(znlog(Mod(p,NN), g0))%5)); next);  \\ construction blind
    my(gf = ffgen([p, m], 'w));
    my(rr = polrootsmod(P*gf^0, gf));
    if(#rr != 5, write(fn, Str(p, ":-3:0:", lift(znlog(Mod(p,NN), g0))%5)); next);
    my(orb = vector(5)); orb[1] = rr[1];
    for(i = 2, 5, orb[i] = orb[i-1]^p);
    my(cls);
    if(m == 5,
      my(V = gf^0);
      for(i = 1, 5, for(j = i+1, 5, V = V*(orb[i] - orb[j])));
      my(c = lift(polcoef(V.pol, 0)));
      cls = if(Mod(c,p) == Mod(sd,p), 3, if(Mod(c,p) == -Mod(sd,p), 4, -4)),
      cls = if(m == 1, 0, m == 2, 1, 2));
    my(ord5 = rr);   \\ SAME convention as the validated crespo.gp run
    my(Vp = matrix(5,5,i,j, ord5[i]^(j-1)));
    my(Up = Vp * (B*Mod(1,p)));
    my(gm = matdet(matid(5)*gf^0 + Up));
    if(gm == 0,
      my(t = ord5[1]); ord5[1] = ord5[2]; ord5[2] = t;
      Vp = matrix(5,5,i,j, ord5[i]^(j-1));
      Up = Vp * (B*Mod(1,p));
      gm = matdet(matid(5)*gf^0 + Up));
    if(gm == 0, write(fn, Str(p, ":", cls, ":0:", lift(znlog(Mod(p,NN), g0))%5)); next);
    my(sq = if(gm^((p^m - 1)/2) == gf^0, 1, -1));
    my(j5 = lift(znlog(Mod(p, NN), g0)) % 5);
    write(fn, Str(p, ":", cls, ":", sq, ":", j5));
    cnt++);
  print("  [", lo, ",", hi, "] emitted ", cnt, " in ", (getwalltime()-t0)/1000., "s");
}
P1951 = x^5 - x^4 - 780*x^3 - 1795*x^2 + 3106*x + 344;
{
system("rm -f full_1951.txt");
run(P1951, 1951, 2, 1000000, "full_1951.txt");
P2141 = x^5 - x^4 - 856*x^3 + 4025*x^2 + 28501*x - 40877;
system("rm -f full_2141.txt");
run(P2141, 2141, 2, 1000000, "full_2141.txt");
}
quit
