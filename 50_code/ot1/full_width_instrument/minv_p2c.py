import numpy as np, time, os
P=999983; t0=time.time(); BUDGET=490
if os.path.exists('p2_state.npz'):
    st=np.load('p2_state.npz'); Aug=st['Aug']; r=int(st['r']); c0=int(st['c0'])
    print(f"resumed at pivot {r}, col {c0}",flush=True)
else:
    H=np.zeros((2321,4801))
    for i,line in enumerate(open('host16000_local.csv')):
        for j,t in enumerate(line.rstrip('\n').split(',')):
            if t!='0': H[i,j]=int(t)%P
    np.save('H_p2.npy',H)
    M=np.mod(H@H.T,P); n=M.shape[0]
    Aug=np.concatenate([M,np.eye(n)],axis=1); r=0; c0=0
    print(f"fresh start, M built ({time.time()-t0:.0f}s)",flush=True)
n=2321
tmp=np.empty_like(Aug)
for c in range(c0,n):
    if time.time()-t0>BUDGET:
        np.savez('p2_state.npz',Aug=Aug,r=r,c0=c)
        print(f"CHECKPOINT at pivot {r}, col {c} ({time.time()-t0:.0f}s)"); raise SystemExit(42)
    nz=np.nonzero(Aug[r:,c])[0]
    if nz.size==0: continue
    i=r+int(nz[0])
    if i!=r: Aug[[r,i]]=Aug[[i,r]]
    Aug[r]*=pow(int(Aug[r,c]),P-2,P); np.mod(Aug[r],P,out=Aug[r])
    col=Aug[:,c].copy(); col[r]=0
    np.outer(col,Aug[r],out=tmp)
    Aug-=tmp; np.mod(Aug,P,out=Aug)
    r+=1
print(f"rank {r}/{n} ({time.time()-t0:.0f}s)",flush=True)
if r==n:
    np.save('Minv_p2.npy',Aug[:,n:]); print("p2 factor checkpointed")
    os.remove('p2_state.npz') if os.path.exists('p2_state.npz') else None
