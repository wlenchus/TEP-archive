import numpy as np, time
P=999983; t0=time.time()
H=np.zeros((2321,4801))
for i,line in enumerate(open('host16000_local.csv')):
    for j,t in enumerate(line.rstrip('\n').split(',')):
        if t!='0': H[i,j]=int(t)%P
M=np.mod(H@H.T,P)
print(f"M built ({time.time()-t0:.0f}s)",flush=True)
n=M.shape[0]
Aug=np.concatenate([M,np.eye(n)],axis=1)
r=0
for c in range(n):
    nz=np.nonzero(Aug[r:,c])[0]
    if nz.size==0: continue
    i=r+int(nz[0]); Aug[[r,i]]=Aug[[i,r]]
    Aug[r]=np.mod(Aug[r]*pow(int(Aug[r,c]),P-2,P),P)
    col=Aug[:,c].copy(); col[r]=0
    Aug=np.mod(Aug-np.outer(col,Aug[r]),P)
    r+=1
print(f"rank {r}/{n} ({time.time()-t0:.0f}s)",flush=True)
if r==n:
    np.save('Minv_p2.npy',Aug[:,n:]); np.save('H_p2.npy',H); print("p2 factor checkpointed")
