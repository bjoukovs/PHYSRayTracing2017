from point import Point

class Rayon(object):

    def __init__(self, start_point):
        self.points_principaux = [] #début, fin, réflexion, diffraction
        self.points_transmission = [] #transmission
        self.points_principaux.append(start_point)

    def add_point_principal(self, point):   #ajouter un point de réflexion ou de diffraction
        self.points_principaux.append(point)

    def add_points_principaux(self, point): #ajouter une liste de points de réflexion ou de diffraction
        self.points_principaux.extend(point)
    
    def get_points_principaux(self):
        return self.points_principaux

    def add_point_transmission(self, point):   #ajouter un point de transmission
        self.points_transmission.append(point)

    def add_points_transmission(self, point): #ajouter une liste de points de transmission
        self.points_transmission.extend(point)
    
    def get_points_transmission(self):
        return self.points_transmission



    def find_all_intersections(self,murs,exception=None):
        #Fonction établissant la liste de tous les points d'intersection (de transmission) d'un rayon, avec une liste de murs exceptions

        new_points = []
        
        for i in range(0,len(self.points_principaux)-1):
            p1 = self.points_principaux[i]
            p2 = self.points_principaux[i+1]

            intersections = Point.intersect(p1,p2,murs)
            for inter in intersections:
                if inter.mur not in exception:
                    new_points.append(inter)
        
        self.add_points_transmission(new_points)
