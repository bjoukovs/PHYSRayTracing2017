from resources.const import *
from input_output.IO import draw
from processing.reflexion import rayons_reflexion
from processing.direct import rayon_direct
from processing.diffraction import diffraction_rays, get_diffraction_coefficient
from classes.point import Point
from classes.rayon import Rayon



def power_cartography(width,height,TXx,TXy,MURS,COINS,COINS_DIFFRACTION):
    
    for i in range(0,int(width)):
        for j in range(0,int(height)):
            if(i != TXx and j != TXy):
                RXx = i+0.5
                RXy = j+0.5
                data = find_all_rays(TXx,TXy,RXx,RXy,MURS,COINS,COINS_DIFFRACTION)
                RAYS_DIRECT, RAYS_REFLEXION, RAYS_DIFFRACTION = data[0], data[1], data[2]

                RAYS_AFFICHAGE =[]
                RAYS_AFFICHAGE.extend(RAYS_REFLEXION)
                RAYS_AFFICHAGE.extend(RAYS_DIRECT)
                RAYS_AFFICHAGE.extend(RAYS_DIFFRACTION)

                calculate_all_coefficients(RAYS_DIRECT,RAYS_REFLEXION,RAYS_DIFFRACTION)

                draw(MURS, RAYS_AFFICHAGE, width, height, TXx, TXy, RXx, RXy) 
            break
        break


def find_all_rays(TXx,TXy,RXx,RXy,MURS,COINS,COINS_DIFFRACTION):
    RAYS_REFLEXION = rayons_reflexion(Point(TXx, TXy), Point(RXx, RXy), MURS)
    RAYS_DIRECT =  rayon_direct(Point(TXx, TXy), Point(RXx, RXy), MURS)
    RAYS_DIFFRACTION = diffraction_rays(Point(TXx,TXy),Point(RXx,RXy),MURS,COINS_DIFFRACTION)

    return [RAYS_DIRECT,RAYS_REFLEXION,RAYS_DIFFRACTION]

def calculate_all_coefficients(RAYS_DIRECT, RAYS_REFLEXION, RAYS_DIFFRACTION):

    #Coefficient de diffraction
    for ray in RAYS_DIFFRACTION:
        diffraction_point = ray.get_points_principaux()[1]
        val = get_diffraction_coefficient(ray,diffraction_point,BETA)
        diffraction_point.set_coefficient_value(val)