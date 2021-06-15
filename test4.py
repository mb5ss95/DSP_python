import numpy as np
import matplotlib.pyplot as plt
import librosa, librosa.display

file1 = "c:/1.wav"
file2 = "c:/2.wav"

sig1, sr1 = librosa.load(file1, sr = 48000)
sig2, sr2 = librosa.load(file2, sr = 48000)

librosa.display.waveplot(sig1, sr1)
librosa.display.waveplot(sig2, sr2)


magnitude1 = np.abs(np.fft.fft(sig1))
magnitude2 = np.abs(np.fft.fft(sig2))

left_f1 = np.linspace(0, sr1, len(magnitude1))
left_specturm1 = magnitude1
left_specturm2 = magnitude2

plt.figure()
plt.subplot(2,1,1)
plt.plot(left_f1, left_specturm1)
plt.subplot(2,1,2)
plt.plot(left_f1, left_specturm2)
plt.show()

corr_spectrum=np.corrcoef(left_specturm1, left_specturm2)[0,1]
print(corr_spectrum)