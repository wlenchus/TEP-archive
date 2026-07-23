#!/bin/bash
# Chunked S2(Gamma0(8000)) host build — validated 07-04 pattern (fresh gp per chunk)
cd /home/claude/ot1_8000
echo "start $(date)" > build.log
gp -q -s 5000000000 << 'GPEOF' >> build.log 2>&1
print("dimS2=", mfdim([8000,2],1)); print("sturm=", mfsturm([8000,2]));
GPEOF
for range in "1,400" "401,800" "801,1141"; do
  A=${range%,*}; B=${range#*,}
  echo "chunk $A..$B $(date)" >> build.log
  gp -q -s 5000000000 << GPEOF >> host8000_raw.txt 2>> build.log
mf=mfinit([8000,2],1); Bb=mfbasis(mf); for(i=$A,min($B,#Bb), print(mfcoefs(Bb[i],2400)))
GPEOF
done
echo "done $(date)" >> build.log
wc -l host8000_raw.txt >> build.log
