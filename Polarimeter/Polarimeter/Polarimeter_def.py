#Polarimeter_def.py

#from errno import EINPROGRESS
from ftplib import parse150
import numpy as np
import math

def propagate(opl,Ein=np.array([[1],[0]])):

    pp1 = np.array([[np.exp(1j*opl),0],[0,np.exp(1j*opl)]]);
 
    Eout1 = np.dot(pp1,Ein)

    return Eout1



def faradayrotaor(theta1, Ein=np.array([[1],[0]])):

     FR1 = np.array([[math.cos(theta1*math.pi/180),math.sin(theta1*math.pi/180)],[-1*math.sin(theta1*math.pi/180),math.cos(theta1*math.pi/180)]]);

     Eout2 = np.dot(FR1,Ein)

     return Eout2


def waveplate(phase,theta1,Ein=np.array([[1],[0]])):

  WP1 = np.array([[math.cos(theta1*math.pi/180),math.sin(theta1*math.pi/180)],[-1*math.sin(theta1*math.pi/180),math.cos(theta1*math.pi/180)]]);

  WP2 = np.array([[np.exp(1j*0), 0],[0, np.exp(1j*phase*math.pi/180)]]);

  WP3 = np.array([[math.cos(-1*theta1*math.pi/180),math.sin(-1*theta1*math.pi/180)],[-1*math.sin(-1*theta1*math.pi/180),math.cos(-1*theta1*math.pi/180)]]);

  Eout1 = np.dot(WP1,Ein)
 
  Eout2 = np.dot(WP2,Eout1)

  Eout3 = np.dot(WP3,Eout2)

  return Eout3

def reflect(Ein=np.array([[1],[0]])):

    R1 = np.array([[-1,0],[0,1]]);

    Eout4 = np.dot(R1, Ein)
    
    return Eout4



