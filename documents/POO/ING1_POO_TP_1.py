## TP 1 - POO
## POURNY Bruce ING1 - ENSG-Géomatique
## Débuté le mercredi 28 février 2024.

import matplotlib.pyplot as plt
import math

class Point:
    def __init__(self, x, y):
        """
        Création d'une nouvelle coord x, y.
        """
        self.x = x
        self.y = y

    def plot(self, style='bx'):
        plt.plot(self.x, self.y, style)

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def duplic_translate(self, dx, dy):
        self_clone = Point(self.x, self.y)
        self_clone.translate(dx, dy)
        return self_clone
    
class Triangle:
    def __init__(self, p1:Point, p2:Point, p3:Point):
        """
        Création d'un triangle avec trois points (classe Point)  p1, p2, p3.
        """
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        if self.alignement():
            raise ValueError("VOUS AVEZ TROIS POINTS ALIGNÉS\n CECI N'EST PAS UN TRIANGLE \n MERCI DE CHANGER IMMÉDIATEMENT VOS COORDONNÉES")

    def aire(p1:Point, p2:Point, p3:Point):
        return (p2.x-p1.x)*(p3.y-p1.y) - (p3.x-p1.x)*(p2.y-p1.y)

    def alignement(self):
        return Triangle.aire(self.p1, self.p2, self.p3) == 0

    def coord_triangle(self, p1:tuple, p2:tuple, p3:tuple):
        """
        Prend en entrée trois couples de coordonnées, au format (x,y) pour chaque point.
        """
        self.p1 = Point(p1[0],p1[1])
        self.p2 = Point(p2[0],p2[1])
        self.p3 = Point(p3[0],p3[1])
    
    def plot(self, style="-"):
        list_x = [self.p1.x, self.p2.x, self.p3.x]
        list_y = [self.p1.y, self.p2.y, self.p3.y]
        plt.plot(list_x, list_y, style)
        plt.plot(list_x[1::-1], list_y[1::-1], style)
        
    


if __name__ =='__main__':
    # Partie "Point"
    
    p1 = Point(0,0)
    p1.plot('bx')
    p2 = p1.duplic_translate(2,1)
    p2.plot('bx')
    p3 = p2.duplic_translate(-1,2)
    p3.plot('bx')

    # Partie "Triangle"

    t1 = Triangle(p1, p2, p3)
    t1.plot()

    # Autres

    plt.show()