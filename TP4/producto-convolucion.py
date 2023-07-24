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
x = lambda t: np.exp(-t+1) * np.heaviside(t, 1)
h1 = lambda t: np.heaviside(t, 1) - np.heaviside(t-1, 1) #Cajon unitario, altura 1, entre 0 y 1
h2 = lambda t: -np.heaviside(t-1, 1) + np.heaviside(t-2, 1) #Cajon unitario, altura -1, entre 1 y 2
h3 = lambda t: (t-2) * np.heaviside(t-2, 1) - (t-3) * np.heaviside(t-3, 1) - np.heaviside(t-3, 1) #Rampa unitaria, con pendiente 1, entre 2 y 3
he = lambda t: h1(t) + h2(t) + h3(t)

# Defino el tiempo
m = 500 # muestras
dt = 1/m
inicio = -5
fin = 5
t = np.arange(inicio, fin + dt, dt) # vector de tiempo


# Convolucion con h1(t)
y1 = np.convolve(x(t), h1(t),'same')*dt # Convolucion entre x y h1

# Convolucion con h2(t)
y2 = np.convolve(x(t), h2(t),'same')*dt # Convolucion entre x y h2

# Convolucion con h3(t)
y3 = np.convolve(x(t), h3(t),'same')*dt # Convolucion entre x y h3

# Convolucion h1(t) + h2(t) + h3(t)
yt = y1 + y2 + y3 

# Convolucion con he(t)
y = np.convolve(x(t), he(t),'same')*dt # Convolucion entre x y he

# Imprimo valores
if len(sys.argv) > 1:
    if sys.argv[1] != 'no-print':
        print('y(t)')
        print(y)

# Graficos

#Figura 1
#h1
fig1, ax1 = plt.subplots(4,1, figsize=(8, 8))

#Pinto los ejes
ax1[0].axvline(0, color='gray')
ax1[0].axhline(0, color='gray')
ax1[1].axvline(0, color='gray')
ax1[1].axhline(0, color='gray')
ax1[2].axvline(0, color='gray')
ax1[2].axhline(0, color='gray')
ax1[3].axvline(0, color='gray')
ax1[3].axhline(0, color='gray')

ax1[0].plot(t, h1(t), label='h1(t)', color='blue')
ax1[0].set_title('h(t)')
ax1[0].legend()
ax1[0].grid()
#h2
ax1[1].plot(t, h2(t), label='h2(t)', color='red')
ax1[1].legend()
ax1[1].grid()
#h3
ax1[2].plot(t, h3(t), label='h3(t)', color='green')
ax1[2].legend()
ax1[2].grid()
#he
ax1[3].plot(t, he(t), label='he(t)', color='blue')
ax1[3].legend()
ax1[3].grid()

ax1[0].set_title('h1(t) = u(t)-u(t-1)')
ax1[0].set_ylabel("h")
ax1[0].set_xlabel("h")
ax1[1].set_title('h2(t) = -u(t-1)+u(t-2)')
ax1[1].set_ylabel("h")
ax1[1].set_xlabel("t")
ax1[2].set_title('h3(t) = rampa(t-2)-rampa(t-3)-u(t-3)')
ax1[2].set_ylabel("h")
ax1[2].set_xlabel("t")
ax1[3].set_title('he(t) = h1 + h2 + h3')
ax1[3].set_ylabel("h")
ax1[3].set_xlabel("t")

#Figura 2
fig2, ax2 = plt.subplots(4,1, figsize=(8, 8))

#Pinto los ejes
ax2[0].axvline(0, color='gray')
ax2[0].axhline(0, color='gray')
ax2[1].axvline(0, color='gray')
ax2[1].axhline(0, color='gray')
ax2[2].axvline(0, color='gray')
ax2[2].axhline(0, color='gray')
ax2[3].axvline(0, color='gray')
ax2[3].axhline(0, color='gray')

ax2[0].plot(t, y1, label='y1(t)', color='red')
ax2[0].legend()
ax2[0].grid()

ax2[1].plot(t, y2, label='y2(t)', color='green')
ax2[1].legend()
ax2[1].grid()

ax2[2].plot(t, y3, label='y3(t)', color='blue')
ax2[2].legend()
ax2[2].grid()

ax2[3].plot(t, yt, label='yt(t)', color='violet')
ax2[3].legend()
ax2[3].grid()

ax2[0].set_title('y1(t) = {x*h1t}(t)')
ax2[0].set_ylabel("y")
ax2[0].set_xlabel("t")
ax2[1].set_title('y2(t) = {x*h2t}(t)')
ax2[1].set_ylabel("y")
ax2[1].set_xlabel("t")
ax2[2].set_title('y3(t) = {x*h3t}(t)')
ax2[2].set_ylabel("y")
ax2[2].set_xlabel("t")
ax2[3].set_title('yt(t) = {x*he}(t)')
ax2[3].set_ylabel("y")
ax2[3].set_xlabel("t")

#Figura 3
fig3, ax3 = plt.subplots(2,1, figsize=(8, 8))

#Pinto los ejes
ax3[0].axvline(0, color='gray')
ax3[0].axhline(0, color='gray')
ax3[1].axvline(0, color='gray')
ax3[1].axhline(0, color='gray')

ax3[0].plot(t, x(t), label='x(t)', color='red')
ax3[0].plot(t, he(t), label='he(t)', color='blue')
ax3[0].legend()
ax3[0].grid()
ax3[1].plot(t, y, label='y(t)', color='green')
ax3[1].legend()
ax3[1].grid()

ax3[0].set_title('x(t)=e^(-t+1).u(t) & he(t)')
ax3[0].set_xlabel("t")
ax3[0].set_ylabel("x,he")

ax3[1].set_title('y(t) = {x*he}(t)')
ax3[1].set_ylabel("y")
ax3[1].set_xlabel("t")
ax3[1].tick_params(axis="y")

#Figura 4
fig4, ax4 = plt.subplots(2,1, figsize=(8, 8))

#Pinto los ejes
ax4[0].axvline(0, color='gray')
ax4[0].axhline(0, color='gray')
ax4[1].axvline(0, color='gray')
ax4[1].axhline(0, color='gray')

ax4[0].plot(t, yt, label='yt(t)', color='violet')
ax4[0].legend()
ax4[0].grid()

ax4[1].plot(t, y, label='y(t)', color='green')
ax4[1].legend()
ax4[1].grid()

ax4[0].set_title('yt(t) = y1(t) + y2(t) + y3(t)')
ax4[0].set_ylabel("y")
ax4[0].set_xlabel("t")
ax4[1].set_title('y(t) = x(t) * he(t)')
ax4[1].set_ylabel("y")
ax4[1].set_xlabel("t")

fig1.tight_layout()
fig2.tight_layout()
fig3.tight_layout()
fig4.tight_layout()
plt.show()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     