from classes.rayon import *
from classes.point import *
from classes.mur import *
from classes.base import *
from resources.const import *
from processing.diffraction import get_direction

#renvoie la list des rayons reflechis
def image_points(start_point, origin_point, murs):        
    #renvoie une liste de liste avec les points images et les murs correspodant a chacun de ces points  (point image, mur pour la reflexion)
    ls=[]
    for mur in murs:
        if(mur.is_horizontal()):
            image_point = Point(start_point.x, 2*mur.coin1.y-start_point.y)
            sub_ls = [image_point, mur]
            if((origin_point.x !=image_point.x) or(origin_point.y !=image_point.y)):
                ls.append(sub_ls)
        else:
            image_point = Point(2*mur.coin1.x-start_point.x, start_point.y)
            sub_ls = [image_point, mur]
            if((origin_point.x !=image_point.x) or(origin_point.y !=image_point.y)):
                ls.append(sub_ls)
    return ls

def rayons_reflexion(start_point,end_point, murs):
     list_rayons = []
     image_elems = image_points(start_point, start_point, murs)
     z = 0
     
     for elem in image_elems:                                                           #1 reflexion

         murge =  [elem[1]]                                                             #list du mur ou reflexion pour utiliser dans intersect()
         intersect_point = Point.intersect(elem[0],end_point,murge)                     #attention  intersect_point est une liste de 1 element et murge utilise car la fonction necessite une liste

         if(len(intersect_point)):
            new_ray = Rayon(start_point)
            intersect_point[0].set_interaction_type("r")
            intersect_point[0].set_direction(get_direction(intersect_point[0],start_point))     #donne la direction
            new_ray.add_point_reflexion(intersect_point[0])
            new_ray.add_point_principal(end_point)                                     #Les 3 points principaux definissant le rayon

            new_ray.find_all_intersections(murs)                                         #Intersection du rayon avec les murs pour la transmission
            list_rayons.append(new_ray)                                                   #rayon en une reflexion   
     

     for elem in image_elems:                             
         mur_intermediaire_ls = []                                                       #liste des AUTRES murs
         for wall in murs:
             if (Mur.is_different(wall,elem[1])):
                 mur_intermediaire_ls.append(wall)   
         image_elems2 = image_points(elem[0],start_point, mur_intermediaire_ls)                      #on cherche les points images des points images par les AUTRES murs
         if(z==0):
             save = elem[1]
             im = image_elems2
             z+=1
         for elem2 in image_elems2:
             murge2 =  [elem2[1]]                                                                   #une list de 1 elem avec le mur pour la deuxieme reflexion
             intersect_point2_2 = Point.intersect(elem2[0],end_point,murge2)                          #comme avant. ici point de deuxieme point de reflexion
             if(len(intersect_point2_2)):

                new_ray = Rayon(start_point)         
                intersect_point2_1 = Point.intersect(elem[0],intersect_point2_2[0],[elem[1]]) #premier point de reflexion

                if(len(intersect_point2_1)):
                    
                    intersect_point2_1[0].set_interaction_type("r")
                    intersect_point2_1[0].set_direction(get_direction( intersect_point2_1[0],start_point)) 
                    intersect_point2_2[0].set_interaction_type("r")
                    intersect_point2_2[0].set_direction(get_direction( intersect_point2_1[0],intersect_point2_2[0])) 
                    new_ray.add_point_reflexion(intersect_point2_1[0])                                          #1 ere reflexion
                    new_ray.add_point_reflexion(intersect_point2_2[0])                                          #2 eme reflexion
                    new_ray.add_point_principal(end_point)                                                      #point final du nouveau rayon

                    new_ray.find_all_intersections(murs)                                                        #Points de transmission

                    list_rayons.append(new_ray)

     return list_rayons
