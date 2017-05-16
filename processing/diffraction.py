from classes.rayon import *
from classes.point import *
from classes.mur import *
from math import pi as PI
from math import atan, atan2, sin, sqrt, pow
from processing.analysis import abs_fresnel


def get_direction(p1,p2):
    ## return la direction, si vertical return "None" si horizontal return 0
    
    if((p2.x != p1.x) and (p2.y != p1.y)):
        direction = (p2.y-p1.y)/(p2.x-p1.x)
    elif (p2.x-p1.x == 0):
        direction = None    
    elif (p2.y-p1.y == 0):
        direction = 0

    return direction

def get_direction_angle(p1,p2):
    #retourne l'angle du segment allant de p1 a p2
    #print(p2.y-p1.y, p2.x-p1.x)
    return atan2(p2.y-p1.y, p2.x-p1.x)

def get_phiprim1(p,coin,mur_cible):
    # return la valeur de phiprim entre le point1 et le point2 par rapport a un mur choisi, mur_cible
    
    murs = coin.murs_associes
    direction = get_direction_angle(coin,p) #angle du segment coin-rayon
    phiprim = None

    for mur in murs:
        if (mur == mur_cible):

            #determination de l'angle du mur
            mur_angle = 0
            if mur.is_horizontal():
                if coin.x==mur.get_xmax():
                    mur_angle = PI
            else:
                mur_angle=PI/2
                if coin.y==mur.get_ymax():
                    mur_angle = -PI/2

            #phiprim est l'angle allant du mur vers le rayon = angle mur - angle rayon
            phiprim = abs(mur_angle - direction)
            return phiprim
        

def get_phiprim2(p,coin):
    # return la valeur de phiprim lorsque c est au niveau d'un coin entre deux murs
    # phiprim est calcule par rapport a un mur bissecteur aux deux autres
    
    murs = coin.murs_associes

    for mur in murs:
        if (mur.is_horizontal()):
            mur_horizontal = Mur(mur.epaisseur, mur.coin1, mur.coin2, mur.epsilon, mur.sigma)
        else:
            mur_vertical = Mur(mur.epaisseur, mur.coin1, mur.coin2, mur.epsilon, mur.sigma)

    alpha = get_phiprim1(p,coin,mur_vertical)

    xmin_hor =  mur_horizontal.get_xmin()
    xmax_hor = mur_horizontal.get_xmax()
    ymin_ver = mur_vertical.get_ymin()
    ymax_ver = mur_vertical.get_ymax()
    
    # reprends tous les cas possibles si coin se trouve en haut a gauche par rapport au p
    if (coin.x <= p.x and coin.y >= p.y):
        if(coin.x == xmin_hor and coin.y == ymax_ver):
            return abs(alpha-PI/4)
        elif(coin.x == xmax_hor and coin.y == ymax_ver):
            return PI/4 + alpha
        elif(coin.x == xmin_hor and coin.y == ymin_ver):
            return abs(alpha-PI/4)
        elif(coin.x == xmax_hor and coin.y == ymin_ver):
            return alpha + PI/4
    
    # reprends tous les cas possibles si coin se trouve en bas a droite par rapport au p
    elif (coin.x >= p.x and coin.y <= p.y):
        if(coin.x == xmax_hor and coin.y == ymin_ver):
            return abs(alpha-PI/4)
        elif(coin.x == xmin_hor and coin.y == ymin_ver):
            return PI/4 + alpha
        elif(coin.x == xmax_hor and coin.y == ymax_ver):
            return abs(alpha-PI/4)
        elif(coin.x == xmin_hor and coin.y == ymax_ver):
            return alpha + PI/4
    
    # reprends tous les cas possibles si coin se trouve en bas a gauche par rapport au p
    elif (coin.x <= p.x and coin.y <= p.y):
        if(coin.x == xmin_hor and coin.y == ymin_ver):
            return abs(alpha-PI/4)
        elif(coin.x == xmax_hor and coin.y == ymin_ver):
            return PI/4 + alpha
        elif(coin.x == xmin_hor and coin.y == ymax_ver):
            return abs(alpha-PI/4)
        elif(coin.x == xmax_hor and coin.y == ymax_ver):
            return alpha + PI/4
     
    # reprends tous les cas possibles si coin se trouve en haut a droite par rapport au p
    elif (coin.x >= p.x and coin.y >= p.y):
        if(coin.x == xmax_hor and coin.y == ymax_ver):
            return abs(alpha-PI/4)
        elif(coin.x == xmin_hor and coin.y == ymax_ver):
            return PI/4 + alpha
        elif(coin.x == xmax_hor and coin.y == ymin_ver):
            return abs(alpha-PI/4)
        elif(coin.x == xmin_hor and coin.y == ymin_ver):
            return alpha + PI/4
    
    


def get_phiprim(p,coin):
    # return phiprim entre deux points pour les deux situations possibles: 1 mur et 2 murs
    murs = coin.murs_associes

    if(len(murs) == 1):
        phiprim = get_phiprim1(p,coin,murs[0])
    else:
        phiprim = get_phiprim2(p,coin)
    
    return phiprim 


def get_phi(p,coin):
    # return la valeur de phi 
    phi = 2*(PI) - get_phiprim(p,coin)

    return phi

def get_diffraction_coefficient(rayon,point,beta):
    # return le coefficient de diffraction 
    s = sqrt(pow(rayon.end_point.x-point.x, 2) + pow(rayon.end_point.y-point.y, 2))       #distance point recepteur
    sp = sqrt(pow(rayon.start_point.x-point.x, 2) + pow(rayon.start_point.y-point.y, 2))  #distance point emmeteur

    L = s*sp/(s+sp)

    delta = PI - (get_phi(rayon.end_point,point.associated_diffraction_corner) - get_phiprim(rayon.start_point,point.associated_diffraction_corner))
    if delta==0:
        delta=0.000001
 
    #page 158 pour le calcul
    argument = 2*beta*L * pow(sin(delta/2),2)
    FT_abs = abs_fresnel(argument)
    D_abs = 0.5/sqrt(2*PI*beta*L)/sin(delta/2)*FT_abs
    return D_abs


def diffraction_rays(p_start,p_finish,murs,coins):
        # return la liste des rayons de diffractions
        Diffraction_rays = []
        
        for coin in coins:           
            p = Point(coin.x,coin.y)
            p.set_interaction_type("d",coin)

            rayon = Rayon(p_start)
            rayon.add_point_principal(p)
            rayon.add_point_principal(p_finish)

            rayon.find_all_intersections(murs,coin.murs_associes)  #Determination des points de transmissions du rayon

            Diffraction_rays.append(rayon)

        
        return Diffraction_rays
