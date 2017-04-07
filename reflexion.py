from point import *
from Rayon import *
#renvoie la list des rayons reflechis
def image_points(start_point, murs):        
    #renvoie une liste de liste avec les points images et les murs correspodant a chacun de ces points  (point image, mur pour la reflexion)
    ls=[]
    for mur in murs:
        if(mur.is_horizontal()):
            image_point = Point(start_point.x, 2*mur.coin1.y-start_point.y)
            sub_ls = [image_point, mur]
            ls.append(sub_ls)
        else:
            image_point = Point(2*mur.coin1.x-start_point.x, start_point.y)
            sub_ls = [image_point, mur]
            ls.append(sub_ls)
    return ls

def rayons_reflexion(start_point,end_point, murs):
     list_rayons = []
     image_elems = image_points(start_point, murs)
     for elem in image_elems:                                                           #1reflexion
         murge =  [elem[1]]                                                             #list du mur ou reflexion pour utiliser dans intersect()
         intersect_point = rayon.intersect(elem[1],end_point,murge)                     #attention  intersect_point est une liste de 1 element et murge utilise car la fonction necessite une liste
         nouveau_rayon = Rayon(start_point)                        
         nouveau_rayon.add_points(rayon.intersect (intersect_point[0],start_points,murs))    #intersection du rayon avec les murs avants reflexions
         nouveau_rayon.add_point(intersect_point[0])
         nouveau_rayon.add_points(rayon.intersect (intersect_point[0],end_points,murs))      #intersection du rayon avec les murs apres reflexions
         nouveau_rayon.add_point(end_point)                                                  #point final du nouveau rayon
         list_rayons.append(nouveau_rayon)                                                   #rayon en une reflexion
                                    
     for elem in image_elems:
         mur_intermediaire_ls = []                                                       #liste des AUTRES murs
         for wall in murs:
             if (wall is not mur):
                 mur_intermediaire_ls.append(wall)   
         image_elems2 = image_points(elem[0], mur_intermediaire_ls)                      #on cherche les points images des points images par les AUTRES murs
         for elem2 in image_elems2:
             murge2 =  [elem2[1]]                                                                     #une list de 1 elem avec le mur pour la deuxieme reflexion
             intersect_point2_2 = rayon.intersect(elem2[1],end_point,murge2)                          #comme avant. ici point de deuxieme point de reflexion
             nouveau_rayon2 = Rayon(start_point)        
             intersect_point2_1 = rayon.intersect(elem2[0],intersect_point2_2[0],[elem[1]])                       #premier point de reflexion
             nouveau_rayon2.add_points(rayon.intersect (intersect_point2_1[0],start_points,murs))             #point entre debut et reflexion 1
             nouveau_rayon2.add_point(intersect_point2_1[0])
             nouveau_rayon2.add_points(rayon.intersect (intersect_point2_1[0],intersect_point2_2[0],murs))    #point entre reflexion 1 et 2
             nouveau_rayon2.add_point(intersect_point2_2[0])
             nouveau_rayon2.add_points(rayon.intersect(intersect_point2_2[0],end_points,murs))                #point entre reflexion 2 et fin
             nouveau_rayon.add_point(end_point)                                                               #point final du nouveau rayon
             list_rayons.append(nouveau_rayon)
     return list_rayons

