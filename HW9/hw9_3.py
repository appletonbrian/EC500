# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 11:56:35 2016

@author: brian
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')


epsilon = 1 #eV
pi = np.pi
mu = np.linspace(0, 2, 1000) #eV
gamma = 0.05 #eV

D_E = 1/(2*pi)*gamma/((mu-epsilon)**2 + gamma**2/4)

plt.grid(True)
plt.xticks([0, 1, 2],["0", "$\epsilon$", "$2\epsilon$"], fontsize = 14)
plt.xlabel("Fermi level in channel", fontsize=12)
plt.ylabel("Density of states, $eV^{-1}$")
plt.title("Density of states in channel at energy level $\epsilon$", y=1.05)

plt.plot(mu, D_E)
plt.savefig("prob_3d.png", dpi=200,  bbox_inches='tight')