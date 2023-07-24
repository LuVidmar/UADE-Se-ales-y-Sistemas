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
m = 10 - 1 # muestras por división
dn = 1/m

inicio = -5
fin = 5

n = np.arange(inicio, fin + dn, dn)

y  = np.convolve(f(n), g(n), 'same') * (dn)
'''
# Grafico
fig, ax1 = plt.subplots(figsize=(8, 8))
ax2 = ax1.twinx()

ax1.axvline(0, color='gray')
ax1.axhline(0, color='gray')

ax1.plot(t, f(t), label='f(t)', color='red')
ax1.plot(t, g(t), label='g(t)', color='blue')
ax2.plot(t, y, label='y(t) = {f*g}(t)', color='green')

ax1.set_xlabel("t")
ax1.set_ylabel("f,g")
ax1.tick_params(axis="y")
ax2.set_ylabel("y")
ax2.tick_params(axis="y")

plt.tight_layout()

plt.axvline(x=0.5, ls='--')

fig.legend()
plt.show()
'''

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

stem3 = ax2.stem(n, y, label='y[n] = {f*g}[n]')
stem3.markerline.set_color('red')
stem3.stemlines.set_color('red')

ax1.set_xlabel("n")
ax1.set_ylabel("f,g")
ax1.tick_params(axis="y")
ax2.set_ylabel("y")
ax2.tick_params(axis="y")

fig.legend()
plt.show()