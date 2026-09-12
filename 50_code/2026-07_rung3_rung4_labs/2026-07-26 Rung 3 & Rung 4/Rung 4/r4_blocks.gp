default(parisize, 3500*1024*1024);
ops = [3, 7, 11, 13, 17, 19];
getlast(f) =
{
  my(X = read(f));
  if(type(X) == "t_VEC", X[#X], X);
}
Ts = vector(#ops, k, Mod(1,3) * getlast(Str("Tt", ops[k], ".bin")));
restrictop(T, B) =
{
  my(n = matsize(B)[1], dim = matsize(B)[2]); if(dim == n, return(T));
  my(BS = matsupplement(B));
  my(F = BS^(-1) * T * BS);
  my(low = F[dim+1..n, 1..dim]);
  if(low != 0 * low, error("block not stable"));
  F[1..dim, 1..dim];
}
{
  blocks = List([matid(384) * Mod(1,3)]);
  facdata = List([vector(#ops)]);
  for(k = 1, #ops,
    my(nb = List(), nf = List());
    for(bi = 1, #blocks,
      my(B = blocks[bi], A = restrictop(Ts[k], B));
      my(cf = factormod(charpoly(A), 3));
      for(fi = 1, matsize(cf)[1],
        my(g = cf[fi,1], mu = cf[fi,2]);
        my(K = matker(subst(g, x, A)^mu));
        my(sub = B * K);
        my(rec = facdata[bi]); rec[k] = g;
        listput(nb, sub); listput(nf, rec)));
    blocks = nb; facdata = nf;
    print("after op ", ops[k], ": ", #blocks, " blocks"));
  print("=== final blocks ===");
  cands = List();
  for(bi = 1, #blocks,
    my(dim = matsize(blocks[bi])[2]);
    my(degs = [poldegree(facdata[bi][k]) | k <- [1..#ops]]);
    my(f = lcm(degs), mu = dim / f);
    my(ordflag = if(facdata[bi][1] != Mod(1,3)*x, "ORD", "---"));
    if(mu >= 2 && ordflag == "ORD",
      listput(cands, bi);
      print("block ", bi, ": dim ", dim, " f ", f, " mult ", mu, " ", ordflag, "  ** CANDIDATE **  factors: ", [lift(facdata[bi][k]) | k <- [1..#ops]]),
      if(ordflag == "ORD", print("block ", bi, ": dim ", dim, " f ", f, " mult ", mu, " ORD"))));
  print("ordinary total: ", vecsum([matsize(blocks[bi])[2] | bi <- [1..#blocks], facdata[bi][1] != Mod(1,3)*x]), " (expect 176)");
  print("candidate blocks: ", #cands);
  writebin("blocks12.bin", [apply(lift, Vec(blocks)), apply(v -> apply(lift, v), Vec(facdata)), Vec(cands)]);
}
quit;
