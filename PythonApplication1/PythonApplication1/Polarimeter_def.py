#Polarimeter_def.py

import numpy as np
import math

def propagate(wavel = 1.55e-6,no=1,opl=1,Ein):

    T11 = np.array([[np.exp(1j * wavel * no * opl), 0],[0, np.exp(1j * wavel * no * opl)]]);

    Eout = T11 * Ein

    return Eout



def faradayrotaor(theta1, Ein):


     T11 = np.array([[math.cos(theta1*math.pi/180), math.sin(theta1*math.pi/180)],[-1*math.sin(theta1*math.pi/180), math.cos(theta1*math.pi/180)]]);

     Eout = T11 * Ein
     return Eout

