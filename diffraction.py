from Rayon import *
from point import *
from mur import *
from math import *

def get_direction(p1,p2):

    if((p2.x-p1.x !=0) and (p2.y-p1.y !=0)):
            direction = (p2.y-p1.y)/(p2.x-p1.x)
    if (p2.x-p1.x = 0):
        direction = None 
    if (p2.y-p1.y = 0):
        direction = 0

return direction  


def get_phiprim (p1,p2):
    mur2 = p2.find_mur(murs)
    direction = get_direction(p1,p2)
    
    if (mur2.is_horizontal):

        if (mur2.get_xmax <= p1.x):
            if (p2.x == mur2.get_xmax):
                if (direction == None):
                    phiprim = math.pi 
                else:
                    phiprim = math.pi - atan(direction) 
            if (p2.x == mur2.get_xmin):
                if (direction == None):
                    phiprim = math.pi
                else:
                    phiprim = atan(direction)
        return phiprim

        if (mur2.get_xmin >= p1.x):

            if (p2.x == mur2.get_xmin):
                if (direction == None):
                    phiprim = math.pi 
                else:
                    phiprim = math.pi - atan(direction) 
            if (p2.x == mur2.get_xmax):
                if (direction == None):
                    phiprim = math.pi
                else:
                    phiprim = atan(direction)
        return phiprim

        if (mur2.get_xmax > p1.x and mur2.get_xmin < p1.x):
                if (direction == None):
                    phiprim = math.pi 
                else:
                    phiprim = atan(direction) 
        return phiprim

    else:
        if (mur2.get_ymax <= p1.y):
            if (p2.y == mur2.get_ymax):
                    phiprim = (math.pi)/2 + atan(direction) 
            if (p2.y == mur2.get_ymin):
                    phiprim = (math.pi)/2 - atan(direction)
        return phiprim

        if (mur2.get_ymin >= p1.y):
            if (p2.y == mur2.get_ymin):
                    phiprim = (math.pi)/2 + atan(direction) 
            if (p2.y == mur2.get_ymax):
                    phiprim = (math.pi)/2 - atan(direction)
        return phiprim

        if (mur2.get_ymin < p1.y < mur2.get_ymax):
                    phiprim = (math.pi)/2 - atan(direction)
        return phiprim


def get_phi(p1,p2):
    phi = 2*(math.pi) - get_phiprim(p1,p2)

    return phi 

def diffraction_rays (p_start, p_finish,murs):
    Diffraction_rays = []
    coins =  []
        for mur in murs:
            p1 = mur.coin1
            p2 = mur.coin2
            for coin in coins:
                if (p1.x != coin.x or p1.y != coin.y):
                    coins.append(mur.coin1)
                if (p2.x != coin.x or p2.y != coin.y):
                    coins.append(mur.coin2)
       
    for coin in coins:
        p = Point(coin.x,coin.y)

        rayon = Rayon(p_start)
        rayon.add_point(p)
        rayon.add_point(p_finish)
        Diffraction_rays.append(rayon)
    
return Diffraction_rays
    
def transmission_points(p_start, p_finish, murs):
    Transmission_points = []
    coins =  []
        for mur in murs:
            p1 = mur.coin1
            p2 = mur.coin2
            for coin in coins:
                if (p1.x != coin.x or p1.y != coin.y):
                    coins.append(mur.coin1)
                if (p2.x != coin.x or p2.y != coin.y):
                    coins.append(mur.coin2)
    
    for coin in coins:
        p = Point(coin.x,coin.y)
        transmission_points.extend(Point.intersect(p_start,p,murs))
        transmission_points.extend(Point.intersect(p1,p_finish,murs))
    
    return Transmission_points