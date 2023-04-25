# Señales continuas

import numpy as np
import matplotlib.pyplot as plt

# INGRESO parámetros
w  = 1
fx = lambda t: np.sin(w*t)
t0 = 0
tn = 2*np.pi
n = 50

# PROCEDIMIENTO
# vector de tiempo
dt = (tn-t0)/n
ti = np.arange(t0,tn,dt)

# señal
senal = fx(ti)

# SALIDA

np.set_printoptions(precision = 4)
print('tiempo: ')
print(ti)
print('señal: x(t) ')
print(senal)

# Gráfica
plt.plot(ti,senal)
plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.xlabel('t')
plt.ylabel('señal x[(t)]')
plt.show()