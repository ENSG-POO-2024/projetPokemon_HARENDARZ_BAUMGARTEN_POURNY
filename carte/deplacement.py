
import numpy as np
from PIL import Image
import carte as c

class joueur:
    def __init__(self,case,map):
        self.case = case
        self.map = map
        
    def deplacement(self, direction):
        x = self.case.x
        y = self.case.y
        if direction == "up":
            if x == 0:
                if self.case.area.id == 0:
                    self.case.area.id = 2
                    self.case.x = 71
                    self.case.y = 42
                elif self.case.area.id == 3:
                    if self.case.y >= 52 and self.case.y <= 55:
                        self.case.area.id = 2
                        self.case.x = 71
                        self.case.y = 17
                    else:
                        self.case.area.id = 2
                        self.case.x = 71
                        self.case.y = 5
                else:
                    self.case.area.id = 2
                    self.case.x = 71
                    self.case.y = 42
            else:
                case_bis = c.Case(x-1,y,self.case.area)
                if case_bis.type_case(self.map) != "obstacle":
                    self.case = case_bis
        if direction == "down":
            if x == 71:
                if self.case.y >= 4 and self.case.y <= 7:
                    self.case.area.id = 3
                    self.case.x = 0
                    self.area.y = 41
                elif self.case.area >= 16 and self.case.y <= 19:
                    self.case.area.id = 3
                    self.case.x = 0
                    self.case.y = 53
                else:
                    self.case.area.id = 0
                    self.case.x = 0
                    self.case.y = 29
            else:
                case_bis = c.Case(x+1,y,self.case.area)
                if case_bis.type_case(self.map) != "obstacle":
                    self.case = case_bis
        if direction == "left":
            if y == 0:
                if x >= 20 and x<= 23:
                    self.case.area.id = 3
                    self.case.x = 45
                    self.case.y = 59
                elif x >= 8 and x <= 11:
                    self.case.area.id = 2
                    self.case.x = 61
                    self.case.y = 79
                else:
                    self.case.area.id = 0
                    self.case.x = 21
                    self.case.y = 59
            else:
                case_bis = c.Case(x,y-1,self.case.area)
                if case_bis.type_case(self.map) != "obstacle":
                    self.case = case_bis
        if direction == "right":
            if y == 59:
                if self.case.area.id == 0:
                    self.case.area.id = 1
                    self.case.x = 45
                    self.case.y = 0
                elif self.case.area.id == 3:
                    self.case.area.id = 0
                    self.case.x = 21
                    self.case.y = 0
            elif y == 79:
                self.case.area.id = 1
                self.case.x = 9
                self.case.y = 0
            else:
                case_bis = c.Case(x,y+1,self.case.area)
                if case_bis.type_case(self.map) != "obstacle":
                    self.case = case_bis
                
                    
if __name__ == "__main__":
    im = np.array(Image.open("..\code\gui\Safari_Zone_entrance_RBY.png").convert('L'))
    im1 = np.array(Image.open("..\code\gui\Safari_Zone_area_1_RBY.png").convert('L'))
    im2 = np.array(Image.open("..\code\gui\Safari_Zone_area_2_RBY.png").convert('L'))
    im3 = np.array(Image.open("..\code\gui\Safari_Zone_area_3_RBY.png").convert('L'))
    
    test = c.convertion_case(im)
    test1 = c.convertion_case(im1)
    test2 = c.convertion_case(im2)
    test3 = c.convertion_case(im3)
    
    test_area0 = c.Area(0,test)
    test_area1 = c.Area(1,test1)
    test_area2 = c.Area(2,test2)
    test_area3 = c.Area(3,test3)
    test_case = c.Case(10,6,test_area0)
    test_map = c.Map([test_area0,test_area1, test_area2, test_area3])
    
    test_joueur = joueur(test_case, test_map)
    
    test_joueur.deplacement("up")
    

            
                    
            
                    