import matplotlib.pyplot as plot
from matplotlib import collections  as coll
import pylab as pl
from resources.const import *
from classes.mur import Mur
from classes.coin import Coin
from classes.base import Base
from classes.receiver import Receiver
import numpy as np
from numpy.matrixlib import matrix

fig, ax = plot.subplots()

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

        #Les trois premieres lignes
        if(i==0):
            width = float(content[0])
            height = float(content[1])
        elif(i==1):
            TXx = float(content[0])
            TXy = float(content[1])
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
        
        #Coins eligibles pour la diffraction
        coins_diffraction = []
        for coin in coins:
            walls = coin.murs_associes
            if(len(walls)==1):
                coins_diffraction.append(coin)
            elif(len(walls)==2):
                mur1, mur2 = walls[0], walls[1]
                if (mur1.is_horizontal() and not mur2.is_horizontal()) or (mur2.is_horizontal() and not mur1.is_horizontal()):
                    coins_diffraction.append(coin)
    
    #station de base
    base = Base(TXx,TXy)
    #antenne receptrice
    receiver = Receiver(RXx,RXy)

    return [width,height,base,receiver,murs,coins,coins_diffraction]



def draw_main_stage(walls,width,height,TXx,TXy):
    lines = []

    #Dessin des murs
    for wall in walls:
        p1=(wall.coin1.x,wall.coin1.y)
        p2=(wall.coin2.x,wall.coin2.y)
        seg = [p1,p2]
        lines.append(seg)

    wallLines = coll.LineCollection(lines)
    wallLines.set_color("white")
    wallLines.set_linewidth(2)    
    ax.add_collection(wallLines)

    ax.plot(TXx,TXy,"r+",markersize = 15)

    #ax.set_title('Ray Tracing')
    fig.canvas.set_window_title("Ray Tracing Visualizer")
    ax.set_xlim(-1, width+1)
    ax.set_ylim(-1, height+1)
    ax.set_axis_bgcolor('black')


def draw_rays(walls, rays_reflexion, width, height, TXx, TXy, RXx, RXy):

    draw_main_stage(walls,width,height,TXx,TXy)
    
    ray_lines = []

    ax.plot(RXx,RXy,"bo",markersize=10)

    #Dessin des rayons
    for ray in rays_reflexion:
        points_principaux = ray.get_points_principaux()
        points_transmission = ray.get_points_transmission()
        
        if(len(points_principaux)>=2):
            for i in range(0,len(points_principaux)-1):
                p1 = (points_principaux[i].x, points_principaux[i].y)
                p2 = (points_principaux[i+1].x, points_principaux[i+1].y)
                seg = [p1,p2]
                ray_lines.append(seg)
                if(i != 0):
                    ax.plot(p1[0], p1[1],"y+",markersize=10)

        if len(points_transmission)>0:
            for pt in points_transmission:
                ax.plot(pt.x, pt.y,"bo",markersize=4)

    ray_lines_collection = coll.LineCollection(ray_lines)
    ray_lines_collection.set_color("green")
    ray_lines_collection.set_linewidth(1)    
    ax.add_collection(ray_lines_collection)

    plot.show()


def draw_power_map(MURS,width,height,base,powers_dbm):
    
    draw_main_stage(MURS,width,height,base.x,base.y)

    for i in range(len(powers_dbm)):
        for j in range(len(powers_dbm[i])):
            plot.text(i+0.5,j+0.5,str(round(powers_dbm[i][j])),horizontalalignment='center',verticalalignment='center',color='green')
    pwrs = matrix(powers_dbm)
    pwrs = pwrs.transpose()
    plot.imshow(pwrs, cmap='hot', interpolation='bicubic',extent=[0,height,width,0])
    plot.colorbar()
    plot.show()