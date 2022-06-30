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

Ein = [[1], [0]]  # initialization of presets is done in __init__

print(Ein)


Eout = Polarimeter_def.propagate(wavel,no,opl,Ein)


print('')
print(Eout)
print('')

