# -*- coding: utf-8 -*-

# Import du modele
from shapes import Point, Triangle, Ring

# Pour dessiner
import matplotlib.pyplot as plt

p1 = Point(1.4, 1.2)
p2 = Point(1.7, 1.3)
p3 = Point(1.3, 1.6)

#p1.plot('ro')
#p2.plot('ro')
#p3.plot('ro')

# Creation d'un triangle
t1 = Triangle(p1,p2,p3)
#t1.plot('r-')


# Echelle de representation
#plt.axis([0, 0, 1, 1])
plt.xlim([1.2, 1.8])
plt.ylim([1.1, 1.7])

R1 = Ring(p1, p2, p3, 0.5)
R1.plot('r--')

from random import random
N = 500
# Generation de points
for i in range(0,N):
    x = random()*0.6 + 1.2
    y = random()*0.6 + 1.1
    p = Point(x,y)
    if p in R1:
        p.plot('bo')