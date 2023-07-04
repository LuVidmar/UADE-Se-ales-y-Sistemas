import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import sys

# --- INGRESO ---
arg = ""
if len(sys.argv) > 1:
    arg = sys.argv[1]
n0 = -6 # tiempo inicial
m = 13 # cantidad de muestras
k = np.pi # desplazamiento

# --- PROCEDIMIENTO ---

# vector de tiempo discreto
ti = np.arange(n0,n0+m)

# Senal
senal = np.sin(ti-k)

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