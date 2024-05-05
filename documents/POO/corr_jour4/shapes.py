# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as plt


class Point:        
    '''
    Classe du modele de point geometrique
    '''

    def __init__(self, coord_x = 0, coord_y = 0):
        '''
        Constructeur permettant de creer des objets "points"
        Entrees : coordonnees flottantes (coord_x,coord_y) du point
        '''
        self.x = coord_x
        self.y = coord_y

    def plot(self, style):
        '''
        Fonction de trace graphique du point prenant en entree:
            - la couleur du trace : g = green, r = red, b = blue, k = black
            - 'o' = rond, 'x' = croix, '^' = triangles...
        '''
        return plt.plot(self.x, self.y, style)            
            

    def translate(self, dx, dy):  
        '''
        Fonction de translation du point suivant un vecteur (dx,dy)
        '''
        self.x += dx
        self.y += dy
        #print (self.x, self.y)
    
    def duplic_translate(self, dx, dy):         
        '''
        duplic_translate : replication d'un point apres translation
        '''
        return Point(self.x+dx, self.y+dy)
        
    def __str__(self):
        '''
        Fonction retournant une chaine de caracteres definissant les 
        caracteristiques de l'objet "point"
        '''
        return "Point de coordonnées ["+(str)(self.x)+", "+(str)(self.y) + "]"    
        
    def __eq__(self, other):
        '''
        Deux points sont égaux s'ils ont les mêmes coordonnées
        '''
        return self.x == other.x and self.y == other.y
    
    
    def distance(self, other):
        if not isinstance(other, Point):
            return None
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)



class Triangle:  
    '''
    Classe du modele de triangle.
    '''

    def __init__(self, p1, p2, p3):
        '''
        Constructeur permettant de creer des objets "triangles"
        Entrees : trois points p1, p2 et p3
        '''
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
 
        # On teste si les points sont alignes
        x1 = p2.x-p1.x
        x2 = p3.x-p1.x
        y1 = p2.y-p1.y
        y2 = p3.y-p1.y
        prod_vector = x1*y2-x2*y1
         
        if (prod_vector == 0):
            # Message d'alerte 
            raise Exception("Erreur : les trois points sont alignes")


    def plot(self, style):
        '''
        Fonction de trace graphique du triangle prenant en entree le
        style du trace : 'go', 'ro', 'r-', 'g-'...
        '''
        
        # Liste des coordonnees
        X = list()
        Y = list()
        
        X.append(self.p1.x)
        X.append(self.p2.x)
        X.append(self.p3.x)
        X.append(self.p1.x)
        
        Y.append(self.p1.y)
        Y.append(self.p2.y)
        Y.append(self.p3.y)
        Y.append(self.p1.y)
        
        # Representation
        plt.plot(X, Y, style)            
            

    def translate(self, dx, dy):  
        '''
        Fonction de translation du point suivant un vecteur (dx,dy)
        '''
        self.p1.translate()
        self.p2.translate()
        self.p3.translate()
       
    
    def duplic_translate(self, dx, dy):
        '''
        Fonction de translation du point suivant un vecteur (dx,dy)
        '''
        # Creation de nouveaux points
        p1_new = self.p1.duplic_translate(dx, dy) 
        p2_new = self.p2.duplic_translate(dx, dy)
        p3_new = self.p3.duplic_translate(dx, dy)              
        
        # Creation du nouveau triangle
        return Triangle(p1_new, p2_new, p3_new)
        
    
    def centroid(self):         
        '''
        Fonction de translation du point suivant un vecteur (dx,dy)
        '''
        # Calcul des coordonnees du centre
        xg = (self.p1.x+self.p2.x+self.p3.x)/3 
        yg = (self.p1.y+self.p2.y+self.p3.y)/3        
        
        # Creation du nouveau point
        return Point(xg, yg)
    

    # ------------------------------------------------------------
    # Fonction permettant de savoir si un point est inclus dans le 
    # triangle au sens geometrique
    # Sortie : true si inclusion, false sinon
    # ------------------------------------------------------------
    def __contains__(self, key):
        
        point = key
        
        # Coordonnees point (x0,y0)
        x0 = point.x
        y0 = point.y
        
        # Coordonnees points du triangle
        xA = self.p1.x;  xB = self.p2.x;  xC = self.p3.x
        yA = self.p1.y;  yB = self.p2.y;  yC = self.p3.y
        
        # PA-PB
        sign1 = (xA-x0)*(yB-y0) - (xB-x0)*(yA-y0)
        # PB-PC
        sign2 = (xB-x0)*(yC-y0) - (xC-x0)*(yB-y0)
        # PC-PA
        sign3 = (xC-x0)*(yA-y0) - (xA-x0)*(yC-y0)
        
        # Tests d'inclusion
        if sign1 < 0 or sign2 < 0 or sign3 < 0:
            return False
        else:
            return True
     


class Ring(Triangle):
    
    def __init__(self, P1, P2, P3, facteurk):
        super().__init__(P1, P2, P3)
        self.facteurk = facteurk
        
        G = self.centroid()
        
        xA = facteurk * (P1.x - G.x) + G.x
        xB = facteurk * (P2.x - G.x) + G.x
        xC = facteurk * (P3.x - G.x) + G.x
        yA = facteurk * (P1.y - G.y) + G.y
        yB = facteurk * (P2.y - G.y) + G.y
        yC = facteurk * (P3.y - G.y) + G.y
        
        A = Point(xA, yA)
        B = Point(xB, yB)
        C = Point(xC, yC)
        
        self.interne = Triangle(A, B, C)
    
    def plot(self, sym):
        super().plot(sym)
        self.interne.plot(sym)
        
        
    def __contains__ (self, p):
        a = not self.interne.__contains__(p)
        b = super().__contains__(p)
        return a and b
	
        














        