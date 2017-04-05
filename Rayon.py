from main import TXx, TXy

class rayon(object):
    points=[]

    def __init__(self): 
        points.append(point(TXx, TXy))

    def add_point(point)
        points.append(point)

    def add_points(point)
        points.extend(point)

    def intersect (p1,p2,murs):
    direction = (p2.y-p1.y)/(p2.x-p1.x)
    ptintersects = []
    for mur in murs :
        if (mur.x1==mur.x2): 
            pty= direction * mur.x1
            if (mur.get_ymin <= pty <= mur.get_ymax):
                p = point (mur.x1,pty)
                p.set_mur(mur)
                ptintersects.append(p)
        if ( mur.y1==mur.y2):
            ptx = mur.y1/ direction 
            if (mur.get_xmin <= ptx <= mur.get_xmax):
                p = point (ptx,mur.y1)
                p.set_mur(mur)
                ptintersects.append(p)        
    return ptintersects 

