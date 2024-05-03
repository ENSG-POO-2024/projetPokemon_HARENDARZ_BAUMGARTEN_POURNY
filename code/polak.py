# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:51:08 2024

@author: Formation
"""


import csv
import numpy as np

Pokelist = []

with open('../data/pokemon_first_gen.csv') as csvfile:
    fichier = csv.reader(csvfile,delimiter = ',')
    for row in fichier:
        Pokelist.append([row[1],row[2],row[5],row[6],row[7],row[8],row[9],row[10]])


Pokelist_legende = Pokelist.pop(0)


print(Pokelist)
print(Pokelist_legende)



class Pokemon:
    def __init__(self,name,tp,pv,at,df,at_spc,df_spc,sp):
        self.name = name
        self.tp = tp            #type
        self.pv = pv            #points de vie
        self.at = at            #attaque
        self.df = df            #défense
        self.at_spc = at_spc    #attaque spéciale
        self.df_spc = df_spc    #défense spéciale
        self.sp = sp            #vitesse(speed)
        
        