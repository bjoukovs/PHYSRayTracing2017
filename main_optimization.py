from input_output.IO import decode_plan
from processing.main_process import power_optimization

print("--- PROGRAMME : Optimisation du placement de la base ---")

data = decode_plan("plan.txt")
MURS = data[4]
COINS = data[5]
COINS_DIFFRACTION = data[6]
width, height, base, receivers = data[0],data[1],data[2],data[3]

power_optimization(width,height,base,receivers,MURS,COINS,COINS_DIFFRACTION)

print("\nFin de programme")