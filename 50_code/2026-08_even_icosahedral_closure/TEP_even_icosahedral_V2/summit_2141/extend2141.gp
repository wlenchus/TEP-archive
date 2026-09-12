P = x^5 - x^4 - 856*x^3 + 4025*x^2 + 28501*x - 40877;
sd = sqrtint(poldisc(P));
faceclass(p) =
{
  my(F = factormod(P, p));
  my(degs = vecsort([poldegree(F[i,1]) | i <- [1..matsize(F)[1]]]));
  if(degs == [1,1,1,1,1], return(0));
  if(degs == [1,2,2], return(1));
  if(degs == [1,1,3], return(2));
  if(degs == [5],
    my(g = ffgen([p, 5], 'w));
    my(rts = polrootsmod(P * g^0, g));
    my(r = rts[1]);
    my(orb = vector(5)); orb[1] = r;
    for(i = 2, 5, orb[i] = orb[i-1]^p);
    my(V = g^0);
    for(i = 1, 5, for(j = i+1, 5, V = V * (orb[i] - orb[j])));
    if(V^p != V, return(-9));
    my(c = lift(polcoef(V.pol, 0)));
    my(s = Mod(sd, p));
    if(Mod(c, p) == s, return(3), if(Mod(c, p) == -s, return(4), return(-9))));
  return(-1);
}
{
forprime(p = 25101, 34400,
  if(p == 2141, next);
  write("classesX_2141.txt", Str(p, ":", faceclass(p))));
print("extended");
}
quit
