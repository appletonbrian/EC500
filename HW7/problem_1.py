# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 13:15:55 2016
@author: Brian Appleton
"""

import matplotlib.pyplot as plt
import numpy as np

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

pi = np.pi

#%% Problem 1 Part A
#Plot the dielectric response of gold using eqn. (2)

#Given:
n_water = 1.33
e_water = 1.33*1.33
particle_diameter = 10e-9
#(note that I'll use 'e' in place of epsilon)

#Given constants for eqn. (2)
c1 = 12.53 #epsilon_inf
c2 = 133e-9 #lambda_p
c3 = 12000e-9 #lambda_gamma

#Define array for wavelength. 0.1nm resolution.
wavelength = np.linspace(290e-9, 1010e-9, 7201)

#Calculate the complex relative dielectric constant using the given eqn. (2)
e_r = c1 - 1/c2**2 / (1/wavelength**2 + 1j/(c3*wavelength))

resonant_e_r = -2*e_water

#Find the index of the element in e_r whose value matches the resonant e_r
resonant_index = np.abs(np.real(e_r)-resonant_e_r).argmin()
resonant_wavelength = wavelength[resonant_index]
print(resonant_wavelength*1e9, "nm found at Re{e_r} = ", np.real(e_r[resonant_index]))


plt.plot(wavelength*1e9, np.real(e_r), label="$\epsilon'$")
plt.plot(wavelength*1e9, np.imag(e_r), label="$\epsilon''$", linestyle='--')
plt.plot(resonant_wavelength*1e9, resonant_e_r, marker='.', markersize=10)
ax = plt.subplot(111)
plt.suptitle("Dielectric response for Au", fontsize = 18)
plt.xlabel("Wavelength, nm", fontsize=14)
plt.ylabel("Relative dielectric constant", fontsize= 14)
plt.legend(fontsize = 20, loc = 'best')
plt.grid(True)
ax.set_xlim(xmin=395, xmax=705)
plt.savefig('prob1_parta.png', dpi=200)


#%% Problem 1 Part B
#Plot the scattering and absorption cross-sections for the 10nm diameter Au NPs. Use the result to find the resonance condition.

plt.clf()
plt.cla()
plt.close()

#Particle radius
R = 10e-9/2

#Grab the real and imaginary parts of the dielectric response for gold that we calculated in Part A
er_re = np.real(e_r)
er_im = np.imag(e_r)

#Calculate the scattering cross-section using eqn. (17)
sigma_sca = (8*pi/3)*((2*pi/wavelength)**4)*(R**6)*(((er_re-e_water)**2+er_im**2)/((er_re+2*e_water)**2+er_im**2))**2

#Calculate the absorption cross-section using eqn. (19)
sigma_abs = (4*pi*2*pi/wavelength*R**3)*((er_im*e_water)/((er_re+2*e_water)**2+er_im**2))

#Calculate the extinction cross-section using eqn. (14)
sigma_ext = sigma_sca+sigma_abs

#Find the resonant wavelength, as the wavelength that maximizes sigma_ext
resonant_index = np.argmax(sigma_ext)
print("Resonant wavelength of sigma_ext is ", wavelength[resonant_index]*1e9, " nm.")

#Calculate the Q factor, as the resonant wavelength divided by the FWHM
half_max = sigma_ext[resonant_index]/2
left_half_max_index = np.abs(sigma_ext[:resonant_index]-half_max).argmin()
right_half_max_index = np.abs(sigma_ext[resonant_index:]-half_max).argmin() + resonant_index-1
FWHM = wavelength[right_half_max_index]-wavelength[left_half_max_index]
Q = wavelength[resonant_index]/FWHM
print("Q = ", Q, " with FWHM = ", FWHM*1e9, " nm.")

#Plot the scattering cross section
ax1 = plt.subplot(311)
plt.plot(wavelength*1e9, sigma_sca*1e18)
plt.suptitle("Scattering, absorption, and extinction cross-sections for $10nm$ Au NP", fontsize=18)
plt.ylabel("Scattering cross-section, $nm^{2}$", fontsize=12)
ax1.set_xlim(xmin=495, xmax=805)
ax1.set_ylim(ymin=0, ymax=63)
plt.grid(True)

#Plot the absorption cross section
ax2 = plt.subplot(312)
plt.plot(wavelength*1e9, sigma_abs*1e18)
plt.ylabel("Absorption cross-section, $nm^{2}$", fontsize=12)
ax2.set_xlim(xmin=495, xmax=805)
ax2.set_ylim(ymin=0, ymax=63)
plt.grid(True)

#Plot the extinction cross section
ax3 = plt.subplot(313)
plt.plot(wavelength*1e9, sigma_ext*1e18)
plt.ylabel("Extinction cross-section, $nm^{2}$",fontsize=12)
ax3.set_xlim(xmin=495, xmax=805)
ax3.set_ylim(ymin=0, ymax=63)
plt.xlabel("Wavelength, $nm$", fontsize=14)
plt.grid(True)
plt.arrow(wavelength[left_half_max_index]*1e9+5,half_max*1e18,FWHM*1e9-5,0, length_includes_head=True, shape='full', head_width=2.5, width=0.1)
plt.arrow(wavelength[right_half_max_index]*1e9-5,half_max*1e18,-FWHM*1e9+5,0, length_includes_head=True, shape='full', head_width=2.5, width=0.1)
plt.annotate(s="$\delta\lambda$", xy=[wavelength[resonant_index]*1e9-3, 22])

fig = plt.gcf()
fig.set_size_inches(9,9)
plt.savefig('prob1_partb.png', dpi=200)

#%% Problem 2
#Plot the scattering and absorption cross-sections from 300-1000nm on a semilog plot

plt.clf()
plt.cla()
plt.close()

#Plot the scattering cross section
ax1 = plt.subplot(211)
plt.semilogy(wavelength*1e9, sigma_sca*1e18)
plt.suptitle("Scattering and absorption cross-sections for $10nm$ Au NP", fontsize=18)
plt.ylabel("Scattering cross-section, $nm^{2}$", fontsize=12)
ax1.set_xlim(xmin=295, xmax=1005)
ax1.set_ylim(ymin=1e-7, ymax=1e2)
plt.grid(True)

#Plot the absorption cross section
ax2 = plt.subplot(212)
plt.semilogy(wavelength*1e9, sigma_abs*1e18)
plt.ylabel("Absorption cross-section, $nm^{2}$", fontsize=12)
ax2.set_xlim(xmin=295, xmax=1005)
ax2.set_ylim(ymin=1e-7, ymax=1e2)
plt.grid(True)
plt.xlabel("Wavelength, $nm$", fontsize=14)

fig = plt.gcf()
fig.set_size_inches(7,7)
plt.savefig('prob2.png', dpi=200)

#%%Problem 4
#Plot the scattering and absorption cross-sections as a function of R^3 at the resonant wavelength

plt.clf()
plt.cla()
plt.close()

#Create an array for the cubed radius
R_cubed = np.linspace(1e-9**3, 10e-9**3, 1001)

#Grab the relative dielectric constants at the resonant wavelength
er_re_res = er_re[resonant_index]
er_im_res = er_im[resonant_index]
wavelength = resonant_wavelength

#Calculate the scattering cross-section using eqn. (17)
sigma_sca = (8*pi/3)*((2*pi/wavelength)**4)*(R_cubed**2)*(((er_re_res-e_water)**2+er_im_res**2)/((er_re_res+2*e_water)**2+er_im_res**2))**2

#Calculate the absorption cross-section using eqn. (19)
sigma_abs = (4*pi*2*pi/wavelength*R_cubed**1)*((er_im_res*e_water)/((er_re_res+2*e_water)**2+er_im_res**2))

#Where are the effective cross-sections equal?
eq_index = np.abs(sigma_sca-sigma_abs).argmin()
r_cubed_eq = R_cubed[eq_index]
print("The scattering and absorption cross sections are equal when the particle diameter is ", r_cubed_eq**(1/3)*2e9, "nm.")
print(r_cubed_eq)

#Plot the scattering cross section
ax1 = plt.subplot(111)
plt.plot(R_cubed*1e27, sigma_sca*1e18, label = "Scattering")
plt.plot(R_cubed*1e27, sigma_abs*1e18, label = "Absorption", linestyle='--')
plt.plot([5**3, 5**3], [0, 500], linestyle = ':', color ='black', linewidth=1.5)
plt.plot([r_cubed_eq*1e27, r_cubed_eq*1e27], [0, 500], linestyle = ':', color ='black', linewidth=1.5)
plt.annotate(s="$d=10nm$", xy=[5**3+15, 153])
plt.annotate(s="$d=18nm$", xy=[r_cubed_eq*1e27+12, 153])
plt.suptitle("Scattering and absorption cross-sections for $10nm$ Au NP", fontsize=12)
plt.ylabel("Effective cross-section, $nm^{2}$", fontsize=12)
plt.xlabel("$R^{3}, nm^{3}$", fontsize=12)
ax1.set_xlim(xmin=0, xmax=1000)
plt.legend(fontsize = 10, loc = 'upper left') 
ax1.set_ylim(ymin=0, ymax=400)
plt.grid(True)

fig = plt.gcf()
fig.set_size_inches(5,5)
plt.savefig('prob4.png', dpi=200)