import numpy as np
import matplotlib.pyplot as plt
import sys

# --- FUNCIONES ---
def ddf(n):
    return 1 if n == 0 else 0

# --- INGRESO ---
if len(sys.argv) > 1:
    arg = sys.argv[1]
n0 = -1 # tiempo inicial
m = 3 # cantidad de muestras

# --- PROCEDIMIENTO ---

# vector n discreto [n0,n0+m]
n = np.arange(n0,n0 + m,1)

# señal
senal = [ddf(nk) for nk in n]

# Imprimo
np.set_printoptions(precision=4)
if arg != 'no-print':
    print('n: ')
    print(n)
    print('señal x[n]: ')
    print(senal)

# Gráficas
plt.xlabel('n')
plt.ylabel('señal x[n]')
plt.stem(n, senal)
plt.show()