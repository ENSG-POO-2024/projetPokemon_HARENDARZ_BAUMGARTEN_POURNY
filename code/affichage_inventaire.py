# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:04:58 2024

@author: romai
"""

import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from PyQt5 import QtCore, QtWidgets, QtMultimedia
import nouveau_combat as nc
import combat as co

import carte as c
import deplacement as d
import random as rd
import affichage_deplacement as de
import pokemon as p

def affiche_poke(self,Equipe,collection,Pokedex,nb_inventory):
    if len(collection) != 0:
        cle = list(collection.keys())
        img_poke = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(cle[nb_inventory]) + ".png")
        img_fond = Image.open('inventory.png')
        img_fond.paste(img_poke, (60, 40))
        fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 11)
        txt_poke = Pokedex[cle[nb_inventory]].name
        draw = ImageDraw.Draw(img_fond)
        draw.text((45, 100), txt_poke, font = fnt, fill =(0, 0, 0))
        img_fond.save("inventory_poke.png")
        label = QLabel(self)
        pixmap = QPixmap("inventory_poke.png")
        label.setPixmap(pixmap) 
        label.setScaledContents(True)
        self.setCentralWidget(label)
        self.show()
    
    
def affiche_team_poke(self,Equipe,collection,Pokedex,nb_team):
    cle = list(Equipe.keys())
    img_poke = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(cle[nb_team]) + ".png")
    img_fond = Image.open('team.png')
    img_fond.paste(img_poke, (60, 40))
    fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 11)
    txt_poke = Pokedex[cle[nb_team]].name
    draw = ImageDraw.Draw(img_fond)
    draw.text((45, 100), txt_poke, font = fnt, fill =(0, 0, 0))
    img_fond.save("inventory_poke.png")
    label = QLabel(self)
    pixmap = QPixmap("inventory_poke.png")
    label.setPixmap(pixmap) 
    label.setScaledContents(True)
    self.setCentralWidget(label)
    self.show()
    
def affiche_choix_starter(self,Equipe,starter,Pokedex,nb_starter):
    cle = list(starter.keys())
    img_poke = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(cle[nb_starter]) + ".png")
    img_fond = Image.open('starter.png')
    img_fond.paste(img_poke, (60, 40))
    fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 11)
    txt_poke = Pokedex[cle[nb_starter]].name
    draw = ImageDraw.Draw(img_fond)
    draw.text((45, 100), txt_poke, font = fnt, fill =(0, 0, 0))
    img_fond.save("inventory_poke.png")
    label = QLabel(self)
    pixmap = QPixmap("inventory_poke.png")
    label.setPixmap(pixmap) 
    label.setScaledContents(True)
    self.setCentralWidget(label)
    self.show()

def affiche_inventaire(self,mode,Equipe,collection,Pokedex,nb_inventory,e):
    if e.key() == 16777217 and mode == 1 and len(collection) != 0:
        self.hide()
        self.inventaireUI()
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
        self.hide()
        self.teamUI()
        mode = 5
        return mode, nb_inventory
    
    else: 
        return mode, nb_inventory
    
def affiche_team(self,mode,Equipe,collection,Pokedex,nb_team,nb_inventory,e):

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
        self.hide()
        self.carteUI()
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
        self.hide()
        self.carteUI()
        mode = 1
        id_starter = cle_starter[nb_starter]
        del environnement[id_starter]
        Equipe[id_starter] = Pokedex[id_starter]
        return mode, nb_starter, environnement, Equipe
    
    else: 
        return mode, nb_starter, environnement, Equipe