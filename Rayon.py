from point import *
class Rayon(object):
    points=[]
    def __init__(self, start_point):
        self.points = []
        self.points.append(start_point)

    def add_point(self, point):   #ajouter un point
        self.points.append(point)

    def add_points(self, point): #ajouter une liste de points
        self.points.extend(point)
    
    def get_points(self):
        return self.points 