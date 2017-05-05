class Base(object):
    
    #antenne de la station de base, definie par sa position, sa puissance d'emission (par defaut 20dBm = 0.1W)
    #et son orientation dans le cas d'une antenne a rayonnement non-omnidirectionnel (par defaut 0 rad)
    #Pour le gain, j'ai regarde sur ce site http://www.cisco.com/c/en/us/products/collateral/wireless/aironet-1130-ag-series/datasheet_c78-502793.html
    #definition du dBi : 10 log

    def __init__(self,x,y,power=0.1,orientation=0):
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
        #4 dBi
        return 2.5119
        #on peut changer cette ligne de code

    