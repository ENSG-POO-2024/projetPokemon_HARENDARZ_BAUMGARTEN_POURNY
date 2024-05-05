# -*- coding: utf-8 -*-
"""
@Date 27 février 2024
@author: Marie-Dominique Van Damme
"""

# Import du modele
from shapes import Point, Triangle

# Fonctions aleatoires
from random import random

# Pour dessiner
import matplotlib.pyplot as plt


# ------------------------------------------------------------------------------
# Creation des 3 points
p1 = Point(0.3,0.1)
p2 = Point(0.6,0.2)
p3 = Point(0.2,0.5)

p1.plot('ro')
p2.plot('ro')
p3.plot('ro')

try:
    t2 = Triangle(Point(0,0), Point(0,10), Point(0, 20))
except:
    print ('Problème a gérer pour ce triangle')


# Creation d'un triangle
t1 = Triangle(p1,p2,p3)
t1.plot('r-')

# Translation du triangle
t2 = t1.duplic_translate(0.10,0.15)
t2.plot('g--')

# Trace des points associes aux triangles
t2.p1.plot('go')
t2.p2.plot('go')
t2.p3.plot('go')

# Representation des centres
t1.centroid().plot('r^')
t2.centroid().plot('g^')


# Nombre de points
N = 5000

# Generation de points
for i in range(0,N):
    x = random()
    y = random()
    p = Point(x,y)
    
    # if t2.contains(p):
    if p in t2:
        continue
    
    # if t1.contains(p):
    if p in t1: 
        p.plot('bx')

# Echelle de representation
plt.axis([0.15,0.75,0.03,0.75])


# ===================================================================





