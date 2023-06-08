import numpy as np
import matplotlib.pyplot as plt

# --- FUNCIONES ---
def ddf(x,sig):
    if -(1/(2*sig)) <= x and x <= (1/(2*sig)):
        val = sig
    else:
        val = 0
    return val

# --- INGRESO ---

t0 = -1 # tiempo inicial
tn = 1 # tiempo final
n = 1000 # cantidad de muestras

# --- PROCEDIMIENTO ---

# vector de tiempo
dt = (tn-t0)/n # intervalo de tiempo
ti = np.arange(t0,tn,dt) # vector de tiempo

# Senal
senal = [ddf(t, 100) for t in ti]

# Imprimo
np.set_printoptions(precision = 4)
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