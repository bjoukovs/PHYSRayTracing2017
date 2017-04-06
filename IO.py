import matplotlib.pyplot as plot
from matplotlib import collections  as coll
import pylab as pl
from const import *
from mur import Mur
from coin import Coin

def decode_plan(filename):
    input = open(filename,'r')
    lines = input.readlines()
    input.close()

    murs = []
    tempcoins = {}
    coins = []

    i=0
    for line in lines:
        content = line.split(" ")

        #Les trois premières lignes
        if(i==0):
            width = float(content[0])
            height = float(content[1])
        elif(i==1):
            TXx = float(content[0])
            TXy = float(content[1])
            TXorientation = float(content[2])
        elif(i==2):
            RXx = float(content[0])
            RXy = float(content[1])

        #Les murs et les coins
        else:
            x1,y1,x2,y2 = float(content[2]),float(content[3]),float(content[4]),float(content[5])
            coin1 = tempcoins.get((x1,y1),None)
            coin2 = tempcoins.get((x2,y2),None)
            if(coin1==None):
                coin1 = Coin(x1,y1)
                tempcoins[(x1,y1)] = coin1
                coins.append(coin1)
            if(coin2==None):
                coin2 = Coin(x2,y2)
                tempcoins[(x2,y2)] = coin2
                coins.append(coin2)

            eps = EPS_1
            sig = SIG_1
            materiau = content[0]
            if materiau=="2":
                eps = EPS_2
                sig = SIG_2
            elif materiau=="3":
                eps = EPS_3
                sig = SIG_3

            m = Mur(float(content[1]),coin1,coin2,eps,sig)
            coin1.add_mur(m)
            coin2.add_mur(m)
            murs.append(m)

        i+=1

    return [width,height,TXx,TXy,TXorientation,RXx,RXy,murs,coins]



def draw(walls,width,height):
    lines = []
    figure = plot.figure()

    for wall in walls:
        p1=(wall.coin1.x,wall.coin1.y)
        p2=(wall.coin2.x,wall.coin2.y)
        seg = [p1,p2]
        lines.append(seg)

    wallLines = coll.LineCollection(lines)

    ax = pl.axes()
    ax.add_collection(wallLines)
    ax.set_title('Line collection')
    ax.set_xlim(-1, width+2)
    ax.set_ylim(-1, height+2)
    plot.show()