# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:16:37 2024

@author: Formation
"""

import csv
import numpy as np
import math as m

List_type = ['Steel','Fighting', 'Dragon','Water','Electric','Fire','Fairy','Ice','Bug','Normal','Grass','Poison','Psychic','Rock','Ground','Ghost','Shadow','Flying']

##Permet de récupérer les indices des types. Traduction de ténèbres à vérifier ? 


table_type = np.genfromtxt('../data/Types.csv',delimiter = ',')


def formule_attack(at,df1,df2):
    '''
    at : attaque de l attaquant
    df : défenses des pokémons 

    Returns
    -------
    Formule du calcul de dégâts
    Sans les coefficients d efficacité de type!
    
    '''
    return at*(df1/df2)


def attack(at1,df1,df2):
    '''
    Parameters
    ----------
    at1 : attaque de l attaquant
    df1 : défense de l attaquant
    df2 : défense du défenseur
        
    Returns
    -------
    Dégâts.
    '''
    return formule_attack(at, df1, df2)


def special_attack(tp1,at_spc1,df_spc1,tp2,df_spc2):
    """
    tp1 : type de l attaquant
    at_spc1 : attaque spéciale de l attaquant
    df_spc1 : défense spéciale de l attaquant
    tp2 : type du défenseur
    df_spc2 : défense spécialedu défenseur

    Returns
    -------
    Cherche le coefficient d efficacité de type.
    Multiplie le résultat de la formule d attaque par le coef
    Renvoie l entier supérieur le plus proche si le résultat est relatif
    """
    i1,i2 = List_type.index(tp1), List_type.index(tp2)
    coef = table_type[i1][i2]
    return m.ceil(formule_attack(at_spc1,df_spc1,df_spc2)*coef)








def tour_joueur(poke_att, poke_def):
    '''
    poke_att : pokémon actif du joueur
    poke_def : pokémon sauvage
    
    Au tour du joueur, il peut choisir entre attaquer, choisir un autre pokémon ou fuir
    '''
    pass


def tour_environnement(poke_att, poke_def):
    '''
    poke_att : pokémon sauvage
    poke_def : pokémon actif du joueur
    
    Au tour du pokémon sauvage, il attaque le pokémon adverse
    '''
    ## Le pokémon sauvage considère ses options : il utilisera l'attaque la plus efficace    
    degats = attack(poke_att.at,poke_att.df,poke_def.df)
    degats_spc = special_attack(poke_att.tp,poke_att.at,poke_att.df,poke_def.tp,poke_def.df)
    
    ## Il inflige des dommages au pokémon actif du joueur
    damage = max(degats,degats_spc)
    poke_def.pv = poke_def.pv - damage
    
    
    
    
    

def combat(Equipe,poke_sauvage):
    fleeing = False ##Flag déterminant si la fuite et donc fin du combat est active.
    
    ## Choix pokémon
    choix = input("Veuillez entrer l'indice du pokémon choisi dans votre équipe: ")
    poke_actif = Equipe[choix]
    
    ## Détermination de l'ordre du tour
    if poke_actif.sp >= poke_sauvage.sp:
        initiative = True     
    else:
        initiative = False
    
    while poke_sauvage.pv > 0  or fleeing == False:
        if initiative:
            tour_joueur(poke_actif, poke_sauvage)
        else:
            tour_environnement(poke_sauvage,poke_actif)
    
        ## Inversion de l'initiative
        initiative = not initiative 
        
        
    
        
    ## Pokemon actif doit avoir vie > 0
    ## Si le pokemon actif meurt, on doit en choisir un autre
    ## 
    
    
    ## Soin après bataille, ajout du pokémon vaincu à l'Equipe
    if not poke_sauvage.pv > 0:
        Equipe.append(poke_sauvage)
    else:
        poke_sauvage.pv = poke_sauvage.pv_totaux
        
    for pokemon in Equipe:
        pokemon.pv = pokemon.pv_totaux

    ## Doit supprimer le pokémon de la case si vaincu
    ## Doit bouger de la case si perdu
        






