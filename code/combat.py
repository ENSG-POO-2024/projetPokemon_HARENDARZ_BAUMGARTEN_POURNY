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

