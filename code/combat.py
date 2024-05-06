# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:16:37 2024

@author: Formation
"""

import csv
import numpy as np
import math as m
import pokemon

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
    return round(formule_attack(at1, df1, df2))


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
    return round(formule_attack(at_spc1,df_spc1,df_spc2)*coef)







## INTERFACE!! ##

def tour_joueur(poke_att, poke_def):
    '''
    poke_att : pokémon actif du joueur
    poke_def : pokémon sauvage
    
    Attaque du joueur.
    '''
    choix_attaque = None
    ##Interface
    ## à construire avec l'interface, le joueur doit choisir entre une attaque spéciale et une attaque normale
    
    if str(choix_attaque) == 'normale':
        damage = attack(poke_att.at, poke_att.df,poke_def.df)
        
    elif str(choix_attaque) == 'speciale':
        damage = special_attack(poke_att.tp,poke_att.at,poke_att.df,poke_def.tp,poke_def.df)
    
    poke_def.pv = poke_def.pv - damage

## INTERFACE!! ##



def tour_environnement(poke_att, poke_def,reserve):
    '''
    poke_att : pokémon sauvage
    poke_def : pokémon actif du joueur
    reserve : nombre de pokémons combattants restants du dresseur
    
    Au tour du pokémon sauvage, il attaque le pokémon adverse
    '''
    ## Le pokémon sauvage considère ses options : il utilisera l'attaque la plus efficace    
    degats = attack(poke_att.at,poke_att.df,poke_def.df)
    degats_spc = special_attack(poke_att.tp,poke_att.at,poke_att.df,poke_def.tp,poke_def.df)
    
    ## Il inflige des dommages au pokémon actif du joueur
    damage = max(degats,degats_spc)
    print(damage)
    poke_def.pv = poke_def.pv - damage
    if poke_def.pv <= 0:
        reserve -=1
        poke_def.etat = False
        return True
    return False
    




## INTERFACE!! ##
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
    while not Equipe[str(choix)].etat:
        choix = input("Ce pokémon est hors de combat! Laissez le un peu tranquille. Veuillez choisir un pokémon capable de se battre: ")
    
    return Equipe[str(choix)]

## INTERFACE!! ##





## INTERFACE!! ##
def combat(Equipe,poke_sauvage):
    '''
    Parameters
    ----------
    Equipe : Dictionnaire des pokémons dans l équipe du dresseur
        Le pokémon actif au combat sera choisi dans ce dictionnaire
    poke_sauvage : Objet de classe pokémon, Adversaire
         Pokémon rencontré dans la nature
         
    ----------
    Fonction gérant le combat
    Fait appel aux Fonctions de Tour, qui permettant aux participants de choisir leur action
    A la fin du combat, tous les pokémons sont soignés. Un éventuel pokémon sauvage vaincu est ajouté à l équipe.
    '''
    fleeing = False         ## Flag déterminant si la fuite et donc fin du combat est active.
    reserve = len(Equipe)   ## Compteur des pokémons du dresseur. Si atteint 0, fin du combat.
    changement = False      ## Flag déterminant si le dresseur doit choisir un nouveau pokémon suite à une attaque du pokémon sauvage
    
    ## Choix pokémon
    poke_actif = choix_pokemon(Equipe)
    
    ## Détermination de l'ordre du tour
    if poke_actif.sp >= poke_sauvage.sp:
        initiative = True     
    else:
        initiative = False
    
    while poke_sauvage.pv > 0  or fleeing == False or reserve != 0:
        if initiative:
            ##Interface
            choix_joueur = None 
            ## devra être modifié pour inclure le choix
            ## Choix entre Fuir, Changer de pokémon, Attaquer
            
            if choix_joueur == 'Fuir':
                fleeing == True ## doit changer le booléen fleeing en True pour atteindre la fin du combat
            elif choix_joueur == 'Changer':
                poke_actif = choix_pokemon(Equipe) ## doit déclencher la fonction choix_pokemon
            elif choix_joueur == 'Attaquer':
                tour_joueur(poke_actif, poke_sauvage)  ## doit déclencher la fonction tour_joueur
                           
        else:
            changement = tour_environnement(poke_sauvage,poke_actif,reserve)
        
        ## Si le pokémon combattant est vaincu, le dresseur en choisit un autre
        if changement == True:
            poke_actif = choix_pokemon(Equipe)
            changement = False
            
        ## Inversion de l'initiative
        initiative = not initiative
        
        
    
        
    ## Pokemon actif doit avoir vie > 0
    ## Si le pokemon actif meurt, on doit en choisir un autre
    ## 
    
    
    ## Soin après bataille, ajout du pokémon vaincu à l'Equipe
    if not poke_sauvage.pv > 0:
        Equipe[str(poke_sauvage.name)] = poke_sauvage
    else:
        poke_sauvage.pv = poke_sauvage.pv_totaux
        
    for pokemon in Equipe:
        pokemon.pv = pokemon.pv_totaux
        pokemon.etat = True

    ## Doit supprimer le pokémon de la case si vaincu
    ## Doit bouger de la case si perdu
        
## INTERFACE!! ##





