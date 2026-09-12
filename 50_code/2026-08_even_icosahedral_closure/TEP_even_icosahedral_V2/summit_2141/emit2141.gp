default(parisize, 1200000000);
P = x^5 - x^4 - 856*x^3 + 4025*x^2 + 28501*x - 40877;
{
print("gal ", polgalois(P)[4], "  disc=2141^4? ", poldisc(P) % 2141^4 == 0);
my(nf = nfinit(P));
print("fielddisc = ", factor(nf.disc), "  sig ", nf.sign);
my(idx2 = poldisc(P) / nf.disc);
print("index^2 = ", factor(idx2));
print("2141 prime ", isprime(2141), "  mod 4: ", 2141%4, "  mod 5: ", 2141%5, "  mod 20: ", 2141%20);
print("primroot mod 2141: ", lift(znprimroot(2141)));
print("ram: ", [[pr.e, pr.f] | pr <- idealprimedec(nf, 2141)]);
\\ index primes: true classes via idealprimedec residue degrees
my(idxp = factor(idx2)[,1]);
for(i = 1, #idxp,
  my(q = idxp[i], dec = idealprimedec(nf, q));
  my(fs = vecsort([pr.f | pr <- dec]));
  my(cls = if(fs == [1,1,1,1,1], 0, fs == [1,2,2], 1, fs == [1,1,3], 2, fs == [5], 9, -9));
  print("index prime ", q, ": f-pattern ", fs, " -> class ", cls));
}
sd = sqrtint(poldisc(P));
print("sqrt(poldisc) exact: ", sd^2 == poldisc(P));
\\ classes + faces to 25100 (covers rho3 recert X = 25071)
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
IDXCLS = Map();  \\ filled from idealprimedec above: 3, 43, 2689 expected
{
  my(nf = nfinit(P), idxp = factor(poldisc(P)/nf.disc)[,1]);
  for(i = 1, #idxp,
    my(q = idxp[i], fs = vecsort([pr.f | pr <- idealprimedec(nf, q)]));
    mapput(IDXCLS, q, if(fs == [1,1,1,1,1], 0, fs == [1,2,2], 1, fs == [1,1,3], 2, fs == [5], 9, -9)));
}
{
system("rm -f classesX_2141.txt chilog_2141.txt");
my(g0 = znprimroot(2141));
forprime(p = 2, 25100,
  if(p == 2141, next);
  my(c);
  if(mapisdefined(IDXCLS, p), c = mapget(IDXCLS, p),
     p == 2, c = 8,   \\ placeholder: 2-adic decider decides (8 = pending)
     c = faceclass(p));
  write("classesX_2141.txt", Str(p, ":", c));
  if(1, write("chilog_2141.txt", Str(p, ":", lift(znlog(Mod(p, 2141), g0)) % 10))));
print("emit done");
}
quit
