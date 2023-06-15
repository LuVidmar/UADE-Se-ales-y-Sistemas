import numpy as np
import matplotlib.pyplot as plt
import sys

def square(t):
    return np.heaviside(t,1) - np.heaviside(t-1,1)

# --- INGRESO ---
arg = sys.argv[1]
t0 = -20 # tiempo inicial
tn = 20 # tiempo final
n = 1000 # cantidad de muestras

# --- PROCEDIMIENTO ---

# vector de tiempo
dt = (tn-t0)/n # intervalo de tiempo
ti = np.arange(t0,tn,dt) # vector de tiempo

# Senal
senal = np.zeros(len(ti)) # vector de ceros
for i in range(t0, tn, 5):
    senal += square(ti-i) # suma de señales cuadradas

# Imprimo
np.set_printoptions(precision = 4)
if arg != 'no-print':
    print('tiempo: ')
    print(ti)
    print('señal: x(t) ')
    print(senal)

# Gráfica
plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.plot(ti,senal, color="red")
plt.xlabel('t')
plt.ylabel('señal x[(t)]')
plt.show()