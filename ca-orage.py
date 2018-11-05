import scipy.sparse
from Orange.widgets.unsupervised.owcorrespondence import correspondence
mat = scipy.sparse.load_npz('tmp.npz')
#print(mat.shape)
ca=correspondence(mat.todense())
#print(ca.D)
