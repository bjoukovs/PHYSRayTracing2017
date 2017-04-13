from Rayon import *
from point import *
from mur import *
from math import pi as PI
from math import atan
from math import atan2

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

def get_phiprim(p1,p2):
    phiprim = []
    murs = p2.murs_associes
    direction = get_direction(p1,p2)

    #angle = atan2(direction[1],direction[0])

    for mur in murs:
        if mur.is_horizontal():
            xmax = mur.get_xmax()
            xmin = mur.get_xmin()

            if(xmax <= p1.x):
                if(direction == None):
                    phiprim.append(PI)
                elif(p2.x == xmax):
                    phiprim.append(PI - atan(direction))
                elif(p2.x == xmin):
                    phiprim.append(atan(direction))

            elif(xmin >= p1.x):
                if(direction == None):
                    phiprim.append(PI)
                elif(p2.x == xmin):
                    phiprim.append(PI - atan(direction))
                elif(p2.x == xmax):
                    phiprim.append(atan(direction))

            elif(xmax > p1.x and xmin < p1.x):
                if(direction == None):
                    phiprim.append(PI)
                else:
                    phiprim.append(atan(direction))

        else:
            if(mur.get_ymax() <= p1.y):
                if (p2.y == mur.get_ymax()):
                    phiprim.append((PI)/2 + atan(direction))
                if(p2.y == mur.get_ymin()):
                    phiprim.append((PI)/2 - atan(direction))

            if(mur.get_ymin() >= p1.y):
                if (p2.y == mur.get_ymin()):
                    phiprim.append((PI)/2 + atan(direction))
                if(p2.y == mur.get_ymax()):
                    phiprim.append((PI)/2 - atan(direction)) 

            if(mur.get_ymin() < p1.y < mur.get_max()):
                    phiprim.append((PI)/2 - atan(direction))
    return phiprim 

def get_phi(p1,p2):
    phi = 2*(PI) - get_phiprim(p1,p2)

    return phi


def diffraction_rays(p_start,p_finish,murs,coins):
        Diffraction_rays = []
        
        for coin in coins:           # coins_unique normalement
            p = Point(coin.x,coin.y)

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