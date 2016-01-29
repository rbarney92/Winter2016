# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:41:15 2015

@author: Rebecca
calculating the RMS values for both the stiff and the nonStiff
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
#loading in the data that was calculated from the other codes

phi_A_0 = np.load('phi_A_0Test.npy')
phi_A_1 = np.load('phi_A_1Test.npy')
phi_A_2 = np.load('phi_A_2Test.npy')
phi_A_3 = np.load('phi_A_3Test.npy')
phi_A_4 = np.load('phi_A_4Test.npy')

phi_central_0 = np.load('Phi_central_0.npy')
phi_central_1 = np.load('Phi_central_1.npy')
phi_central_2 = np.load('Phi_central_2.npy')
phi_central_3 = np.load('Phi_central_3.npy')
phi_central_4 = np.load('Phi_central_4.npy')

phi_up_0 = np.load('Phi_up_0.npy')
phi_up_1 = np.load('Phi_up_1.npy')
phi_up_2 = np.load('Phi_up_2.npy')
phi_up_3 = np.load('Phi_up_3.npy')
phi_up_4 = np.load('Phi_up_4.npy')

phi_quick_0 = np.load('Phi_quick_0.npy')
phi_quick_1 = np.load('Phi_quick_1.npy')
phi_cuick_2 = np.load('Phi_quick_2.npy')
phi_quick_3 = np.load('Phi_quick_3.npy')
phi_quick_4 = np.load('Phi_quick_4.npy')

phi_trap_0 = np.load('Phi_trap_0.npy')
phi_trap_1 = np.load('Phi_trap_1.npy')
phi_trap_2 = np.load('Phi_trap_2.npy')
phi_trap_3 = np.load('Phi_trap_3.npy')
phi_trap_4 = np.load('Phi_trap_4.npy')

# ------------------------------------------------------
L = 1.0
# -------------------------------------------
#defining the x values to be plotted based on the size of th arrays of phi

x = np.linspace(0,L,101)
x1 = np.linspace(0,L,21)
x2 = np.linspace(0,L,6)
x3 = np.linspace(0,L,41)
x4 = np.linspace(0,L,81)

# --------------------------------------------
# plotting the figures

plt.figure()
plt.plot(x,phi_A_0,marker='o',linestyle='None',markersize=4)
plt.plot(x, phi_central_0,marker='x',linestyle='None',markersize=6)
plt.plot(x,phi_up_0)
plt.plot(x,phi_quick_0)
plt.plot(x,phi_trap_0)
plt.xlabel('x')
plt.ylabel('phi')
plt.title('Case 1')
plt.legend(['A','Central Difference','Upwind','Quick','Crank-Nicholson'],loc='upper right')
plt.savefig('Case_1.jpg')


plt.figure()
plt.plot(x1,phi_A_1,marker='o',linestyle='None',markersize=4)
plt.plot(x1,phi_central_1,marker='x',linestyle='None',markersize=6)
plt.plot(x1,phi_up_1)
plt.plot(x1,phi_quick_1)
plt.plot(x1,phi_trap_1)
plt.xlabel('x')
plt.ylabel('phi')
plt.title('Case 2')
plt.legend(['A','Central Difference','Upwind','Quick','Crank-Nicholson'],loc='upper right')
plt.savefig('Case_2.jpg')

plt.figure()
plt.plot(x2,phi_A_2,marker='o',linestyle='None',markersize=4)
plt.plot(x2,phi_central_2,marker='x',linestyle='None',markersize=6)
plt.plot(x2,phi_up_2)
plt.plot(x2,phi_cuick_2)
plt.plot(x2,phi_trap_2)
plt.xlabel('x')
plt.ylabel('phi')
plt.title('Case 3')
plt.legend(['A','Central Difference','Upwind','Quick','Crank-Nicholson'],loc='upper right')
plt.savefig('Case_3.jpg')

plt.figure()
plt.plot(x3,phi_A_3,marker='o',linestyle='None',markersize=4)
plt.plot(x3,phi_central_3,marker='x',linestyle='None',markersize=6)
plt.plot(x3,phi_up_3)
plt.plot(x3,phi_quick_3)
plt.plot(x3,phi_trap_3)
plt.xlabel('x')
plt.ylabel('phi')
plt.title('Case 4')
plt.legend(['A','Central Difference','Upwind','Quick','Crank-Nicholson'],loc='upper right')
plt.savefig('Case_4.jpg')

plt.figure()
plt.plot(x4,phi_A_4,marker='o',linestyle='None',markersize=4)
plt.plot(x4,phi_central_4,marker='x',linestyle='None',markersize=6)
plt.plot(x4,phi_up_4)
plt.plot(x4,phi_quick_4)
plt.plot(x4,phi_trap_4)
plt.xlabel('x')
plt.ylabel('phi')
plt.title('Case 5')
plt.legend(['A','Central Difference','Upwind','Quick','Crank-Nicholson'],loc='upper right')
plt.savefig('Case_5.jpg')

# ------------------------------------------------------
#calculating the RMS values

phi_0 = np.array((phi_trap_0,phi_central_0,phi_up_0,phi_quick_0,phi_A_0))
phi_1 = np.array((phi_trap_1,phi_central_1,phi_up_1,phi_quick_1,phi_A_1))
phi_2 = np.array((phi_trap_2,phi_central_2,phi_up_2,phi_cuick_2,phi_A_2))
phi_3 = np.array((phi_trap_3,phi_central_3,phi_up_3,phi_quick_3,phi_A_3))
phi_4 = np.array((phi_trap_4,phi_central_4,phi_up_4,phi_quick_4,phi_A_4))

RMS_0 = np.zeros((1,4))
RMS_1 = np.zeros((1,4))
RMS_2 = np.zeros((1,4))
RMS_3 = np.zeros((1,4))
RMS_4 = np.zeros((1,4))

for i in range(0,1):
    for j in range(0,4):
        RMS_0[i,j] = np.math.sqrt((1.0/101.)*sum(((phi_0[j]-phi_0[4])**2.0)))
        RMS_1[i,j] = np.math.sqrt((1.0/21.)*sum(((phi_1[j]-phi_1[4])**2.0)))
        RMS_2[i,j] = np.math.sqrt((1.0/6.)*sum(((phi_2[j]-phi_2[4])**2.0)))
        RMS_3[i,j] = np.math.sqrt((1.0/41.)*sum(((phi_3[j]-phi_3[4])**2.0)))
        RMS_4[i,j] = np.math.sqrt((1.0/81.)*sum(((phi_4[j]-phi_4[4])**2.0)))