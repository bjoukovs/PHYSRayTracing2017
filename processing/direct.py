from classes.rayon import *
from processing.analysis import intersect

def rayon_direct(start_point,end_point, murs):

    #renvoie le rayon direct (dans une liste)

    list_rayon = []
    nouveau_rayon = Rayon(start_point)                        
    nouveau_rayon.add_point_principal(end_point)
    nouveau_rayon.find_all_intersections(murs) #determination des points de transmission
    list_rayon.append(nouveau_rayon)
    return list_rayon