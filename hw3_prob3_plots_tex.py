import matplotlib.pyplot as plt
import numpy as np
import math

pi=np.pi

### Plot Y/p vs. beam thickness

t     = [0.28,0.28,0.22,0.22,0.2,0.28,0.2,0.28,0.2,0.23,0.2]
ratio = [3.050118458,2.595810079,3.620531455,3.65236015,4.091044123,3.121220534,3.973178487,2.419079448,3.924434437,4.140484899,3.87030299]

t_fit     = np.arange(0.2, 0.28, 0.01)
ratio_fit = -14.7676*t_fit+6.973

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.scatter(t,ratio)
plt.plot(t_fit, ratio_fit)


ax = plt.subplot(111)
#ax.set_ylim(ymax=1e9)
#ax.set_xlim(xmin=0.9, xmax=1.1)


plt.xlabel('Beam thickness, $\mu m$', fontsize='16')
plt.ylabel('$Y/\\rho$ ratio, $10^8 \ m^2/s^2$', fontsize='16')
plt.suptitle('Comparison of $Y/\\rho$ ratio to beam thickness', fontsize='18')

plt.legend(title='$\gamma, rad/s$')
plt.grid(True)
plt.xticks(fontsize='14')
plt.yticks(fontsize='14')


plt.savefig('hw3_3a.png', bbox_inches='tight')

### Plot w_0 vs. volume

plt.clf()

v   = [2.394,1.568,2.02554,1.65528,0.4416,1.274,0.4928,0.826,0.28,0.94024,0.1728]
w_0 = [0.653451272,1.137256541,1.43256625,1.438849435,1.520530844,1.702743218,2.086017522,2.871415685,3.342654583,3.68194659,6.44026494]

v_fit = np.arange(0.01, 2.99, 0.01)
w_0_fit = 2.067*(1/v_fit)**0.5

plt.scatter(v, w_0, label = r'$\omega_0$')
plt.plot(v_fit, w_0_fit, label = 'Fit')

ax = plt.subplot(111)
ax.set_ylim(ymin=0, ymax=7)
ax.set_xlim(xmin=0.0, xmax=3.0)
plt.grid(True)

plt.xlabel('Beam volume, $\mu m^3$', fontsize='16')
plt.ylabel('Resonant frequency, $10^8 \ rad/s$', fontsize='16')
plt.suptitle('Resonant frequency vs. beam volume', fontsize='18')

plt.savefig('hw3_3b.png', bbox_inches='tight')






