import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

N = 512
fc = float(input("fc"))
fs = float(input("fs"))

fh = 2.0*(fc/fs)
b, a = signal.butter(N,2.0*(fc/fs))
w, H = signal.freqz(b,a)
#test
n = np.arange(0, 1, (1.0/fs))
x1 = np.sin(2*np.pi*300*n)
x2 = np.sin(2*np.pi*800*n)
x = x1+x2


plt.subplot(3, 1, 1)
plt.plot(w,H)
plt.xlabel('w')
plt.ylabel('Mag')
plt.subplot(3,1,2)
plt.plot(w, np.angle(H))
plt.xlabel('w')
plt.ylabel('ph')



#lfilter(b,a,x)

