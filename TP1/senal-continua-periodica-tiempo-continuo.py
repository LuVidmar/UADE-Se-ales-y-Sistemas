import numpy as np
import matplotlib.pyplot as plt
import sys

# --- INGRESO ---
arg = ""
if len(sys.argv) > 1:
    arg = sys.argv[1]
t0 = -2 * np.pi # tiempo inicial
tn = 2 * np.pi # tiempo final
n = 100 # cantidad de muestras

# --- PROCEDIMIENTO ---

# vector de tiempo
dt = (tn-t0)/n # intervalo de tiempo
ti = np.arange(t0,tn,dt) # vector de tiempo

# Senal
senal = np.sin(ti)

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