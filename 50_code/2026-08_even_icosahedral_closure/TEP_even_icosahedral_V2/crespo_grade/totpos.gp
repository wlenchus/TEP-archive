
P = x^5 - x^4 - 780*x^3 - 1795*x^2 + 3106*x + 344;
ps = polsym(P, 8); G = matrix(5,5,i,j, ps[i+j-1]);
orth(GG) = {my(n = matsize(GG)[1]); if(n == 0, return(matrix(0,0))); if(n == 1, my(c = GG[1,1], s); if(!issquare(c, &s), error("nonsq")); return(Mat(1/s))); my(H = matconcat([GG, matrix(n,1); matrix(1,n), Mat(-1)])); my(v = qfsolve(H)); my(w = v[1..n], t = v[n+1]); my(v1 = w/t); my(K = matker(Mat((GG*v1)~))); my(B2 = orth(K~*GG*K)); matconcat([Mat(v1), K*B2]);}
B = orth(G);
default(realprecision, 80);
rts = real(polroots(P));
c = 0; neg = 0;
{
forperm(5, s,
  my(sv = Vec(s));
  \\ even permutations only
  my(par = 1, t = sv);
  for(i = 1, 5, for(j = i+1, 5, if(t[i] > t[j], par = -par)));
  if(par == 1,
    my(V = matrix(5,5,i,j, rts[sv[i]]^(j-1)));
    my(gm = matdet(matid(5) + V*B));
    c++;
    if(gm < 0, neg++)));
}
print(c, " even orderings, negatives: ", neg);
quit
