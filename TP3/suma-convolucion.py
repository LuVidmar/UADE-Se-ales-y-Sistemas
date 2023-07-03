import numpy as np
import matplotlib.pyplot as plt
import sys

"""
Basado en el ejemplo que se muestra en:
https://es.wikipedia.org/wiki/Convoluci%C3%B3n

Definimos:
f(n) = square(n) = u(n+1/2) - u(n-1/2)
g(n) = e ^ -(n-1) * u(n)
"""

def square(n):
    return np.heaviside(n+1/2, 1) - np.heaviside(n-1/2, 1)

# Defino las funciones a convolucionar
f = lambda n: square(n)
g = lambda n: np.exp(-n+1) * np.heaviside(n, 1)

# Defino el tiempo
m = 20 # muestras
n = np.linspace(-1, 3, m) # m muestras entre -2 y 2

# Convolucion
y = np.convolve(f(n), g(n),'full')

# Defino el tiempo de convolución
n1 = np.linspace(-1, 3, 2*m-1) # 2m-1 muestras entre -2 y 2

# Imprimo valores
if len(sys.argv) > 1:
    if sys.argv[1] != 'no-print':
        print('y[n]')
        print(y)

# Grafico
fig, ax1 = plt.subplots(figsize=(8, 8))
ax2 = ax1.twinx()

ax1.axvline(0, color='gray')
ax1.axhline(0, color='gray')

stem1 = ax1.stem(n, f(n), label='f[n]')
stem1.markerline.set_color('blue')
stem1.stemlines.set_color('blue')

stem2 = ax1.stem(n, g(n), label='g[n]')
stem2.markerline.set_color('green')
stem2.stemlines.set_color('green')

stem3 = ax2.stem(n1, y, label='y[n] = {f*g}[n]')
stem3.markerline.set_color('red')
stem3.stemlines.set_color('red')

ax1.set_xlabel("n")
ax1.set_ylabel("f,g")
ax1.tick_params(axis="y")
ax2.set_ylabel("y")
ax2.tick_params(axis="y")

fig.legend()
plt.show()