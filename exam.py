import numpy as np
import matplotlib.pyplot as plt
import librosa, librosa.display
from sklearn.preprocessing import normalize

file1 = "C:/woo_EPG_ka_0.9s.wav"
file2 = "C:/woo_ka_0.9s.wav"

sig1, sr = librosa.load(file1, sr = 22050)
sig2, sr = librosa.load(file2, sr = 22050)

norm1=sig1/np.linalg.norm(sig1)
norm2=sig2/np.linalg.norm(sig2)

librosa.display.waveplot(norm1, sr)
librosa.display.waveplot(norm2, sr)

corr_time=np.corrcoef(norm1, norm2)[0,1]
print(corr_time)

fft1 = np.fft.fft(norm1)
fft2 = np.fft.fft(norm2)

magnitude1 = np.abs(fft1)
magnitude2 = np.abs(fft2)

f1 = np.linspace(0,sr,len(magnitude1))

left_f1 = f1[:int(len(magnitude1)/2)]
left_specturm1 = magnitude1[:int(len(magnitude1)/2)]
left_specturm2 = magnitude2[:int(len(magnitude2)/2)]

plt.figure()
plt.subplot(2,1,1);plt.plot(left_f1, left_specturm1)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.title("woo_EPG_ka_0.9s")
plt.subplot(2,1,2);plt.plot(left_f1, left_specturm2)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.title("woo_ka_0.9s")
plt.show()

corr_spectrum=np.corrcoef(left_specturm1, left_specturm2)[0,1]
print(corr_spectrum)