# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 21:09:05 2016

@author: brian
"""

import numpy as np
import matplotlib.pyplot as plt

max_time = 60000
num_elements = 300000
t = np.linspace(0,max_time,num_elements) #time in fs (1e-15 seconds)

#Frequency of carrier
f1 = 193 #THz

#Free spectral range (frequency difference between carrier and each sideband)
delta_f = 33 #GHz

#Frequency of signal 2 (carrier + 1 FSR)
f2 = f1+delta_f/1000

#Frequency of signal 3 (carrier - 1 FSR)
f3 = f1-delta_f/1000

#Define signals E1, E2, E3
#E1=0*t
E1 = np.sin(2*np.pi*f1*1e12*t*1e-15)
E2 = np.sin(2*np.pi*f2*1e12*t*1e-15)
E3 = np.sin(2*np.pi*f3*1e12*t*1e-15)
E4 = (E1/3+E2/3+E3/3)

#Plot E1
min_index = np.argmin(E1[:int(num_elements/max_time*4)])
x_min= t[min_index]
ax = plt.subplot(311)
plt.plot(t, E1)
ax.set_ylim(ymin = -1.5, ymax = 1.5)
ax.set_xlim(xmin=0, xmax =10)
ax.set_yticklabels([])
ax.set_xticklabels([])
plt.title("Carrier frequency: 193 THz")
#plt.show()

#Plot E3
ax = plt.subplot(312)
plt.plot(t, E3)
ax.set_ylim(ymin = -1.5, ymax = 1.5)
ax.set_xlim(xmin=0, xmax =10)
ax.set_yticklabels([])
ax.set_xticklabels([])
plt.title("Left sideband: 193 THz - 33 GHz")
#plt.show()

#Plot E2
ax = plt.subplot(313)
plt.plot(t, E1)
ax.set_ylim(ymin = -1.5, ymax = 1.5)
ax.set_xlim(xmin=0, xmax =10)
ax.set_yticklabels([])
plt.title("Right sideband: 193 THz + 33 GHz")
plt.xlabel("Time, fs")

fig = plt.gcf()
fig.set_size_inches(6, 8)
plt.savefig("component_frequencies.png", dpi=200, bbox_inches = "tight")

#Clear
plt.clf()
plt.cla()


#Plot added signal
ax = plt.subplot(111)
plt.plot(t, E4)
ax.set_ylim(ymin = -3, ymax = 3)
plt.title("Beat note resulting from summation")
ax.set_yticklabels([])
ax.set_xticklabels([0, 10, 20, 30, 40, 50, 60])
plt.xlabel("Time, ps")

#add markers to added signal
plt.plot([15151.5,15151.5],[-1.5,1.5], color='black', linestyle='--')
plt.plot([45454.5,45454.5],[-1.5,1.5], color='black', linestyle='--')
fig.set_size_inches(6, 4)
plt.savefig("beat_note.png", dpi=200, bbox_inches = "tight")

#Plot square of added signal
if(True):
    plt.clf()
    plt.cla()
    ax = plt.subplot(111)
    plt.plot(t, E4**2)
    #ax.set_ylim(ymin = -3, ymax = 3)
    plt.title("Beat note power")
    #ax.set_yticklabels([])
    ax.set_xticklabels([0, 10, 20, 30, 40, 50, 60])
    plt.xlabel("Time, ps")
    plt.plot([15151.5,15151.5],[-1.5,1.5], color='black', linestyle='--')
    plt.plot([45454.5,45454.5],[-1.5,1.5], color='black', linestyle='--')
    fig.set_size_inches(6, 4) 
    plt.savefig("beat_note_power.png", dpi=200, bbox_inches = "tight") 

