import numpy as np
from cheb import cheb
import matplotlib.pyplot as plt

epsilon = 0.4
N = 4


beta = ((np.sqrt(1+epsilon**2) + 1)/epsilon)**(1/N)
r1 = (beta**2-1)/(2*beta)
r2 = (beta**2+1)/(2*beta)


u = [1]
for n in range(N//2):
    phi = np.pi/2 + (2*n+1)*np.pi/(2*N)
    v = [1, -2*r1*np.cos(phi) ,(r1**2)*(np.cos(phi)**2)+(r2**2)*(np.sin(phi)**2)]
    p = np.convolve(v, u)
    print(p.shape)
    u = p


p1 = epsilon**2*np.convolve(cheb(N), cheb(N)) + [[0]*(2*N) + [1]]

G = abs(np.polyval(p, 1j))/np.sqrt(1+epsilon**2)


Omega = np.arange(0,2, 0.01)
H_stable = abs(G/np.polyval(p, 1j*Omega))
H_cheb = abs(np.sqrt(1/np.polyval(p1.reshape(-1), 1j*Omega)))
plt.plot(Omega, H_stable, 'x', markersize=4, label="Design")
plt.plot(Omega, H_cheb, label="Specification")

plt.xlabel(r'$\omega / \pi$')
plt.ylabel(r'$|H_{a, LP}(j \omega)|$')
plt.legend()
plt.show()
