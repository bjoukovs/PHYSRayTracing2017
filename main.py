from resources.const import *
from input_output.IO import decode_plan
from processing.main_process import power_cartography, power_optimization
from classes.receiver import Receiver

data = decode_plan("plan.txt")
MURS = data[4]
COINS = data[5]
COINS_DIFFRACTION = data[6]
width, height, base, receiver = data[0],data[1],data[2],data[3]

#power_cartography(width,height,base,receiver,MURS,COINS,COINS_DIFFRACTION)
receiver_liste = [Receiver(19,19), Receiver (18,4), Receiver(13,6)]
power_optimization(width,height,base,receiver_liste,MURS,COINS,COINS_DIFFRACTION)