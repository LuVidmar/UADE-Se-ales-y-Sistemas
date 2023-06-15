import numpy as np
import matplotlib.pyplot as plt
import sys

# --- INGRESO ---
arg = sys.argv[1]
n0 = -10 # discreto inicial
m = 20 # cantidad de muestras

# --- PROCEDIMIENTO ---

# vector n discreto [n0,n0+m]
n = np.arange(n0,n0 + m,1)

# Senal
senal = np.exp(1j*np.pi*n/10) # e^(j*pi*n/10)

# Parte real
x = [ele.real for ele in senal]
# Parte imaginaria
y = [ele.imag for ele in senal]


# Imprimo
np.set_printoptions(precision=4)
if arg != 'no-print':
    print('n: ')
    print(n)
    print('señal x[n]: ')
    print(senal)

# Gráfica
plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.stem(x, y)
plt.ylabel('Imaginario')
plt.xlabel('Real')
plt.show()