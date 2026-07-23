default(nbthreads, 1);
default(parisizemax, 13000000000);
gettime();
mf = mfinit([16000,2],1);
B = mfbasis(mf);
print("mfinit+mfbasis ms = ", gettime(), " nforms = ", #B);
gettime();
for(i=1,#B, write("/home/claude/ot1_16000/host16000_local.csv", strjoin(apply(x->Str(x), Vec(mfcoefs(B[i],4800))), ",")); if(i%200==0, print("row ", i, " ms=", gettime())));
if(#B == 2321, print("EXPORT LOOP COMPLETE"), print("EXPORT COUNT UNEXPECTED"));
