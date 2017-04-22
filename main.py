from resources.const import *
from input_output.IO import decode_plan
from processing.main_process import power_cartography


data = decode_plan("plan.txt")
MURS = data[5]
COINS = data[6]
COINS_DIFFRACTION = data[7]
width, height, base, RXx, RXy = data[0],data[1],data[2],data[3],data[4]

power_cartography(width,height,base,MURS,COINS,COINS_DIFFRACTION)