"""
La función dft(x) calcula la Transformada Discreta de Fourier (DFT) de la señal x.
La función fft(x) calcula la Transformada Rápida de Fourier (FFT) de la señal x.

El parámetro x es un array que representa la señal de entrada.

La función dft(x) devuelve un array que representa la DFT de la señal x.
La función fft(x) devuelve un array que representa la FFT de la señal x.

El número de puntos de muestra se define en la variable N.
El espaciado de muestra se define en la variable T.

La señal se genera en la variable y a partir de la variable x.
La DFT de la señal se calcula en la variable ydft.
La FFT de la señal se calcula en la variable yfft.
El eje de frecuencia se calcula en la variable xf.

Se grafica la señal, su DFT y su FFT.
"""

import numpy as np
import matplotlib.pyplot as plt
import time

def dft(x):
    """
    Calcula la Transformada Discreta de Fourier (DFT) de la señal x
    :param x: (array) señal de entrada
    :return: (array) DFT de la señal x
    """
    N = x.size # Número de puntos de muestra
    n = np.arange(N) # Vector de tiempo
    k = n.reshape((N, 1)) # Vector de frecuencia
    M = np.exp(-2j * np.pi * k * n / N) # Matriz de la DFT -> e^(-j*2*pi*k*n/N) , k = 0, 1, ..., N-1
    return np.dot(M, x) # Producto punto entre la matriz de la DFT y la señal de entrada

def fft(x):
    """
    Calcula la Transformada Rápida de Fourier (FFT) de la señal x
    :param x: (array) señal de entrada
    :return: (array) FFT de la señal x
    """
    N = x.size
    if N <= 32:
        return dft(x) # Si el número de puntos de muestra es menor o igual a 32, calculo la DFT
    else:
        X_even = fft(x[::2]) # FFT de los puntos pares
        X_odd = fft(x[1::2]) # FFT de los puntos impares
        factor = np.exp(-2j * np.pi * np.arange(N) / N) # Factor de la FFT -> e^(-j*2*pi*k/N) , k = 0, 1, ..., N-1
        return np.concatenate([X_even + factor[:int(N / 2)] * X_odd,
                               X_even + factor[int(N / 2):] * X_odd]) # Concatenación de las FFT de los puntos pares e impares
    

# Número de puntos de muestra (potencia de 2)
N = 2048

# Espaciado de muestra
T = 1.0 / N

# Generar una señal
t = np.linspace(0.0, 1.0, N)
y = np.sin(5.0 * 2.0 * np.pi * t) + 0.5 * np.sin(10.0 * 2.0 * np.pi * t) + 4.0 * np.cos(600.0 * 2.0 * np.pi * t) + 0.25 * np.cos(200.0 * 2.0 * np.pi * t)

# Calcular la DFT de la señal
start_time = time.time()
ydft = dft(y)
end_time = time.time()
timeOfExecutionDFT = end_time - start_time

# Calcular la FFT de la señal
start_time = time.time()
yfft = fft(y)
end_time = time.time()
timeOfExecutionFFT = end_time - start_time

# Calcular el eje de frecuencia
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

# Graficar la señal, su DFT y su FFT
fig, axs = plt.subplots(nrows=3, ncols=1, figsize=(16, 8))

axs[0].set_title('Señal')
axs[0].plot(t, y)
axs[0].set_xlabel('Tiempo (t)')
axs[0].set_ylabel('Amplitud')

axs[1].set_title('DFT')
axs[1].plot(xf, 2.0/N * np.abs(ydft[:N//2])) 
axs[1].set_xlabel('Frecuencia (Hz)')
axs[1].set_ylabel('Magnitud')

axs[2].set_title('FFT')
axs[2].plot(xf, 2.0/N * np.abs(yfft[:N//2]))
axs[2].set_ylabel('Magnitud')
axs[2].set_xlabel('Frecuencia (Hz)')

# Dar aviso en el gráfico de cuál es el tiempo de ejecución de la DFT y la FFT
axs[1].text(0.95, 0.95, 'Tiempo de ejecución DFT: {:.6f} s'.format(timeOfExecutionDFT), horizontalalignment='right', verticalalignment='top', transform=axs[1].transAxes)
axs[2].text(0.95, 0.95, 'Tiempo de ejecución FFT: {:.6f} s'.format(timeOfExecutionFFT), horizontalalignment='right', verticalalignment='top', transform=axs[2].transAxes)

# Ajustamos los espacios entre las gráficas
plt.subplots_adjust(wspace=0.5, hspace=0.5)

plt.show()