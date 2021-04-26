import numpy as np
from lattice import lattice
# %c = [0 0.44 0.36 0.02]
# %v = [1 0.4 0.18 - 0.2]

dignum = open("dignum.dat", "r")
digden = open("digden.dat", "r")

c = np.array(dignum.read().strip().split(), dtype=np.float64)
v = np.array(digden.read().strip().split(), dtype=np.float64)
#print(c[0], v[0])

C, K = lattice(c, v)


#print(C, K)