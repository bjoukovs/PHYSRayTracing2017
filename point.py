class Point(object):
    _x = 0
    _y = 0
    _mur = None
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self.mur = None
    
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y

    def set_mur(self, mur):
        self.mur = mur
    
    def find_mur(self, murs):
        c = None
        for mur in murs:
            if (self.mur.x1 == self.x and self.mur.x2 == self.x and ((self.y<=self.mur.get_ymax() and self.y>=self.mur.get_ymin()))) \
            or (self.mur.y1 == self.y and self.mur.y2 ==self.y and ((self.x<=self.mur.get_xmax() and self.x>=self.mur.get_xmin()))):
               c = mur
        return c

    def intersect(p1,p2,murs):
        ptintersects = []
        if((p2.x-p1.x !=0) and (p2.y-p1.y !=0)):
            direction = (p2.y-p1.y)/(p2.x-p1.x)
            for mur in murs :
                if (mur.is_horizontal()): 
                    if((mur.coin1.y>p2.y and mur.coin1.y<p1.y) or(mur.coin1.y<p2.y and mur.coin1.y>p1.y) ):
                        ptx= (mur.coin1.y-p1.y)/direction + p1.x
                        if (mur.get_xmin() <= ptx <= mur.get_xmax()):
                            p = Point(ptx ,mur.coin1.y)
                            Point.set_mur(p, mur)
                            ptintersects.append(p)
                else:
                    if (mur.coin1.x>p2.x and mur.coin1.x<p1.x) or (mur.coin1.x<p2.x and mur.coin1.x>p1.x):
                        pty =(mur.coin1.x-p1.x)*direction + p1.y
                        if (mur.get_ymin() <= pty <= mur.get_ymax()):
                            p = Point(mur.coin1.x, pty)
                            Point.set_mur(p,mur)
                            ptintersects.append(p) 
        elif(p2.x== p1.x):
            for mur in murs :
                if (mur.is_horizontal()): 
                    if((mur.coin1.y>p2.y and mur.coin1.y<p1.y) or(mur.coin1.y<p2.y and mur.coin1.y>p1.y) ):
                        p = Point(p1.x ,mur.coin1.y)
                        Point.set_mur(p,mur)
                        ptintersects.append(p)
        elif(p2.y==p1.y):
            for mur in murs :
                if (mur.is_horizontal()==False):
                    if((mur.coin1.x>p2.x and mur.coin1.x<p1.x) or(mur.coin1.x<p2.x and mur.coin1.x>p1.x) ): 
                        p = Point(mur.coin1.x,p1.y)
                        Point.set_mur(p,mur)
                        ptintersects.append(p)
        return ptintersects 

