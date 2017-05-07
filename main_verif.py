from resources.const_verif import *
from input_output.IO import decode_plan
from processing.main_process import power_verif
from classes.receiver import Receiver

data = decode_plan("plan_verif.txt")
MURS = data[4]
COINS = data[5]
COINS_DIFFRACTION = data[6]
width, height, base, receivers = data[0],data[1],data[2],data[3]

power_verif(width,height,base,MURS,COINS,COINS_DIFFRACTION)
