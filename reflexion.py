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
     for elem in image_elems:                        #1reflexion
         murge =  [elem[2]]
         intersect_point = rayon.intersect (elem[1],end_point,murge) #attention  intersect_point est une liste et murge utilisé car la fonction nécessite une liste
         nouveau_rayon = Rayon(start_point)                        
         nouveau_rayon.add_points(rayon.intersect (intersect_point,start_points,murs))  #intersection du rayon avec les murs avants réflexions
         nouveau_rayon.add_point([intersect_point)
         nouveau_rayon.add_points(rayon.intersect (intersect_point,end_points,murs))  #intersection du rayon avec les murs après réflexions
         nouveau_rayon.add_point(end_point)                                           #point final du nouveau rayon
         list_rayons.append(nouveau_rayon)                                           #rayon en une réflexion                         
         mur_intermediaire_ls = []
         for wall un murs:                           #2 reflexions
            if (wall=!= mur):
                mur_intermediaire_ls.append(wall)
            image_points(elem[1], mur_intermediaire_ls)

    return list_rayons


def relflexion(start_point, end_point, murs):
    rayons =[]
    rayon.extend(une_reflexion(start_point,end_point, murs))

    