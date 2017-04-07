from const import *
from IO import draw, decode_plan
from reflexion import rayons_reflexion
from point import *
from Rayon import *

data = decode_plan("plan.txt")
MURS = data[7]
COINS = data[8]
width, height, TXx, TXy, TXorientation, RXx, RXy = data[0],data[1],data[2],data[3],data[4],data[5],data[6]

draw(MURS, width, height, TXx, TXy, RXx, RXy) 
"""ls = Point.intersect(Point(1,1), Point(-1,3), [MURS[3]])
print(MURS[3].coin1.x, MURS[3].coin1.y)
print(MURS[3].coin2.x, MURS[3].coin2.y) 
print(ls[0].x, ls[0].y)"""
rayons_reflexion(Point(TXx, TXy), Point(RXx, RXy), MURS)