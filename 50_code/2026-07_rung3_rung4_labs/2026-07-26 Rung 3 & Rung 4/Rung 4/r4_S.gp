default(parisize, 3000*1024*1024);
adjLi = read("sat_adj.bin"); dt = read("sat_det.bin");
S = adjLi / (dt / 81);
if(denominator(S) != 1, error("S not integral: deepest entry denom"));
print("S = 81*Li^{-1} integral: max |entry| digits ~ ", #digits(vecmax(apply(abs, concat(Vec(S))))));
writebin("sat_S.bin", S);
quit;
