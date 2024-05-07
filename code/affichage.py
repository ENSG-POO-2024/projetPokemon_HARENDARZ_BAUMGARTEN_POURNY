# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:48:22 2024

@author: romai
"""

import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from PyQt5 import QtCore, QtWidgets, QtMultimedia
from PyQt5 import QtGui

import carte as c
import deplacement as d
import random as rd

import affichage_deplacement as de



import csv
import numpy as np




class Pokemon:
    def __init__(self,name,tp,pv,at,df,at_spc,df_spc,sp,coord = None):
        self.name = name
        self.tp = tp            #type
        self.pv = pv            #points de vie
        self.at = at            #attaque
        self.df = df            #défense
        self.at_spc = at_spc    #attaque spéciale
        self.df_spc = df_spc    #défense spéciale
        self.sp = sp            #vitesse(speed)
        self.coord = coord



Pokelist = []

with open('../data/pokemon_first_gen.csv') as csvfile:
    fichier = csv.reader(csvfile,delimiter = ',')
    for row in fichier:
        Pokelist.append([row[1],row[2],row[5],row[6],row[7],row[8],row[9],row[10]])


Pokelist_legende = Pokelist.pop(0)


        
Pokedex = []

for elt in Pokelist:
    Pokedex.append(Pokemon(elt[0],elt[1],elt[2],elt[3],elt[4],elt[5],elt[6],elt[7]))

pix = 232
piy = 400
area = 0

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
a = 1



j1 = d.joueur(case_depart, test_map)
id_Poke = 0



class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('gui\logos\py_symbol.png'))
        global mode 
        global id_Poke
        id_Poke = 0
        mode = 0
        self.menuUI()
        self.son()
        
        
    
    def menuUI(self):
        self.setWindowIcon(QtGui.QIcon('gui\logos\py_symbol.png'))
        label = QLabel(self)
        self.setCentralWidget(label)
        pixmap = QPixmap("gui\logos\menu_background.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        self.show()

    def carteUI(self):
        super(MainWindow, self).__init__()
        self.setWindowIcon(QtGui.QIcon('gui\logos\py_symbol.png'))
        self.title = "Pykémon"
        self.setWindowTitle(self.title)
        label = QLabel(self)
        pixmap = QPixmap("gui\maps\game.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        self.setCentralWidget(label)
        self.show()
        
    def combatUI(self):
        global id_Poke
        super(MainWindow, self).__init__()
        self.setWindowIcon(QtGui.QIcon('gui\logos\py_symbol.png'))
        self.title = "Pykémon"
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
        
        
        
    
        
    def son(self):
        app = QtWidgets.QApplication(sys.argv)
        filename = "..\code\gui\The Great Marsh & Pal Park [Pokémon Diamond & Pearl].mp3"
        fullpath = QtCore.QDir.current().absoluteFilePath(filename) 
        url = QtCore.QUrl.fromLocalFile(fullpath)
        content = QtMultimedia.QMediaContent(url)
        player = QtMultimedia.QMediaPlayer()
        player.setMedia(content)
        player.play()
        sys.exit(app.exec_())
        
       
    
    
    def keyPressEvent(self, e):
        global j1
        global all_img
        global img4
        global mode
        global id_Poke
        if e.key() == Qt.Key_Space and mode == 0:
            mode = 1
            self.hide()
            self.carteUI()
            
        if mode == 1:
            mode, id_Poke = de.affiche_deplacement(self, j1, e, Pokedex)
        
        if mode == 2:
            self.hide()
            self.combatUI()
            mode = 3
        
        if mode == 3:
            
            
            
                
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())





