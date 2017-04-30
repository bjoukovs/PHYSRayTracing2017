from resources.const import *
from input_output.IO import draw_power_map, draw_rays
from processing.reflexion import rayons_reflexion
from processing.direct import rayon_direct
from processing.diffraction import diffraction_rays, get_diffraction_coefficient
from classes.point import Point
from classes.rayon import Rayon
from math import sqrt, log10
from processing.transmission import set_transmission_coefficient, set_reflexion_coefficient

def power_cartography(width,height,base,receiver,MURS,COINS,COINS_DIFFRACTION):
    
    #Cette fonction permet de donner la cartographie complete de l'etage, pour chaque metre carre
    #en termes de puissance recue (en dBm)
    #le resultat est stocke dans la matrice 'powers_dbm'

    powers_dbm = []

    for i in range(0,int(width)):

        powers_dbm.append([])

        for j in range(0,int(height)):
            receiver.set_x(i+0.5)
            receiver.set_y(j+0.5)
            if(base.x != receiver.x or base.y != receiver.y):

                print(round(100/height/width*((i*height)+j)),"%")

                data = find_all_rays(base.x,base.y,receiver.x,receiver.y,MURS,COINS,COINS_DIFFRACTION)
                RAYS_DIRECT, RAYS_REFLEXION, RAYS_DIFFRACTION = data[0], data[1], data[2]

                RAYS_AFFICHAGE =[]
                RAYS_AFFICHAGE.extend(RAYS_REFLEXION)
                RAYS_AFFICHAGE.extend(RAYS_DIRECT)
                RAYS_AFFICHAGE.extend(RAYS_DIFFRACTION)

                calculate_all_coefficients(RAYS_DIRECT,RAYS_REFLEXION,RAYS_DIFFRACTION)

                power = calculate_total_power(base,receiver,RAYS_DIRECT,RAYS_REFLEXION,RAYS_DIFFRACTION)
                powers_dbm[i].append(10*log10(power*1000)) #definition de dBm
                #draw_rays(MURS, RAYS_AFFICHAGE, width, height, base.x, base.y, receiver.x, receiver.y)
            else:
                powers_dbm[i].append(0)
            #break
        #break

    draw_power_map(MURS,width,height,base,powers_dbm) 

        

def find_all_rays(TXx,TXy,RXx,RXy,MURS,COINS,COINS_DIFFRACTION):

    #revoie tous les rayons

    RAYS_REFLEXION = rayons_reflexion(Point(TXx, TXy), Point(RXx, RXy), MURS)
    RAYS_DIRECT =  rayon_direct(Point(TXx, TXy), Point(RXx, RXy), MURS)
    RAYS_DIFFRACTION = diffraction_rays(Point(TXx,TXy),Point(RXx,RXy),MURS,COINS_DIFFRACTION)

    return [RAYS_DIRECT,RAYS_REFLEXION,RAYS_DIFFRACTION]



def calculate_all_coefficients(RAYS_DIRECT, RAYS_REFLEXION, RAYS_DIFFRACTION):

    #cette fonction a pour but de calculer tous les coefficients et le stocke dans
    #chaque point du rayon associe a une interaction

    #Coefficient de diffraction
    for ray in RAYS_DIFFRACTION:
        diffraction_point = ray.get_points_principaux()[1]
        val = get_diffraction_coefficient(ray,diffraction_point,BETA)
        diffraction_point.set_coefficient_value(val)

    #Coefficient de transmission
    for ray in RAYS_DIRECT + RAYS_DIFFRACTION + RAYS_REFLEXION:
        set_transmission_coefficient(ray)
    #Coefficient de reflexion
    for ray in RAYS_REFLEXION:
        set_reflexion_coefficient(ray)
       
def calculate_total_power(base,receiver,RAYS_DIRECT,RAYS_REFLEXION,RAYS_DIFFRACTION):

    #cette fonction calcule la puissance totale recue en un point (somme des carres)
    #c'est donc valable pour un metre carre

    all_rays = RAYS_DIRECT + RAYS_DIFFRACTION + RAYS_REFLEXION
    power_total = 0

    for ray in all_rays:
        En = sqrt(60*base.power*base.get_gain()) #eq 8.78
        d = 0
        points_principaux = ray.get_points_principaux()
        points_transmission = ray.get_points_transmission()

        for i in range(len(points_principaux)):
            point = points_principaux[i]
            En = En*point.coefficient_value
            if i>0:
                point_previous = points_principaux[i-1]
                d += sqrt((point_previous.x-point.x)**2 + (point_previous.y-point.y)**2) #calcul de la distance parcourrue par le rayon

        for i in range(len(points_transmission)):
            En = En * points_transmission[i].coefficient_value

        En = En/d

        #Eq 8.83 attention a modifier car il faut prendre en compte la hauteur equivalente de l'antenne pas encore definie
        power_total = power_total + (receiver.get_hauteur_equivalente()*En)**2

    power_total = power_total/8/receiver.resistance
    return(power_total)
                   

