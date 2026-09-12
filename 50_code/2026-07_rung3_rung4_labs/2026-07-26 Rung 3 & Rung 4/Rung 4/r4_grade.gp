default(parisize, 3000*1024*1024);
getlast(f) =
{
  my(X = read(f));
  if(type(X) == "t_VEC", X[#X], X);
}
restrictop(Tm, B) =
{
  my(n = matsize(B)[1], dim = matsize(B)[2]);
  if(dim == n, return(Tm));
  my(BS = matsupplement(B));
  my(F = BS^(-1) * Tm * BS);
  F[1..dim, 1..dim];
}
{
  ops = [3, 7, 11, 13, 17, 19];
  Ts = vector(#ops, k, Mod(1,3) * getlast(Str("Tt", ops[k], ".bin")));
  X = read("blocks12.bin"); blocks = X[1]; facdata = X[2];
  w = ffgen([3, 4], 'w);
  g0 = ffprimroot(w); th = g0^20;
  if(th^2 != -1, error("theta wrong"));
  \\ census: joint eigen-tuples for ordinary blocks of dim <= 4
  print("--- census joint tuples (blocks dim <= 4, ordinary) ---");
  tup = List(); tupbi = List();
  for(bi = 1, #blocks,
    if(facdata[bi][1] == x, next);
    my(B = Mod(1,3) * blocks[bi], dim = matsize(B)[2]);
    if(dim > 4, next);
    my(As = vector(#ops, k, restrictop(Ts[k], B) * w^0));   \\ FF-ify
    \\ joint eigenlines: refine eigenspaces successively
    my(spaces = List([matid(dim) * w^0]));
    for(k = 1, #ops,
      my(ns = List());
      for(si = 1, #spaces,
        my(S = spaces[si], A = restrictop(As[k], S));
        my(cp = charpoly(A), fa = factor(cp));
        for(fi = 1, matsize(fa)[1],
          if(poldegree(fa[fi,1]) == 1,
            my(lam = -polcoef(fa[fi,1], 0));
            my(K = matker(A - lam));
            if(#K > 0, listput(ns, S * K)))));
      spaces = ns);
    for(si = 1, #spaces,
      my(S = spaces[si]);
      my(vals = vector(#ops, k, my(Av = restrictop(As[k], S)); Av[1,1]));
      listput(tup, vals); listput(tupbi, bi)));
  print(#tup, " joint eigenlines extracted from dim<=4 ordinary blocks");
  \\ key embeddings
  print("--- key match ---");
  for(es = 0, 1, for(et = 0, 1,
    my(s = (-1)^es * th, t = (-1)^et * th);
    my(gm = (s - 1)/2);
    my(k3 = -gm*t, k7 = t, k11 = -t, k13 = -gm, k17 = w^0, k19 = -gm*t);
    \\ stabilization roots: X^2 - k3 X - 1
    my(d = k3^2 + 4, r, rts);
    rts = if(issquare(d, &r), [(k3+r)/2, (k3-r)/2], []);
    print("embedding (s,t) = (", es, ",", et, "): key tame = ", [k7, k11, k13, k17, k19], "  alpha/beta = ", rts);
    for(ti = 1, #tup,
      my(v = tup[ti]);
      if(v[2] == k7 && v[3] == k11 && v[4] == k13 && v[5] == k17 && v[6] == k19,
        my(which = if(#rts >= 1 && v[1] == rts[1], "ALPHA", if(#rts >= 2 && v[1] == rts[2], "BETA", "a3-MISMATCH")));
        print("   MATCH block ", tupbi[ti], ": a3 = ", v[1], " -> ", which)))));
}
quit;
