default(nbthreads, 1);
default(parisizemax, 13000000000);
gettime();
mf = mfinit([16000,2],1);
B = mfbasis(mf);
print("mfinit+mfbasis done, ms = ", gettime(), ", nforms = ", #B);
gettime();
for(i = 1, #B,
  v = Vec(mfcoefs(B[i], 4800));
  write("/home/claude/ot1_16000/host16000_local.csv", strjoin(apply(x -> Str(x), v), ","));
  if(i % 100 == 0, print("wrote ", i, " forms, ms = ", gettime()));
);
print("HOST WRITTEN, total forms = ", #B);
