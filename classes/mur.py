from math import pi as PI
from math import pow,sqrt

class Mur(object):
    
    _epaisseur = 0
    _coin1 = None
    _coin2 = None
    _epsilon = 0
    _sigma = 0
    _alpha = 0
    _beta = 0

    def __init__(self, e, coin1, coin2, eps, sig):    #mur : type epaisseur coord x y  coord x y epsilon sigma
        self._coin1 = coin1
        self._coin2 = coin2
        self._epsilon = eps 
        self._sigma = sig
        self._epaisseur = e
        self._alpha = get_alpha(eps,sig)
        self._beta = get_beta(esp,sig)

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
    @property
    def alpha(self):
        return self._alpha
    @property
    def beta(self):
        return self._beta

    def get_alpha(eps,sig):
        omega = 2*PI*2.45*pow(10,9)
        uo = 4*PI*pow(10,-7)
        e = eps
        s = sig

        return omega * sqrt((uo*e)/2) * sqrt(sqrt(1+pow(s/(omega*e),2))-1)    
    
    def get_beta(eps,sig):
        omega = 2*PI*2.45*pow(10,9)
        uo = 4*PI*pow(10,-7)
        e = eps
        s = sig

        return omega * sqrt((uo*e)/2) * sqrt(sqrt(1+pow(s/(omega*e),2))+1)

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
