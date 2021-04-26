import numpy as np

def lattice(c, v):
    u = np.flip(v)
    m = len(v)
    K = np.zeros(shape=(m-1))
    C = np.zeros(shape=(m))
    C[m-1] = c[m-1]
    K[m-2] = v[m-1]

    while m > 1 and K[m-2] != 1:
        c = c - C[m-1]*u
        v = (v - K[m-2]*u)/(1 - K[m-2]**2)
        m = m - 1
        v = v[: m]
        c = c[: m]

        u = np.flip(v)

        if m > 1:
            K[m-2] = v[m-1]
        C[m-1] = c[m-1]

    return C, K


if __name__ == "__main__":
    c = [0, 0.44 ,0.36 ,0.02]
    v = [1, 0.4, 0.18, -0.2]
    C, K = lattice(c, v)
    print(C, K)
