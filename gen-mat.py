
import scipy.sparse

import sys

if __name__ == '__main__':
    density=0.2
    n=10
    if len(sys.argv)==2:
        #print(sys.argv)
        n=int(sys.argv[1])
        mat=scipy.sparse.rand(n, n, density=density, format="csr")
        scipy.sparse.save_npz('tmp.npz', mat)
