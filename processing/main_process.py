from resources.const import *
from input_output.IO import draw_power_map, draw_rays, draw_bitrate_map, show_maps
from processing.reflexion import rayons_reflexion, set_reflexion_coefficient
from processing.direct import rayon_direct
from processing.diffraction import diffraction_rays, get_diffraction_coefficient
from classes.point import Point
from classes.rayon import Rayon
from math import sqrt, log10
from processing.transmission import set_transmission_coefficient
from classes.receiver import Receiver
from classes.base import Base


def power_cartography(width,height,base,MURS,COINS,COINS_DIFFRACTION,receivers=None):
    
    #Cette fonction permet de donner la cartographie complete de l'etage, pour chaque metre carre
    #en termes de puissance recue (en dBm)
    #le resultat est stocke dans la matrice 'powers_dbm'

    print("\nCartographie de la puissance et du debit pour la base en",base.x,base.y)

    powers_dbm = []
    receiver = Receiver(0,0)

    for i in range(0,int(width)):

        powers_dbm.append([])

        for j in range(0,int(height)):
            receiver.set_x(i+0.5)
            receiver.set_y(j+0.5)
            if(base.x != receiver.x or base.y != receiver.y):

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
            print_progress(i*height+j, width*height)
            #break
        #break

    print("")

    draw_power_map(MURS,width,height,base,powers_dbm,receivers)

    bitrate = compute_bitrate(powers_dbm)
    draw_bitrate_map(MURS,width,height,base,bitrate,receivers)

    show_maps()

def power_verif(width,height,base,MURS,COINS,COINS_DIFFRACTION,receivers=None):
    #Cette fonction permet de vérifier les résultats pour un cas particulier

    print("\nCartographie de la puissance et du debit pour la base en",base.x,base.y)

    powers_dbm = []
    receiver = Receiver(0,0)

    for i in range(0,int(width)):

        powers_dbm.append([])

        for j in range(0,int(height)):
            receiver.set_x(i+0.5)
            receiver.set_y(j+0.5)
            if(base.x != receiver.x or base.y != receiver.y):

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
            print_progress(i*height+j, width*height)
            #break
        #break

    print("")

    draw_power_map(MURS,width,height,base,powers_dbm,receivers)

    bitrate = compute_bitrate(powers_dbm)
    draw_bitrate_map(MURS,width,height,base,bitrate,receivers)

    show_maps()


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

        power_total = power_total + (receiver.get_hauteur_equivalente()*En)**2

    power_total = power_total/8/receiver.resistance
    return(power_total)
                   

def compute_bitrate(powers):
    pmin = -93
    pmax = -73 #atention le debit vaut dmax au dela de cette valeur
    dmin = 6
    dmax = 54
    increment = (dmax-dmin)/(pmax-pmin)

    bitrate = []
    for idx, lines in enumerate(powers):
        bitrate.append([])
        for power in lines:
            
            if power<pmin:
                bitrate[idx].append(0)
            elif power>pmax:
                bitrate[idx].append(dmax)
            else:
                bitrate[idx].append(dmin + (power-pmin)*increment)
    
    return bitrate

def power_optimization(width,height,base,receiver,MURS,COINS,COINS_DIFFRACTION):
    #Cette fonction renvoie la position preferable de l'antenne pour avoir une bonne connexion
    # en plusieurs endroits (receveir = list)
    # et donne, pour la situation preferable, la cartographie complete de l'etage, pour chaque metre carre
    #en termes de puissance recue (en dBm)
    #le resultat est stocke dans la matrice 'powers_dbm'

    print("\nOptimisation de la position de la base pour "+str(int(len(receiver)))+" recepteurs")

    pos_base_x = 0
    pos_base_y = 0
    receiver_average = 1
    i=0
    for i in range(0,int(width)):
        for j in range(0,int(height)):
            base.set_x(i+0.5)
            base.set_y(j+0.5)

            n=1
            for elem in receiver:
                if(base.x == elem.x or base.y == elem.y):
                    n=0
                    break

            power = 0
            for elem in receiver:
                if(n==1):
                    data = find_all_rays(base.x,base.y,elem.x,elem.y,MURS,COINS,COINS_DIFFRACTION)
                    RAYS_DIRECT, RAYS_REFLEXION, RAYS_DIFFRACTION = data[0], data[1], data[2]
                    RAYS_AFFICHAGE =[]
                    RAYS_AFFICHAGE.extend(RAYS_REFLEXION)
                    RAYS_AFFICHAGE.extend(RAYS_DIRECT)
                    RAYS_AFFICHAGE.extend(RAYS_DIFFRACTION)
                    calculate_all_coefficients(RAYS_DIRECT,RAYS_REFLEXION,RAYS_DIFFRACTION)
                    power += 10*log10((calculate_total_power(base,elem,RAYS_DIRECT,RAYS_REFLEXION,RAYS_DIFFRACTION))*1000)
            if i==0 and j==0:
                receiver_average = power
                pos_base_x = base.x
                pos_base_y = base.y
            elif( receiver_average < power):
                receiver_average = power
                pos_base_x = base.x
                pos_base_y = base.y
            print_progress(i*height+j,width*height)


    receiver_average = receiver_average/len(receiver)
    print('\n\nPuissance en moyenne geometrique :', receiver_average,'dBm')
    print("Position optimale :", pos_base_x, pos_base_y )
    base = Base(pos_base_x, pos_base_y)
    power_cartography(width,height,base,MURS,COINS,COINS_DIFFRACTION,receiver)


def print_progress(current,max):
    percent = round(100/max*current)
    print('Progression : {0}%\r'.format(percent),end="")

