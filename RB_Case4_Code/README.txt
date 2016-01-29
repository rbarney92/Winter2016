README file:

RB_Trap_Analytic - this code calculates the trapezoidal and analytic solutions
- np.save was used to save each case and then each dt and dx used (These are commented out in the code)

DtEquations - this code is where the matrix equations for the last 3 methods, Central Differencing, Upwind, and QUICK, were defined. The case (Dt and dx) values could be changed at the top by chanigng cs. Holdin dt and dx constant can be seen further down in the code, a commented portion, where dx and dt were changed manually.

RB_CS4 - this code is where the values you analyzed, called the RKSolver code as well for time-integration. Similarly to the DtEquations code, the case could be changed at the top, and then changing dt and dx were completed manually. Each case and method was saved again with np.save.

Analysis - this code analyzed the data. Firt by imported each portion of saved data and then plotting the values and calculating the RMS values.

Analysis_dtdx - this code analyzed the data saved from changing dt while keeping dx constant and the changing dx while keeping dt constant.