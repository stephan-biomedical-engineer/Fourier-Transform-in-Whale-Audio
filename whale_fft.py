#Código desenvolvido por Stephan Costa Barros na Faculdade de Engenharia Elétrica da Universidade Federal de Uberlândia
#Disciplina de Sinais e Sistemas, ministrada por Gabriela Vieira Lima
#Leia os arquivos license.txt e os arquivos de Appends para mais informações sobre o código
#Este código é uma adaptação do código whale_fft.py desenvolvido por MathWorks

#Bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Carregar o arquivo de áudio
whale_file = 'bluewhale.wav'
fs, whale = wavfile.read(whale_file)

# Normalizar o sinal
whale = whale.astype(np.float32) / np.max(np.abs(whale))

# Pegar um trecho do sinal
whale = whale[int(2.45e4):int(3.10e4)]
t = np.arange(0, len(whale)) / fs

# Plotar o sinal de áudio no domínio do tempo
plt.figure()
plt.plot(t, whale)
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.title('Audio Signal')
plt.xlim([0, t[-1]])
plt.show()

# Calcular a Transformada de Fourier
n = len(whale)
fft_result = np.fft.fft(whale)
frequencies = np.fft.fftfreq(n, 1/fs)
positive_freq_indices = np.where(frequencies > 0)

# Plotar o espectro unilateral de frequências
plt.figure()
plt.plot(frequencies[positive_freq_indices], np.abs(fft_result[positive_freq_indices]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Unilateral Frequency Spectrum')
plt.show()

# Encontrar a frequência dominante
max_magnitude_index = np.argmax(np.abs(fft_result[positive_freq_indices]))
dominant_freq = frequencies[positive_freq_indices][max_magnitude_index]
print("Frequência dominante:", dominant_freq, "Hz")

# Escrever observações
# Observações:
# - Analisando o espectro de frequências, podemos observar picos em determinadas frequências.
# - A frequência dominante pode indicar a frequência principal da vocalização da baleia.
# - Podemos observar outras frequências presentes, que podem ser harmônicas ou ruído.

