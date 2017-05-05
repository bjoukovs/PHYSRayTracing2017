from scipy.special import fresnel
from math import sqrt, pi, pow
from resources.const import *
import numpy as np

#integrale de fresnel de -inf a inf (voir page 150)
fresnel_inf = (1,-1)

#valeur moyenne asymptotique de l'integrale de fresnel de 0 a -inf (voir page 149)
fresnel_asymptotic_neg = (-0.5,0.5)

def abs_fresnel(x):

    #renvoie la fonction 8.81

    borne_inf = sqrt(2/pi)*sqrt(x)  #chgt de variable pour (voir remarque suivante)
    val = fresnel(borne_inf)
    #val = (0,0)
    val_fresnel = (val[0], -val[1])
    #fresnel donne integrale de 0 a borne_inf de sin(pi/2 * t**2) et cos(pi/2 * t**2) , donne un tuple.
    #l'integrale dont on a besoin est integrale(sin t**2 - j cos t**2) voir page 149 et 159.
    #ceci explique le changement de variable effectue ainsi que le changement de signe de la deuxieme valeur donnee par fresnel

    #int(x a inf) = int(-inf a inf) - int(0 a x) -(-int(-inf a 0))
    res = (fresnel_inf[0] - val_fresnel[0] + fresnel_asymptotic_neg[0], fresnel_inf[1] - val_fresnel[1] + fresnel_asymptotic_neg[1])

    return (2*sqrt(x)*sqrt(res[0]*res[0] + res[1]*res[1]))

def get_alpha(eps,sig):
       
        e = eps
        s = sig

        return OMEGA * sqrt((UO*e)/2) * sqrt(sqrt(1+pow(s/(OMEGA*e),2))-1)    

def get_beta(eps,sig):

        e = eps
        s = sig

        return OMEGA * sqrt((UO*e)/2) * sqrt(sqrt(1+pow(s/(OMEGA*e),2))+1)
