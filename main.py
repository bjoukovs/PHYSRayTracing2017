from const import *
from IO import draw, decode_plan
from cartography import cartography


data = decode_plan("plan.txt")
MURS = data[6]
COINS = data[7]
COINS_DIFFRACTION = data[8]
width, height, TXx, TXy, RXx, RXy = data[0],data[1],data[2],data[3],data[4],data[5]

cartography(width,height,TXx,TXy,MURS,COINS,COINS_DIFFRACTION)


