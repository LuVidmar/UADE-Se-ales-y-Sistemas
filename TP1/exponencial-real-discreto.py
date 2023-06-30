import numpy as np
import matplotlib.pyplot as plt
import sys

# --- INGRESO ---
if len(sys.argv) > 1:
    arg = sys.argv[1]
n0 = -1 # tiempo inicial
m = 7 # cantidad de muestras

# --- PROCEDIMIENTO ---

# vector n discreto [n0,n0+m]
n = np.arange(n0,n0 + m,1)

# señal
senal = np.exp(n) # e^(n)

# Imprimo
np.set_printoptions(precision=4)
if arg != 'no-print':
    print('n: ')
    print(n)
    print('señal x[n]: ')
    print(senal)

# Gráficas
plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.stem(n, senal)
plt.xlabel('n')
plt.ylabel('señal x[n]')
plt.show()