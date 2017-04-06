from const import *
from mur import *
from graphics import draw


murs = []
TXx = 0
TXy = 0
TXorientation = 0
RXx = 0
RXy = 0

width = 0
height = 0


input = open("plan.txt",'r')
lines = input.readlines()

i=0
for line in lines:
    content = line.split(" ")

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

    else:
        eps = EPS_1
        sig = SIG_1

        materiau = content[0]
        if materiau=="2":
            eps = EPS_2
            sig = SIG_2
        elif materiau=="3":
            eps = EPS_3
            sig = SIG_3

        m = mur(float(content[1]),float(content[2]),float(content[3]),float(content[4]),float(content[5]),eps,sig)
        murs.append(m)

    i+=1


input.close()

draw(murs,width,height)