import numpy as np
import matplotlib.pyplot as plt

a = 1

# Definimos el rango de tiempo
m = 1000 # número de muestras
t = np.linspace(-2, 2, m+1)

# Definimos la función Delta Dirac
def delta(t):
    d = np.where(t == 0.0, 1e100, 0) # Función Delta de Dirac, uso 1e100 porque si pongo infinito, el programa no funciona.
    return d
# AVISO: Se la definió de esta manera debido a que por calculo directo usando la definición se llegaba a un resultado no correcto.
def delta_fourier(w,t0): # Transformada de Fourier de la función Delta de Dirac
    d_f = np.exp(-1j*w*t0) # e^(-j*w*t0) -> la inserto de manera manual, porque de la otra manera se rompe el programa.
    return d_f

# Definimos la transformada de Fourier de x(t)
def X(w, x):
    integrand = x * np.exp(-1j*w*t) # Contenido de la integral -> x(t) * e^(-j*w*t)
    integral = np.trapz(integrand, t) # Calculo la integral usando la regla del trapecio con los valores de t.
    return integral

# Definimos el rango de frecuencia
w = np.linspace(-10, 10, m+1)

# Definimos las funciones y sus transformadas de Fourier
x1 = np.exp(-a*t) * np.heaviside(t, 1) # Función 1
Xw1 = np.array([X(wi, x1) for wi in w]) # Transformada de Fourier de la función 1
Xw1R = np.real(Xw1) # Parte real de la transformada de Fourier de la función 1
Xw1I = np.imag(Xw1) # Parte imaginaria de la transformada de Fourier de la función 1
# Módulo de la transformada de Fourier de la función 1
if np.all(Xw1R == 0):
    Xw1M = Xw1I
elif np.all(Xw1I == 0.0):
    Xw1M = Xw1R
else:
    Xw1M = np.sqrt(np.power(Xw1R, 2) + np.power(Xw1I, 2))
# Fase de la transformada de Fourier de la función 1
if np.all(Xw1R == 0):
    # llenar de 1.5 como la cantidad de muestras para demostrar de que tiende a infinito
    Xw1F = np.ones_like(w) * 1.5
elif np.all(Xw1I == 0.0):
    Xw1F = np.zeros_like(w)
else:
    Xw1F = np.arctan2(Xw1I, Xw1R)

x2 = np.exp(-a*np.abs(t)) # Función 2
Xw2 = np.array([X(wi, x2) for wi in w]) # Transformada de Fourier de la función 2
Xw2R = np.real(Xw2) # Parte real de la transformada de Fourier de la función 2
Xw2I = np.zeros_like(w) # Parte imaginaria de la transformada de Fourier de la función 2
# Módulo de la transformada de Fourier de la función 2
if np.all(Xw2R == 0):
    Xw2M = Xw2I
elif np.all(Xw2I == 0.0):
    Xw2M = Xw2R
else:
    Xw2M = np.sqrt(np.power(Xw2R, 2) + np.power(Xw2I, 2))
# Fase de la transformada de Fourier de la función 2
if np.all(Xw2R == 0):
    # llenar de 1.5 como la cantidad de muestras para demostrar de que tiende a infinito
    Xw2F = np.ones_like(w) * 1.5
elif np.all(Xw2I == 0.0):
    Xw2F = np.zeros_like(w)
else:
    Xw2F = np.arctan2(Xw2I, Xw2R)

x3 = np.heaviside(t+1, 1) - np.heaviside(t-1, 1) # Función 3
Xw3 = np.array([X(wi, x3) for wi in w]) # Transformada de Fourier de la función 3
Xw3R = np.real(Xw3) # Parte real de la transformada de Fourier de la función 3
Xw3I = np.zeros_like(w) # Parte imaginaria de la transformada de Fourier de la función 3
# Módulo de la transformada de Fourier de la función 3
if np.all(Xw3R == 0):
    Xw3M = Xw3I
elif np.all(Xw3I == 0.0):
    Xw3M = Xw3R
else:
    Xw3M = np.sqrt(np.power(Xw3R, 2) + np.power(Xw3I, 2))
# Fase de la transformada de Fourier de la función 3
if np.all(Xw3R == 0):
    # llenar de 1.5 como la cantidad de muestras para demostrar de que tiende a infinito
    Xw3F = np.ones_like(w) * 1.5
elif np.all(Xw3I == 0.0):
    Xw3F = np.zeros_like(w)
else:
    Xw3F = np.arctan2(Xw3I, Xw3R)

x4 = delta(t) # Función 4
Xw4 = delta_fourier(w,0) # Transformada de Fourier de la función 4
Xw4R = np.real(Xw4) # Parte real de la transformada de Fourier de la función 4
Xw4I = np.imag(Xw4) # Parte imaginaria de la transformada de Fourier de la función 4
# Módulo de la transformada de Fourier de la función 4
if np.all(Xw4R == 0):
    Xw4M = Xw4I
elif np.all(Xw4I == 0.0):
    Xw4M = Xw4R
else:
    Xw4M = np.sqrt(np.power(Xw4R, 2) + np.power(Xw4I, 2))
# Fase de la transformada de Fourier de la función 4
if np.all(Xw4R == 0):
    # llenar de 1.5 como la cantidad de muestras para demostrar de que tiende a infinito
    Xw4F = np.ones_like(w) * 1.5
elif np.all(Xw4I == 0.0):
    Xw4F = np.zeros_like(w)
else:
    Xw4F = np.arctan2(Xw4I, Xw4R)

fig, axs = plt.subplots(nrows=5, ncols=4, figsize=(16, 8))

axs[0, 0].plot(t, x1, label='x1(t)', color='blue')
axs[0, 0].set_xlabel('t')
axs[0, 0].set_ylabel('x1(t)')
axs[1, 0].plot(w, Xw1R, label='Re{X1(w)}', color='red')
axs[1, 0].set_xlabel('w')
axs[1, 0].set_ylabel('Re{X1(w)}')
axs[2, 0].plot(w, Xw1I, label='Im{X1(w)}', color='green')
axs[2, 0].set_xlabel('w')
axs[2, 0].set_ylabel('Im{X1(w)}')
axs[3, 0].plot(w, Xw1M, label='|X1(w)|', color='orange')
axs[3, 0].set_xlabel('w')
axs[3, 0].set_ylabel('|X1(w)|')
axs[4, 0].plot(w, Xw1F, label='Fase{X1(w)}', color='purple')
axs[4, 0].set_xlabel('w')
axs[4, 0].set_ylabel('Fase{X1(w)}')

axs[0, 1].plot(t, x2, label='x2(t)', color='blue')
axs[0, 1].set_xlabel('t')
axs[0, 1].set_ylabel('x2(t)')
axs[1, 1].plot(w, Xw2R, label='Re{X2(w)}', color='red')
axs[1, 1].set_xlabel('w')
axs[1, 1].set_ylabel('Re{X2(w)}')
axs[2, 1].plot(w, Xw2I, label='Im{X2(w)}', color='green')
axs[2, 1].set_xlabel('w')
axs[2, 1].set_ylabel('Im{X2(w)}')
axs[3, 1].plot(w, Xw2M, label='|X2(w)|', color='orange')
axs[3, 1].set_xlabel('w')
axs[3, 1].set_ylabel('|X2(w)|')
axs[4, 1].plot(w, Xw2F, label='Fase{X2(w)}', color='purple')
axs[4, 1].set_xlabel('w')
axs[4, 1].set_ylabel('Fase{X2(w)}')

axs[0, 2].plot(t, x3, label='x3(t)', color='blue')
axs[0, 2].set_xlabel('t')
axs[0, 2].set_ylabel('x3(t)')
axs[1, 2].plot(w, Xw3R, label='Re{X3(w)}', color='red')
axs[1, 2].set_xlabel('w')
axs[1, 2].set_ylabel('Re{X3(w)}')
axs[2, 2].plot(w, Xw3I, label='Im{X3(w)}', color='green')
axs[2, 2].set_xlabel('w')
axs[2, 2].set_ylabel('Im{X3(w)}')
axs[3, 2].plot(w, Xw3M, label='|X3(w)|', color='orange')
axs[3, 2].set_xlabel('w')
axs[3, 2].set_ylabel('|X3(w)|')
axs[4, 2].plot(w, Xw3F, label='Fase{X3(w)}', color='purple')
axs[4, 2].set_xlabel('w')
axs[4, 2].set_ylabel('Fase{X3(w)}')

axs[0, 3].plot(t, x4, label='x4(t)', color='blue')
axs[0, 3].set_xlabel('t')
axs[0, 3].set_ylabel('x4(t)')
axs[1, 3].plot(w, Xw4R, label='Re{X4(w)}', color='red')
axs[1, 3].set_xlabel('w')
axs[1, 3].set_ylabel('Re{X4(w)}')
axs[2, 3].plot(w, Xw4I, label='Im{X4(w)}', color='green')
axs[2, 3].set_xlabel('w')
axs[2, 3].set_ylabel('Im{X4(w)}')
axs[3, 3].plot(w, Xw4M, label='|X4(w)|', color='orange')
axs[3, 3].set_xlabel('w')
axs[3, 3].set_ylabel('|X4(w)|')
axs[4, 3].plot(w, Xw4F, label='Fase{X4(w)}', color='purple')
axs[4, 3].set_xlabel('w')
axs[4, 3].set_ylabel('Fase{X4(w)}')

#ajuste de los subplots con hsapce y wspace
plt.subplots_adjust(hspace=0.5, wspace=0.5)
# Grafico
plt.show()