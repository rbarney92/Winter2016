# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 10:48:01 2015

MAE 219 - Case Study 4, defining the equations (the phidot)

@author: Rebecca
"""

import numpy as np

def DtEquations(t,phi):    
  
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
        
    # coefficient values for the equations     
    u = 0.2 #velocity for the transport (m/s)
    D = 0.005 #diffusion coefficient (m^2/s)
    L = 1.0  #length of the rod (m)

    C = np.array((0.1,0.5,2.0,0.5,0.5))
    s = np.array((0.25,0.25,0.25,0.5,1.0))

#    deltaX = D*C[cs]/(u*s[cs])
    deltaX = 0.01
    
    n = int(L/deltaX) + 1    
    
    amat = np.zeros((n,n)) # 101x101 because the last value is known (it is the first from BC)
    i,j = np.indices(amat.shape)
    
# ---------------------------------------------------------------    
    # these are the values for the central differencing
    a = u/(2.0*deltaX) + D/(deltaX**2.0)
    b = -(2.0*D/(deltaX**2.0))
    c = -u/(2.0*deltaX) + D/(deltaX**2.0)
    
# --------------------------------------------------------------    
    #upwind values
#    a = u/deltaX + D/(deltaX**2.0)
#    b = - u/deltaX - 2.0*D/(deltaX**2.0)
#    c = D/(deltaX**2.0)
    
# ----------------------------------------------------------------
    #quick values
#    a1 = 3./8.
#    a2 = 1./8.
#    
#    a = 2.0*u/deltaX*a2 - u/deltaX*a1 + u/deltaX + D/(deltaX**2.0)
#    b = - u/deltaX - u/deltaX*a2 + 2.0*u/deltaX*a1 - 2.0*D/(deltaX**2.0)
#    c = - u/deltaX*a1 + D/(deltaX**2.0)
#    d = -u/deltaX*a2
# -----------------------------------------------------------------    
    #for ALL schemes
    #these are creating the tri-diagonal system
    #j-1 creates the upper diagonal
    #j+1 creates the lower diagonal
    amat[i==j] = b
    amat[i==j-1] = c
    amat[i==j+1] = a
    
# ----------------------------------------------------------------
    #for the quick scheme
#    amat[i==j+2] = d
#    amat[0,n-3] = d
#    amat[0,n-2] = a
#    amat[1,n-2] = d
#    amat[n-1,1] = c

# ----------------------------------------------------------------    
    #for all schemes but quick
    amat[0,n-2] = a
    amat[n-1,1] = c
    amat[n-1,n-2] = a
    
    phidot = np.dot(amat,phi)    
    
    return phidot