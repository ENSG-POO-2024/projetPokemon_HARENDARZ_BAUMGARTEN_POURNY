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


def creation_Environnement(Pokedex):
    '''
    Crée la liste des pokémons trouvés dans l environnement
    '''
    Environnement = Pokedex
    return Environnement



## INTERFACE!! ##
def starter(Environnement,choix):
    '''
    choix : information venant de l interface sur le pokémon de départ
    '''    
    ## Choix possibles : Bulbasaur, Charmander, Squirtle, Pikachu
    
    Equipe, Collection = {int(choix):Environnement[int(choix)]}, {int(choix):Environnement[int(choix)]}
    
    ## on supprime le pokémon choisi de l'environnement : ce dictionnaire régit également les pokémons rencontrés dans la nature. 
    del Environnement[int(choix)]
    
    return Equipe, Collection
    
    
## INTERFACE!! ##





## Fonctions utilitaires pour le dresseur
    
'''
Les fonctions de gestion vont être intégrées dans la structure de l interface.

'''

def gestion_collection(Equipe, Collection):
    '''
    Fonction secondaire de gestion, cas taille Collection > 6 et taille Equipe == 6.

    '''
    id_poke_1 = input('Quel est le pokémon que vous souhaitez enlever de votre équipe ? ')
    if id_poke_1 == None:
        pass
    id_poke_2 = input('Par quel pokémon souhaitez vous le remplacer ? ')
    while id_poke_2 in Equipe:
        id_poke_2 = input('Ce pokémon est déjà dans votre équipe ! Il ne peut pas se dédoubler. Choisissez-en un autre : ')
    del Equipe[int(id_poke_1)]
    Equipe[int(id_poke_2)] = Collection[int(id_poke_2)]
    gestion_collection(Equipe, Collection)

    

    
def gestion(Equipe, Collection):
    '''
    Permet d intervertir un pokémon de l équipe avec l un de ceux de la collection.
    Si la collection contient moins de 6 pokémons, ajoute plutôt l intégralité des pokémons à l équipe.

    '''
    
    if len(Collection) > 6 and len(Equipe) == 6:
        gestion_collection(Equipe, Collection)
    elif len(Collection) <= 6:
        Equipe = Collection
        print("Tous les pokémons de votre collection ont été ajoutés à votre équipe.")
    
    else: 
        while len(Equipe)<6:
            id_poke = input('Quel est le pokémon que vous souhaitez ajouter à votre équipe ? ')
            while id_poke in Equipe:
                id_poke = input('Ce pokémon est déjà dans votre équipe ! Il ne peut pas se dédoubler. Choisissez-en un autre : ')
            Equipe[int(id_poke)] = Collection[int(id_poke)]
        
        choix = input('Souhaitez vous modifier un pokémon de votre équipe ? ')
        if choix == True:
            gestion_collection(Equipe, Collection)
        
    
    

def soin(Collection):
    '''
    Soigne tous les pokémons de l équipe lors d un passage à un centre de soin.
    '''
    for pokemon in Collection:
        Collection[pokemon].pv = Collection[pokemon].pv_totaux
        Collection[pokemon].etat = True
        
        
        
 
        
##tests : 
        
# =============================================================================
# Equipe, Collection = starter(pokemon.Pokedex)
# =============================================================================
