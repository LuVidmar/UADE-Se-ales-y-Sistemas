import numpy as np
import matplotlib.pyplot as plt
import sys

"""
Para corroborar si un sistema es variable,
debo verificar que al desplazar la entrada en el tiempo,
la salida se desplaza en la misma cantidad.

x(t) -> y(t)
x(t - t0) -> y(t - t0)
"""

# Defino la entrada
x = lambda t: np.heaviside(t, 1) # u(t)

# Defino la salida
y = lambda t: t * x(t)

# Defino el tiempo
t = np.linspace(-0.5, 3, 200) # 200 muestras entre -0.5 y 3
t0 = 1/2 # desplazamiento

# Veamos si el sistema es variable
xd = lambda t: x(t-t0)
y1 = lambda t: t * xd(t)
y2 = lambda t: y(t-t0)

# Imprimo valores
if len(sys.argv) > 1:
    if sys.argv[1] != 'no-print':
        print('y(x(t - t0))')
        print(y1(t))
        print('y(t - t0)')
        print(y2(t))

# Grafico
plt.xlabel('t')
plt.ylabel('señal')
plt.axvline(0, color='gray')
plt.axhline(0, color='gray')
plt.plot(t, x(t), label='x(t)')
plt.plot(t, y(t), label='y(x(t))')
plt.plot(t, y1(t), label='y(x(t - t0))')
plt.plot(t, y2(t), label='y(t - t0)')
plt.legend()
plt.show()

"""
El sistema es variable, ya que:
y(x(t - t0)) != y(t - t0)
"""