#Polarimeter_main.py


import numpy as np
import matplotlib.pyplot as plt

import Polarimeter_def

param = 0.01
m = 128

tcol, Etcol, Signalcol = Polarimeter_def.proc1(param,m)


print('')
print('Polarimeter_main.py')
print('')


fig = plt.figure(figsize = (10,6), facecolor='lightblue')

ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

ax1.plot(tcol,np.real(Etcol))
ax2.plot(tcol,np.imag(Etcol))
ax3.plot(tcol,np.real(Signalcol))

plt.show()



