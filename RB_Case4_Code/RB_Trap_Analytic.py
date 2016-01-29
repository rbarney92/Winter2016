# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 14:09:27 2015

This is Case Study 4 - Trapezoidal/Crank Nicolson

@author: Rebecca
"""

import numpy as np
import matplotlib.pyplot as plt
import math

cs = 4
if cs == 0:
    Case = "C = 0.1, s = 0.25"
elif cs == 1:
    Case = "C = 0.5, s = 0.25"
elif cs == 2:
    Case = "C = 2.0, s= 0.25"
elif cs == 3:
    Case = "C = 0.5, s = 0.5"
elif cs == 4:
    Case = "C = 0.5, s = 1"

u = 0.2 #velocity for the transport (m/s)
D = 0.005 #diffusion coefficient (m^2/s)
L = 1.0  #length of the rod (m)
k = 2.0*np.pi/L

C = np.array((0.1,0.5,2.0,0.5,0.5))
s = np.array((0.25,0.25,0.25,0.5,1.0))

#deltaX = D*C[cs]/(u*s[cs])
#dt = C[cs]*deltaX/u   

# -------------------------------------------------
# these values are for keeping dt constant, changing dx (dividing by 2.0 and 4.0)
#similar idea for changing dt and keeping deltaX constant
#dx was defined to be the smallest dx from above calculations

#dt = 0.005
#deltaX = 0.01/4.0
#previous value of dt was 0.125 (for files saved as dt1, dt2, dt3)
dt = 0.0625
deltaX = 0.01

# --------------------------------------------------


n = int(L/deltaX) + 1 #have to add in an extra node to account for the start and the end   
x = np.linspace(0,L,n)
phi0 =np.sin(k*x)

time = 0.0
tau = 1.0/(D*k**2.0) #this is the time which the problem will run

amat = np.zeros((n-1,n-1))
bmat = np.zeros((n-1,n-1))
i,j = np.indices(amat.shape)
  
a = u*dt/(4.0*deltaX) - D*dt/(2.0*deltaX**2.0)
b = (1.0+2.0*D*dt/(2.0*deltaX**2.0))
c = -(dt*u/(4.0*deltaX)) - D*dt/(2.0*deltaX**2.0)

a1 = - u*dt/(4.0*deltaX) + D*dt/(2.0*deltaX**2.0)
b1 = (1.0-2.0*D*dt/(2.0*deltaX**2.0))
c1 = dt*u/(4.0*deltaX) + D*dt/(2.0*deltaX**2.0)

#these are creating the tri-diagonal system
#j-1 creates the upper diagonal
#j+1 creates the lower diagonal
amat[i==j] = b
amat[i==j-1] = a
amat[i==j+1] = c

amat[0,n-2] = c
amat[n-2,0] = a

bmat[i==j] = b1
bmat[i==j-1] = a1
bmat[i==j+1] = c1

bmat[0,n-2] = c1
bmat[n-2,0] = a1

phi_initial = np.zeros(n)
phinew = np.zeros(n)

phinewTemp = np.zeros(n-1) #this is initialized to add the last value to solve the problem 
#the last value equals the first value

#setting the column vectors to 1's on the far ends
phi_initial = phi0[0:-1]
    
tf = tau

while time <= tf: 
    phiT = np.dot(bmat,phi_initial)
    phinewTemp = np.linalg.solve(amat,phiT)    
    phi_initial = phinewTemp
    
    time = time + dt  

print time    
phinew = np.append(phinewTemp,phinewTemp[0])

#np.save('phi_trap_Test1.npy',phinew)

plt.figure()   
plt.plot(x,phinew)

# ------------------------------------------
# analytic solution

#the time step (tau) has to match the end time to compare 'apples to apples'

phiAnalytic = (math.exp((-k**2.0)*D*time)*np.sin(k*(x-u*time)))

np.save('phi_A_DT1Test.npy',phiAnalytic)
#plt.plot(x,phiAnalytic)
        

