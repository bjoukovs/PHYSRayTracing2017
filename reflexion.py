#renvoie la list des rayons reflechis
def image_points(start_point, murs):        
    #renvoie une liste de liste avec les points images et les murs correspodant à chacun de ces points
    ls=[]
    for mur in murs:
        if(mur.is_horizontal()):
            image_point = point(start_point.x, 2*mur.coin1.y-start_point.y)
            sub_ls = [image_point, mur]
            ls.append(sub_ls)
        else:
            image_point = point(2*mur.coin1.x-start_point.x, start_point.y)
            sub_ls = [image_point, mur]
            ls.append(sub_ls)
    return ls

def une_reflexion(start_point,end_point, murs):
     list_rayons = []
     image_elems = image_points(start_point, murs)
     for elem in image_elems:
         murge =  [elem[2]]
         intersect_point = rayon.intersect (elem[1],end_point,murge) #attention  intersect_point est une liste et murge utilisé car la fonction nécessite une liste
         nouveau_rayon = Rayon(start)

def relflexion(start_point, end_point, murs):
    mur_list = []
    image_points = image_points(start_point, murs)

    