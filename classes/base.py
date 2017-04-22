class Base(object):
    
    #antenne de la station de base, definie par sa position, sa puissance d'emission (par defaut 20dBm = 0.1W)
    #et son orientation dans le cas d'une antenne a rayonnement non-omnidirectionnel (par defaut 0 rad)

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
        return 1
        #on peut changer cette ligne de code

    