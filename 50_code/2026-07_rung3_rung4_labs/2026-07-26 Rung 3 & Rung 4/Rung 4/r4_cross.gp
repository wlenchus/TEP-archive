default(parisize, 2500*1024*1024);
X = read("blocks12.bin");
blocks = X[1]; facdata = X[2];
ops = [3, 7, 11, 13, 17, 19];
{
  \\ group ORDINARY blocks by tame tuple (indices 2..6)
  keys = List(); groups = List();
  for(bi = 1, #blocks,
    if(facdata[bi][1] != x,   \\ ordinary: a3-factor not x
      my(tk = [facdata[bi][k] | k <- [2..6]]);
      my(found = 0);
      for(g = 1, #keys, if(keys[g] == tk, listput(groups[g], bi); found = 1; break));
      if(!found, listput(keys, tk); listput(groups, List([bi])))));
  print(#keys, " distinct tame classes among ordinary blocks");
  for(g = 1, #keys,
    my(bis = Vec(groups[g]));
    my(tot = vecsum([matsize(blocks[bi])[2] | bi <- bis]));
    my(fs = [poldegree(lcm([facdata[bi][k] | k <- [2..6]])) | bi <- bis]);
    my(germs = vecsum([matsize(blocks[bi])[2] / poldegree(lcm(concat([facdata[bi][k] | k <- [1..6]], x))) | bi <- bis]));
    if(#bis >= 2 || germs >= 2,
      print("tame class ", g, ": blocks ", bis, "  a3-factors ", [facdata[bi][1] | bi <- bis],
            "  dims ", [matsize(blocks[bi])[2] | bi <- bis], "  tame tuple ", keys[g])));
}
quit;
