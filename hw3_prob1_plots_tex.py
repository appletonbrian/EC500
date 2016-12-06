import matplotlib.pyplot as plt
import numpy as np
import math

pi=np.pi

### Plot |A|^2

w_0   = 1.0 #rad/s
gamma = [0.00001*w_0, 0.001*w_0, 0.1*w_0] #rad/s
f_m   = 0.1 #m/s^2
w     = np.arange(0.9,1.10,0.001) # generate array from 0.9 to 1.1 rad/s

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

for g in gamma:	
	amp_sqrd = f_m**2 / ((w_0**2 - w**2)**2 + (w**2)*(g**2))
	plt.semilogy(w, amp_sqrd, label=str("%.0e" %g))
	index_peak = np.argmax(amp_sqrd)
	print('peak amplitude for gamma = ', g, 'is ',  amp_sqrd[index_peak], ' found at w = ', w[index_peak])

ax = plt.subplot(111)
ax.set_ylim(ymax=1e9)
ax.set_xlim(xmin=0.9, xmax=1.1)


plt.xlabel('$\omega, rad/s$', fontsize='16')
plt.ylabel('$|A|^2$', fontsize='16')
plt.suptitle('$|A|^2$ as a function of driving frequency $\omega$', fontsize='18')

plt.legend(title='$\gamma, rad/s$')
plt.grid(True)
plt.xticks(fontsize='14')
plt.yticks(fontsize='14')


plt.savefig('hw3_1a.png', bbox_inches='tight')

### Plot phase

plt.clf() #clear figure

for g in gamma:	
	theta = np.arctan(-1*w*g/(w_0**2-w**2))
	plt.plot(w, theta, label=str("%.0e" %g))

ax = plt.subplot(111)
ax.set_xlim(xmin=0.9, xmax=1.1)

plt.xlabel('$\omega, rad/s$', fontsize='16')
plt.ylabel('$\\phi, rad$', fontsize='16')
plt.suptitle('$\\phi$ as a function of driving frequency $\omega$', fontsize='18')

plt.legend(title='$\gamma, rad/s$')
plt.grid(True)

plt.yticks([-pi/2, -pi/4, 0, pi/4, pi/2],
           [r'$\frac{-\pi}{2}$', r'$\frac{-\pi}{4}$', r'$0$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$'], fontsize='16')
plt.xticks(fontsize='14')

plt.savefig('hw3_1b.png', bbox_inches='tight')

### Plot Lorentzian - FIRST ATTEMPT

plt.clf()

w2      = np.arange(0.8,1.201,0.001) # generate array from 0.8 to 1.2 rad/s
g       = gamma[0] # grab gamma = 1e-5*w_0
high_q_amp_sqrd = f_m**2 / ((w_0**2 - w2**2)**2 + (w2**2)*(g**2))
lorentz = (1/pi)*(0.5*g)/((w2-w_0)**2+(0.5*g)**2)

index_w0 = 200 #index of w2 where w2=1 rad/s
#index_w0 = np.where(w2==w_0)[0][0] #find index where w=w_0. This doesn't work here becuase of storage errors.
scaling_factor = high_q_amp_sqrd[index_w0]/lorentz[index_w0] #calculate scaling factor from amplitude at w=w_0
print("Scaling factor: ", scaling_factor)

lorentz = scaling_factor*lorentz # scale the lorentzian

error_percent = np.absolute((high_q_amp_sqrd - lorentz)/high_q_amp_sqrd)*100

plt.semilogy(w2, lorentz, label=r'$Scaled\ Lorentzian$')
plt.semilogy(w2, high_q_amp_sqrd, label=r'$|A|^2, \gamma = 0.00001\omega_0$')
#plt.semilogy(w2, error_percent, label=r'$Normalized\ error$')

plt.legend()

ax = plt.subplot(111)

ax.set_ylim(ymax=1e9)

plt.grid(True)

plt.xlabel('$\omega, rad/s$', fontsize='16')
plt.ylabel('$Amplitude$', fontsize='16')
plt.suptitle('Lorentzian fit for highest $Q$', fontsize='18')



ax2 = ax.twinx()
ax2.plot(w2, error_percent, label=r'$|Percent\ error|$', color='r')
ax2.set_ylabel(r'$|Percent\ error|$', color='r', fontsize='16')

ax2.set_xlim(xmin=0.8, xmax=1.2)
plt.xticks([0.80, 0.90, 1.00, 1.10, 1.20],['0.80', '0.90', '1.00', '1.10', '1.20'])

### Plot Lorentzian - SECOND ATTEMPT

plt.clf()

w2      = np.arange(0.8,1.201,0.001) # generate array from 0.8 to 1.2 rad/s
g       = gamma[0] # grab gamma = 1e-5*w_0
#high_q_amp_sqrd = f_m**2 / ((w_0**2 - w2**2)**2 + (w2**2)*(g**2))
high_q_amp_sqrd = (2*w2**2*g)/pi/((w_0**2-w2**2)**2+g**2 * w2**2)
lorentz = (1/pi)*(0.5*g)/((w2-w_0)**2+(0.5*g)**2)

index_w0 = 200 #index of w2 where w2=1 rad/s
#index_w0 = np.where(w2==w_0)[0][0] #find index where w=w_0. This doesn't work here becuase of storage errors.
scaling_factor = high_q_amp_sqrd[index_w0]/lorentz[index_w0] #calculate scaling factor from amplitude at w=w_0
print("Scaling factor: ", scaling_factor)

#lorentz = scaling_factor*lorentz # scale the lorentzian

error_percent = np.absolute((high_q_amp_sqrd - lorentz)/high_q_amp_sqrd)*100

plt.semilogy(w2, lorentz, label=r'$Lorentzian$')
plt.semilogy(w2, high_q_amp_sqrd, label=r'$|A|^2_{scaled}, \gamma = 10^{-5}\omega_0$')
#plt.semilogy(w2, error_percent, label=r'$Normalized\ error$')

plt.legend()

ax = plt.subplot(111)

ax.set_ylim(ymax=1e5)

plt.grid(True)

plt.xlabel('$\omega, rad/s$', fontsize='16')
plt.ylabel('$Amplitude$', fontsize='16')
plt.suptitle('Lorentzian fit for highest $Q$', fontsize='18')

ax2 = ax.twinx()
ax2.plot(w2, error_percent, label=r'$|Percent\ error|$', color='r')
ax2.set_ylabel(r'$|Percent\ error|$', color='r', fontsize='16')

ax2.set_xlim(xmin=0.8, xmax=1.2)
plt.xticks([0.80, 0.90, 1.00, 1.10, 1.20],['0.80', '0.90', '1.00', '1.10', '1.20'])

plt.savefig('hw3_1c_try2.png', bbox_inches='tight')







