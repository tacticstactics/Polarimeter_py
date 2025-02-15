﻿import numpy as np
import matplotlib.pyplot as plt
import Polarimeter_def
import Sphere_def

if __name__ == "__main__":
    Ein = np.array([[1],[0]]) # 0  Parallel


print('')
print('Ein')
print(Ein)
print('')

E1 = Ein

# Three: steps. Propagte, waveplate and Faraday rotator.

# Just Propagate

E2 = Polarimeter_def.propagate(1, E1)

#Waveplate: Phase

theta2 = 45 # fixed.Do not change
phase2 = 89 #90 for QWP, 180 for HWP 

E3 = Polarimeter_def.waveplate(phase2,theta2,E2)

#Faraday Rotation 

theta_fr = 40

E4 = Polarimeter_def.faradayrotaor(theta_fr,E3)


Eout = E4

print('E3 = Eout =:')
print(Eout)
print('')


xabsEout = np.abs(Eout[0,0])
xrealEout = np.real(Eout[0,0])
xphaseEout = np.angle(Eout[0,0], deg=True)

print('Absolute of x of Eout:')
print(xabsEout)
print('')

print('Real of x of Eout:')
print(xrealEout)
print('')

print('Phase of x of Eout:')
print(xphaseEout)
print('')

yabsEout = np.abs(Eout[1,0])
yrealEout = np.real(Eout[1,0])
yphaseEout = np.angle(Eout[1,0], deg=True)

print('Absolute of y of Eout:')
print(yabsEout)
print('')

print('Real of y of Eout:')
print(yrealEout)
print('')

print('Phase of y of Eout:')
print(yphaseEout)
print('')

m = 128

Eoutx_col = np.zeros(m)
Eouty_col = np.zeros(m)

value_in_YZplane = phase2
value_in_XYplane = theta_fr


for ii in range(m):

    opl1 = 0.05 * ii

    Eout_propagate = Polarimeter_def.propagate(opl1,Eout)

    Eoutx_col[ii] = np.real(Eout_propagate[0,0])   
    Eouty_col[ii] = np.real(Eout_propagate[1,0])



C0 = Sphere_def.Sphere0()
C45 = Sphere_def.Sphere45()
C90 = Sphere_def.Sphere90()
C135 = Sphere_def.Sphere135()
H0 = Sphere_def.SphereH0()


fig = plt.figure(figsize = (8,4), facecolor='lightblue')
ax1 = fig.add_subplot(1, 2, 1)

ax1.plot(Eoutx_col, Eouty_col)
ax1.set_xlim(-1,1)
ax1.set_ylim(-1,1)


xyz_init = np.zeros((3, 1))

xyz_init[1,:] = 1.05

print("xyz_init =")
print(xyz_init)



x1 = xyz_init[0,:]
y1 = xyz_init[1,:]
z1 = xyz_init[2,:]

# YZ Plane
x2 = x1
y2 = np.cos(value_in_YZplane*np.pi/180)*y1 - np.sin(value_in_YZplane*np.pi/180)*z1
z2 = np.sin(value_in_YZplane*np.pi/180)*y1 + np.cos(value_in_YZplane*np.pi/180)*z1

# XY Plane

x3 = np.cos(value_in_XYplane*np.pi/180)*x2 - np.sin(value_in_XYplane*np.pi/180)*y2
y3 = np.sin(value_in_XYplane*np.pi/180)*x2 + np.cos(value_in_XYplane*np.pi/180)*y2
z3 = z2

xyz_end = np.zeros((3, 1))

xyz_end[0,:] = x3
xyz_end[1,:] = y3
xyz_end[2,:] = z3

print("xyz_end =")
print(xyz_end)


ax21 = fig.add_subplot(1, 2, 2, projection='3d')

ax21.scatter(C0[0,:], C0[1,:], C0[2,:], color='gray', linewidths = 1, s=1)
ax21.scatter(C45[0,:], C45[1,:], C45[2,:], color='gray', linewidths = 1, s=1)
ax21.scatter(C90[0,:], C90[1,:], C90[2,:], color='gray', linewidths = 1, s=1)
ax21.scatter(C135[0,:], C135[1,:], C135[2,:], color='gray', linewidths = 1, s=1)
ax21.scatter(H0[0,:], H0[1,:], H0[2,:], color='gray', linewidths = 1, s=1)

ax21.scatter(xyz_init[0,:], xyz_init[1,:], xyz_init[2,:], color='green', s=10)
ax21.scatter(xyz_end[0,:], xyz_end[1,:], xyz_end[2,:], color='red', s=10)

ax21.set_xlabel('X axis')
ax21.set_ylabel('Y axis')
ax21.set_zlabel('Z axis')

plt.grid(True)
plt.show()