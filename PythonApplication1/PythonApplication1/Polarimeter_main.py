#Polarimeter_main.py

print('Polarimeter_main.py')

import numpy as np
import matplotlib.pyplot as plt

import Polarimeter_def

wavel = 1.55e-6
no = 1
ne=1.1
#return no

#def new_func():

#no = new_func()

opl = 10000

Ein = np.array([[1],[0]])


print('')
print('Ein')
print(Ein)

E1=Ein


E2=Polarimeter_def.faradayrotaor(45,E1)

print('')
print('E2')
print(E2)

E3=Polarimeter_def.propagate(wavel,no,opl,E2)

print('')
print('E3')
print(E3)


E4=Polarimeter_def.propagate(wavel,no,opl,E3)

print('')
print('E4')
print(E4)



Eout = E4

print('')
print('Eout')
print(Eout)

print('')
print('')




n_a = np.array([[1, -1, 2],
                [2, -2 ,1],
                [3, 1 ,-1]])
n_b = np.array([[2, 1, 3],
                [1, 1, 2],
                [-1, 2, 3]])

dim= n_a.shape[0]
print('dim')
print(dim)

n_mult=np.empty((dim,dim))
for row in range(dim):
    for col in range(dim):
        n_mult[row,col ] = sum(n_a[row, :]*n_b[:, col])
n_mult

print('n_mult')
print(Ein)

