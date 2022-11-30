
#Waveplate_main.py


print('Waveplate_main.py')

import numpy as np

#from scipy.fftpack import fft, fftshift
#from scipy import signal

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

import Polarimeter_def



Ein = np.array([[1],[0]])
#Ein = np.array([[0],[1]])

print('')
print('Ein')
print(Ein)
print('')

E1 = Ein


#Waveplate

theta2 = 45

phase2 = 90 # unit: degree. phase 90 is equivalent to QWP



E2 = Polarimeter_def.waveplate(phase2,theta2,E1)

Eout = E2

print('Eout = E2 =:')
print(Eout)
print('')

m = 256

Eoutx_col = np.zeros(m);
Eouty_col = np.zeros(m);
opl1_col = np.zeros(m);

for ii in range(m):

    opl1 = 0.05 * ii

    opl1_col[ii] = opl1   

    Eout_propagate=Polarimeter_def.propagate(opl1,Eout)

    Eoutx_col[ii] = np.real(Eout_propagate[0,0])   
    Eouty_col[ii] = np.real(Eout_propagate[1,0])


#n = 2048
#thetacol = np.zeros(n);
#PX_qwpcol = np.zeros(n);


# Assume QWP

#phase_qwp = 90 # degree. QWP


#for jj in range(n):
    
 #   theta_var = 0.5 * jj

  #  Eout_qwp = Polarimeter_def.waveplate(phase_qwp,theta_var,Eout)
    
   # thetacol[jj]=theta_var
   # PX_qwpcol[jj] = abs(Eout_qwp[0,0])**2 # Linear Polarization Component





fig = plt.figure(figsize = (12,4), facecolor='lightblue')
ax1 = plt.axes(projection = '3d')

ax1.plot3D(opl1_col,Eoutx_col, Eouty_col)
ax1.set_title('3d Scatter plot geeks for geeks');

plt.show()



