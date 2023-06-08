import numpy as np
import matplotlib.pyplot as plt

# --- INGRESO ---

t0 = -1 # tiempo inicial
tn = 1 # tiempo final
n = 100 # cantidad de muestras

# --- PROCEDIMIENTO ---

# vector de tiempo
dt = (tn-t0)/n # intervalo de tiempo
ti = np.arange(t0,tn,dt) # vector de tiempo

# Senal
senal = np.exp(1j*2*np.pi*ti) # e^(j*2*pi*t)

# Parte real
x = [ele.real for ele in senal]
# Parte imaginaria
y = [ele.imag for ele in senal]

# Imprimo
np.set_printoptions(precision = 4)
print('tiempo: ')
print(ti)
print('señal: x(t) ')
print(senal)

# Gráfica
plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.plot(x,y, color="red", marker='.')
plt.ylabel('Imaginario')
plt.xlabel('Real')
plt.show()