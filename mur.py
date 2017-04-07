class Mur(object):
    
    _epaisseur = 0
    _coin1 = None
    _coin2 = None
    _epsilon = 0
    _sigma = 0

    def __init__(self, e, coin1, coin2, eps, sig):    #mur : type epaisseur coord x y  coord x y epsilon sigma
        self._coin1 = coin1
        self._coin2 = coin2
        self._epsilon = eps 
        self._sigma = sig
        self._epaisseur = e
    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @property
    def epaisseur(self):
        return self._epaisseur
    @property
    def coin1(self):
        return self._coin1
    @property
    def coin2(self):
        return self._coin2
    @property
    def epsilon(self):
        return self._epsilon
    @property
    def sigma(self):
        return self._sigma

    def get_xmin(self):
        return min(self.coin1.x, self.coin2.x)

    def get_xmax(self):
        return max(self.coin1.x, self.coin2.x)

    def get_ymin(self):
        return min(self.coin1.y, self.coin2.y)

    def get_ymax(self):
        return max(self.coin1.y, self.coin2.y)

    def is_horizontal(self):
        res = False
        if(self.coin1.y== self.coin2.y):
            res = True
        return res
    def is_different(self, other):
        res = True
        if((self.coin1.x ==other.coin1.x ) and (self.coin2.x ==other.coin2.x ) and (self.coin1.y ==other.coin1.y ) and (self.coin2.y ==other.coin2.y)):
            res = False
        return res
