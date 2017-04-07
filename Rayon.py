class Rayon(object):

    def __init__(self, TXx, TYy):
        
        self.points = []
        self.points.append(point(TXx, TXy))

    def add_point(point):   #ajouter un point
        self.points.append(point)

    def add_points(point): #ajouter une liste de points
        self.points.extend(point)
    
    def get_points(self):
        return self.points 

    def intersect (p1,p2,murs):
        direction = (p2.y-p1.y)/(p2.x-p1.x)
        ptintersects = []
        for mur in murs :
            if (mur.is_horizontal()): 
                pty= direction * mur.coin1.x
                if (mur.get_ymin() <= pty <= mur.get_ymax()):
                    p = point (mur.coin1.x,pty)
<<<<<<< HEAD
=======
                    p.set_mur(mur)
>>>>>>> 31c9a5c54e6dfb0f766db1d2f96f068f7b602dc5
                    ptintersects.append(p)
            else:
                ptx = mur.coin1.y/ direction 
                if (mur.get_xmin() <= ptx <= mur.get_xmax()):
                    p = point (ptx,mur.coin1.y)
<<<<<<< HEAD
=======
                    p.set_mur(mur)
>>>>>>> 31c9a5c54e6dfb0f766db1d2f96f068f7b602dc5
                    ptintersects.append(p)        
        return ptintersects 

