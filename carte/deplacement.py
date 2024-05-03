
import numpy as np
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
                case_bis = c.Case()
                case_bis.x = x-1
                case_bis.y = y
                if self.case_bis.c.type_case(map) != "obstacle":
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
                case_bis = c.Case()
                case_bis.x = x + 1
                case_bis.y = y
                if self.case_bis.c.type_case(map) != "obstacle":
                    self.case = case_bis
        if direction == "left":
            
            
                    