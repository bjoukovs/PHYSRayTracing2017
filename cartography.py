from IO import draw
from reflexion import rayons_reflexion
from direct import rayon_direct
from diffraction import diffraction_rays, get_diffraction_coefficient
from point import Point
from Rayon import Rayon

def cartography(width,height,TXx,TXy,MURS,COINS,COINS_DIFFRACTION):
    
    
    
    for i in range(0,int(width)):
        for j in range(0,int(height)):
            if(i != TXx and j != TXy):
                RXx = i+0.5
                RXy = j+0.5
                RAYS_REFLEXION = rayons_reflexion(Point(TXx, TXy), Point(RXx, RXy), MURS)
                RAYS_DIRECT =  rayon_direct(Point(TXx, TXy), Point(RXx, RXy), MURS)
                RAYS_DIFFRACTION = diffraction_rays(Point(TXx,TXy),Point(RXx,RXy),MURS,COINS_DIFFRACTION)
                RAYS_AFFICHAGE =[]
                RAYS_AFFICHAGE.extend(RAYS_REFLEXION)
                RAYS_AFFICHAGE.extend(RAYS_DIRECT)
                RAYS_AFFICHAGE.extend(RAYS_DIFFRACTION)

                #Coefficient de diffraction
                #for ray in RAYS_DIFFRACTION:
                #    diffraction_point = ray.get_points_principaux()[1]
                #    val = get_diffraction_coefficient(ray,diffraction_point,BETA)
                #    diffraction_point.set_coefficient_value(val)
                #    print(val)

                draw(MURS, RAYS_AFFICHAGE, width, height, TXx, TXy, RXx, RXy) 
            break
        break
