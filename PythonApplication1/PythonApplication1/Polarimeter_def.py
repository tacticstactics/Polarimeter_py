#Polarimeter_def.py

#from errno import EINPROGRESS
from ftplib import parse150
import numpy as np
import math

def propagate(wavel,no,opl,Ein=np.array([[1],[0]])):

    T11 = np.array([[np.exp(1j*wavel*no*opl),0],[0,np.exp(1j*wavel*no*opl)]]);

    #T11 = np.array([[1, 0],[0, 1]])

    Eout1 = np.dot(T11,Ein)

    return Eout1



def faradayrotaor(theta1, Ein=np.array([[1],[0]])):


     FR11 = np.array([[math.cos(theta1*math.pi/180),math.sin(theta1*math.pi/180)],[-1*math.sin(theta1*math.pi/180),math.cos(theta1*math.pi/180)]]);

     Eout2 = np.dot(FR11,Ein)

     return Eout2


def waveplate(wavel,no,ne,opl,theta1,Ein=np.array([[1],[0]])):

  WP1 = np.array([[math.cos(theta1*math.pi/180),math.sin(theta1*math.pi/180)],[-1*math.sin(theta1*math.pi/180),math.cos(theta1*math.pi/180)]]);

  WP2 = np.array([[np.exp(1j * wavel * no * opl), 0],[0, np.exp(1j * wavel * ne * opl)]]);

  WP3 = np.array([[math.cos(-1*theta1*math.pi/180),math.sin(-1*theta1*math.pi/180)],[-1*math.sin(-1*theta1*math.pi/180),math.cos(-1*theta1*math.pi/180)]]);

  Eout1 = np.dot(WP1,Ein)
 
  Eout2 = np.dot(WP2,Eout1)

  Eout3 = np.dot(WP3,Eout2)

  return Eout3


