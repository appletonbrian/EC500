import numpy as np
import matplotlib.pyplot as plt


#Look at requirements for TIR

#number of chords in circle
m = np.arange(3,1000,1)

#angle of incidence phi
phi = np.pi*(m-2)/2/m
brian_is_dumb = (m-2)/m

plt.plot(m, brian_is_dumb)
plt.show()

