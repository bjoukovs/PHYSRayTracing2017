from const import *
from IO import draw, decode_plan
from reflexion import rayons_reflexion
from direct import rayon_direct
from diffraction import diffraction_rays, get_diffraction_coefficient
from point import Point
from Rayon import Rayon


data = decode_plan("plan.txt")
MURS = data[7]
COINS = data[8]
width, height, TXx, TXy, TXorientation, RXx, RXy = data[0],data[1],data[2],data[3],data[4],data[5],data[6]

RAYS_REFLEXION = rayons_reflexion(Point(TXx, TXy), Point(RXx, RXy), MURS)
RAYS_DIRECT =  rayon_direct(Point(TXx, TXy), Point(RXx, RXy), MURS)
RAYS_DIFFRACTION = diffraction_rays(Point(TXx,TXy),Point(RXx,RXy),MURS,COINS)
RAYS_AFFICHAGE =[]
RAYS_AFFICHAGE.extend(RAYS_REFLEXION)
RAYS_AFFICHAGE.extend(RAYS_DIRECT)
RAYS_AFFICHAGE.extend(RAYS_DIFFRACTION)

#Coefficient de diffraction
for ray in RAYS_DIFFRACTION:
    diffraction_point = ray.get_points_principaux()[1]
    val = get_diffraction_coefficient(ray,diffraction_point,BETA)
    diffraction_point.set_coefficient_value(val)
    print(val)


draw(MURS, RAYS_AFFICHAGE, width, height, TXx, TXy, RXx, RXy) 

