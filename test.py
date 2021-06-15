import numpy as np

n = np.arange(-2, 5)
N = len(n)
xn = np.array([1, 1, 0.5])
hn = np.array([0, 0, 1, 0.5, 0.25])

yn = np.zeros(N)

for i in range(N):
    if xn[i] != 0:
        print("n = ", i)
        for k in range(3):
            yn[i+k]=yn[i+k]+xn[i]*hn[2+k]
        print("y(n) = ", yn)