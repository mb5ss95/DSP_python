import numpy as np


def dfts(x, n):
    wn = np.exp(-1j*0.5*np.pi)
    xn = np.zeros(n, dtype="complex64")

    for i in range(n):
        summ = 0
        for j in range(n):
            summ = summ +  x[j]*(wn**(i*j))
        xn[i] = summ
    return xn

x = [0, 1, 2, 3]
n = len(x)

print(dfts(x, n))
