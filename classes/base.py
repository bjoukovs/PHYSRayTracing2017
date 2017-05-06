class Base(object):
    
    #antenne de la station de base, definie par sa position, sa puissance d'emission (par defaut 15dBm = 0.0056W)
    #et son orientation dans le cas d'une antenne a rayonnement non-omnidirectionnel (par defaut 0 rad)
    #Pour le gain, j'ai regarde sur ce site http://www.cisco.com/c/en/us/products/collateral/wireless/small-business-100-series-wireless-access-points/datasheet-c78-736450.html
    #definition du  x[dBi] = 10 log x

    def __init__(self,x,y,power=0.0056,orientation=0):
        self._x = x
        self._y = y
        self._power = power
        self._orientation = orientation

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def power(self):
        return self._power

    def get_gain(self,theta=0):
        #3.7 dBi
        return 2.34
        #on peut changer cette ligne de code
        
    def set_x(self,x):
        self._x = x

    def set_y(self,y):
        self._y = y
    