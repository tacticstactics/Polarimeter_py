
#Waveplate_def.py

from ftplib import parse150
import numpy as np
import math


def waveplate(phase,theta1,Ein=np.array([[1],[0]])):

  WP1 = np.array([[math.cos(theta1*math.pi/180),math.sin(theta1*math.pi/180)],[-1*math.sin(theta1*math.pi/180),math.cos(theta1*math.pi/180)]]);

  WP2 = np.array([[np.exp(1j*0), 0],[0, np.exp(1j*phase*math.pi/180)]]);

  WP3 = np.array([[math.cos(-1*theta1*math.pi/180),math.sin(-1*theta1*math.pi/180)],[-1*math.sin(-1*theta1*math.pi/180),math.cos(-1*theta1*math.pi/180)]]);

  Eout1 = np.dot(WP1,Ein)
 
  Eout2 = np.dot(WP2,Eout1)

  Eout3 = np.dot(WP3,Eout2)

  return Eout3