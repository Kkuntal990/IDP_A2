import numpy as np

def add(x,y):
    m = len(x)
    n = len(y)

    if m==n:
        z = x + y
    elif m > n:
        z = x + np.pad(y, (m-n,0))
    else:
        z = y + np.pad(y, (n-m,0))

    return z