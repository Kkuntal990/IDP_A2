import numpy as np

def cheb(N):
    v = [1 ,0]
    u = [1]

    if N == 0:
        w = u

    elif  N == 1:
        w = v

    else:

        for __ in range(N-1):
            p = np.convolve([2 ,0], v)
            m = len(p)
            n = len(u)

            w = p + np.pad(u, (m-n,0))
            u = v
            v = w

    return w
