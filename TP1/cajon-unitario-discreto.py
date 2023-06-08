import numpy as np
import matplotlib.pyplot as plt

def square(n):
    return np.heaviside(n,1) - np.heaviside(n-1.5,1)

# --- INGRESO ---

n0 = -1 # tiempo inicial
m = 4 # cantidad de muestras

# --- PROCEDIMIENTO ---

# vector n discreto [n0,n0+m]
n = np.arange(n0,n0 + m,1)

# señal
senal = square(n)

# Imprimo
np.set_printoptions(precision=4)
print('n: ')
print(n)
print('señal x[n]: ')
print(senal)

# Gráficas
plt.xlabel('n')
plt.ylabel('señal x[n]')
plt.stem(n, senal)
plt.show()