from const import *
from IO import draw, decode_plan
from reflexion import rayons_reflexion
from point import *
from Rayon import *

data = decode_plan("plan.txt")
MURS = data[7]
COINS = data[8]
width, height, TXx, TXy, TXorientation, RXx, RXy = data[0],data[1],data[2],data[3],data[4],data[5],data[6]

RAYS_REFLEXION = rayons_reflexion(Point(TXx, TXy), Point(RXx, RXy), MURS)

draw(MURS, RAYS_REFLEXION, width, height, TXx, TXy, RXx, RXy) 


