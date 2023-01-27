
import numpy as np

def Sphere0():
    
    mm = 1 #theta
    stepii = 30
    
    nn = 360 #phi
    stepjj = 1
    
    C0 = np.zeros((3, nn))
    
    for ii in range(mm):
        theta1 = stepii * ii
        for jj in range(nn):

            phi1 = stepjj * jj
            
            x1 = 0
            y1 = np.cos(phi1 * np.pi/180)
            z1 = np.sin(phi1 * np.pi/180)
            C0[0,jj] = x1
            C0[1,jj] = y1
            C0[2,jj] = z1
            
    return C0

def Sphere45():
    
    mm = 1 #theta
    stepii = 30
    
    nn = 360 #phi
    stepjj = 1

    C45 = np.zeros((3, nn))
    
    for ii in range(mm):
        theta1 = 45
        
        
        for jj in range(nn):

            phi1 = stepjj * jj
            
            x1 = 0
            y1 = np.cos(phi1 * np.pi/180)
            z1 = np.sin(phi1 * np.pi/180)
            
            # Rotate 90 degree in XY plane

            x2 = np.cos(theta1*np.pi/180)*x1 - np.sin(theta1*np.pi/180)*y1
            y2 = np.sin(theta1*np.pi/180)*x1 + np.cos(theta1*np.pi/180)*y1
            z2 = z1


            C45[0,jj] = x2
            C45[1,jj] = y2
            C45[2,jj] = z2

    return C45

def Sphere90():
    
    mm = 1 #theta
    stepii = 30
    
    nn = 360 #phi
    stepjj = 1

    C90 = np.zeros((3, nn))
    
    for ii in range(mm):
        theta1 = 90
        
        for jj in range(nn):

            phi1 = stepjj * jj
            
            x1 = 0
            y1 = np.cos(phi1 * np.pi/180)
            z1 = np.sin(phi1 * np.pi/180)
            
            # Rotate 90 degree in XY plane

            x2 = np.cos(theta1*np.pi/180)*x1 - np.sin(theta1*np.pi/180)*y1
            y2 = np.sin(theta1*np.pi/180)*x1 + np.cos(theta1*np.pi/180)*y1
            z2 = z1


            C90[0,jj] = x2
            C90[1,jj] = y2
            C90[2,jj] = z2

    return C90


def Sphere135():

    mm = 1 #theta
    stepii = 30
    
    nn = 360 #phi
    stepjj = 1

    C135 = np.zeros((3, nn))
    
    for ii in range(mm):
        theta1 = 135
        
        for jj in range(nn):

            phi1 = stepjj * jj
            
            x1 = 0
            y1 = np.cos(phi1 * np.pi/180)
            z1 = np.sin(phi1 * np.pi/180)
            
            # Rotate 90 degree in XY plane

            x2 = np.cos(theta1*np.pi/180)*x1 - np.sin(theta1*np.pi/180)*y1
            y2 = np.sin(theta1*np.pi/180)*x1 + np.cos(theta1*np.pi/180)*y1
            z2 = z1


            C135[0,jj] = x2
            C135[1,jj] = y2
            C135[2,jj] = z2
    
    return C135
            


def SphereH0():

    mm = 1 #theta
    stepii = 30
    
    nn = 360 #phi
    stepjj = 1
    
    H0 = np.zeros((3, nn))
    
    for jj in range(nn):

            phi1 = stepjj * jj
            
            x1 = np.cos(phi1 * np.pi/180)
            y1 = np.sin(phi1 * np.pi/180)
            z1 = 0


            H0[0,jj] = x1
            H0[1,jj] = y1
            H0[2,jj] = z1
    return H0


