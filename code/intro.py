# -*- coding: utf-8 -*-
"""
Created on Sun May 12 18:24:27 2024

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



def affiche_intro(self,Pokedex,txt,slide = None):
    if slide != None and slide > 1 :
        img_fond = Image.open('oak_intro_poke.png')
    else:
        img_fond = Image.open('oak_intro.png')
    fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 23)
    draw = ImageDraw.Draw(img_fond)
    draw.text((45, 225), txt, font = fnt, fill =(0, 0, 0))
    img_fond.save("oak_intro2.png")
    label = QLabel(self)
    pixmap = QPixmap("oak_intro2.png")
    label.setPixmap(pixmap) 
    label.setScaledContents(True)
    self.setCentralWidget(label)
    self.show()
    
def suite(self,mode,Pokedex,slide,e):
    if e.key() == Qt.Key_Space:
        if slide == 0:
            txt = "Hello there !\nAnd welcome to the world of Pokemon !"
            affiche_intro(self,Pokedex,txt,slide)
            slide += 1
            return mode, slide
        
        if slide == 1:
            txt = "My name is OAK ! People call me \nThe Pokemon PROF!"
            affiche_intro(self,Pokedex,txt,slide)
            slide += 1 
            return mode, slide
        
        if slide == 2:
            txt = "This world is inhabited by \nCreatures called Pokemon!"
            affiche_intro(self,Pokedex,txt,slide)
            slide += 1 
            return mode, slide
        
        if slide == 3:
            txt = "For some people Pokemon are pets.\nOthers, use them for fights."
            affiche_intro(self,Pokedex,txt,slide)
            slide += 1 
            return mode, slide
        
        if slide == 4:
            txt = "Myself..."
            affiche_intro(self,Pokedex,txt,slide)
            slide += 1 
            return mode, slide
        
        if slide == 5:
            txt = "I study Pokemon as a profession."
            affiche_intro(self,Pokedex,txt,slide)
            slide += 1 
            return mode, slide
        
        if slide == 6:
            txt = "It's now your time to choose a Pokemon\nAnd start your adventure!"
            affiche_intro(self,Pokedex,txt,slide)
            slide += 1 
            return mode, slide
        
        if slide == 7:
            self.hide()
            self.choix_pokeUI()
            mode = 6
            return mode, slide
        
    return mode, slide
    
    
    