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
         intersect_point = Point.intersect(elem[0],end_point,murge)                     #attention  intersect_point est une liste de 1 element et murge utilise car la fonction necessite une liste
         if(len(intersect_point)):
            nouveau_rayon = Rayon(start_point)                        
            Rayon.add_points(nouveau_rayon, Point.intersect(intersect_point[0],start_point,murs))    #intersection du rayon avec les murs avants reflexions
            Rayon.add_point(nouveau_rayon, intersect_point[0])
            Rayon.add_points(nouveau_rayon, Point.intersect (intersect_point[0],end_point,murs))      #intersection du rayon avec les murs apres reflexions
            Rayon.add_point(nouveau_rayon, end_point)                                                  #point final du nouveau rayon
            list_rayons.append(nouveau_rayon)                                                   #rayon en une reflexion
                                    
     for elem in image_elems:
         mur_intermediaire_ls = []                                                       #liste des AUTRES murs
         for wall in murs:
             if (wall is not elem[1]):
                 mur_intermediaire_ls.append(wall)   
         image_elems2 = image_points(elem[0], mur_intermediaire_ls)                      #on cherche les points images des points images par les AUTRES murs
         for elem2 in image_elems2:
             murge2 =  [elem2[1]]                                                                     #une list de 1 elem avec le mur pour la deuxieme reflexion
             intersect_point2_2 = Point.intersect(elem2[0],end_point,murge2)                          #comme avant. ici point de deuxieme point de reflexion
             if(len(intersect_point2_2)):
                nouveau_rayon2 = Rayon(start_point)        
                intersect_point2_1 = Point.intersect(elem2[0],intersect_point2_2[0],[elem[1]])                       #premier point de reflexion
                if(len(intersect_point2_1)):
                    Rayon.add_points(nouveau_rayon2, Point.intersect(intersect_point2_1[0],start_point,murs))             #point entre debut et reflexion 1
                    Rayon.add_point(nouveau_rayon2, intersect_point2_1[0])
                    Rayon.add_points(nouveau_rayon2, Point.intersect(intersect_point2_1[0],intersect_point2_2[0],murs))    #point entre reflexion 1 et 2
                    Rayon.add_point(nouveau_rayon2, intersect_point2_2[0])
                    Rayon.add_points(nouveau_rayon2, Point.intersect(intersect_point2_2[0],end_point,murs))                #point entre reflexion 2 et fin
                    Rayon.add_point(nouveau_rayon2, end_point)                                                               #point final du nouveau rayon
                    list_rayons.append(nouveau_rayon2)
     print(len(list_rayons))
     return list_rayons

