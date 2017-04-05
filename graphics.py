import matplotlib.pyplot as plot
from matplotlib import collections  as coll
import pylab as pl

def draw(walls,width,height):
    lines = []
    figure = plot.figure()

    for wall in walls:
        p1=(wall.x1,wall.y1)
        p2=(wall.x2,wall.y2)
        print(p1)
        print(p2)
        seg = [p1,p2]
        lines.append(seg)

    wallLines = coll.LineCollection(lines)

    ax = pl.axes()
    ax.add_collection(wallLines)
    ax.set_title('Line collection')
    ax.set_xlim(x.min(), x.max())
    ax.set_ylim(ys.min(), ys.max())
    plot.show()
    #ax.autoscale()
    #ax.margins(0.1)