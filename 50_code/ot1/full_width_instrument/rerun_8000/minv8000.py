import numpy as np, sys
P=int(sys.argv[1]) if len(sys.argv)>1 else 1000003
tag='p1' if P==1000003 else 'p2'
rows=np.load('host8000_obj.npy',allow_pickle=True)
H=np.array([[int(x)%P for x in r] for r in rows],dtype=np.float64)
print('H',H.shape)
M=np.mod(H@H.T,P); n=M.shape[0]
Aug=np.concatenate([M,np.eye(n)],axis=1)
for c in range(n):
    nz=np.nonzero(Aug[c:,c])[0]
    if nz.size==0: raise SystemExit(f'SINGULAR at {c}')
    i=c+int(nz[0]); Aug[[c,i]]=Aug[[i,c]]
    Aug[c]=np.mod(Aug[c]*pow(int(Aug[c,c]),P-2,P),P)
    col=Aug[:,c].copy(); col[c]=0.0
    Aug=np.mod(Aug-np.outer(col,Aug[c]),P)
Minv=Aug[:,n:]
chk=np.mod(M@Minv,P); ok=np.allclose(chk,np.eye(n))
print('Minv check I:',ok)
assert ok
np.save(f'H_{tag}_8000.npy',H); np.save(f'Minv_{tag}_8000.npy',Minv)
print('saved',tag)
