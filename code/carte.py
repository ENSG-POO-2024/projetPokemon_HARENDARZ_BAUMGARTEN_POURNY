# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:52:49 2024

@author: Formation
"""


import numpy as np
from PIL import Image




def convertion_case(carte):
    """
    

    Parameters
    ----------
    carte : np.array
        matrice de l'image de la carte 

    Returns
    -------
    new_map : np.array
        matrice de la carte 

    """
    n,m = np.shape(carte)
    i = int(n/8)
    j = int(m/8)
    new_map = np.zeros((i,j))
    for x in range(i):
        for y in range(j):
            moy = 0
            for h in range(x*8,x*8+8):
                for l in range(y*8,y*8+8):
                    moy = moy + carte[h,l]
            new_map[x,y] = int(moy/64)
    return new_map



class Area:
    
    def __init__(self,id,tab):
        self.id = id
        self.tab = tab

class Map:
    def __init__(self,area_tab):
        self.area_tab = area_tab
        
        
class Case:
    def __init__(self,x,y,area_id):
        self.x = x
        self.y = y
        self.area_id = area_id
        
    def type_case(self,map):
        """
        

        Parameters
        ----------
        map : Map
            

        Returns
        -------
        str
            renvoie le type de la case en question: Herbe, sol ou obstacle

        """
        num_pix = map.area_tab[self.area_id].tab[self.x,self.y]
        if num_pix == 183 or num_pix == 193:
            return "Herbe"
        elif num_pix > 210 or num_pix == 202 or num_pix == 101:
            return "sol"
        elif num_pix <= 175 and num_pix != 101:
            return "obstacle"
        else:
            return "obstacle"
    
####################
##  MAP CREATION  ##
####################

def creation_carte(pix,piy):
    img0 = Image.open("..\code\gui\Safari_Zone_entrance_RBY.png")
    img1 = Image.open("..\code\gui\Safari_Zone_area_1_RBY.png")
    img2 = Image.open("..\code\gui\Safari_Zone_area_2_RBY.png")
    img3 = Image.open("..\code\gui\Safari_Zone_area_3_RBY.png")
    img4 = Image.open("..\code\gui\player_front.png")

    all_img = [img0,img1,img2,img3]

    new_image = img0
    new_image.paste(img4, (pix,piy), mask = img4) 
    new_image.save("gui\maps\game.png")

    img0 = Image.open("..\code\gui\Safari_Zone_entrance_RBY.png")

    im = np.array(img0.convert('L'))
    im1 = np.array(img1.convert('L'))
    im2 = np.array(img2.convert('L'))
    im3 = np.array(img3.convert('L'))

    test = convertion_case(im)
    test1 = convertion_case(im1)
    test2 = convertion_case(im2)
    test3 = convertion_case(im3)

    test_area0 = Area(0,test)
    test_area1 = Area(1,test1)
    test_area2 = Area(2,test2)
    test_area3 = Area(3,test3)

    test_map = Map([test_area0,test_area1, test_area2, test_area3])

    case_depart = Case(50,29,0)
    
    return test_map, case_depart


if __name__ == "__main__":
    
# =============================================================================
#     Test
# =============================================================================
    im = np.array(Image.open("..\code\gui\Safari_Zone_entrance_RBY.png").convert('L'))
    im1 = np.array(Image.open("..\code\gui\Safari_Zone_area_1_RBY.png").convert('L'))
    im2 = np.array(Image.open("..\code\gui\Safari_Zone_area_2_RBY.png").convert('L'))
    im3 = np.array(Image.open("..\code\gui\Safari_Zone_area_3_RBY.png").convert('L'))
    
    test = convertion_case(im)
    test1 = convertion_case(im1)
    test2 = convertion_case(im2)
    test3 = convertion_case(im3)
    
    test_area0 = Area(0,test)
    test_area1 = Area(1,test2)
    test_case = Case(10,6,0)
    test_map = Map([test_area0,test_area1])
    test_type = test_case.type_case(test_map)
    
    #test_herbe = repertoire_herbe(test_map)
