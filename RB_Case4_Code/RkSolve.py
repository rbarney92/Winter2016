# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 09:51:13 2015

Case study 4 - runga kutta integration over the distance

@author: Rebecca
"""

from numpy import array
from scipy.integrate import ode
import DtEquations as dtphi
import numpy as np
import time
import csv

def RkSolve(tSpan,y0,options):
    # here, the solver is defined
    solver_RK5 = 'dopri5'
    # unpack option values
    opt_rtol = options[0]
    opt_atol = options[1]
    dt = options[2]
    # use initial and final time range
    t0 = tSpan[0]
    tmax = tSpan[1]
    # set equation to solve, two different solvers to solve the sytem of EQs
    solverRK = ode(dtphi.DtEquations)
     # initialize time and solution vectors for RK method and BDF 
    tRK   = []
    solRK = []
    solRK.append(y0)
    tRK.append(t0)
    
    startRK = time.clock()
    
    solverRK.set_initial_value(y0, t0)
    # Solver 1 - using the Runge-Kutta 5 method (dopri5)
    print('starting ODE solver '+solver_RK5)
    solverRK.set_integrator(solver_RK5,nsteps=1000,atol=opt_atol,rtol=opt_rtol)

    stepTimestart = (time.clock()) 
#    c = open('CoarseTime_Nonstiff.csv','w')
#    b = csv.writer(c)    
    
    count = 1.0
    
    #starting the solver    
    while solverRK.successful() and solverRK.t < tmax:
        solverRK.integrate(solverRK.t + dt)
        tRK.append(solverRK.t)
        solRK.append(solverRK.y)
        if np.floor(tRK[-1]) == count:
            stepTime = ((time.clock()-stepTimestart))
            stepTimestart = time.clock()
#            d = [stepTime,solverRK.t]
#            b.writerow(d)
            count = count+1.0
#        print(solverRK.successful,solverRK.t)
    elapsedRK = (time.clock() - startRK)
    print('time to solve %g' %(elapsedRK))
#    c.close()

    # Array conversion and processing for sensitivity and plotting
    tRK   = array(tRK)
    solRK = array(solRK)    

    return tRK, solRK   
        

