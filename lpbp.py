import numpy as np

def lpbp(p, Omega0, B, Omega_p2):
    N = len(p)
    const = [1 ,0 ,Omega0^2]
    v = const
    if N > 2 :
        for i in range(N-1):
            M = len(v)
            v(M-i) = v(M-i) + p(i+1)*B ^ i

            if i < N-1:
                v = np.convolve(const, v)
            #end
        #end

        den = v

    elif N == 2:
        M = len(v)
        v(M-1) = v(M-1) + p(N)*B
        den = v

    else:
        den = p

    num = np.zeros(N-1)
    num[0] = 1

    G_bp = abs(np.polyval(den, 1j*Omega_p2)/(np.polyval(num, 1j*Omega_p2)))

    return num, den, G_bp

