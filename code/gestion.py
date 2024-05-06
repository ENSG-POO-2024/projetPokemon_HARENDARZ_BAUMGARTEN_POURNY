# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:50:32 2024

@author: Formation
"""


import pokemon

'''
Equipe : Dictionnaire des pokémons actifs dans l équipe du dresseur
Collection : Dictionnaire des pokémons possédés par le dresseur
'''



## INTERFACE!! ##
def starter(Pokedex):
    choix = input('Choisissez votre pokémon de départ: ')
    
    ## Choix possibles : Bulbasaur, Charmander, Squirtle, Pikachu
    
    Equipe, Collection = {str(choix):Pokedex[str(choix)]}, {str(choix):Pokedex[str(choix)]}
    return Equipe, Collection
    
    
## INTERFACE!! ##


def gestion_collection(Equipe, Collection):
    nom_poke_1 = input('Quel est le pokémon que vous souhaitez enlever de votre équipe ? ')
    if nom_poke_1 == None:
        pass
    nom_poke_2 = input('Par quel pokémon souhaitez vous le remplacer ? ')
    while nom_poke_2 in Equipe:
        nom_poke_2 = input('Ce pokémon est déjà dans votre équipe ! Il ne peut pas se dédoubler. Choisissez-en un autre :')
    del Equipe[str(nom_poke_1)]
    Equipe[str(nom_poke_2)] = Collection[str(nom_poke_2)]
    gestion_collection(Equipe, Collection)

    
    
def gestion(Equipe, Collection):
    '''
    Permet d intervertir un pokémon de l équipe avec l un de ceux de la collection.
    Si la collection contient moins de 6 pokémons, ajoute plutôt l intégralité des pokémons à l équipe.

    '''
    if len(Collection) > 6:
        gestion_collection(Equipe, Collection)
    if len(Collection) <= 6:
        Equipe = Collection
        print("Tous les pokémons de votre collection ont été ajoutés à votre équipe.")
        
        
    
    

def soin(Equipe):
    '''
    Soigne tous les pokémons de l équipe lors d un passage à un centre de soin.
    '''
    for pokemon in Equipe:
        pokemon.pv = pokemon.pv_totaux
        pokemon.etat = True
