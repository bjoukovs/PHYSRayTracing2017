from const import *
from mur import *


murs = []


input = open("plan.txt",'r')
lines = input.readlines()

for line in lines:
    content = line.split(" ")

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


input.close()