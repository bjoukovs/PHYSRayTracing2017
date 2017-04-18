from scipy.special import fresnel
from math import sqrt

#integrale de fresnel de -inf a inf (voir page 150)
fresnel_inf = (1,-1)

def abs_fresnel(x):
    val = fresnel(x) #fresnel de 0 à x, donne un tuple reel et imag

    #int(x a inf) = int(-inf à inf) - int(0 a x)
    res = (fresnel_inf[0] - val[0], fresnel_inf[1] - val[1])

    return (sqrt(res[0]*res[0] + res[1]*res[1]))