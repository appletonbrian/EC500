import matplotlib.pyplot as plt
import numpy as np
import math

pi=np.pi

### Plot |A|^2

w_0   = 1.0 #rad/s
gamma = [0.00001*w_0, 0.001*w_0, 0.1*w_0] #rad/s
f_m   = 0.1 #m/s^2
w     = np.arange(0.9,1.10,0.001) # generate array from 0.01 to 10.0 rad/s

font = {'fontname':'STIX Math'}

for g in gamma:	
	amp_sqrd = f_m**2 / ((w_0**2 - w**2)**2 + (w**2)*(g**2))
	plt.semilogy(w, amp_sqrd, label=str("%.0e" %g))

ax = plt.subplot(111)
ax.set_ylim(ymax=1e9)
ax.set_xlim(xmin=0.9, xmax=1.1)


plt.xlabel('$\omega, rad/s$', fontsize=18)
plt.ylabel('$|A|^2$', fontsize=18)
plt.suptitle('$|A|^2$ as a function of driving frequency $\omega$', **font, fontsize=18)

plt.legend(title='$\gamma, rad/s$', fontsize=12)
plt.grid(True)
#plt.show()

plt.savefig('hw3_1a.png', bbox_inches='tight')

### Plot phase

plt.clf() #clear figure

for g in gamma:	
	theta = np.arctan(-1*w*g/(w_0**2-w**2))
	plt.plot(w, theta, label=str("%.0e" %g))

ax = plt.subplot(111)
ax.set_xlim(xmin=0.9, xmax=1.1)

plt.xlabel('$\omega, rad/s$', fontsize=18)
plt.ylabel('$\\theta, rad$', fontsize=18)
plt.suptitle('$\\theta$ as a function of driving frequency $\omega$',**font, fontsize=18)

plt.legend(title='$\gamma, rad/s$', fontsize=12)
plt.grid(True)

plt.yticks([-pi/2, -pi/4, 0, pi/4, pi/2],
           [r'$\frac{-\pi}{2}$', r'$\frac{-\pi}{4}$', r'$0$', r'$\frac{\pi}{4}$', r'$\frac{-\pi}{2}$'])

plt.savefig('hw3_1b.png', bbox_inches='tight')










