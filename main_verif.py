from resources.const import *
from input_output.IO import decode_plan, draw_rays, show_maps
from processing.main_process import power_verif, calculate_all_coefficients
from classes.receiver import Receiver
from classes.coin import Coin
from processing.direct import rayon_direct
from classes.point import Point
from processing.reflexion import rayons_reflexion
from processing.diffraction import diffraction_rays
from math import pi as PI
from math import atan, atan2, sin, sqrt, pow, asin,cos
from cmath import exp as cexp
from cmath import polar
from processing.analysis import abs_fresnel_verif

data = decode_plan("plan_verif.txt")
MURS = data[4]
COINS = data[5]
COINS_DIFFRACTION = data[6]
width, height, base, receivers = data[0],data[1],data[2],data[3]

####################################
#Remarque préliminaire : pour obtenir les 
#valeurs suivantes, il faut changer, dans le
#fichier resources.const le EPS 2 et SIG2
#par les valeurs suivies du commentaire "#!!! a changer"

#Dans ce problème : 
alpha = 0.77
beta = 125.69
gamma = complex(alpha,beta)

#Verification de transmission orthogonal : on attent t^2 = 0,54
RAYS_DIRECT = []
RAYS_DIRECT.extend(rayon_direct(Point(1, 10), Point(11, 10), MURS))
calculate_all_coefficients(RAYS_DIRECT, [], [])
pt_trans = RAYS_DIRECT[0].get_points_transmission()[0]
coef = pt_trans.coefficient_value
print("le coefficient de transmission au carré attendu est près de 0.54, ici on obtient :", coef*coef)

#Verification de reflexion orthogonal : 
r = complex(0.42, -0.0025)
s=0.3
num = (1-r*r)* r *cexp(-2*gamma*s)
den = 1-(r*r*cexp((-2*gamma*s)))
coeffth = polar(r + num/den)[0] 

RAYS_REFLEXION = rayons_reflexion(Point(0, 10), Point(9, 10), MURS)
calculate_all_coefficients([], RAYS_REFLEXION, [])
pt_ref = RAYS_REFLEXION[0].get_points_reflexions()[0]
coef = pt_ref.coefficient_value
print("le coefficient de reflexion au carré attendu est :", coeffth*coeffth)
print("le coefficient de reflexion au carré ici est :", coef*coef)

#Verification de diffraction : 
d1=9
d2 = 1
h = 2
nu = h * sqrt((2*(d1+d2))/(WAVELENGTH*d1*d2))
print(nu)
coefth2 = abs_fresnel_verif(nu)*sqrt(2)/2

coins = []
coins.append(COINS_DIFFRACTION [1])
RAYS_DIFFRACTION = diffraction_rays(Point(1, 10), Point(11, 10),MURS,coins)
calculate_all_coefficients([], [], RAYS_DIFFRACTION)
pt_dif = RAYS_DIFFRACTION[0].get_points_principaux()[1]
coef = pt_dif.coefficient_value
print("le coefficient de diffraction au carré attendu est :",coefth2*coefth2)
print("le coefficient de diffraction au carré ici est :", coef*coef)
#draw_rays(MURS,RAYS_DIFFRACTION,width,height,1,10,11,20)
#power_verif(width,height,base,MURS,COINS,COINS_DIFFRACTION)
show_maps()