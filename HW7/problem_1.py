# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 13:15:55 2016

@author: brian
"""

import matplotlib.pyplot as plt
import numpy as np

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

pi = np.pi

#%% Problem 1 Part A

#Given:
n_water = 1.33
e_water = 1.33*1.33
particle_diameter = 10e-9
#(note that I'll use 'e' in place of epsilon)


#
c1 = 12.53 #epsilon_inf
c2 = 133e-9 #lambda_p
c3 = 12000e-9 #lambda_gamma



wavelength = np.linspace(490e-9,810e-9,3200)

#Calculate the complex relative dielectric constant using the given eqn. (2)
e_r = c1 - 1/c2**2 / (1/wavelength**2 + 1j/(c3*wavelength))

resonant_e_r = -2*e_water

#Find the index of the element in e_r whose value matches the resonant e_r
resonant_index = np.abs(np.real(e_r)-resonant_e_r).argmin()

resonant_wavelength = wavelength[resonant_index]
print(resonant_wavelength*1e9, "nm found at Re{e_r} = ", np.real(e_r[resonant_index]))



plt.plot(wavelength*1e9, np.real(e_r), linewidth = 2)
ax = plt.subplot(111)
plt.suptitle("Real part of relative dielectric constant for Au", fontsize = 18)
plt.xlabel("Wavelength, nm", fontsize=14)
plt.ylabel("$\epsilon^{'}$", fontsize=18)
plt.grid(True)
ax.set_xlim(xmin=495, xmax=605)
ax.set_ylim(ymax=-0.6, ymin=-8.4)
plt.savefig('prob1_parta.png')

#%% Problem 1 Part B

plt.clf()

#Plot the scattering and absorption cross-sections for the 10nm Au NPs. Use the result to find the resonance condition.
R = 10e-9

er_re = np.real(e_r)
er_im = np.imag(e_r)



#Calcualte the scattering cross-section using eqn. (17)
sigma_sca = (8*pi/3)*((2*pi/wavelength)**4)*(R**6)*(((er_re-e_water)**2+er_im**2)/((er_re+2*e_water)**2+er_im**2))**2
denom = ((er_re+2*e_water)**2+er_im**2)

#Calculate the absorption cross-section using eqn. (19)
sigma_abs = (4*pi*2*pi/wavelength*R**3)*((er_im*e_water)/((er_re+2*e_water)**2+er_im**2))

#Calculate the extinction cross-section using eqn. (14)
sigma_ext = sigma_sca+sigma_abs

#Find the resonant wavelength, as the wavelength that maximizes sigma_ext
resonant_index = np.argmax(sigma_ext)
print("Resonant wavelength of sigma_ext is ", wavelength[resonant_index]*1e9, " nm.")

ax1 = plt.subplot(311)
plt.plot(wavelength*1e9, sigma_sca)
plt.suptitle("Scattering, absorption, and extinction cross-sections for $10nm$ Au NP", fontsize=18)
plt.ylabel("Scattering cross-section, $m^{2}$")
ax1.set_xlim(xmin=495, xmax=805)
ax1.set_ylim(ymin=0, ymax=9.15e-16)
plt.grid(True)

ax2 = plt.subplot(312)
plt.plot(wavelength*1e9, sigma_abs)
plt.ylabel("Absorption cross-section, $m^{2}$")
ax2.set_xlim(xmin=495, xmax=805)
ax2.set_ylim(ymin=0, ymax=9.15e-16)
plt.grid(True)

ax3 = plt.subplot(313)
plt.plot(wavelength*1e9, sigma_ext)
plt.ylabel("Extinction cross-section, $m^{2}$")
ax3.set_xlim(xmin=495, xmax=805)
ax3.set_ylim(ymin=0, ymax=9.15e-16)
plt.xlabel("Wavelength, $nm$")
plt.grid(True)

fig = plt.gcf()
fig.set_size_inches(9,9)
plt.savefig('prob1_partb.png')


