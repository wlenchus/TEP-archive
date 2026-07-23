default(nbthreads, 1); default(parisizemax, 4000000000);
gettime();
mf = mfinit([4000,2],1); B = mfbasis(mf);
print("mfinit 4000: ms=", gettime(), " nforms=", #B);
for(i=1,#B, write("/home/claude/ot1_16000/host4000.csv", strjoin(apply(x->Str(x), Vec(mfcoefs(B[i], 1200))), ",")));
print("HOST4000 EXPORTED rows=", #B);
