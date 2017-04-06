from const import *
from IO import draw, decode_plan

#Décodage du plan et enregistrement des coins et des murs
data = decode_plan("plan.txt")
MURS = data[7]
COINS = data[8]
width, height, TXx, TXy, TXorientation, RXx, RXy = data[0],data[1],data[2],data[3],data[4],data[5],data[6]

draw(MURS, width, height, TXx, TXy, RXx, RXy)