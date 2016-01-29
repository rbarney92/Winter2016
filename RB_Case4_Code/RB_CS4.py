# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 09:51:13 2015

Case Study 4 - The Central Differencing method

@author: Rebecca
"""

import numpy as np
import math
# matplotlib library for plotting like matlab
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
from matplotlib import rcParams
# modules that were created to match MatLab code
import RkSolve as odeRK

rcParams.update({'figure.autolayout': True})

#defining the case, differing dt and dx values
#make sure this value of cs corresponds to the value of cs in the DtEquations 
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
k = 2*np.pi/L

C = np.array((0.1,0.5,2.0,0.5,0.5))
s = np.array((0.25,0.25,0.25,0.5,1.0))

#deltaX = D*C[cs]/(u*s[cs]) 
#dt = C[cs]*deltaX/u 

# ----------------------------------------------------------------
#need to keep dt stable and change dx to understand how this effects the answers
#kept dt the smallest dt and dx from the calculated dt above
#dt = 0.005
#deltaX = 0.01/2.0
deltaX = 0.01
dt = 0.0625

#----------------------------------------------------------------

n = int(L/deltaX) + 1    
x = np.linspace(0,L,n)
phi0 =np.sin(k*x)
    
time = 0.0
tau = 1.0/(D*k**2.0)

# given ode45 settings
optionsRK = [1e-6, 1e-6, dt]

#initial parameters
y0 = phi0

#setting the time span
tSpan = [0, tau]

#gets the final time and position values for the non-stiff method used
phi_tc,phi = odeRK.RkSolve(tSpan,y0,optionsRK)
Phi = phi[-1,:]

np.save('Phi_cs_Test1.npy',Phi)

plt.plot(Phi) #plots the solutiona at last time step
