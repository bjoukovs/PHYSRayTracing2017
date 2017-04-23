from classes.rayon import *
from classes.point import *
from classes.mur import *
from classes.base import *
from const import *
from reflexion import get_reflexion_perpendiculaire
from math import pi as PI
from math import atan, atan2, sin, sqrt, pow, asin,cos
from cmath import exp

def get_theta_i (direction,p2):
    mur = p2.mur 
    
    if mur.is_horizontal():
        if direction == None:
            return PI/2
        else:
            return atan(direction)

    else:
        return PI/2 - atan(direction)

def get_theta_t (theta_i,eps):
    n = sqrt(eps)
    no = sqrt(1/(36*PI)*pow(10,-9))

    if theta_i < asin(n/no):
        return asin((no/n)sin(theta_i))
    else:
        return 0


def get_s(theta_t,epaisseur):

    return epaisseur/cos(theta_t)

def set_transmission_coefficient(rayon,beta):
    points_transmissions = rayon.points_transmission
    UO = 4*PI*pow(10,-7)
    EO = 1/(36*PI)*pow(10,-9)

    for pt_trans in points_transmissions:
        mur = pt_trans.mur

        direction = pt_trans.rayon_direction
        theta_i = get_theta_i(direction,pt_trans)
        theta_t = get_theta_t(theta_i,mur.epsilon)
        s = get_s(theta_t,mur.epaisseur)

        Z1 = sqrt(UO/EO)
        Z2 = sqrt(UO/mur.epsilon)
        r = get_reflexion_perpendiculaire(Z1,Z2,theta_i,theta_t)

        num = (1-pow(r,2))*exp(complex(0,-beta*s))
        den = 1-(pow(r,2)*exp(complex(0,(-2*beta*s)+(beta*2*s*sin(theta_t)*sin(theta_i)))))

        pt_trans.coefficient_value = num/den


    



