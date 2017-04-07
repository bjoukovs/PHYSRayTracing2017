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

def reflexion(start_point,end_point, murs):
     list_rayons = []
     image_elems = image_points(start_point, murs)
     for elem in image_elems: #1reflexion
         murge =  [elem[2]]
         intersect_point = rayon.intersect(elem[1],end_point,murge) #attention  intersect_point est une liste de 1 element et murge utilise car la fonction necessite une liste
         nouveau_rayon = Rayon(start_point)                        
         nouveau_rayon.add_points(rayon.intersect (intersect_point[0],start_points,murs))  #intersection du rayon avec les murs avants reflexions
         nouveau_rayon.add_point([intersect_point[0])
         nouveau_rayon.add_points(rayon.intersect (intersect_point[0],end_points,murs))  #intersection du rayon avec les murs après reflexions
         nouveau_rayon.add_point(end_point)                                           #point final du nouveau rayon
         list_rayons.append(nouveau_rayon)                                           #rayon en une reflexion
                                    
    for elem in image_elems:  #2 reflexions
        mur_intermediaire_ls = []
        for wall un murs:
            if (wall=!= mur):
                mur_intermediaire_ls.append(wall)
        image_elems2 = image_points(elem[1], mur_intermediaire_ls)
        for elem2 in image_elems2:
            murge2_2 =  [elem2[2]]
            intersect_point2_2 = rayon.intersect(elem2[1],end_point,murge2) #attention  intersect_point est une liste et murge utilise car la fonction necessite une liste
            nouveau_rayon2 = Rayon(start_point)        
            intersect_point2_1 = rayon.intersect(elem[1],intersect_point2_2[0],murge)        
            nouveau_rayon2.add_points(rayon.intersect (intersect_point2_1[0],start_points,murs))
            nouveau_rayon2.add_point([intersect_point2_1[0])
            nouveau_rayon2.add_points(rayon.intersect (intersect_point2_1[0],intersect_point2_2[0],murs)) 
            nouveau_rayon2.add_point([intersect_point2_2[0])
            nouveau_rayon2.add_points(rayon.intersect(intersect_point2_2[0],end_points,murs))
            nouveau_rayon.add_point(end_point)                                           #point final du nouveau rayon
            list_rayons.append(nouveau_rayon)
    return list_rayons

