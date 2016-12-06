import matplotlib.pyplot as plt
import numpy as np
import math

pi=np.pi

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

### Plot Y(x,t) = Asin(k_n*x)cos(w_n*t) for fundamental wavelength lambda = 2L

#Let L = pi
L  = pi

#Let A = 1 unit
A = 1.0

#Let Period = 1 second
T = 1.0

#Create array for time from 0 to 6T
dt = 0.01
t  = np.arange(0, 3*T+dt, dt)

#Calculate k_n
kn = pi/L

#Calculate w_n
wn = 2*pi/T

#First plot y1: x1  = L/2
x1 = L/2
y1 = A*np.sin(kn*x1)*np.cos(wn*t)
plt.plot(t, y1, label = '$x = L/2$')



#Second plot y2: x2 = L/3
x2 = L/4
y2 = A*np.sin(kn*x2)*np.cos(wn*t)
plt.plot(t, y2, label = '$x = L/4$')


#Third plot y3: x3 = 2L/3
x3 = L/8
y3 = A*np.sin(kn*x3)*np.cos(wn*t)
plt.plot(t, y3, label = '$x = L/8$')

plt.legend(title = 'Position')
plt.grid()
plt.xlabel('Time, $t/T$', fontsize='16')
plt.ylabel('Amplitude, $a/A$', fontsize='16')
plt.suptitle('Amplitude vs. time at position $x$ along beam of length $L$ for $\lambda = 2L$', fontsize='18')
plt.savefig('hw3_2a.png', bbox_inches='tight')


