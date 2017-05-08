from resources.const_verif import *
from input_output.IO import decode_plan, draw_rays, show_maps
from processing.main_process import power_verif, calculate_all_coefficients
from classes.receiver import Receiver
from processing.direct import rayon_direct
from classes.point import Point
from processing.reflexion import rayons_reflexion

data = decode_plan("plan_verif.txt")
MURS = data[4]
COINS = data[5]
COINS_DIFFRACTION = data[6]
width, height, base, receivers = data[0],data[1],data[2],data[3]

#RAYS_DIRECT = []
#RAYS_DIRECT.extend(rayon_direct(Point(1, 10), Point(11, 10), MURS))
#RAYS_DIRECT.extend(rayon_direct(Point(1, 10), Point(11, 12), MURS))
#RAYS_REFLEXION = rayons_reflexion(Point(0, 10), Point(9, 10), MURS)
#calculate_all_coefficients(RAYS_DIRECT, [], [])
#draw_rays(MURS,RAYS_DIRECT,width,height,1,10,11,20)
#show_maps()
power_verif(width,height,base,MURS,COINS,COINS_DIFFRACTION)
