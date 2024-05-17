# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:51:08 2024

@author: Formation
"""

import csv
import numpy as np


List_type = ['Steel','Fighting', 'Dragon','Water','Electric','Fire','Fairy','Ice','Bug','Normal','Grass','Poison','Psychic','Rock','Ground','Ghost','Dark','Flying']

##Permet de récupérer les indices des types.


table_type = np.genfromtxt('../data/Types.csv',delimiter = ',')


class Pokemon:
    def __init__(self,ident,name,tp,pv,at,df,at_spc,df_spc,sp):
        self.id = ident         #identifiant du pokémon
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
    
    
    def formule_attack(self,at,df1,df2):
        '''
        poke_def : pokémon défenseur
    
        Returns
        -------
        Formule du calcul de dégâts
        Sans les coefficients d efficacité de type!
        
        '''
        return (at *10) / df2
    
    
    
    
    
    def attack(self,poke_def):
        '''
        Parameters
        ----------
        poke_def : pokémon défenseur
            
        Returns
        -------
        Dégâts.
        '''

        return round(self.formule_attack(self.at,self.df,poke_def.df))





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
    
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        """
        Fonction permettant d afficher le nom du pokémon lorsqu il apparaît dans une liste par exemple.
        Sert principalement au confort visuel de nous autres, codeurs.
        """
        return self.name        
    
    
    ## Inutilisée en l'état, ne sert à rien car pas d'interface.
    def carac(self):
        print('Mes pv actuels sont : ' + str(self.pv))
        print('Mon type est : ' + str(self.tp))
    


def creation_pokedex():
    """
    Returns
    -------
    Pokedex : Dictionnaire
    Pokelist : Liste
        
    La fonction retourne l ensemble des pokémons de la première génération sous deux formes :
        une liste et un dictionnaire, aux usages différents.
    """
    
    Pokelist = []
    with open('../data/pokemon_first_gen.csv') as csvfile:
        fichier = csv.reader(csvfile,delimiter = ',')
        ident = 0
        for row in fichier:
            Pokelist.append([ident,row[1],row[2],row[5],row[6],row[7],row[8],row[9],row[10]])
            ident += 1
    
    Pokelist_legende = Pokelist.pop(0)
        
    Pokedex = {}

    for elt in Pokelist:
        Pokedex[elt[0]] = Pokemon(elt[0],elt[1],elt[2],elt[3],elt[4],elt[5],elt[6],elt[7],elt[8])

    return Pokedex, Pokelist


    
if __name__ == "__main__":
    Pokedex, Pokelist = creation_pokedex()
# =============================================================================
#     print(Pokedex)
#     print(Pokelist)
# =============================================================================
    print
    print(Pokedex[1])
    print(Pokedex[1].pv)
    print(Pokedex[2].special_attack(Pokedex[1]))


