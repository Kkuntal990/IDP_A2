import numpy as np
from polypower import polypower
from add import add

def bilin(p, om):
    N = len(p)

    const = [-1 ,1]
    v = 1
    if N > 2:

        for i in range(N-1):
            v = np.convolve(v, const)
            v = add(v, p(i+1)*polypower([1 ,1], i))

        digden = v

    elif N == 2:

        M = len(v)
        v(M-1) = v(M-1) + p(N)
        v(M) = v(M) + p(N)
        digden = v

    else:
        digden = p



    dignum = polypower([-1 ,0 ,1], (N-1)/2)

    G_bp = abs(np.polyval(digden, np.exp(-1j*om))/np.polyval(dignum, np.exp(-1j*om)))
