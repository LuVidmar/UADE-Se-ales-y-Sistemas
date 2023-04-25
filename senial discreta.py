# Señales discretas


import numpy as np
import matplotlib.pyplot as plt

# INGRESO - parámetros
w0 = 2*np.pi/12
fx = lambda n: np.sin(w0*n)
n0 = 0
m = 20

# PROCEDIMIENTO
# vector n discreto [n,m)
n = np.arange(n0,m+1,1)

# señal
senal = fx(n)

# SALIDA
np.set_printoptions(precision=4)
print('n: ')
print(n)
print('señal x[n]: ')
print(senal)

# Gráficas
plt.stem(n, senal)
plt.xlabel('n')
plt.ylabel('señal x[n]')
plt.show()