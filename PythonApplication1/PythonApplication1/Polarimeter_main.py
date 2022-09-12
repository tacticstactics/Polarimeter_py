#Polarimeter_main.py

print('Polarimeter_main.py')

import numpy as np
import matplotlib.pyplot as plt

import Polarimeter_def

wavel = 1.55
no = 1
ne=1.1
theta1=22.5

#def new_func():

#no = new_func()

opl = 100

Ein = np.array([[1],[0]])


print('')
print('Ein')
print(Ein)

E1=Ein


E2=Polarimeter_def.faradayrotaor(theta1,E1)

print('')
print('E2')
print(E2)

E3=Polarimeter_def.propagate(wavel,no,opl,E2)

print('')
print('E3')
print(E3)

opl2=8000
theta2=45

E4=Polarimeter_def.waveplate(wavel,no,ne,opl2,theta2,E3)

print('')
print('E4')
print(E4)

Eout = E4

print('')
print('Eout')
print(Eout)

print('')
print('')

m = 512

PX_powercol = np.zeros((m,1));
PY_powercol = np.zeros((m,1));

for ii in range(m):

    opl1 = ii*1

    Eout_propagate=Polarimeter_def.propagate(wavel,no,opl1,Eout)

    PX_powercol[(ii)] = Eout_propagate[0,0]
    
    print('')
    print('Eout_propagate')
    print(Eout_propagate)

    PY_powercol[(ii)] = Eout_propagate[1,0]


fig = plt.figure(figsize = (10,4), facecolor='lightblue')

ax1 = fig.add_subplot(1, 2, 1)

ax1.plot(np.real(PX_powercol),np.real(PY_powercol))

ax2 = fig.add_subplot(1, 2, 2)

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

