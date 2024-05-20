# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:04:58 2024

@author: romai
"""


from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from PIL import Image, ImageDraw, ImageFont
import os

import affichage_deplacement as de

path = os.getcwd()


def affiche_poke(self,Equipe,collection,Pokedex,nb_inventory):
    """
    

    Parameters
    ----------
    Equipe : list
        list des Pokemon dans l'équipe'
    collection : list
        list des Pokemon dans notre inventaire
    Pokedex : list
        list de tout les pokemon
    nb_inventory : int
        endroit où on se trouve dans l'inventaire

    Returns
    -------
    None.

    """
    if len(collection) != 0:
        cle = list(collection.keys())
        img_poke = Image.open("..\code\gui\pokemon\spr_rb-supgb_" + de.affiche_id(cle[nb_inventory]) + ".png")
        img_fond = Image.open("gui\inventory\inventory.png")
        img_fond.paste(img_poke, (60, 40))
        fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 11)
        txt_poke = Pokedex[cle[nb_inventory]].name
        draw = ImageDraw.Draw(img_fond)
        draw.text((45, 100), txt_poke, font = fnt, fill =(0, 0, 0))
        img_fond.save("inventory_poke.png")
        self.inventaire.reloadPixmap(self.max_width, self.max_height)
    
    
def affiche_team_poke(self,Equipe,collection,Pokedex,nb_team):
    """
    

    Parameters
    ----------
    Equipe : list
        list des Pokemon dans l'équipe
    collection : list
        list des Pokemon dans notre inventaire
    Pokedex : list
        list de tout les pokemon
    nb_team : int
        endroit où on se trouve dans l'équipe

    Returns
    -------
    None.

    """
    cle = list(Equipe.keys())
    img_poke = Image.open("..\code\gui\pokemon\spr_rb-supgb_" + de.affiche_id(cle[nb_team]) + ".png")
    img_fond = Image.open(path+"\\gui\\inventory\\team.png")
    img_fond.paste(img_poke, (60, 40))
    fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 11)
    txt_poke = Pokedex[cle[nb_team]].name
    draw = ImageDraw.Draw(img_fond)
    draw.text((45, 100), txt_poke, font = fnt, fill =(0, 0, 0))
    img_fond.save("inventory_poke.png")
    self.inventaire.reloadPixmap(self.max_width, self.max_height)
    
def affiche_choix_starter(self,Equipe,starter,Pokedex,nb_starter):
    """
    

    Parameters
    ----------
    Equipe : list
        list des Pokemon dans l'équipe
    starter : list
        list des starters disponibles
    Pokedex : list
        list de tout les pokemon
    nb_starter : int
        endroit où on se trouve dans le choix du starter

    Returns
    -------
    None.

    """
    cle = list(starter.keys())
    img_poke = Image.open("..\code\gui\pokemon\spr_rb-supgb_" + de.affiche_id(cle[nb_starter]) + ".png")
    img_fond = Image.open("gui\inventory\inventory.png")
    img_fond.paste(img_poke, (60, 40))
    fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 11)
    txt_poke = Pokedex[cle[nb_starter]].name
    draw = ImageDraw.Draw(img_fond)
    draw.text((45, 100), txt_poke, font = fnt, fill =(0, 0, 0))
    img_fond.save("inventory_poke.png")
    self.inventaire.reloadPixmap(self.max_width, self.max_height)

def affiche_inventaire(self,mode,Equipe,collection,Pokedex,nb_inventory,e):
    """
    

    Parameters
    ----------
    mode : int
        chaque action ne peut que s'effectuer dans le bon mode
    Equipe : list
        list des Pokemon dans l'équipe
    collection : list
        list des Pokemon dans notre inventaire
    Pokedex : list
        list de tout les pokemon
    nb_inventory : int
       endroit où on se trouve dans l'inventaire
    e : PyQt5.QtGui.QKeyEvent
        correspond à l'input de l'utilisateur

    Returns
    -------
    mode : int
        chaque action ne peut que s'effectuer dans le bon mode, change dans certains cas pour passer à d'autres mechanique de jeu
    nb_inventory : int
       endroit où on se trouve dans l'inventaire

    """
    print("Fonction")
    if e.key() == Qt.Key_Tab and mode == 1 and len(collection) != 0:
        self.inventaireUI()
        self.carte.widgetHide()
        self.inventaire.widgetShow()
        mode = 4
        return mode, nb_inventory

    if e.key() == Qt.Key_Right and mode == 4:
        nb_inventory = (nb_inventory + 1) % (len(collection))
        affiche_poke(self, Equipe, collection, Pokedex, nb_inventory)
        return mode, nb_inventory
    
    if e.key() == Qt.Key_Left and mode == 4:
        nb_inventory = (nb_inventory - 1) % (len(collection))
        affiche_poke(self, Equipe, collection, Pokedex, nb_inventory)
        return mode, nb_inventory
    
    if e.key() == Qt.Key_Space and mode == 4:
        self.teamUI()
        mode = 5
        return mode, nb_inventory
    
    else: 
        return mode, nb_inventory
    
def affiche_team(self,mode,Equipe,collection,Pokedex,nb_team,nb_inventory,e):
    """

    Parameters
    ----------
    mode : int
        chaque action ne peut que s'effectuer dans le bon mode
    Equipe : list
        list des Pokemon dans l'équipe
    collection : list
        list des Pokemon dans notre inventaire
    Pokedex : list
        list de tout les pokemon
    nb_team : int
       endroit où on se trouve dans l'équipe
    nb_inventory : int
       endroit où on se trouve dans l'inventaire
    e : PyQt5.QtGui.QKeyEvent
        correspond à l'input de l'utilisateur

    Returns
    -------
    mode : int
        chaque action ne peut que s'effectuer dans le bon mode
    nb_team : int
        endroit où on se trouve dans l'équipe
    collection : list
        list des Pokemon dans notre inventaire
    Equipe : list
        list des Pokemon dans l'équipe

    """
    
    if e.key() == Qt.Key_Right:
        nb_team = (nb_team + 1) % (len(Equipe))
        affiche_team_poke(self, Equipe, collection, Pokedex, nb_team)
        return mode, nb_team, collection, Equipe
    
    if e.key() == Qt.Key_Left:
        nb_team = (nb_team - 1) % (len(Equipe))
        affiche_team_poke(self, Equipe, collection, Pokedex, nb_team)
        return mode, nb_team, collection, Equipe
    
    if e.key() == Qt.Key_Space:
        cle_equipe = list(Equipe.keys())
        cle_collection = list(collection.keys())
        self.inventaire.widgetHide()
        self.carte.widgetShow()
        mode = 1
        id_collection = cle_collection[nb_inventory]
        id_equipe = cle_equipe[nb_team]
        del collection[id_collection]
        del Equipe[id_equipe]
        collection[id_equipe] = Pokedex[id_equipe]
        Equipe[id_collection] =  Pokedex[id_collection]
        return mode, nb_team, collection, Equipe
    
    else: 
        return mode, nb_team, collection, Equipe
        
def affiche_starter(self,mode,Equipe,starter,Pokedex,environnement,nb_starter,e):
    """
    

    Parameters
    ----------
    mode : int
       chaque action ne peut que s'effectuer dans le bon mode
    Equipe : dic
        dictionnaire des Pokemon dans l'équipe
    starter : dic
        dictionnaire des starters disponibles
    Pokedex : dic
        dictionnaire de tout les pokemon
    environnement : dic
        dictionnaire des pokemon que l'on peut attraper
    nb_starter : int
        endroit où on se trouve dans le choix du starter
    e : PyQt5.QtGui.QKeyEvent
        correspond à l'input de l'utilisateur

    Returns
    -------
    mode : int
       chaque action ne peut que s'effectuer dans le bon mode
    nb_starter : int
        endroit où on se trouve dans le choix du starter
    environnement : dic
        dictionnaire des pokemon que l'on peut attraper
    nb_starter : int
        endroit où on se trouve dans le choix du starter
    Equipe : dic
       dictionnaire des Pokemon dans l'équipe

    """
    if e.key() == Qt.Key_Right:
        nb_starter= (nb_starter + 1) % (len(starter))
        affiche_choix_starter(self, Equipe, starter, Pokedex, nb_starter)
        return mode, nb_starter, environnement, Equipe
    
    if e.key() == Qt.Key_Left:
        nb_starter= (nb_starter - 1) % (len(starter))
        affiche_choix_starter(self, Equipe, starter, Pokedex, nb_starter)
        return mode, nb_starter, environnement, Equipe
    
    if e.key() == Qt.Key_Space:
        cle_starter = list(starter.keys())
        self.inventaire.widgetHide()
        self.carteUI()
        mode = 1
        id_starter = cle_starter[nb_starter]
        del environnement[id_starter]
        Equipe[id_starter] = Pokedex[id_starter]
        return mode, nb_starter, environnement, Equipe
    
    else: 
        return mode, nb_starter, environnement, Equipe