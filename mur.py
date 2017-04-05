class mur(object):
    
    epaisseur = 0
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    epsilon = 0
    sigma = 0

    def __init__(self, e, x1, y1, x2, y2, eps, sig):    #mur : type épaisseur coord x y  coord x y epsilon sigma
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.epsilon = eps 
        self.sigma = sig
        self.epaisseur = e
    
