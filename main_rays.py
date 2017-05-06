from input_output.IO import decode_plan, draw_rays, show_maps
from processing.main_process import calculate_all_coefficients, find_all_rays

print("--- PROGRAMME : Affichage de rayons ---")

data = decode_plan("plan.txt")
MURS = data[4]
COINS = data[5]
COINS_DIFFRACTION = data[6]
width, height, base, receivers = data[0],data[1],data[2],data[3]

data = find_all_rays(base.x,base.y,receivers[0].x,receivers[0].y,MURS,COINS,COINS_DIFFRACTION)
RAYS_DIRECT, RAYS_REFLEXION, RAYS_DIFFRACTION = data[0], data[1], data[2]

RAYS_AFFICHAGE =[]
RAYS_AFFICHAGE.extend(RAYS_REFLEXION)
RAYS_AFFICHAGE.extend(RAYS_DIRECT)
RAYS_AFFICHAGE.extend(RAYS_DIFFRACTION)

calculate_all_coefficients(RAYS_DIRECT,RAYS_REFLEXION,RAYS_DIFFRACTION)

draw_rays(MURS,RAYS_AFFICHAGE,width,height,base.x,base.y,receivers[0].x,receivers[0].y)

show_maps()

print("\nFin de programme")