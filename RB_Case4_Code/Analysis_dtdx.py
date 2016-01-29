# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 11:22:52 2015

Case Study 4 - analysis continued for the different dt and dx cases

Analyzing the stability, accuracy, and effective order

@author: Rebecca
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
#loading in the data that was calculated from the other codes

phi_A_dx1 = np.load('Phi_A_DX1.npy')
phi_A_dx2 = np.load('Phi_A_DX2.npy')
phi_A_dx3 = np.load('Phi_A_DX3.npy')

phi_trap_dx1 = np.load('Phi_trap_dx1.npy')
phi_trap_dx2 = np.load('Phi_trap_dx2.npy')
phi_trap_dx3 = np.load('Phi_trap_dx3.npy')

phi_cs_dx1 = np.load('Phi_cs_dx1.npy')
phi_cs_dx2 = np.load('Phi_cs_dx2.npy')
phi_cs_dx3 = np.load('Phi_cs_dx3.npy')

phi_up_dx1 = np.load('Phi_up_dx1.npy')
phi_up_dx2 = np.load('Phi_up_dx2.npy')
phi_up_dx3 = np.load('Phi_up_dx3.npy')

phi_quick_dx1 = np.load('Phi_quick_dx1.npy')
phi_quick_dx2 = np.load('Phi_quick_dx2.npy')
phi_quick_dx3 = np.load('Phi_quick_dx3.npy')

# -------------------------------------
#TIME changing

phi_A_dt1 = np.load('Phi_A_DT1Test.npy')
phi_A_dt2 = np.load('Phi_A_DT2Test.npy')
phi_A_dt3 = np.load('Phi_A_DT3Test.npy')

phi_trap_dt1 = np.load('Phi_trap_Test1.npy')
phi_trap_dt2 = np.load('Phi_trap_Test2.npy')
phi_trap_dt3 = np.load('Phi_trap_Test3.npy')

phi_cs_dt1 = np.load('Phi_cs_Test1.npy')
phi_cs_dt2 = np.load('Phi_cs_Test2.npy')
phi_cs_dt3 = np.load('Phi_cs_Test3.npy')

phi_up_dt1 = np.load('Phi_up_Test1.npy')
phi_up_dt2 = np.load('Phi_up_Test2.npy')
phi_up_dt3 = np.load('Phi_up_Test3.npy')

phi_quick_dt1 = np.load('Phi_quick_Test1.npy')
phi_quick_dt2 = np.load('Phi_quick_Test2.npy')
phi_quick_dt3 = np.load('Phi_quick_Test3.npy')

# ------------------------------------------------------
L = 1.0
# -------------------------------------------
#defining the x values to be plotted based on the size of th arrays of phi

x = np.linspace(0,L,101)
x1 = np.linspace(0,L,201)
x2 = np.linspace(0,L,401)

dx = [0.01,0.01/2.0,0.01/4.0]
dt = [0.125,0.0625,0.03125]

# --------------------------------------------
# plotting the figures

plt.figure()
plt.plot(x,phi_A_dx1)
plt.plot(x,phi_trap_dx1)
plt.plot(x, phi_cs_dx1)
plt.plot(x,phi_up_dx1)
plt.plot(x, phi_quick_dx1)

plt.figure()
plt.plot(x1,phi_A_dx2)
plt.plot(x1,phi_trap_dx2)
plt.plot(x1, phi_cs_dx2)
plt.plot(x1,phi_up_dx2)
plt.plot(x1, phi_quick_dx2)

plt.figure()
plt.plot(x2,phi_A_dx3)
plt.plot(x2,phi_trap_dx3)
plt.plot(x2, phi_cs_dx3)
plt.plot(x2,phi_up_dx3)
plt.plot(x2, phi_quick_dx3)

# ------------------------------------------------------
#calculating the RMS values for changing dt

phi_dx1 = np.array((phi_trap_dx1,phi_cs_dx1,phi_up_dx1,phi_quick_dx1,phi_A_dx1))
phi_dx2 = np.array((phi_trap_dx2,phi_cs_dx2,phi_up_dx2,phi_quick_dx2,phi_A_dx2))
phi_dx3 = np.array((phi_trap_dx3,phi_cs_dx3,phi_up_dx3,phi_quick_dx3,phi_A_dx3))


RMS_1 = np.zeros((1,4))
RMS_2 = np.zeros((1,4))
RMS_3 = np.zeros((1,4))

for i in range(0,1):
    for j in range(0,4):
        RMS_1[i,j] = np.math.sqrt((1.0/101.)*sum(((phi_dx1[j]-phi_dx1[4])**2.0)))
        RMS_2[i,j] = np.math.sqrt((1.0/201.)*sum(((phi_dx2[j]-phi_dx2[4])**2.0)))
        RMS_3[i,j] = np.math.sqrt((1.0/401.)*sum(((phi_dx3[j]-phi_dx3[4])**2.0)))

RMS_trap = np.array((RMS_1[0,0],RMS_2[0,0],RMS_3[0,0]))
RMS_cs = np.array((RMS_1[0,1],RMS_2[0,1],RMS_3[0,1]))
RMS_up = np.array((RMS_1[0,2],RMS_2[0,2],RMS_3[0,2]))
RMS_quick = np.array((RMS_1[0,3],RMS_2[0,3],RMS_3[0,3]))

plt.figure()
plt.plot(dx,RMS_trap)
plt.plot(dx,RMS_cs)
plt.plot(dx,RMS_up)
plt.plot(dx,RMS_quick)
plt.yscale('log')
plt.xscale('log')
plt.xlabel('log(dx)')
plt.ylabel('log(RMS)')
plt.title('RMS values changing dx')
plt.legend(['Trap','CS','Upwind','Quick'],loc='lower left')
plt.savefig('ChangingDX.jpg')

#fitting a polynomial (linear) to the RMS values
#the np.polyfit returns ...Ax^2+Bx+C ... so the first value for a linear fit is the slope
# The slope here equals the effective order

slope_trap, b = np.polyfit(np.log10(dx),np.log10(RMS_trap),1)
slope_cs, b = np.polyfit(np.log10(dx),np.log10(RMS_cs),1)
slope_up, b = np.polyfit(np.log10(dx),np.log10(RMS_up),1)
slope_quick, b = np.polyfit(np.log10(dx),np.log10(RMS_quick),1)
print slope_trap
print slope_cs
print slope_up
print slope_quick


# ---------------------------------------------------
# calculating RMS values for changing dt

phi_dt1 = np.array((phi_trap_dt1,phi_cs_dt1,phi_up_dt1,phi_quick_dt1,phi_A_dt1))
phi_dt2 = np.array((phi_trap_dt2,phi_cs_dt2,phi_up_dt2,phi_quick_dt2,phi_A_dt2))
phi_dt3 = np.array((phi_trap_dt3,phi_cs_dt3,phi_up_dt3,phi_quick_dt3,phi_A_dt3))


RMS_1dt = np.zeros((1,4))
RMS_2dt = np.zeros((1,4))
RMS_3dt = np.zeros((1,4))

for i in range(0,1):
    for j in range(0,4):
        RMS_1dt[i,j] = np.math.sqrt((1.0/101.)*sum(((phi_dt1[j]-phi_dt1[4])**2.0)))
        RMS_2dt[i,j] = np.math.sqrt((1.0/201.)*sum(((phi_dt2[j]-phi_dt2[4])**2.0)))
        RMS_3dt[i,j] = np.math.sqrt((1.0/401.)*sum(((phi_dt3[j]-phi_dt3[4])**2.0)))

RMS_trapdt = np.array((RMS_1dt[0,0],RMS_2dt[0,0],RMS_3dt[0,0]))
RMS_csdt = np.array((RMS_1dt[0,1],RMS_2dt[0,1],RMS_3dt[0,1]))
RMS_updt = np.array((RMS_1dt[0,2],RMS_2dt[0,2],RMS_3dt[0,2]))
RMS_quickdt = np.array((RMS_1dt[0,3],RMS_2dt[0,3],RMS_3dt[0,3]))

plt.figure()
plt.plot(dt,RMS_trapdt)
plt.plot(dt,RMS_csdt)
plt.plot(dt,RMS_updt)
plt.plot(dt,RMS_quickdt)
plt.yscale('log')
plt.xscale('log')
plt.xlabel('log(dt)')
plt.ylabel('log(RMS)')
plt.title('RMS values changing dt')
plt.legend(['Trap','CS','Upwind','Quick'],loc='upper right')
plt.savefig('changingDT.jpg')

#fitting a polynomial (linear) to the RMS values
#the np.polyfit returns ...Ax^2+Bx+C ... so the first value for a linear fit is the slope
# The slope here equals the effective order

slope_trapdt, bdt = np.polyfit(np.log10(dt),np.log10(RMS_trapdt),1)
slope_csdt, bdt = np.polyfit(np.log10(dt),np.log10(RMS_csdt),1)
slope_updt, bdt = np.polyfit(np.log10(dt),np.log10(RMS_updt),1)
slope_quickdt, bdt = np.polyfit(np.log10(dt),np.log10(RMS_quickdt),1)
print slope_trapdt
print slope_csdt
print slope_updt
print slope_quickdt