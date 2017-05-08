#################
# UTILISEZ LES FICHIERS MAIN_CARTOGRAPHY ET MAIN_OPTIMIZATION
#################
#J ai separe le programme en deux afin qu on puisse plus facilement utiliser l un ou l autre programme

from resources.const import *
from input_output.IO import decode_plan
from processing.main_process import power_cartography, power_optimization
from classes.receiver import Receiver

data = decode_plan("plan.txt")
MURS = data[4]
COINS = data[5]
COINS_DIFFRACTION = data[6]
width, height, base, receivers = data[0],data[1],data[2],data[3]

#power_cartography(width,height,base,MURS,COINS,COINS_DIFFRACTION)
power_optimization(width,height,base,receivers,MURS,COINS,COINS_DIFFRACTION)