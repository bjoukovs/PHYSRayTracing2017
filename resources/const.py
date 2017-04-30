from math import pi as PI
from math import pow

SIG_1 = 0.02
SIG_2 = 0.014
SIG_3 = 0.04

F = 2.45*pow(10,9) #frequence
WAVELENGTH = 3*pow(10,8)/F
BETA = 2*PI*F/3/pow(10,8)
OMEGA = 2*PI*F

EPS_0 = 1/(36*PI)*pow(10,-9) 
UO = 4*PI*pow(10,-7)

EPS_1 = 4.6*EPS_0 #BRIQUE
EPS_2 = 5*EPS_0 #BETON
EPS_3 = 2.25*EPS_0 #CLOISON