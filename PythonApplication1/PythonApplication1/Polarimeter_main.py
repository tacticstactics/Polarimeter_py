#Polarimeter_main.py


import numpy as np
import matplotlib.pyplot as plt

import Polarimeter_def

wavel = 1.55e-6

def new_func():
    no = 1
    return no

no = new_func()

opl = 1

Ein = 1

print(Ein)


#Eout = Polarimeter_def.propagate(wavel,no,opl,Ein)


print('')
#print(Eout)
print('')

n_a = np.array([[1, -1, 2],
                [2, -2 ,1],
                [3, 1 ,-1]])
n_b = np.array([[2, 1, 3],
                [1, 1, 2],
                [-1, 2, 3]])
dim= n_a.shape[0]
n_mult=np.empty((dim,dim))
for row in range(dim):
    for col in range(dim):
        n_mult[row,col ] = sum(n_a[row, :]*n_b[:, col])
n_mult


