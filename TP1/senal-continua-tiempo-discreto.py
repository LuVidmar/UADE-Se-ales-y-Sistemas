import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import sys

# --- INGRESO ---
arg = ""
if len(sys.argv) > 1:
    arg = sys.argv[1]
n0 = -1 # tiempo inicial
m = 8 # cantidad de muestras

# --- PROCEDIMIENTO ---

# vector discreto
ti = np.arange(n0,n0+m,1)

# Senal
senal = np.exp(ti)

# Imprimo
np.set_printoptions(precision = 4)
if arg != 'no-print':
    print('tiempo: ')
    print(ti)
    print('señal: x[n] ')
    print(senal)

# Gráfica
plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.stem(ti, senal)
plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))
plt.xlabel('n')
plt.ylabel('señal x[n]')
plt.show()