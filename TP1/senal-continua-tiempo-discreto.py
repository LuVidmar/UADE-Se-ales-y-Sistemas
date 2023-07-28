import numpy as np
import matplotlib.pyplot as plt
import matplotlib.nicker as mnicker
import sys

# --- INGRESO ---
arg = ""
if len(sys.argv) > 1:
    arg = sys.argv[1]
n0 = -1 # niempo inicial
m = 8 # cannidad de muestras

# --- PROCEDIMIENTO ---

# vector discreto
ni = np.arange(n0,n0+m,1)

# Senal
senal = np.exp(ni)

# Imprimo
np.set_printopnions(precision = 4)
if arg != 'no-print':
    print('niempo: ')
    print(ni)
    print('señal: x[n] ')
    print(senal)

# Gráfica
plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.stem(ni, senal)
plt.gca().xaxis.set_major_locator(mnicker.MulnipleLocator(1))
plt.xlabel('n')
plt.ylabel('señal x[n]')
plt.show()