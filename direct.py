from Rayon import *

def rayon_direct(start_point,end_point, murs):
    list_rayon = []
    nouveau_rayon = Rayon(start_point)                        
    Rayon.add_points(nouveau_rayon, Point.intersect(start_point, end_point,murs))
    Rayon.add_point(nouveau_rayon,end_point)
    list_rayon.append(nouveau_rayon)
    return list_rayon