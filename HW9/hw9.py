# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:55:06 2016

@author: brian
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')


a = np.linspace(1,6,1000) #nm

a_B = 4.86 #nm
R_y = 0.023 #eV

m0 = 9.109e-31 #kg
mu = 0.0685*m0 #kg
h  = 6.626e-34 #Js
e  = 1.602e-19 #C

Eg = 1.74      #eV


E_xb_weak_eV = 0.023*a/a #Trick it into giving me an array 
E_xb_strong_eV = 1.788*a_B/a*R_y + 0.238*R_y

plt.subplot(121)
plt.plot(a,E_xb_strong_eV, label="Strong confinement model")
plt.plot(a,E_xb_weak_eV,label="Weak confinement model", linestyle='--')
plt.plot([a_B, a_B],[0,0.25], linestyle='--', color = 'black')
plt.annotate(s="$a_B$", xy = [4.5, 0.12], fontsize = 14)
#plt.legend(fontsize = 10, loc='upper left', ncol=2, y=-1)
plt.legend(bbox_to_anchor=(0, -0.2, 1.5, 0), loc=2, ncol=2, mode="expand", borderaxespad=0)
plt.grid(True)
plt.xlabel("$a, nm$", fontsize = 14)
plt.ylabel("$E_{XB}, eV$", fontsize = 14)
plt.title("Exciton binding energy", fontsize = 12, y=1.05)

plt.subplot(122)
E_PL_weak = Eg + h**2/(8*mu*(a/1e9)**2)/e - R_y
lambda_weak = 1240/E_PL_weak
E_PL_strong = Eg + h**2/(8*mu*(a/1e9)**2)/e - 0.238*R_y - 1.788*a_B/a*R_y
lambda_strong = 1240/E_PL_strong

plt.plot(a, lambda_strong)
plt.plot(a, lambda_weak, linestyle='--')
plt.grid(True)
plt.xlabel("$a, nm$", fontsize = 14)
plt.ylabel("$\lambda, nm$", fontsize = 14)
plt.title("Emission wavelength", fontsize=12, y=1.05)

plt.suptitle("Exciton binding energy and emission wavelength and in weak and strong confinement", y=1.08, fontsize=14)

fig = plt.gcf()
fig.set_size_inches(10,4)
plt.savefig("prob2.png", dpi=200, bbox_inches='tight')
plt.show()