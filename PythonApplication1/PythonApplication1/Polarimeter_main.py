#Polarimeter_main.py

print('Polarimeter_main.py')

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftshift

import Polarimeter_def



Ein = np.array([[1],[0]])
#Ein = np.array([[0],[1]])

print('')
print('Ein')
print(Ein)

E1 = Ein

theta1 = 45

E2 = Polarimeter_def.faradayrotaor(theta1,E1)

opl1 = 0
E3 = Polarimeter_def.propagate(opl1,E2)

print('')
print('E3')
print(E3)



#Waveplate

phase2 = 0 # degree. QWP, 90
theta2 = 45


print('')
print('E3')
print(E3)


E4 = Polarimeter_def.waveplate(phase2,theta2,E3)

Eout = E4

print('Eout = E4:')
print(Eout)



m = 256

Eoutx_col = np.zeros((m,1));
Eouty_col = np.zeros((m,1));


for ii in range(m):

    opl1 = 0.05 * ii

    Eout_propagate=Polarimeter_def.propagate(opl1,Eout)

    Eoutx_col[(ii)] = np.real(Eout_propagate[0,0])   
    Eouty_col[(ii)] = np.real(Eout_propagate[1,0])


n = 1024
thetacol = np.zeros((n,1));
PX_qwpcol = np.zeros((n,1));


# Assume QWP

phase_qwp = 90 # degree. QWP


for jj in range(n):
    
    theta_var = 1 * jj

    Eout_qwp = Polarimeter_def.waveplate(phase_qwp,theta_var,Eout)
    
    thetacol[(jj)]=theta_var
    PX_qwpcol[(jj)] = abs(Eout_qwp[0,0])**2



len_PX_qwpcol = len(PX_qwpcol)
print('Length of PX_qwpcol = ')
print(len_PX_qwpcol)
print('')

X1 = fft(PX_qwpcol,n)
N = len(X1)

print('Length of X1 = N = ')
print(N)
print('')

df = 1/N


Shifted_X1 = fftshift(X1)

len_Shifted_X1 = len(Shifted_X1)

print('Length of Shifted_X1 = ')
print(len_Shifted_X1)
print('')


Shifted_sampleIndex = np.arange(-N//2, N//2)

Shifted_f = Shifted_sampleIndex*df

len_Shifted_f = len(Shifted_f)

print('Length of Shifted_f = ')
print(len_Shifted_f)
print('')



fig = plt.figure(figsize = (10,4), facecolor='lightblue')
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)

ax1.plot(Eoutx_col, Eouty_col)
ax1.set_xlim(-1,1)
ax1.set_ylim(-1,1)

ax2.plot(thetacol,PX_qwpcol, ".-")
ax2.set_ylim(-0.1,1.1)


ax3.stem(Shifted_f, np.abs(Shifted_X1)/N, use_line_collection=True)
#ax3.stem(freq, np.abs(X1), 'b', markerfmt=" ", basefmt="-b")
#ax3.set_xlim(0,1000)

#ax3.plot(Shifted_f, np.abs(Shifted_X1)/o)#, use_line_collection=True)

# Assume this light hits rotating qwp and fixed polarizer.

plt.show()







#n_a = np.array([[1, -1, 2],
#                [2, -2 ,1],
#                [3, 1 ,-1]])
#n_b = np.array([[2, 1, 3],
#                [1, 1, 2],
#                [-1, 2, 3]])

#dim= n_a.shape[0]
#print('dim')
#print(dim)

#n_mult=np.empty((dim,dim))
#for row in range(dim):
#    for col in range(dim):
#        n_mult[row,col ] = sum(n_a[row, :]*n_b[:, col])
#n_mult

#print('n_mult')
#print(Ein)

