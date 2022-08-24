#Polarimeter_def.py

from errno import EINPROGRESS
from ftplib import parse150
import numpy as np
import math

def propagate(wavel=1.55e-6,no=1,opl=1,Ein=np.array([[1], [0]])):

    T11 = np.array([[np.exp(1j*wavel*no*opl),0],[0,np.exp(1j*wavel*no*opl)]]);

    #T11 = np.array([[1, 0],[0, 1]])

    Eout = np.dot(T11,Ein)

    return Eout



def faradayrotaor(theta1=45, Ein=np.array([[1],[0]])):


     FR11 = np.array([[math.cos(theta1*math.pi/180),math.sin(theta1*math.pi/180)],[-1*math.sin(theta1*math.pi/180),math.cos(theta1*math.pi/180)]]);

     Eout = np.dot(FR11,Ein)

     return Eout


def waveplate(wavel=1.55e-6,no=1,ne=1.1,opl=1,theta1=45,Ein=np.array([[1],[0]])):

  WP1 = np.array([[math.cos(theta1*math.pi/180),math.sin(theta1*math.pi/180)],[-1*math.sin(theta1*math.pi/180),math.cos(theta1*math.pi/180)]]);

  WP2 = np.array([[np.exp(1j * wavel * ne * opl), 0],[0, np.exp(1j * wavel * no * opl)]]);

  WP3 = np.array([[math.cos(-1*theta1*math.pi/180),math.sin(-1*theta1*math.pi/180)],[1*math.sin(theta1*math.pi/180),math.cos(-1*theta1*math.pi/180)]]);

   #p1 = np.array([[np.exp(1j * wavel * no * opl), 0],[0, np.exp(1j * wavel * no * opl)]]);
   #T12 = np.array([[(-1)*math.cos(theta1*math.pi/180), math.sin(theta1*math.pi/180)],[-1*math.sin(theta1*math.pi/180), math.cos(theta1*math.pi/180)]])
   #WP11 = np.array([[math.cos(theta1*math.pi/180),math.sin(theta1*math.pi/180)],[-1*math.sin(theta1*math.pi/180),math.cos(theta1*math.pi/180)]]);

  Eout1 = np.dot(WP1,Ein)
 
  Eout2 = np.dot(WP2,Eout1)

  Eout3 = np.dot(WP3,Eout2)

  return Eout3


