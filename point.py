class point(object):
    x = 0
    y = 0
    mur = None 

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_mur(self, mur):
        self.mur = mur
    
    def find_mur(self, murs):
        c = None
        for mur in murs:
            if (self.mur.x1 == self.x and self.mur.x2 == self.x and ((self.y<=self.mur.get_ymax() and self.y>=self.mur.get_ymin()))) \
            or (self.mur.y1 == self.y and self.mur.y2 ==self.y and ((self.x<=self.mur.get_xmax() and self.x>=self.mur.get_xmin()))):
               c = mur
        return c