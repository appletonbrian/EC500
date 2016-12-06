# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 11:58:37 2016

@author: brian
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

m_h = 2
m_e = m_h/2

k = np.linspace(0,1,100)
h = k**2/m_h
e = k**2/m_e

plt.plot(k,h, color='black')
plt.plot(k,e, color='black')
plt.suptitle("Dispersion relationship for electrons and holes", fontsize=13.5)
plt.ylabel("$E$", fontsize=14)
plt.xlabel("$k$", fontsize=14)
plt.annotate(s="Electrons\n$m=m^\star_e$", xy=[0.49,0.5], fontsize=12)
plt.annotate(s="Holes\n$m=2m^\star_e$", xy=[0.72,0.15], fontsize=12)


frame = plt.gca()
fig = plt.gcf()
fig.set_size_inches(5,5)
frame.axes.get_yaxis().set_ticks([0])
frame.axes.get_xaxis().set_ticks([0])
frame.set_xlim(xmin=-0.02)
frame.set_ylim(ymin=-0.02)

plt.savefig('prob1b.png',dpi=200)