        # -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:16:37 2024

@author: Formation
"""

import csv
import numpy as np
import pokemon
import utilitaire
import random as rd

List_type = ['Steel','Fighting', 'Dragon','Water','Electric','Fire','Fairy','Ice','Bug','Normal','Grass','Poison','Psychic','Rock','Ground','Ghost','Dark','Flying']

##Permet de récupérer les indices des types.


table_type = np.genfromtxt('../data/Types.csv',delimiter = ',')



'''
Environnement : Dictionnaire, variable globale, des pokémons dans l environnement
Equipe : Dictionnaire des pokémons actifs dans l équipe du dresseur
Collection : Dictionnaire des pokémons possédés par le dresseur
poke_att : pokémon infligeant les dégâts
poke_def : pokémon recevant les dégâts
'''



## INTERFACE!! ##

def tour_joueur(poke_att, poke_def, choix_attaque):
    '''
    poke_att : pokémon actif du joueur
    poke_def : pokémon sauvage
    
    Attaque du joueur. Explicite: selon le choix d attaque du joueur, calcule les dégâts correspondants.
    '''
    ##Interface
    ## à construire avec l'interface, le joueur doit choisir entre une attaque spéciale et une attaque normale
    
    if choix_attaque == 'normale':
        damage = poke_att.attack(poke_def)
        
    elif choix_attaque == 'speciale':
        damage = poke_att.special_attack(poke_def)
    
    poke_def.pv = poke_def.pv - damage

## INTERFACE!! ##



def tour_environnement(poke_att, poke_def):
    '''
    poke_att : pokémon sauvage
    poke_def : pokémon actif du joueur
    reserve : nombre de pokémons combattants restants du dresseur
    
    Au tour du pokémon sauvage, il attaque le pokémon adverse.
    Le pokémon sauvage choisit automatiquement l attaque la plus léthale.
    '''
    ## Le pokémon sauvage considère ses options : il utilisera l'attaque la plus efficace    
    degats = poke_att.attack(poke_def)
    degats_spc = poke_att.special_attack(poke_def)
    damage = max(degats,degats_spc)
    
    ## Il inflige des dommages au pokémon actif du joueur
    poke_def.pv = poke_def.pv - damage
    
    ## s'il vainc son adversaire, l'équipe du joueur comprend un pokémon de moins et il devra immédiatemment choisir un nouveau pokémon
    if poke_def.pv <= 0:
        poke_def.etat = False




## INTERFACE!! ##
        
def choix_pokemon(Equipe):
    '''
    Parameters
    ----------
    Equipe : Dictionnaire des pokémons dans l équipe du dresseur
        Le pokémon actif au combat sera choisi dans ce dictionnaire

    Fonction permettant au dresseur de choisir son pokémon actif.
    '''
    L = list(Equipe.keys())
    list_poke_vie = []
    for cle in L:
        if Equipe[cle].etat:
            list_poke_vie.append(Equipe[cle])
    poke_actif = list_poke_vie[rd.randint(0, len(list_poke_vie) - 1)]
    return poke_actif

## INTERFACE!! ##




def fin_combat(Equipe,Collection,poke_sauvage,Environnement):
    ## Soin après bataille, ajout du pokémon vaincu à l'Equipe
    if not poke_sauvage.pv > 0:
        if len(Equipe) < 6:
            Equipe[poke_sauvage.id] = poke_sauvage
        else:
            Collection[poke_sauvage.id] = poke_sauvage
        del Environnement[poke_sauvage.id]
    else:
        poke_sauvage.pv = poke_sauvage.pv_totaux
    utilitaire.soin(Equipe)
    utilitaire.soin(Collection)

    ## Doit supprimer le pokémon de la case si vaincu
    ## Doit bouger de la case si perdu    
    


'''
La fonction combat va être intégrée dans la structure de l interface.

Cette fonction a structuré notre vision du combat. Elle n a pas pu être utilisée telle quelle.
Elle reste cependant assez claire pour visualiser notre système de combat par rapport au code de l interface.
'''

## INTERFACE!! ##
def combat(Equipe,Collection,poke_sauvage):
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
    
    while poke_sauvage.pv > 0  or fleeing == False or reserve > 0:
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
            """
            Voir la fonction tour environnement dans l archive. La fonction renvoie un booléen correspondant 
            à l état de santé du pokémon défenseur.
            """
            
        ## Si le pokémon combattant est vaincu, le dresseur en choisit un autre
        if changement == True:
            poke_actif = choix_pokemon(Equipe)
            changement = False
            
        ## Inversion de l'initiative
        initiative = not initiative
        
        
        
    ## Pokemon actif doit avoir vie > 0
    ## Si le pokemon actif meurt, on doit en choisir un autre
    
    ## Appel de la fin du combat
        
    fin_combat(Equipe,Collection,poke_sauvage,Environnement)
    
    
    

        
## INTERFACE!! ##
    
    
    
    


