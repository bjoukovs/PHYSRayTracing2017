from classes.rayon import *
from classes.point import *
from classes.mur import *
from math import pi as PI
from math import atan, atan2, sin, sqrt, pow
from processing.analysis import abs_fresnel

def get_coins_solo(coins):          
    coins_solo = []

    for coin in coins:                          
        if(len(coin.murs_associes)==1):
            coins_solo.append(coin)
        
    return coins_solo

def get_coins_double(coins):
    coins_double =[]

    for coin in coins:
        if(len(coin.murs_associes)==2):     
            coins_double.append(coin)

    return coins_double

def get_vertical_walls(coins_double):
    vertical_walls = []

    for coin in coins_double:
        for wall in coin.murs_associes:
            if (wall.is_horizontal == False):        
                vertical_walls.append(wall)

    return vertical_walls

def get_direction(p1,p2):
    ## return la valeur absolue de ma direction, si vertical return "None" si horizontal return 0
    
    if((p2.x-p1.x !=0) and (p2.y-p1.y !=0)):
        direction = abs(p2.y-p1.y)/abs(p2.x-p1.x)
        return direction
    elif (p2.x-p1.x == 0):
        direction = None
        return direction
    elif (p2.y-p1.y == 0):
        direction = 0
        return direction

def get_phiprim1(p1,p2,mur_cible):
    # return la valeur de phiprim entre le point1 et le point2 par rapport a un mur choisi, mur_cible
    
    phiprim = []
    murs = p2.murs_associes
    direction = get_direction(p1,p2)
    phiprim = None

    for mur in murs:
        if (mur == mur_cible):
            
            # cas mur horizontal
            if mur.is_horizontal():
                xmax = mur.get_xmax()
                xmin = mur.get_xmin()
                
                #cas mur a gauche
                if(xmax <= p1.x):
                    if(direction == None):
                        phiprim = PI
                    elif(p2.x == xmax):
                        return PI - atan(direction)
                    elif(p2.x == xmin):
                        return atan(direction)
                
                #cas mur a droite
                elif(xmin >= p1.x):
                    if(direction == None):
                        return PI
                    elif(p2.x == xmin):
                        return PI - atan(direction)
                    elif(p2.x == xmax):
                        return atan(direction)
                
                #cas mur au niveau du point 
                elif(xmax > p1.x and xmin < p1.x):
                    if(direction == None):
                        return PI
                    else:
                        return atan(direction)
            
            #cas mur vertical
            else:
                ymax = mur.get_ymax()
                ymin = mur.get_ymin()
                
                # cas mur en dessous 
                if(ymax <= p1.y):
                    if (p2.y == ymax):
                        return PI/2 + atan(direction)
                    elif(p2.y == ymin):
                        return PI/2 - atan(direction)
                
                # cas mur au dessus
                elif(ymin >= p1.y):
                    if (p2.y == ymin):
                        return PI/2 + atan(direction)
                    elif(p2.y == ymax):
                        return PI/2 - atan(direction) 
                
                # cas mur au niveau du point
                elif(ymin < p1.y < ymax):
                    return PI/2 - atan(direction)

    return phiprim
        

def get_phiprim2(p1,p2):
    # return la valeur de phiprim lorsque c est au niveau d'un coin entre deux murs
    # phiprim est calcule par rapport a un mur bissecteur aux deux autres
    
    murs = p2.murs_associes

    for mur in murs:
        if (mur.is_horizontal()):
            mur_horizontal = Mur(mur.epaisseur, mur.coin1, mur.coin2, mur.epsilon, mur.sigma)
        else:
            mur_vertical = Mur(mur.epaisseur, mur.coin1, mur.coin2, mur.epsilon, mur.sigma)

    alpha = get_phiprim1(p1,p2,mur_vertical)

    xmin_hor =  mur_horizontal.get_xmin()
    xmax_hor = mur_horizontal.get_xmax()
    ymin_ver = mur_vertical.get_ymin()
    ymax_ver = mur_vertical.get_ymax()
    
    # reprends tous les cas possibles si p2 se trouve en haut a gauche par rapport au p1
    if (p2.x <= p1.x and p2.y >= p1.y):
        if(p2.x == xmin_hor and p2.y == ymax_ver):
            return abs(alpha-PI/4)
        elif(p2.x == xmax_hor and p2.y == ymax_ver):
            return PI/4 + alpha
        elif(p2.x == xmin_hor and p2.y == ymin_ver):
            return abs(alpha-PI/4)
        elif(p2.x == xmax_hor and p2.y == ymin_ver):
            return alpha + PI/4
    
    # reprends tous les cas possibles si p2 se trouve en bas a droite par rapport au p1
    elif (p2.x >= p1.x and p2.y <= p1.y):
        if(p2.x == xmax_hor and p2.y == ymin_ver):
            return abs(alpha-PI/4)
        elif(p2.x == xmin_hor and p2.y == ymin_ver):
            return PI/4 + alpha
        elif(p2.x == xmax_hor and p2.y == ymax_ver):
            return abs(alpha-PI/4)
        elif(p2.x == xmin_hor and p2.y == ymax_ver):
            return alpha + PI/4
    
    # reprends tous les cas possibles si p2 se trouve en bas a gauche par rapport au p1
    elif (p2.x <= p1.x and p2.y <= p1.y):
        if(p2.x == xmin_hor and p2.y == ymin_ver):
            return abs(alpha-PI/4)
        elif(p2.x == xmax_hor and p2.y == ymin_ver):
            return PI/4 + alpha
        elif(p2.x == xmin_hor and p2.y == ymax_ver):
            return abs(alpha-PI/4)
        elif(p2.x == xmax_hor and p2.y == ymax_ver):
            return alpha + PI/4
     
    # reprends tous les cas possibles si p2 se trouve en haut a droite par rapport au p1
    elif (p2.x >= p1.x and p2.y >= p1.y):
        if(p2.x == xmax_hor and p2.y == ymax_ver):
            return abs(alpha-PI/4)
        elif(p2.x == xmin_hor and p2.y == ymax_ver):
            return PI/4 + alpha
        elif(p2.x == xmax_hor and p2.y == ymin_ver):
            return abs(alpha-PI/4)
        elif(p2.x == xmin_hor and p2.y == ymin_ver):
            return alpha + PI/4
    
    


def get_phiprim(p1,p2):
    # return phiprim entre deux points pour les deux situations possibles: 1 mur et 2 murs
    murs = p2.murs_associes

    if(len(murs) == 1):
        phiprim = get_phiprim1(p1,p2,murs[0])
    else:
        phiprim = get_phiprim2(p1,p2)
    
    return phiprim 


def get_phi(p1,p2):
    # return la valeur de phi 
    phi = 2*(PI) - get_phiprim(p1,p2)

    return phi

def get_diffraction_coefficient(rayon,point,beta):
    # return le coefficient de diffraction 
    s = sqrt(pow(rayon.end_point.x-point.x, 2) + pow(rayon.end_point.y-point.y, 2))       #distance point recepteur
    sp = sqrt(pow(rayon.start_point.x-point.x, 2) + pow(rayon.start_point.y-point.y, 2))  #distance point emmeteur

    L = s*sp/(s+sp)

    delta = PI - (get_phi(rayon.end_point,point.associated_diffraction_corner) - get_phiprim(rayon.end_point,point.associated_diffraction_corner))
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

            rayon.find_all_intersections(murs,coin.murs_associes)  # donne au rayon tous les points dintersection qu'il subit durant
                                                                   # son parcours pour permettre de calculer les transmissions

            Diffraction_rays.append(rayon)

        
        return Diffraction_rays
