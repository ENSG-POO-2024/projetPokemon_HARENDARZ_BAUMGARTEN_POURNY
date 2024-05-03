# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:52:49 2024

@author: Formation
"""


import numpy as np
from PIL import Image

im = np.array(Image.open("..\code\gui\Safari_Zone_entrance_RBY.png").convert('L'))
im2 = np.array(Image.open("..\code\gui\Safari_Zone_area_3_RBY.png").convert('L'))

def convertion_case(carte):
    n,m = np.shape(carte)
    i = int(n/8)
    j = int(n/8)
    new_map = np.zeros((i,j))
    for x in range(i):
        print(x)
        for y in range(j):
            moy = 0
            for h in range(x*8,x*8+8):
                for l in range(y*8,y*8+8):
                    moy = moy + carte[h,l]
            new_map[x,y] = int(moy/64)
    return new_map

test = convertion_case(im)
test2 = convertion_case(im2)


class area:
    def __init__(self,id,n,m,tab):
        self.id = id
        self.size = (n,m)
        tab = tab

class map:
    def __init__(self,area_tab):
        self.area_tab = area_tab
        
        
class case:
    def __init__(self,x,y,area_id):
        self.x = x
        self.y = y
        self.area_id = area_id
        
    def type_case(self,map):
        num_pix = map.area_tab[self.area_id][self.x,self.y]
        if num_pix == 183 or num_pix == 193:
            return "Herbe"
        elif num_pix > 200:
            return "sol"
        elif num_pix <= 175 and num_pix != 101:
            return "obstacle"
        else:
            return "inconnu"
    




