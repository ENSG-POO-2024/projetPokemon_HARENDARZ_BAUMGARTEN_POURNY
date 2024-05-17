# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:58:35 2024

@author: Formation
"""

import csv
import numpy as np
import random as rd
import pokemon
import utilitaire

List_type = ['Steel','Fighting', 'Dragon','Water','Electric','Fire','Fairy','Ice','Bug','Normal','Grass','Poison','Psychic','Rock','Ground','Ghost','Dark','Flying']

##Permet de récupérer les indices des types.


table_type = np.genfromtxt('../data/Types.csv',delimiter = ',')


##Les formules d'attaque ont été intégrées à la classe pokémon en tant que méthode.


# =============================================================================
# def formule_attack(at,df1,df2):
#     '''
#     at : attaque de l attaquant
#     df : défenses des pokémons 
# 
#     Returns
#     -------
#     Formule du calcul de dégâts
#     Sans les coefficients d efficacité de type!
#     
#     '''
#     return at*(df1/df2)
# 
# 
# def attack(at1,df1,df2):
#     '''
#     Parameters
#     ----------
#     at1 : attaque de l attaquant
#     df1 : défense de l attaquant
#     df2 : défense du défenseur
#         
#     Returns
#     -------
#     Dégâts.
#     '''
#     return round(formule_attack(at1, df1, df2))
# 
# 
# def special_attack(tp1,at_spc1,df_spc1,tp2,df_spc2):
#     """
#     tp1 : type de l attaquant
#     at_spc1 : attaque spéciale de l attaquant
#     df_spc1 : défense spéciale de l attaquant
#     tp2 : type du défenseur
#     df_spc2 : défense spécialedu défenseur
# 
#     Returns
#     -------
#     Cherche le coefficient d efficacité de type.
#     Multiplie le résultat de la formule d attaque par le coef
#     Renvoie l arrondi si le résultat est relatif
#     """
#     i1,i2 = List_type.index(tp1), List_type.index(tp2)
#     coef = table_type[i1][i2]
#     return round(formule_attack(at_spc1,df_spc1,df_spc2)*coef)
# =============================================================================




'''
Equipe : Dictionnaire des pokémons dans l équipe du dresseur
poke_actif : pokémon du joueur actif dans le combat
poke_att : pokémon infligeant les dégâts
poke_def : pokémon recevant les dégâts
'''


"""
AKA Cimetière.
Ce fichier regroupe des brouillons et fonctions à présent inutilisées.
Elles sont conservées dans le cas où elles pourraient être réutilisées ou modifiées.
"""




def choix_pokemon(Equipe):
    '''
    Parameters
    ----------
    Equipe : Dictionnaire des pokémons dans l équipe du dresseur
        Le pokémon actif au combat sera choisi dans ce dictionnaire

    Fonction permettant au dresseur de choisir son pokémon actif
    '''
    
    ##Interface
    choix = input("Veuillez entrer le nom du pokémon choisi dans votre équipe: ")
    
    ## On vérifie que le pokémon est en état de se battre
    while not Equipe[int(choix)].etat:
        choix = input("Ce pokémon est hors de combat! Laissez le un peu tranquille. Veuillez choisir un pokémon capable de se battre: ")
    
    return Equipe[int(choix)]



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
    return not poke_def.etat




