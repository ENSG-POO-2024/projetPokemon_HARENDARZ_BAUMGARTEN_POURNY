# -*- coding: utf-8 -*-

import math

# Import du modèle
from shapes import Point

# Fonctions aléatoires
from random import random

# Pour dessiner
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Poisson:
    
    SIZE = 10
    
    distance_min = 0.3
    distance_max = 4
    
    turnFactor = 0.5
    
    def __init__(self, position, dx, dy):
        self.position = position
        self.dx = dx
        self.dy = dy
        
    def __str__(self):
        txt = "Poisson: position = " + str(self.position) 
        txt += ", déplacement = (" + str(self.dx) + "," + str(self.dy) + ")"
        return txt
    
    #def normaliseDeplacement(self):
    def vitesse(self):
        l = math.sqrt(self.dx**2 + self.dy**2)
        return l
    
    def __eq__(self, other):
        if isinstance(other, Poisson):
            return other.position == self.position
        return False
        
    def distance(self, other):
        return self.position.distance(other.position)
    
    def miseAjourPosition(self):
        self.position.translate(self.dx, self.dy)
        

    def normaliserVitesse(self):
        l=math.sqrt(self.dx*self.dx + self.dy*self.dy)
        self.dx /= l
        self.dy /= l
        

    def dansZoneAlignement(self, poisson):
        '''
        Retourne vrai si un autre poisson est proche,
        c'est à dire dans la zone d'alignement.
        '''
        d = self.distance(poisson)
        return d < Poisson.distance_max and d > Poisson.distance_min

    

    def eviteMur(self):
        
        # Les coordonnées des murs
        xmin = 0
        xmax = Poisson.SIZE
        ymin = 0
        ymax = Poisson.SIZE
        
        # Etape 1: on s'arrête au mur
        if self.position.x < xmin:
            self.position.x = xmin
        if self.position.x > xmax:
            self.position.x = xmax
        if self.position.y < ymin:
            self.position.y = ymin
        if self.position.y > ymax:
            self.position.y = ymax
        
        # Etape 2: Change de direction
        if (self.position.x - xmin) < Poisson.distance_min:
            self.dx += Poisson.turnFactor
            self.normaliserVitesse()
            return True
        elif (xmax - self.position.x) < Poisson.distance_min:
            self.dx -= Poisson.turnFactor
            self.normaliserVitesse()
            return True
        elif (self.position.y - ymin) < Poisson.distance_min:
            self.dy += Poisson.turnFactor
            self.normaliserVitesse()
            return True
        elif (ymax - self.position.y) < Poisson.distance_min:
            self.dy -= Poisson.turnFactor
            self.normaliserVitesse()
            return True

        return False
    
    
    def eviterPoisson(self, poissons):
        '''
        Pour éviter les poissons trop proches,
        on calcule le vecteur unitaire entre les deux poissons
        que l'on retranche à sa propre direction
        '''
        if poissons[0] != self:
            p = poissons[0]
        else:
            p = poissons[1]
        d = self.distance(p)
        
        for poisson in poissons:
            if self != poisson:
                if self.distance(poisson) < d:
                    p = poisson
                    d = self.distance(poisson)
                
        # Evitement
        if d < Poisson.distance_min and d > 0:
            diffX = (p.position.x - self.position.x) / d
            diffY = (p.position.y - self.position.y) / d
            self.dx = self.dx - diffX / 4
            self.dy = self.dy - diffY / 4
            self.normaliserVitesse()
            return True

        return False
        
    
    def calculDirectionMoyenne(self, poissons):
        '''
        La nouvelle direction du poisson est une moyenne des directions
        '''
        dxTotal = 0
        dyTotal = 0
        nbTotal = 0
        for poisson in poissons:
            if self.dansZoneAlignement(poisson):
                nbTotal += 1
                dxTotal += poisson.dx
                dyTotal += poisson.dy
        if nbTotal > 0:
            self.dx = (self.dx + dxTotal / nbTotal) / 2
            self.dy = (self.dy + dyTotal / nbTotal) / 2
            self.normaliserVitesse()
           
    
    def miseAJour(self, poissons):
        
        if not self.eviteMur():
            if not self.eviterPoisson(poissons):
                self.calculDirectionMoyenne(poissons)
        
        self.miseAjourPosition()
        #print('      ', self.position.x, self.position.y)
        
        
        
class Banc:
    
    def __init__(self, nbpoisson = 50):
        self.poissons = []
        cpt = 0
        while cpt < nbpoisson:
            x = round(random()*Poisson.SIZE, 2)
            y = round(random()*Poisson.SIZE, 2)
            vx = round(random(), 2)
            vy = round(random(), 2)
            p = Point(x, y)
            f = Poisson(p, vx, vy)
            if f not in self.poissons:
                self.poissons.append(f)
                cpt += 1
    
    def __len__(self):
        print (len(self.poissons))
        return len(self.poissons)
    
    def __getitem__(self, k):
        return self.poissons[k]
        '''
        if isinstance(k, int):
            if k >= 0  and k < len(self.poissons):
                return self.poissons[k]
        else:
            print (type(k))
        raise KeyError(k)
        '''
    
    def __contains__(self, key):
        return key in self.poissons
        '''
        print ('contains')
        for p in self.poissons:
            if p == key:
                return True
        return False
        '''
        

class Simulateur:
    
    def __init__(self):
        self.banc = Banc()
    
    def update(self, i):
        C = []
        for p in self.banc:
        # for i in range(len(self.banc)):
            p = self.banc[i]
            p.miseAJour(self.banc.poissons)
            C.append([p.position.x, p.position.y])
        self.scatter.set_offsets(C)
        
        self.fig.gca().relim()
        self.fig.gca().autoscale_view() 
        
        return self.scatter,


    def start_simulation(self):
        self.fig = plt.figure(figsize=(8, 5))
        ax = self.fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=True)
        
        X = []
        Y = []
        for i in range(len(self.banc)):
            X.append(self.banc[i].position.x)
            Y.append(self.banc[i].position.y)
        self.scatter = ax.scatter(X, Y, s=30, facecolor="red", alpha=0.8)
            
        self.ani = FuncAnimation(self.fig, self.update, interval=100)

        ax.set_xlim(0, Poisson.SIZE)
        ax.set_ylim(0, Poisson.SIZE)
        plt.show()



