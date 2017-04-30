from classes.rayon import Rayon
from classes.point import Point
from classes.mur import Mur
from classes.base import Base
from resources.const import *
from math import pi as PI
from math import atan, atan2, sin, sqrt, pow, asin,cos
from cmath import exp as cexp
from cmath import polar

def get_theta_i (direction,p2):
    mur = p2.mur 
    
    if mur.is_horizontal():
        if direction == None:
            return PI/2
        else:
            return PI/2 - atan(direction)

    else:
        if direction == None:
            return 0
        else:
            return atan(direction)


def get_theta_t (theta_i,eps):
    n = sqrt(eps)
    no = sqrt(EPS_0)
    #cdt angle critique ?
    return asin((no/n)*sin(theta_i))


def get_s(theta_t,epaisseur):

    if theta_t != PI/2:
        return epaisseur/cos(theta_t)
    else:
        return 0

    
def get_reflexion_perpendiculaire(Z1,Z2,theta_i,theta_t):

    num = Z2*cos(theta_i)-Z1*cos(theta_t)
    den = Z2*cos(theta_i)+Z1*cos(theta_t)

    return num/den 


def set_transmission_coefficient(rayon):
    points_transmissions = rayon.get_points_transmission()

    for pt_trans in points_transmissions:
        mur = pt_trans.mur
        alpha = mur.alpha
        beta = mur.beta
        gamma = complex(alpha,beta)

        direction = abs(pt_trans.direction)
        theta_i = get_theta_i(direction,pt_trans)
        theta_t = get_theta_t(theta_i,mur.epsilon)
        s = get_s(theta_t,mur.epaisseur)
        #print(theta_i, theta_t)
        Z1 = sqrt(UO/EPS_0)
        Z2 = sqrt(UO/mur.epsilon)
        r = get_reflexion_perpendiculaire(Z1,Z2,theta_i,theta_t)

        num = (1-pow(r,2))*cexp(-gamma*s)
        den = 1-(pow(r,2)*cexp((-2*gamma*s)+(gamma*2*s*sin(theta_t)*sin(theta_i))))
        #num = (1-pow(r,2))
        #den = (1-(pow(r,2)))

        coeff_abs = polar(num/den)[0]  #module
        pt_trans.set_coefficient_value(coeff_abs)
    




    




