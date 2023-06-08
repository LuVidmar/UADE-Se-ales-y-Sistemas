import numpy as np
import matplotlib.pyplot as plt

def square(t):
    return np.heaviside(t,1) - np.heaviside(t-1,1)

# --- INGRESO ---

t0 = -1 # tiempo inicial
tn = 2 # tiempo final
n = 500 # cantidad de muestras

# --- PROCEDIMIENTO ---

# vector de tiempo
dt = (tn-t0)/n # intervalo de tiempo
ti = np.arange(t0,tn,dt) # vector de tiempo

# Senal
senal = square(ti)

# Imprimo
np.set_printoptions(precision = 4)
print('tiempo: ')
print(ti)
print('señal: x(t) ')
print(senal)

# Gráfica
plt.plot(ti,senal, color="red")
plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.xlabel('t')
plt.ylabel('señal x[(t)]')
plt.show()