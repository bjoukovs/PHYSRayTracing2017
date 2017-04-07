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