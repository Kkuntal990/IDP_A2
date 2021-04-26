import numpy as np
import matplotlib.pyplot as plt
from para import *
from lpbp import lpbp
from bilin import bilin
from lp_stable_cheb import lp_stable_cheb

epsilon = 0.4

[p, G_lp] = lp_stable_cheb(epsilon, N)

Omega_L = np.arange(-2,2, 0.01)
H_analog_lp = G_lp*abs(1/np.polyval(p, 1j*Omega_L))

[num, den, G_bp] = lpbp(p, Omega_0, B, Omega_p1)

Omega = np.arange(-0.65, 0.65, 0.01)
H_analog_bp = G_bp*abs(np.polyval(num, 1j*Omega)/np.polyval(den, 1j*Omega))

[dignum, digden, G] = bilin(den, omega_p1)

omega = np.arange(-2*np.pi/5, 2*np.pi/5, np.pi/1000)
H_dig_bp = G*abs(np.polyval(dignum, np.exp(-1j*omega))/np.polyval(digden, np.exp(-1j*omega)))
plt.plot(omega/np.pi, H_dig_bp)
plt.xlabel(r'$\omega / \pi$')
plt.ylabel(r'$|H_{d, BP}(\omega)|$')

iir_num = G*dignum
iir_den = digden
