import numpy as np
import matplotlib.pyplot as plt
import sys

"""
Definimos:
1. Entrada del sistema: x1(t) un cajon de 1 de ancho centrado en t=0, x2(t) un cajon de 2 de ancho centrado en t=0
2. Sistema: h(t) un triangulo de 1 de ancho y 1 de alto desde t=0
3. Salida del sistema: y(t) = {h(t)*(k1*x1(t)+k2*x2(t))} convolucion de h(t) y la suma de x(t)
"""

def rect1(t):
    return np.heaviside(t+1/2, 1) - np.heaviside(t-1/2, 1)

def rect2(t):
    return (np.heaviside(t+1, 1) - np.heaviside(t-1, 1)) * 1/2

def triangle(t):
    returnarr = []
    for i in t:
        if 1 - np.abs(i) < 0:
            returnarr.append(0)
        else:
            returnarr.append(1 - np.abs(i))
    return returnarr * np.heaviside(t, 1)

# Defino la entrada
x1 = lambda t: rect1(t)
x2 = lambda t: rect2(t)

# Defino el sistema
h = lambda t: triangle(t)

# Defino el tiempo
m = 200 # muestras
t = np.linspace(-2, 2, m) # m muestras entre -2 y 2
k1 = 0.5 # constante de escala
k2 = 3 # constante de escala

# Sistema sin suma
y0 = np.convolve(x1(t), h(t),'full')
y1 = np.convolve(x2(t), h(t),'full')
# Sistema con suma
y2 = np.convolve(k1*x1(t)+k2*x2(t), h(t),'full')

# Defino el tiempo de convolución
t1 = np.linspace(-2, 2, 2*m-1) # 2m-1 muestras entre -2 y 2

# Imprimo valores
if len(sys.argv) > 1:
    if sys.argv[1] != 'no-print':
        print('y(t)')
        print(y1)
        print('ys(t)')
        print(y2)

# Grafico
fig, ax1 = plt.subplots(figsize=(8, 8))
ax2 = ax1.twinx()

ax1.axvline(0, color='gray')
ax1.axhline(0, color='gray')

ax1.plot(t1, h(t1), label='h(t)', color='blue')
ax1.plot(t1, x1(t1), label='x1(t)', color='green')
ax1.plot(t1, x2(t1), label='x2(t)', color='magenta')
ax2.plot(t1, y0, label='y1(t) = {h*x1}(t)', color='green', linestyle='--')
ax2.plot(t1, y1, label='y2(t) = {h*x2}(t)', color='magenta', linestyle='--')
ax2.plot(t1, y2, label='y(t) = {h*(1/2*x1+3*x2)}(t)', color='red')

ax1.set_xlabel("t")
ax1.set_ylabel("x,h")
ax1.tick_params(axis="y")
ax2.set_ylabel("y")
ax2.tick_params(axis="y")

fig.legend()
plt.show()