# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 18:49:31 2016

@author: brian
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import special




'''
Calculate intensity transmission
I(f)
'''
kappa = 0.12
gamma = 0.9
FSR = 0.02 #THz, = 10 GHz
f = np.linspace(192.9, 193.1, 10100) #THz, = 180 to 200 THz
q = np.sqrt(gamma*(1-kappa))*np.exp(1j*2*np.pi*f/FSR)

#Optical amplitude transmission
I_A = 1/(np.sqrt(1-kappa))*(1-kappa-q)/(1-q)
I_P = I_A*I_A.conjugate()
#I_P = np.abs(I_A)
#print(I_P)
plt.plot(f, I_P)
plt.title("Intensity transmission between 192.9 and 193.1 THz, FSR = 20 GHz", y=1.05)
plt.xlabel("Frequency, THz")
plt.ylabel("Intensity transmission")
plt.savefig("compact_oeo_intensity.png", dpi = 200)
plt.clf()
plt.cla()


'''
Calculate E_out
E(t)
Bessel: scipy.special.jn(v,z) where v is the integer order and z is the argument
'''
def I(f, f_FSR):
    kappa = 0.12
    gamma = 0.9
    q = np.sqrt(gamma*(1-kappa))*np.exp(1j*2*np.pi*f/f_FSR)
    I_A = 1/(np.sqrt(1-kappa))*(1-kappa-q)/(1-q)
    return I_A

def plot_fft(tone, Fs, fmin, fmax):
    '''
    Plot fft of a signal "tone", ndarray of shape (N,)
    Fs is sampling frequency
    Plot will be cenetered at zero frequency.
    '''
    fft = np.fft.fft(tone)
    N = len(tone)
    #the frequency axis of the shifted fft goes from -Fs/2 to Fs/2, in intervals of Fs/N
    #The point Fs/2 is excluded
    f = np.arange(-Fs/2, Fs/2, Fs/N)
    #plt.semilogy(f,np.fft.fftshift(np.absolute(fft)))
    plt.plot(f,np.fft.fftshift(np.absolute(fft)))
    ax = plt.subplot(111)
    ax.set_xlim(xmin=fmin, xmax=fmax)
    ax.set_ylim(ymin=0, ymax=1e-4)
    plt.xlabel('Frequency, Hz')
    plt.ylabel('|X|')
    plt.grid(True)
    #plt.show()
    plt.savefig("compact_oeo_fft.png", dpi=200)
    plt.clf()
    plt.cla()

v0 = 193 #Carrier frequency, THz
N = 1000000 #number of samples
tf = 1000000 #total duration of simulation, ps
Fs = N/(tf/1e12)
print("Frequency resolution:", Fs/N/1e6, "MHz")
t = np.linspace(0,tf, N) #picoseconds
omega_rf = 0.02*2*np.pi #Microwave frequency, THz
P = 1 #input power
V_pi = 2.8 #V
V_0 = 0.1 #V, no idea what to put for this

E_out = 0*t

for p in range(-100,101):
    vp = v0 + p*omega_rf/(2*np.pi)    
    E_out = E_out +  (1j)**p*special.jn(p,np.pi*V_0/V_pi)*np.exp(1j*2*np.pi*(vp*1e12)*(t/1e12))*I(vp, omega_rf/(2*np.pi))
    E_out = np.sqrt(P)*E_out

E_out_P = E_out*E_out.conjugate()
plot_fft(E_out_P, Fs, 18e9, 22e9)

plt.plot(t, E_out_P)
plt.xlabel("ps")
ax = plt.subplot(111)
ax.set_xlim(xmin=0, xmax=200)
plt.savefig("compact_oeo_mag_power.png", dpi=200)
#plt.show()




