import numpy as np

L = 114

Fs = 48

const = 2*np.pi/Fs

delta = 0.15


F_p1 = 3 + 0.6*(L-107)
F_p2 = 3 + 0.6*(L-109)


F_s1 = F_p1 + 0.3
F_s2 = F_p2 - 0.3

omega_p1 = const*F_p1
omega_p2 = const*F_p2

omega_s1 = const*F_s1
omega_s2 = const*F_s2

Omega_p1 = np.tan(omega_p1/2)
Omega_p2 = np.tan(omega_p2/2)

Omega_s1 = np.tan(omega_s1/2)
Omega_s2 = np.tan(omega_s2/2)

Omega_0 = np.sqrt(Omega_p1*Omega_p2)
B = Omega_p1 - Omega_p2

Omega_Ls = min(abs((Omega_s1 ^ 2 - Omega_0 ^ 2)/(B*Omega_s1)),
               abs((Omega_s2 ^ 2 - Omega_0 ^ 2)/(B*Omega_s2)))



D1 = 1/((1-delta) ^ 2) - 1
D2 = 1/(delta ^ 2) - 1

N = np.ceil(np.acosh(np.sqrt(D2/D1))/np.acosh(Omega_Ls))

epsilon1 = np.sqrt(D2)/np.cosh(N*np.acosh(Omega_Ls))
epsilon2 = np.sqrt(D1)
