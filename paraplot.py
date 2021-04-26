import numpy as np
import matplotlib.pyplot as plt


for N in range(4,5):
    for epsilon in np.arange(0.35, 0.6, 0.05):
        Omega = np.arange(0,2, 0.01)
        H = 1/np.sqrt(1 + (epsilon**2)*np.cosh(N*np.acosh(Omega))**2);
        plt.plot(Omega,H)

plt.xlabel(r'$\omega / \pi$')
plt.ylabel(r'$|H_{a, LP}(j \omega)|$')
# gtext('\epsilon = 0.35')
# gtext('\epsilon = 0.6')