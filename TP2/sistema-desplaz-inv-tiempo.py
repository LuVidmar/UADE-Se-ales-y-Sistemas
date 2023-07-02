import numpy as np
import matplotlib.pyplot as plt
import sys

"""
Definimos:
1. Entrada del sistema: x(t) un cajon de 1 de ancho desde t=0
2. Sistema: h(t) un triangulo de 1 de ancho y 1 de alto desde t=0
3. Salida del sistema: y(t) = {h(t)*x(t)} convolucion de h(t) y x(t)
"""

def rect(t):
    return np.heaviside(t+1/2, 1) - np.heaviside(t-1/2, 1)

def triangle(t):
    returnarr = []
    for i in t:
        if 1 - np.abs(i) < 0:
            returnarr.append(0)
        else:
            returnarr.append(1 - np.abs(i))
    return returnarr * np.heaviside(t, 1)

# Defino la entrada
x = lambda t: rect(t)

# Defino el sistema
h = lambda t: triangle(t)

# Defino el tiempo
m = 200 # muestras
t = np.linspace(-2, 2, m) # m muestras entre -2 y 2
t0 = 0.5 # desplazamiento

# Sistema sin desplazamiento
y1 = np.convolve(x(t), h(t),'full')

# Sistema con desplazamiento
y2 = np.convolve(x(t), h(t0-t),'full')

# Defino el tiempo de convolución
t1 = np.linspace(-2, 2, 2*m-1) # 2m-1 muestras entre -2 y 2

# Imprimo valores
if len(sys.argv) > 1:
    if sys.argv[1] != 'no-print':
        print('y(t)')
        print(y1)
        print('yd(t)')
        print(y2)

# Grafico
fig, ax1 = plt.subplots(figsize=(8, 8))
ax2 = ax1.twinx()

ax1.axvline(0, color='gray')
ax1.axhline(0, color='gray')

ax1.plot(t1, h(t1), label='h(t)', color='red')
ax1.plot(t1, h(t1-t0), label='h(t-t0)', color='blue')
ax1.plot(t1, x(t1), label='x(t)', color='green')
ax2.plot(t1, y1, label='y(t) = {h(t)*x(t)}', color='red', linestyle='--')
ax2.plot(t1, y2, label='yd(t) = {h(t0-t)*x(t)}', color='blue', linestyle='--')

ax1.set_xlabel("t")
ax1.set_ylabel("x,h")
ax1.tick_params(axis="y")
ax2.set_ylabel("y")
ax2.tick_params(axis="y")

fig.legend()
plt.show()