import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from pydub import AudioSegment
import os

# Obtener la ruta del directorio actual
dir_path = os.path.dirname(os.path.realpath(__file__))

# Cargar archivo de audio
audio = AudioSegment.from_file(os.path.join(dir_path, "audio.mp3"), format="mp3")

# Exportar como archivo WAV
audio.export("audio.wav", format="wav")

# Cargar archivo de audio
sample_rate, samples_stereo = wavfile.read('audio.wav')

# Calcular FFT de audio estéreo -> lado izquierdo
fft_stereo_left = np.abs(np.fft.fft(samples_stereo[:, 0]))
# Normalizar FFT, sino me grafica magnitudes mayores a 7e9, ahora me grafica entre 0 y 1
fft_stereo_left_max = np.max(fft_stereo_left)
fft_stereo_left = fft_stereo_left / fft_stereo_left_max

# Calcular eje de frecuencia
freqs_stereo_left = np.abs(np.fft.fftfreq(len(samples_stereo[:, 0])) * sample_rate)

# Calcular FFT de audio estéreo -> lado derecho
fft_stereo_right = np.abs(np.fft.fft(samples_stereo[:, 1]))
# Normalizar FFT, sino me grafica magnitudes mayores a 7e9, ahora me grafica entre 0 y 1
fft_stereo_right_max = np.max(fft_stereo_right)
fft_stereo_right = fft_stereo_right / fft_stereo_right_max

# Calcular eje de frecuencia
freqs_stereo_right = np.abs(np.fft.fftfreq(len(samples_stereo[:, 1])) * sample_rate)

# Convertir audio estéreo a mono
samples_mono = np.mean(samples_stereo, axis=1, dtype=samples_stereo.dtype)

# Calcular FFT de audio mono
fft_mono = np.abs(np.fft.fft(samples_mono))
# Normalizar FFT, sino me grafica magnitudes mayores a 7e9, ahora me grafica entre 0 y 1
fft_mono_max = np.max(fft_mono)
fft_mono = fft_mono / fft_mono_max

# Calcular eje de frecuencia
freqs_mono = np.abs(np.fft.fftfreq(len(samples_mono)) * sample_rate)

# Graficar las FFT en 3 subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 8))

# Graficar FFT de audio estéreo -> lado izquierdo
ax1.plot(freqs_stereo_left, fft_stereo_left)
ax1.set_title('FFT Audio Estéreo - Lado Izquierdo')
ax1.set_xlabel('Frecuencia (Hz)')
ax1.set_ylabel('Magnitud')

# Graficar FFT de audio estéreo -> lado derecho
ax2.plot(freqs_stereo_right, fft_stereo_right)
ax2.set_title('FFT Audio Estéreo - Lado Derecho')
ax2.set_xlabel('Frecuencia (Hz)')
ax2.set_ylabel('Magnitud')

# Graficar FFT de audio mono
ax3.plot(freqs_mono, fft_mono)
ax3.set_title('FFT Audio Mono - Promedio')
ax3.set_xlabel('Frecuencia (Hz)')
ax3.set_ylabel('Magnitud')

# Dar aviso en el gráfico de cuál es el máximo valor de la FFT en la esquina superior derecha
ax1.text(0.95, 0.95, 'Max: {:.2f}'.format(fft_stereo_left_max), horizontalalignment='right', verticalalignment='top', transform=ax1.transAxes)
ax2.text(0.95, 0.95, 'Max: {:.2f}'.format(fft_stereo_right_max), horizontalalignment='right', verticalalignment='top', transform=ax2.transAxes)
ax3.text(0.95, 0.95, 'Max: {:.2f}'.format(fft_mono_max), horizontalalignment='right', verticalalignment='top', transform=ax3.transAxes)

# Ajustar subplots con hspace y wspace
plt.subplots_adjust(wspace=0.5, hspace=0.5)

# Mostrar gráficos
plt.show()