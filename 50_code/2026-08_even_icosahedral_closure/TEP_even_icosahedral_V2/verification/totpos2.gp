\\ Total-positivity of gamma across ALL 120 orderings, both fields. The ~60 nonvanishing values
\\ (the even-coset relative to det(U)) are the conjugates of gamma; count negatives.
run(P, name) = {
  my(ps = polsym(P, 8), G = matrix(5,5,i,j, ps[i+j-1]));
  my(B = orth(G));
  default(realprecision, 80);
  my(rts = real(polroots(P)));
  my(nz = 0, neg = 0, mn = 10.0^99, mx = -10.0^99);
  forperm(5, s,
    my(sv = Vec(s));
    my(V = matrix(5,5,i,j, rts[sv[i]]^(j-1)));
    my(gm = matdet(matid(5) + V*B));
    if(abs(gm) > 10.0^-40,
      nz++;
      if(gm < 0, neg++);
      mn = min(mn, gm); mx = max(mx, gm)));
  print(name, ": nonvanishing conjugates ", nz, " of 120;  NEGATIVES = ", neg,
        ";  min = ", mn, "  max = ", mx);
}
orth(GG) = {my(n = matsize(GG)[1]); if(n == 0, return(matrix(0,0))); if(n == 1, my(c = GG[1,1], s); if(!issquare(c, &s), error("nonsq")); return(Mat(1/s))); my(H = matconcat([GG, matrix(n,1); matrix(1,n), Mat(-1)])); my(v = qfsolve(H)); my(w = v[1..n], t = v[n+1]); my(v1 = w/t); my(K = matker(Mat((GG*v1)~))); my(B2 = orth(K~*GG*K)); matconcat([Mat(v1), K*B2]);}
{
run(x^5 - x^4 - 780*x^3 - 1795*x^2 + 3106*x + 344, "Doud-1951");
run(x^5 - x^4 - 856*x^3 + 4025*x^2 + 28501*x - 40877, "Doud-2141");
}
quit
