class Rayon(object):

    def __init__(self, start_point):
        
        self.points = []
        self.points.append(start_point)

    def add_point(point):   #ajouter un point
        self.points.append(point)

    def add_points(point): #ajouter une liste de points
        self.points.extend(point)
    
    def get_points(self):
        return self.points 

    def intersect (p1,p2,murs):
        if((p2.x-p1.x=!=0) and (p2.y-p1.y=!=0)):
            direction = (p2.y-p1.y)/(p2.x-p1.x)
            ptintersects = []
            for mur in murs :
                if (mur.is_horizontal()): 
                    ptx= (mur.coin1.y-p1.y)/direction + p1.x
                    if (mur.get_xmin() <= ptx <= mur.get_xmax() and mur.coin1.y=!= p1.y and mur.coin1.y=!= p2.y):
                        p = point (ptx ,mur.coin1.y)
    <<<<<<< HEAD
    =======
                        p.set_mur(mur)
    >>>>>>> 31c9a5c54e6dfb0f766db1d2f96f068f7b602dc5
                        ptintersects.append(p)
                else:
                    pty =(mur.coin1.x-p1.x)*direction + p1.y
                    if (mur.get_xmin() <= ptx <= mur.get_xmax()and mur.coin1.x=!= p1.x and mur.coin1.y=!= p2.x):
                        p = point (mur.coin1.x, pty)
    <<<<<<< HEAD
    =======
                        p.set_mur(mur)
    >>>>>>> 31c9a5c54e6dfb0f766db1d2f96f068f7b602dc5
                        ptintersects.append(p) 
        elif(p2.x== p1.x):
            for mur in murs :
                if (mur.is_horizontal()): 
                    p = point (p1.x ,mur.coin1.y)
    <<<<<<< HEAD
    =======
                        p.set_mur(mur)
    >>>>>>> 31c9a5c54e6dfb0f766db1d2f96f068f7b602dc5
                        ptintersects.append(p)
        elif(p2.y==p1.y)
            for mur in murs :
                if (mur.is_horizontal()==False): 
                    p = point (mur.coin1.x,p1.y)
    <<<<<<< HEAD
    =======
                        p.set_mur(mur)
    >>>>>>> 31c9a5c54e6dfb0f766db1d2f96f068f7b602dc5
                        ptintersects.append(p)
        return ptintersects 

