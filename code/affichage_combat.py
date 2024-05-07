# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:25:58 2024

@author: romai
"""

import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from PyQt5 import QtCore, QtWidgets, QtMultimedia

import carte as c
import deplacement as d
import random as rd
import affichage_deplacement as de

def affiche_combat(self,id_Poke,Equipe,Pokedex,e):
    if e.Key == Qt.Key_Space:
        cle = list(Equipe.keys())
        img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
        img_fond = Image.open('intro_fight.png')
        img_fight = img_fond 
        fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 11)
        img_fight.paste(img_Poke_ennemie, (100,10))
        img_player = Image.open("player.png")
        img_fight.paste(img_player, (10,40))
        draw = ImageDraw.Draw(img_fight)
        txt = Pokedex[id_Poke].name
        draw.text((15, 105), txt, font = fnt, fill =(0, 0, 0))
        img_fight.save("fight.png")
        label = QLabel(self)
        pixmap = QPixmap("fight.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        self.setCentralWidget(label)
        self.show()