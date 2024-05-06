# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:51:08 2024

@author: Formation
"""


import csv
import numpy as np


List_type = ['Steel','Fighting', 'Dragon','Water','Electric','Fire','Fairy','Ice','Bug','Normal','Grass','Poison','Psychic','Rock','Ground','Ghost','Shadow','Flying']

##Permet de récupérer les indices des types. Traduction de ténèbres à vérifier ? 


table_type = np.genfromtxt('../data/Types.csv',delimiter = ',')


class Pokemon:
    def __init__(self,name,tp,pv,at,df,at_spc,df_spc,sp):
        self.name = name        #nom
        self.tp = tp            #type
        self.pv = int(pv)            #points de vie actuels
        self.pv_totaux = int(pv)     #points de vie totaux
        self.at = int(at)            #attaque
        self.df = int(df)            #défense
        self.at_spc = int(at_spc)    #attaque spéciale
        self.df_spc = int(df_spc)    #défense spéciale
        self.sp = int(sp)            #vitesse(speed)
        self.etat = True        #en état de combat
    
    
    def formule_attack(self,poke_def):
        '''
        poke_def : pokémon défenseur
    
        Returns
        -------
        Formule du calcul de dégâts
        Sans les coefficients d efficacité de type!
        
        '''
        return self.at*(self.df/poke_def.df)
    
    
    
    def attack(self,poke_def):
        '''
        Parameters
        ----------
        poke_def : pokémon défenseur
            
        Returns
        -------
        Dégâts.
        '''
        return round(self.formule_attack(poke_def))


    def special_attack(self,poke_def):
        """
        poke_def : pokémon défenseur
        
    
        Returns
        -------
        Cherche le coefficient d efficacité de type.
        Multiplie le résultat de la formule d attaque par le coef
        Renvoie l arrondi si le résultat est relatif
        """
        i1,i2 = List_type.index(self.tp), List_type.index(poke_def.tp)
        coef = table_type[i1][i2]
        return round(self.formule_attack(self.at_spc,self.df_spc,poke_def.df_spc)*coef)
        
    



Pokelist = []

with open('../data/pokemon_first_gen.csv') as csvfile:
    fichier = csv.reader(csvfile,delimiter = ',')
    for row in fichier:
        Pokelist.append([row[1],row[2],row[5],row[6],row[7],row[8],row[9],row[10]])


Pokelist_legende = Pokelist.pop(0)


        
Pokedex = []

for elt in Pokelist:
    Pokedex.append(Pokemon(elt[0],elt[1],elt[2],elt[3],elt[4],elt[5],elt[6],elt[7]))
    
    
    
    
    
# =============================================================================
# print(Pokelist)
# print(Pokelist_legende)
# print(Pokedex[0].name)
# =============================================================================
