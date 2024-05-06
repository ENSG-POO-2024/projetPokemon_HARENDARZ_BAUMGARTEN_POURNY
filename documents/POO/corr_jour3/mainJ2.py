# -*- coding: utf-8 -*-
"""
@Date 3 mars 2024
@author Marie-Dominique Van Damme
"""

# Import du modele
from shapes import Point
from banc import Poisson 

P = Point()
o = Poisson(P, 1, 1)
o.miseAjourPosition()
print (o)

o2 = Poisson(P, 1, 1)
o3 = o

print (o == Poisson(P, 1, 1))
print (o == o2)
print (o == o3)

print (o != Poisson(P, 1, 1))
print (o != Poisson(Point(1, 2), 1, 1))

#print ('vitesse', o.vitesse)




