from resources.const import *
from input_output.IO import decode_plan
from processing.main_process import power_cartography


data = decode_plan("plan.txt")
MURS = data[4]
COINS = data[5]
COINS_DIFFRACTION = data[6]
width, height, base, receiver = data[0],data[1],data[2],data[3]

power_cartography(width,height,base,receiver,MURS,COINS,COINS_DIFFRACTION)