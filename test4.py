import numpy as np
import matplotlib.pyplot as plt
import librosa, librosa.display

file1 = "c:/1.wav"
file2 = "c:/2.wav"

sig1, sr1 = librosa.load(file1, sr = 48000)
sig2, sr2 = librosa.load(file2, sr = 48000)

librosa.display.waveplot(sig1, sr1)
librosa.display.waveplot(sig2, sr2)

fft1 = np.fft.fft(sig1)
fft2 = np.fft.fft(sig2)

magnitude1 = np.abs(fft1)
magnitude2 = np.abs(fft2)

f1 = np.linspace(0, sr1, len(magnitude1))

left_f1 = f1[:int(len(magnitude1)/2)]
left_specturm1 = magnitude1[:int(len(magnitude1)/2)]
left_specturm2 = magnitude2[:int(len(magnitude2)/2)]

plt.figure()
plt.show()