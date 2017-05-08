from resources.const import *
from input_output.IO import decode_plan, draw_rays, show_maps
from processing.main_process import power_verif, calculate_all_coefficients
from classes.receiver import Receiver
from processing.direct import rayon_direct
from classes.point import Point
from processing.reflexion import rayons_reflexion
from math import pi as PI
from math import atan, atan2, sin, sqrt, pow, asin,cos
from cmath import exp as cexp
from cmath import polar

data = decode_plan("plan_verif.txt")
MURS = data[4]
COINS = data[5]
COINS_DIFFRACTION = data[6]
width, height, base, receivers = data[0],data[1],data[2],data[3]

#Dans ce problème : 
alpha = 0.77
beta = 125.69
gamma = complex(alpha,beta)
#verification de transmission orthogonal : on attent t^2 = 0,54
RAYS_DIRECT = []
RAYS_DIRECT.extend(rayon_direct(Point(1, 10), Point(11, 10), MURS))
calculate_all_coefficients(RAYS_DIRECT, [], [])
pt_trans = RAYS_DIRECT[0].get_points_transmission()[0]
coef = pt_trans.coefficient_value
print("le coefficient de transmission au carré attendu est près de 0.54, ici on obtient :", coef*coef)

#verification de reflexion orthogonal : on attent t^2 = 0,54
r = complex(0.42, -0.0025)
s=0.3
num = (1-r*r)* r *cexp(-2*gamma*s)
den = 1-(r*r*cexp((-2*gamma*s)))
coeffth = polar(r + num/den)[0]  #module

RAYS_REFLEXION = rayons_reflexion(Point(0, 10), Point(9, 10), MURS)
calculate_all_coefficients([], RAYS_REFLEXION, [])
pt_ref = RAYS_REFLEXION[0].get_points_reflexions()[0]
coef = pt_ref.coefficient_value
print("le coefficient de reflexion au carré attendu est :", coeffth*coeffth)
print("le coefficient de reflexion au carré ici est :", coef*coef)

#draw_rays(MURS,RAYS_DIRECT,width,height,1,10,11,20)
#show_maps()
#power_verif(width,height,base,MURS,COINS,COINS_DIFFRACTION)
show_maps()