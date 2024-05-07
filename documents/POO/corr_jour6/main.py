# -*- coding: utf-8 -*-

from traces import TraceGPS
from activite import NiveauConfirme, NiveauDebutant

t1 = TraceGPS("../../abbaye-de-valcroissant.dat")
print (t1)
t1.plot()

v1 = t1.vitesseReelParcours()
v2 = t1.vitesseTheoriqueParcours(NiveauConfirme())
v3 = t1.vitesseTheoriqueParcours(NiveauDebutant())

print("Vitesse réelle = " + str(round(v1, 2)) + " km/h")
print("Vitesse théorique confirmé = " + str(round(v2, 2)) + " km/h")
print("Vitesse théorique débutant = " + str(round(v3, 2)) + " km/h")		
