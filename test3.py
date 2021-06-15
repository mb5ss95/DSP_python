import numpy as np

def conv(a, b):
    if len(a) != len(b):
        return

    a_mean = np.mean(a)
    b_mean = np.mean(b)

    summ = 0
    for i in range(len(a)):
        summ = summ + (a[i]-a_mean) * (b[i]-b_mean)

    return summ / (len(a)-1)