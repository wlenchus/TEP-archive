default(parisize, 3000*1024*1024);
getlast(f) =
{
  my(X = read(f));
  if(type(X) == "t_VEC", X[#X], X);
}
{
  ops = [3, 7, 11, 13, 17, 19];
  Ts = vector(#ops, k, getlast(Str("Tt", ops[k], ".bin")));
  \\ 1. commutation mod 3^18
  m = 3^18; bad = 0;
  for(i = 1, #ops, for(j = i+1, #ops,
    if((Ts[i]*Ts[j] - Ts[j]*Ts[i]) % m != 0*Ts[1], bad++)));
  print("non-commuting pairs mod 3^18: ", bad, " (expect 0)");
  \\ 2. trace sanity vs original matrices
  M3 = read("M3_12.bin"); M7 = read("M7_12.bin");
  print("tr(U3): conj ", Ts[1][1,1]*0 + trace(Ts[1]) % 3^18, " vs orig ", lift(Mod(trace(M3), 3^18)));
  print("tr(T7): conj ", trace(Ts[2]) % 3^18, " vs orig ", lift(Mod(trace(M7), 3^18)));
  \\ 3. dump ALL ordinary blocks' factor tuples
  X = read("blocks12.bin"); blocks = X[1]; facdata = X[2];
  print("--- ordinary blocks (a3-factor != x): [a3 | a7 a11 a13 a17 a19] dim ---");
  for(bi = 1, #blocks,
    if(facdata[bi][1] != x,
      print(bi, ": ", facdata[bi], "  dim ", matsize(blocks[bi])[2])));
}
quit;
