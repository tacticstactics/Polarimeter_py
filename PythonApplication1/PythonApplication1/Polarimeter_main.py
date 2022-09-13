#Polarimeter_main.py

print('Polarimeter_main.py')

import numpy as np
import matplotlib.pyplot as plt

import Polarimeter_def

wavel = 1
no = 1.5
ne = 1.6


#Ein = np.array([[1],[0]])
Ein = np.array([[0],[1]])

print('')
print('Ein')
print(Ein)

E1 = Ein

theta1 = 0

E2 = Polarimeter_def.faradayrotaor(theta1,E1)

opl1 = 0
E3 = Polarimeter_def.propagate(wavel,no,opl1,E2)

#Waveplate

opl2 = 0.5 * wavel/(ne-no)
theta2 = 45

print('WP Thickness:')
print(opl2)


E4 = Polarimeter_def.waveplate(wavel,no,ne,opl2,theta2,E3)

Eout = E4

print('Eout = E4:')
print(Eout)



m = 256

PX_powercol = np.zeros((m,1));
PY_powercol = np.zeros((m,1));


for ii in range(m):

    opl1 = 0.05 * ii

    Eout_propagate=Polarimeter_def.propagate(wavel,no,opl1,Eout)

    PX_powercol[(ii)] = np.real(Eout_propagate[0,0])   
    PY_powercol[(ii)] = np.real(Eout_propagate[1,0])


n = 256

PX_qwpcol = np.zeros((n,1));
PY_qwpcol = np.zeros((n,1));
thetacol = np.zeros((n,1));

# Assume QWP

qwpt = 0.25 * wavel/(ne-no)

print('QWP Thickness:')
print(qwpt)


for jj in range(n):
    
    theta_var = 2 * jj

    Eout_qwp = Polarimeter_def.waveplate(wavel,no,ne,qwpt,theta_var,Eout)
    
    thetacol[(jj)]=theta_var
    PX_qwpcol[(jj)] = abs(Eout_qwp[0,0])**2
    PY_qwpcol[(jj)] = abs(Eout_qwp[1,0])**2


fig = plt.figure(figsize = (10,4), facecolor='lightblue')
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
ax1.plot(np.real(PX_powercol),np.real(PY_powercol))
ax1.set_xlim(-1,1)
ax1.set_ylim(-1,1)
ax2.plot(thetacol,PX_qwpcol, thetacol,PY_qwpcol)
ax2.set_ylim(-0.1,1.1)

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

