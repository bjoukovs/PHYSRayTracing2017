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
from processing.analysis import full_transpose


def decode_plan(filename):

    #Cette fonction permet de lire le plan et de renvoyer la liste de murs et de coins correspondants
    #ainsi que l'emetteur par defaut et les recepteurs definis

    print("Decodage du plan en cours...",end='') 

    input = open(filename,'r')
    lines = input.readlines()
    input.close()

    murs = []
    tempcoins = {}
    coins = []
    receivers = []

    for line in lines:
        content = line.split(" ")

        #Les premieres lignes (dimensions, base, recepteurs)

        keyword = content[0]
        if keyword=="DIMENSIONS":
            width = float(content[1])
            height = float(content[2])
        elif keyword=="BASE":
            base = Base(float(content[1]),float(content[2]))
        elif keyword=="RECEIVER":
            receivers.append(Receiver(float(content[1]),float(content[2])))

        #Les murs et les coins
        elif keyword == "W":
            x1,y1,x2,y2 = float(content[3]),float(content[4]),float(content[5]),float(content[6])
            coin1 = tempcoins.get((x1,y1),None) #Ces etapes permettent de ne pas generer de coins doubles
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
            materiau = content[1]
            if materiau=="2":
                eps = EPS_2
                sig = SIG_2
            elif materiau=="3":
                eps = EPS_3
                sig = SIG_3

            m = Mur(float(content[2]),coin1,coin2,eps,sig)
            coin1.add_mur(m)
            coin2.add_mur(m)
            murs.append(m)
        
    #Coins eligibles pour la diffraction (coins uniquement associes a un mur ou a deux murs perpendiculaires)
    coins_diffraction = []
    for coin in coins:
        walls = coin.murs_associes
        if(len(walls)==1):
            coins_diffraction.append(coin)
        elif(len(walls)==2):
            mur1, mur2 = walls[0], walls[1]
            if (mur1.is_horizontal() and not mur2.is_horizontal()) or (mur2.is_horizontal() and not mur1.is_horizontal()):
                coins_diffraction.append(coin)
    
    print("OK")

    return [width,height,base,receivers,murs,coins,coins_diffraction]



def draw_main_stage(walls,width,height,TXx,TXy,fig,ax,receivers=None):

    #Genere l'affichage de l'etage

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

    ax.plot(TXx,TXy,"r1",markersize = 12)

    if receivers != None:
        for rec in receivers:
            ax.plot(rec.x, rec.y, "g1",markersize=12)

    fig.canvas.set_window_title("Ray Tracing Visualizer")
    ax.set_xlim(-1, width+1)
    ax.set_ylim(-1, height+1)
    ax.set_facecolor('black')


def draw_rays(walls, rays_reflexion, width, height, TXx, TXy, RXx, RXy):

    #Genere l'affichage des rayons

    print("\nGeneration de l'affichage graphique des rayons...")

    fig, ax = plot.subplots()
    draw_main_stage(walls,width,height,TXx,TXy,fig,ax)  
    ray_lines = []
    ax.plot(RXx,RXy,"b1",markersize=12) #Emetteur

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


def draw_power_map(MURS,width,height,base,powers_dbm,receivers=None):

    #Genere l'affichage de la carte de puissances

    print("\nGeneration de l'affichage graphique de la puissance...")

    fig, ax = plot.subplots()
    draw_main_stage(MURS,width,height,base.x,base.y,fig,ax,receivers)
    pwrs = full_transpose(powers_dbm)
    image = ax.imshow(pwrs, cmap='hot', interpolation='bicubic',extent=[0,width,height,0])
    fig.colorbar(image)
    
    ax.set_xlabel("Power map [dBm]")

def draw_bitrate_map(MURS,width,height,base,bitrate,receivers=None):

    #Genere l'affichage du bitrate

    print("\nGeneration de l'affichage graphique du debit...")

    fig, ax = plot.subplots()
    draw_main_stage(MURS,width,height,base.x,base.y,fig,ax,receivers)
    bitrates = full_transpose(bitrate)
    image = ax.imshow(bitrates, cmap='bone', interpolation='bicubic',extent=[0,width,height,0])
    fig.colorbar(image)

    ax.set_xlabel("Bitrate map [Mbps]")

def show_maps():
    #Affiche les fenetres
    plot.show()