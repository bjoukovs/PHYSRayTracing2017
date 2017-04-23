from classes.rayon import *
from classes.point import *
from classes.mur import *
from diffraction import get_direction
from math import pi as PI
from math import atan, atan2, sin, sqrt, pow, asin,cos

def get_theta_i (p1,p2):
    mur = p2.mur 
    direction = get_direction(p1,p2)

    if mur.is_horizontal():
        return atan(direction)

    else:
        return PI/2 - atan(direction)

def get_theta_t (theta_i,eps):
    n = sqrt(eps)
    no = sqrt((1/36*PI)*pow(10,-9))

    return asin((no/n)sin(theta_i))

def get_s(theta_t,epaisseur):

    return epaisseur/cos(theta_t)




