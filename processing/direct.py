from classes.rayon import *

def rayon_direct(start_point,end_point, murs):
    list_rayon = []
    nouveau_rayon = Rayon(start_point)                        
    nouveau_rayon.add_points_transmission(Point.intersect(start_point, end_point,murs))
    nouveau_rayon.add_point_principal(end_point)
    list_rayon.append(nouveau_rayon)
    return list_rayon