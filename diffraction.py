from Rayon import *
from point import *
from mur import *
from math import pi as PI
from math import atan
from math import atan2

def get_coins_solo(coins):
    coins_solo = []

    for coin in coins:                          ## est inutile finalement je le laisse au cas ou dici la fin du projet
        if(len(coin.murs_associes)==1):
            coins_solo.append(coin)
        
    return coins_solo

def get_coins_double(coins):
    coins_double =[]

    for coin in coins:
        if(len(coin.murs_associes)==2):      ## est inutile finalement je le laisse au cas ou dici la fin du projet
            coins_double.append(coin)

    return coins_double

def get_vertical_walls(coins_double):
    vertical_walls = []

    for coin in coins_double:
        for wall in coin.murs_associes:
            if (wall.is_horizontal == False):        ## est inutile finalement je le laisse au cas ou dici la fin du projet
                vertical_walls.append(wall)

    return vertical_walls

def get_direction(p1,p2):

    #direction = (p2.x-p1.x,p2.y-p1.y)
    #return direction

    if((p2.x-p1.x !=0) and (p2.y-p1.y !=0)):
        direction = (p2.y-p1.y)/(p2.x-p1.x)
        return direction
    if (p2.x-p1.x == 0):
        direction = None
        return direction
    if(p2.y-p1.y == 0):
        direction = 0
        return direction

def get_phiprim1(p1,p2,mur_cible):
    phiprim = []
    murs = p2.murs_associes
    direction = get_direction(p1,p2)
    phiprim = None

    #angle = atan2(direction[1],direction[0])

    for mur in murs:
        if (mur is mur_cible):

            if mur.is_horizontal():
                xmax = mur.get_xmax()
                xmin = mur.get_xmin()

                if(xmax <= p1.x):
                    if(direction == None):
                        phiprim = PI
                    elif(p2.x == xmax):
                        phiprim = PI - atan(direction)
                    elif(p2.x == xmin):
                        phiprim = atan(direction)

                elif(xmin >= p1.x):
                    if(direction == None):
                        phiprim = PI
                    elif(p2.x == xmin):
                        phiprim = PI - atan(direction)
                    elif(p2.x == xmax):
                        phiprim = atan(direction)

                elif(xmax > p1.x and xmin < p1.x):
                    if(direction == None):
                        phiprim = PI
                    else:
                        phiprim = atan(direction)

            else:
                ymax = mur.get_ymax()
                ymin = mur.get_ymin()

                if(ymax <= p1.y):
                    if (p2.y == ymax):
                        phiprim = PI/2 + atan(direction)
                    elif(p2.y == ymin):
                        phiprim = PI/2 - atan(direction)

                elif(ymin >= p1.y):
                    if (p2.y == ymin):
                        phiprim = PI/2 + atan(direction)
                    elif(p2.y == ymax):
                        phiprim = PI/2 - atan(direction) 

                elif(ymin < p1.y < ymax):
                    phiprim = PI/2 - atan(direction)
        return phiprim 

def get_phiprim2(p1,p2):
    murs = p2.murs_associes

    for mur in murs:
        if (mur.is_horizontal()):
            mur_horizontal = mur
        else:
            mur_vertical = mur

    alpha = get_phiprim1(p1,p2,mur_vertical)

    if (p2.x <= p1.x and p2.y >= p1.y):
        if(p2.x == mur_horizontal.get_xmin and p2.y == mur_vertical.get_ymax):
            return abs(alpha-PI/4)
        elif(p2.x == mur_horizontal.get_xmax and p2.y == mur_vertical.get_ymax):
            return PI/4 + alpha
        elif(p2.x == mur_horizontal.get_xmin and p2.y == mur_vertical.get_ymin):
            return abs(alpha-PI/4)
        elif(p2.x == mur_horizontal.get_xmax and p2.y == mur_vertical.get_ymin):
            return alpha + PI/4

    elif (p2.x >= p1.x and p2.y <= p1.y):
        if(p2.x == mur_horizontal.get_xmax and p2.y == mur_vertical.get_ymin):
            return abs(alpha-PI/4)
        elif(p2.x == mur_horizontal.get_xmin and p2.y == mur_vertical.get_ymin):
            return PI/4 + alpha
        elif(p2.x == mur_horizontal.get_xmax and p2.y == mur_vertical.get_ymax):
            return abs(alpha-PI/4)
        elif(p2.x == mur_horizontal.get_xmin and p2.y == mur_vertical.get_ymax):
            return alpha + PI/4
        
    elif (p2.x <= p1.x and p2.y <= p1.y):
        if(p2.x == mur_horizontal.get_xmin and p2.y == mur_vertical.get_ymin):
            return abs(alpha-PI/4)
        elif(p2.x == mur_horizontal.get_xmax and p2.y == mur_vertical.get_ymin):
            return PI/4 + alpha
        elif(p2.x == mur_horizontal.get_xmin and p2.y == mur_vertical.get_ymax):
            return abs(alpha-PI/4)
        elif(p2.x == mur_horizontal.get_xmax and p2.y == mur_vertical.get_ymax):
            return alpha + PI/4
        
    elif (p2.x >= p1.x and p2.y >= p1.y):
        if(p2.x == mur_horizontal.get_xmax and p2.y == mur_vertical.get_ymax):
            return abs(alpha-PI/4)
        elif(p2.x == mur_horizontal.get_xmin and p2.y == mur_vertical.get_ymax):
            return PI/4 + alpha
        elif(p2.x == mur_horizontal.get_xmax and p2.y == mur_vertical.get_ymin):
            return abs(alpha-PI/4)
        elif(p2.x == mur_horizontal.get_xmin and p2.y == mur_vertical.get_ymin):
            return alpha + PI/4
    
    


def get_phiprim(p1,p2):
    murs = p2.murs_associes

    if(len(murs)>1):
        phiprim = get_phiprim1(p1,p2,murs[0])
    else:
        phiprim = get_phiprim2(p1,p2)
    
    return phiprim 


def get_phi(p1,p2):
    phi = 2*(PI) - get_phiprim(p1,p2)

    return phi


def diffraction_rays(p_start,p_finish,murs,coins):
        Diffraction_rays = []
        
        for coin in coins:           # coins_unique normalement
            p = Point(coin.x,coin.y)
            p.set_interaction_type("d",coin)

            rayon = Rayon(p_start)
            rayon.add_point_principal(p)
            rayon.add_point_principal(p_finish)

            rayon.find_all_intersections(murs,coin.murs_associes)

            Diffraction_rays.append(rayon)

        
        return Diffraction_rays 
    

def transmission_points(p_start,p_finish,coins):
    Transmission_point = []
    '''
    coins = []
    coins_remove = []
    coins_unique = []
    j=0

    for mur in murs:
        p1 = mur.coin1
        p2 = mur.coin2
        coins.append(p1)
        coins.append(p2)

    while (j<= len(coins)-1):
            coins_unique.append(coins[j])
            if(j!= len(coins)-1):
                for k in range(j+1,len(coins)-1,1): 
                    if (coins[k].x == coins[j].x and coins[k].y == coins[j].y):
                        coins_remove.append(coins[k])
                for remove in coins_remove:
                    if(remove in coins):
                        coins.remove(remove)
                j+=1

    '''

    for coin in coins:
        p = Point(coin.x,coin.y)
        Transmission_point.extend(Point.intersect(p_start,p,murs))
        Transmission_point.extend(Point.intersect(p1,p_finish,murs))

        
    return Transmission_point 