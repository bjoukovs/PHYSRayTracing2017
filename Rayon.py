class Rayon(object):

    def __init__(self, TXx, TYy):
        
        self.points = []
        self.points.append(point(TXx, TXy))

    def add_point(point):
        self.points.append(point)

    def add_points(point):
        self.points.extend(point)
    
    def get_points(self):
        return self.points 

    def intersect (p1,p2,murs):
        direction = (p2.y-p1.y)/(p2.x-p1.x)
        ptintersects = []
        for mur in murs :
            if (mur.x1==mur.x2): 
                pty= direction * mur.x1
                if (mur.get_ymin() <= pty <= mur.get_ymax()):
                    p = point (mur.x1,pty)
<<<<<<< HEAD
=======
                    p.set_mur(mur)
>>>>>>> 31c9a5c54e6dfb0f766db1d2f96f068f7b602dc5
                    ptintersects.append(p)
            if ( mur.y1==mur.y2):
                ptx = mur.y1/ direction 
                if (mur.get_xmin() <= ptx <= mur.get_xmax()):
                    p = point (ptx,mur.y1)
<<<<<<< HEAD
=======
                    p.set_mur(mur)
>>>>>>> 31c9a5c54e6dfb0f766db1d2f96f068f7b602dc5
                    ptintersects.append(p)        
        return ptintersects 

