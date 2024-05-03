# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:51:08 2024

@author: Formation
"""


import csv
import numpy as np




class Pokemon:
    def __init__(self,name,tp,pv,at,df,at_spc,df_spc,sp,coord = None):
        self.name = name
        self.tp = tp            #type
        self.pv = pv            #points de vie
        self.at = at            #attaque
        self.df = df            #défense
        self.at_spc = at_spc    #attaque spéciale
        self.df_spc = df_spc    #défense spéciale
        self.sp = sp            #vitesse(speed)
        self.coord = coord



Pokelist = []

with open('../data/pokemon_first_gen.csv') as csvfile:
    fichier = csv.reader(csvfile,delimiter = ',')
    for row in fichier:
        Pokelist.append([row[1],row[2],row[5],row[6],row[7],row[8],row[9],row[10]])


Pokelist_legende = Pokelist.pop(0)


        
Pokedex = []

for elt in Pokelist:
    Pokedex.append(Pokemon(elt[0],elt[1],elt[2],elt[3],elt[4],elt[5],elt[6],elt[7]))
    
    
    
    
    
print(Pokelist)
print(Pokelist_legende)
print(Pokedex[0].name)