

class point(object):
    x = 0
    y = 0
    mur = None 

    def __init__(self, x, y)
        self.x = x
        self.y = y

    def set_mur(self, mur)
        self.mur = mur
    
    def find_mur(self, murs)
        for mur in murs:
            if((mur.x1 == x & mur.x2 ==x && ((y<=mur.get_ymax() && y>=mur.get_ymin()))) || (mur.y1 == y & mur.y2 ==y && ((x<=mur.get_xmax() && x>=mur.get_xmin())))):
                self.mur = mur