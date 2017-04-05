import matplotlib.pyplot as plot
from matplotlib import collections  as coll
import pylab as pl

def draw(walls):
    lines = []
    figure = plot.figure()

    for wall in walls:
        p1=(wall.x1,wall.y1)
        p2=(wall.x2,wall.y2)
        seg = [p1,p2]
        lines.append(seg)

    wallLines = coll.LineCollection(lines)

    ax = pl.axes()
    ax.add_collection(wallLines)
    plot.show()
    #ax.autoscale()
    #ax.margins(0.1)