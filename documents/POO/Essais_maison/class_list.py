# Class-list
# Test à la maison
# POURNY Bruce ING1

class Coord:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
    def __str__(self):
        txt = "Coord: ["
        txt += str(self.x) + ", "
        txt += str(self.y) + "]"
        return txt
    def __eq__(self,c2) -> bool :
        return self.x == c2.x
    
class Point(Coord):
    def __init__(self, x, y, page):
        super().__init__(x, y)
        self.page = page

