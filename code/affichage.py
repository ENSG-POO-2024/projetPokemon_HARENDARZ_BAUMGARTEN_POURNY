# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:48:22 2024

@author: romai
"""

import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import random as rd

import carte as c
import deplacement as d
import affichage_deplacement as de
import affichage_combat as ac
import affichage_inventaire as ai
import intro
import pokemon as p
from saving_mechanics import *
from gui import gui_resources
from menu_gui import *
from music_gui import *
from widget_surcharge_gui import Widget, Widget2
from other_widgets_gui import *

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
test_map, case_depart = c.creation_carte(pix,piy)

j1 = d.joueur(case_depart, test_map)
id_Poke = 0


# =============================================================================
# CREATION DES FENETRES
# =============================================================================
class MainWindow(QMainWindow, Widget):
    def __init__(self, app):
        global mode 
        global id_Poke
        super().__init__()
        QtGui.QFontDatabase.addApplicationFont("fonts/Retro_Gaming.ttf")    # Special font imported
        self.max_width, self.max_height = self.startup_ratio(app)
        self.setWindowIcon(QtGui.QIcon('gui\logos\py_symbol.png'))
        self.setAnimated(True)
        self.setEnabled(True)

        self.setMinimumSize(QtCore.QSize(1280, 720))
        self.setMaximumSize(QtCore.QSize(self.max_width, self.max_height))
        self.retranslateUi()
        self.screen_resize(self.max_width, self.max_height)
        
        id_Poke = 0
        mode = 0

        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget) 
       
        self.player = MusicJukebox()
        self.main_menu = menuUi_class(self.max_width, self.max_height, self.centralwidget)
        self.main_menu.widgetShow()
        
        self.lateralMenu = optionsMenu(self.centralwidget)
        self.lateralMenu.centerWidget(self.max_width, self.max_height)
        # self.lateralMenuButton = Ui_LateralMenuButton(self.centralwidget)
        # self.lateralMenuButton.clicked.connect(self.lateralMenu.test_for_hiding)
        
        self.lateralMenu.volumeHorizontalSlider.valueChanged.connect(self.changeVolume)
        self.lateralMenu.closeButton.clicked.connect(sys.exit)
        

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Pykemon_MainWindow", "Pykémon : Attrapy-les tous !"))

    def screen_resize(self, width, height):
        self.setGeometry(QtCore.QRect(0, 0, width, height))
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)     
    
    def startup_ratio(self, app):
        screen = app.primaryScreen()
        size = screen.size()
        self.ratio = size.width()/1920
        return [size.width(), size.height()]
    
    def closeEvent(self, event):
        # fade out
        self.fade_out()
        self.player.stop_song()
        super().closeEvent(event)

    def changeVolume(self):
        self.player.setVolume(self.lateralMenu.volumeHorizontalSlider.value())
    
#Fenêtre de l'ecran d'acceuille
    def menuUI(self):
        self.menu = menuUi_class(self.max_width,self.max_height,self.centralwidget)
        self.menu.widgetShow()

#Fenêtre de la carte
    def carteUI(self):
        self.carte = carteUi_class(self.max_width,self.max_height,self.centralwidget)
        self.carte.widgetShow()
    
#Fenêtre de l'inventaire
    def inventaireUI(self):
        global nb_inventory
        ai.affiche_poke(self,Equipe,collection,Pokedex,nb_inventory)
        self.inventaire = inventraireUi_class(self.max_width,self.max_height,self.centralwidget)
        self.inventaire.widgetShow()
        nb_inventory = 0
        
#Fenêtre de l'équipe
    def teamUI(self):
        global nb_team
        ai.affiche_team_poke(self,Equipe,collection,Pokedex,nb_team)
        self.inventaire = inventraireUi_class(self.max_width,self.max_height,self.centralwidget)
        self.inventaire.widgetShow()
        nb_team = 0
        
#Fenêtre des combats
    def combatUI(self):
        global id_Poke
        global phase
        global poke_combattant
        img_Poke_ennemie = Image.open("..\code\gui\pokemon\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
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
        
        self.combat = combatUi_class(self.max_width,self.max_height,self.centralwidget)

        phase = "intro"
        poke_combattant = None
        
#Fenêtre du choix du starter
    def choix_pokeUI(self):
        global starter
        global nb_starter
        ai.affiche_choix_starter(self,Equipe,starter,Pokedex,nb_starter)
        self.inventaire = inventraireUi_class(self.max_width,self.max_height,self.centralwidget)
        self.inventaire.widgetShow()
        
#Fenêtre de l'introduction
    def introUI(self):
        intro.affiche_intro(self,"Hello there !\nAnd welcome to the world of Pokemon !")
        self.intro = introUi_class(self.max_width,self.max_height,self.centralwidget)
        self.intro.widgetShow()
        
  
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
        global music_state
                                  
#Chaque mode permet de gérer une partie du jeu
        if e.key() == Qt.Key_Escape:
            self.lateralMenu.test_for_hiding()
    
#Mode de l'écran d'acceuille
        if mode == 0:        
            mode = 7
            self.introUI()
            self.main_menu.widgetHide()

#Mode de la carte
        elif mode == 1:
            self.player.play_song('Exploration')
            self.carte.reloadPixmap(self.max_width, self.max_height )
            self.carte.widgetShow()
            mode, id_Poke = de.affiche_deplacement(self, j1, e, Pokedex,environnement)
            mode, nb_inventory = ai.affiche_inventaire(self,mode,Equipe,collection,Pokedex,nb_inventory,e)
            
             
#Mode de l'introduction du combat
        elif mode == 2:
            self.player.stop_song()
            self.player.play_song(rd.choice(['Combat1','Combat2']))
            self.inventaire.widgetHide()
            self.carte.widgetHide()

            self.combatUI()
            self.combat.widgetShow()
            mode = 3
 
#Mode du combat
        elif mode == 3:
            mode, phase, poke_combattant = ac.affiche_combat(self,mode, id_Poke, Equipe, Pokedex, e, phase, collection, environnement, poke_combattant)
            self.combat.reloadPixmap(self.max_width, self.max_height)
            if mode == 1:
                self.player.stop_song()
 
#Mode de l'inventaire
        elif mode == 4:
            mode, nb_inventory = ai.affiche_inventaire(self,mode,Equipe,collection,Pokedex,nb_inventory,e)
            self.inventaire.reloadPixmap(self.max_width, self.max_height)

            

#Mode de l'équipe        
        elif mode == 5:
            mode, nb_team, collection, Equipe = ai.affiche_team(self,mode,Equipe,collection,Pokedex,nb_team,nb_inventory,e)
#Mode du choix du starter            
        elif mode == 6:
            mode, nb_starter, environnement, Equipe = ai.affiche_starter(self, mode, Equipe, starter, Pokedex, environnement, nb_starter, e)
            self.inventaire.reloadPixmap(self.max_width, self.max_height)
 
#Mode de l'intoduction
        elif mode == 7:
            mode, slide, music_state = intro.suite(self,mode,slide, e)
            self.intro.reloadPixmap(self.max_width, self.max_height)
            if music_state:
                self.player.stop_song()
                music_state == False  
            
                
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow(app)
    w.show()
    sys.exit(app.exec_())






