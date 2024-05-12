# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:58:35 2024

@author: Formation
"""

import csv
import numpy as np
import math as m
import random as rd
import pokemon
import utilitaire

List_type = ['Steel','Fighting', 'Dragon','Water','Electric','Fire','Fairy','Ice','Bug','Normal','Grass','Poison','Psychic','Rock','Ground','Ghost','Dark','Flying']

##Permet de récupérer les indices des types.


table_type = np.genfromtxt('../data/Types.csv',delimiter = ',')


'''
Equipe : Dictionnaire des pokémons dans l équipe du dresseur
poke_actif : pokémon du joueur actif dans le combat
poke_att : pokémon infligeant les dégâts
poke_def : pokémon recevant les dégâts
'''


def choix_pokemon(Equipe):
    '''
    Parameters
    ----------
    Equipe : Dictionnaire des pokémons dans l équipe du dresseur
        Le pokémon actif au combat sera choisi dans ce dictionnaire

    Fonction permettant au dresseur de choisir son pokémon actif
    '''
    L = list(Equipe.keys())
    list_poke_vie = []
    for cle in L:
        if Equipe[cle].etat:
            list_poke_vie.append(Equipe[cle])
    poke_actif = list_poke_vie[rd.randint(0, len(list_poke_vie) - 1)]
    return poke_actif



def initiative(poke_actif,poke_sauvage):
    '''
    Compare les vitesses des deux pokémons combattants.

    Return
    -------
    initiative : booléen
        détermine qui commencera le premier tour

    '''
    ## Détermination de l'ordre du tour
    if poke_actif.sp >= poke_sauvage.sp:
        initiative = True     
    else:
        initiative = False
    return initiative




def combat(Equipe,poke_actif,poke_sauvage):
    '''
    Initialise le combat.
    Renvoie l initiative et la réserve
    
    '''
    reserve = len(Equipe) ## Nombre de pokémons en état de se battre du dresseur
    initiative = initiative(poke_actif,poke_sauvage) ## Initiative, True si le dresseur commence le premier tour.
    return initiative,reserve



def tour_environnement(poke_att, poke_def,reserve):
    '''
    poke_att : pokémon sauvage
    poke_def : pokémon actif du joueur
    reserve : nombre de pokémons combattants restants du dresseur
    
    Au tour du pokémon sauvage, il attaque le pokémon adverse
    return: booléen déterminant si le joueur doit changer de pokémon
    '''
    ## Le pokémon sauvage considère ses options : il utilisera l'attaque la plus efficace    
    degats = poke_att.attack(poke_def)
    degats_spc = poke_att.special_attack(poke_def)
    damage = max(degats,degats_spc)
    
    ## Il inflige des dommages au pokémon actif du joueur
    poke_def.pv = poke_def.pv - damage
    
    ## s'il vainc son adversaire, l'équipe du joueur comprend un pokémon de moins et il devra immédiatemment choisir un nouveau pokémon
    if poke_def.pv <= 0:
        reserve -=1
        poke_def.etat = False
        return True
    return False




