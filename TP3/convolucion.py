import numpy as np
import matplotlib.pyplot as plt
import sys

"""
Basado en el ejemplo que se muestra en:
https://es.wikipedia.org/wiki/Convoluci%C3%B3n

Definimos:
f(t) = square(t) = u(t+1/2) - u(t-1/2)
g(t) = e ^ -(t-1) * u(t)
"""

def square(t):
    return np.heaviside(t+1/2, 1) - np.heaviside(t-1/2, 1)

# Defino las funciones a convolucionar
f = lambda t: square(t)
g = lambda t: np.exp(-t+1) * np.heaviside(t, 1)

# Defino el tiempo
m = 500 # muestras
t = np.linspace(-1, 3, m) # m muestras entre -2 y 2

# Convolucion
y = np.convolve(f(t), g(t),'full')

# Defino el tiempo de convolución
t1 = np.linspace(-1, 3, 2*m-1) # 2m-1 muestras entre -2 y 2

# Imprimo valores
if len(sys.argv) > 1:
    if sys.argv[1] != 'no-print':
        print('y(t)')
        print(y)

# Grafico
fig, ax1 = plt.subplots(figsize=(8, 8))
ax2 = ax1.twinx()

ax1.axvline(0, color='gray')
ax1.axhline(0, color='gray')

ax1.plot(t, f(t), label='f(t)', color='red')
ax1.plot(t, g(t), label='g(t)', color='blue')
ax2.plot(t1, y, label='y(t) = {f*g}(t)', color='green')

ax1.set_xlabel("t")
ax1.set_ylabel("f,g")
ax1.tick_params(axis="y")
ax2.set_ylabel("y")
ax2.tick_params(axis="y")

fig.legend()
plt.show()