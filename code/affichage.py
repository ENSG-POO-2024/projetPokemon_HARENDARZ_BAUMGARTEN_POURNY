# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:48:22 2024

@author: romai
"""

import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from PyQt5 import QtCore, QtWidgets, QtMultimedia
from PyQt5 import QtGui
import os

import carte as c
import deplacement as d
import affichage_deplacement as de
import affichage_combat as ac
import affichage_inventaire as ai
import intro
import pokemon as p
from gui.saving_mechanics import *

# =============================================================================
# INITIALISATION DES VARIABLES
# =============================================================================
path = os.getcwd()

Pokedex, Pokelist = p.creation_pokedex() 
Equipe = {}
collection  = {10: Pokedex[10]}
starter = {1: Pokedex[2], 4: Pokedex[4], 7:Pokedex[7], 25: Pokedex[25]}
environnement, autre = p.creation_pokedex() 

nb_inventory = 0
nb_team = 0
nb_starter = 0
slide = 1


pix = 232
piy = 400
area = 0

#Création de la carte
img0 = Image.open("..\code\gui\Safari_Zone_entrance_RBY.png")
img1 = Image.open("..\code\gui\Safari_Zone_area_1_RBY.png")
img2 = Image.open("..\code\gui\Safari_Zone_area_2_RBY.png")
img3 = Image.open("..\code\gui\Safari_Zone_area_3_RBY.png")
img4 = Image.open("..\code\gui\player_front.png")

all_img = [img0,img1,img2,img3]

new_image = img0
new_image.paste(img4, (pix,piy), mask = img4) 
new_image.save("gui\maps\game.png")

img0 = Image.open("..\code\gui\Safari_Zone_entrance_RBY.png")

im = np.array(img0.convert('L'))
im1 = np.array(img1.convert('L'))
im2 = np.array(img2.convert('L'))
im3 = np.array(img3.convert('L'))

test = c.convertion_case(im)
test1 = c.convertion_case(im1)
test2 = c.convertion_case(im2)
test3 = c.convertion_case(im3)

test_area0 = c.Area(0,test)
test_area1 = c.Area(1,test1)
test_area2 = c.Area(2,test2)
test_area3 = c.Area(3,test3)

test_map = c.Map([test_area0,test_area1, test_area2, test_area3])

case_depart = c.Case(50,29,0)

j1 = d.joueur(case_depart, test_map)
id_Poke = 0


# =============================================================================
# CREATION DES FENETRES
# =============================================================================
class MainWindow(QMainWindow):

    def __init__(self):
        global mode 
        global id_Poke
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('gui\logos\py_symbol.png'))
        self.resize(640,300)
        id_Poke = 0
        mode = 0
        self.menuUI()
        self.son()
    
#Fenêtre de l'ecran d'acceuille
    def menuUI(self):
        self.resize(840,500)
        self.setWindowIcon(QtGui.QIcon('gui\logos\py_symbol.png'))
        self.title = "Pykémon"
        self.setWindowTitle(self.title)
        label = QLabel(self)
        self.setCentralWidget(label)
        pixmap = QPixmap("gui\logos\Retropix.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        self.show()

#Fenêtre de la carte
    def carteUI(self):
        super(MainWindow, self).__init__()
        self.resize(840,500)
        self.setWindowIcon(QtGui.QIcon('gui\ logos\py_symbol.png'))
        self.title = "Pykémon"
        self.setWindowTitle(self.title)
        label = QLabel(self)
        pixmap = QPixmap("gui\maps\game.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        self.setCentralWidget(label)
        global_variables = {'Equipe': None, 'collection': None, 'environnement':None, 'nb_inventory':None, 'nb_team':None, 'slide':None, 'case_depart':None} 
        fill_global_variables(global_variables)
        self.show()
    
#Fenêtre de l'inventaire
    def inventaireUI(self):
        global nb_inventory
        super(MainWindow, self).__init__()
        self.resize(840,500)
        self.setWindowIcon(QtGui.QIcon('gui\logos\py_symbol.png'))
        self.title = "Pykémon"
        self.setWindowTitle(self.title)
        ai.affiche_poke(self,Equipe,collection,Pokedex,nb_inventory)
        nb_inventory = 0
        
#Fenêtre de l'équipe
    def teamUI(self):
        global nb_team
        super(MainWindow, self).__init__()
        self.resize(840,500)
        self.setWindowIcon(QtGui.QIcon('gui\logos\py_symbol.png'))
        self.title = "Pykémon"
        self.setWindowTitle(self.title)
        ai.affiche_team_poke(self,Equipe,collection,Pokedex,nb_team)
        nb_team = 0
        
#Fenêtre des combats
    def combatUI(self):
        global id_Poke
        global phase
        global poke_combattant
        super(MainWindow, self).__init__()
        self.resize(840,500)
        self.setWindowIcon(QtGui.QIcon('gui\logos\py_symbol.png'))
        self.title = "Pykémon"
        self.setWindowTitle(self.title)
        img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
        img_fond = Image.open(path+"\\gui\\battle\\intro_fight.png")
        img_fight = img_fond 
        fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 11)
        img_fight.paste(img_Poke_ennemie, (100,10))
        img_player = Image.open(path+"\\gui\\battle\\player.png")
        img_fight.paste(img_player, (10,40))
        draw = ImageDraw.Draw(img_fight)
        txt = Pokedex[id_Poke].name
        draw.text((15, 105), txt, font = fnt, fill =(0, 0, 0))
        img_fight.save("fight.png")
        label = QLabel(self)
        pixmap = QPixmap("fight.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        phase = "intro"
        poke_combattant = None
        self.setCentralWidget(label)
        self.show()
        
#Fenêtre du choix du starter
    def choix_pokeUI(self):
        global starter
        global nb_starter
        super(MainWindow, self).__init__()
        self.resize(840,500)
        self.setWindowIcon(QtGui.QIcon('gui\logos\py_symbol.png'))
        self.title = "Pykémon"
        self.setWindowTitle(self.title)
        ai.affiche_choix_starter(self,Equipe,starter,Pokedex,nb_starter)
        
#Fenêtre de l'introduction
    def introUI(self):
        super(MainWindow, self).__init__()
        self.resize(840,500)
        self.setWindowIcon(QtGui.QIcon('gui\logos\py_symbol.png'))
        self.title = "Pykémon"
        self.setWindowTitle(self.title)
        intro.affiche_intro(self,"Hello there !\nAnd welcome to the world of Pokemon !")
        
#Gère le son
    def son(self):
        global player
        global player2
        app = QtWidgets.QApplication(sys.argv)
        filename = "..\code\gui\The Great Marsh & Pal Park [Pokémon Diamond & Pearl].mp3"
        filename2 = "..\code\gui\Pokémon Black & White - Battle! Elite Four (CPS-2 Remix).mp3"
        fullpath = QtCore.QDir.current().absoluteFilePath(filename)
        fullpath2 = QtCore.QDir.current().absoluteFilePath(filename2)
        url = QtCore.QUrl.fromLocalFile(fullpath)
        url2 = QtCore.QUrl.fromLocalFile(fullpath2)
        content = QtMultimedia.QMediaContent(url)
        content2 = QtMultimedia.QMediaContent(url2)
        player = QtMultimedia.QMediaPlayer()
        player2 = QtMultimedia.QMediaPlayer()
        player.setMedia(content)
        player2.setMedia(content2)
        player.play()
        sys.exit(app.exec_())
        
  
### Gère les commandes    
    def keyPressEvent(self, e):
        global j1
        global all_img
        global img4
        global mode
        global id_Poke
        global Equipe
        global phase
        global poke_combattant
        global nb_inventory
        global nb_team
        global nb_starter
        global collection
        global environnement
        global slide
    
#Chaque mode permet de gérer une partie du jeu
    
#Mode de l'écran d'acceuille
        if mode == 0:        
            mode = 7
            self.hide()
            self.introUI()

#Mode de la carte
        elif mode == 1:
            player2.stop()
            player.play()
            mode, id_Poke = de.affiche_deplacement(self, j1, e, Pokedex,environnement)
            mode, nb_inventory = ai.affiche_inventaire(self,mode,Equipe,collection,Pokedex,nb_inventory,e)
            
#Mode de l'introduction du combat
        elif mode == 2:
            player.stop()
            player2.play()
            self.hide()
            self.combatUI()
            mode = 3
 
#Mode du combat
        elif mode == 3:
                mode, phase, poke_combattant = ac.affiche_combat(self,mode, id_Poke, Equipe, Pokedex, e, phase, collection, environnement, poke_combattant)
 
#Mode de l'inventaire
        elif mode == 4:
            mode, nb_inventory = ai.affiche_inventaire(self,mode,Equipe,collection,Pokedex,nb_inventory,e)

#Mode de l'équipe        
        elif mode == 5:
            mode, nb_team, collection, Equipe = ai.affiche_team(self,mode,Equipe,collection,Pokedex,nb_team,nb_inventory,e)

#Mode du choix du starter            
        elif mode == 6:
            mode, nb_starter, environnement, Equipe = ai.affiche_starter(self, mode, Equipe, starter, Pokedex, environnement, nb_starter, e)
 
#Mode de l'intoduction
        elif mode == 7:
            mode, slide = intro.suite(self,mode,slide, e)
            
                
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())






