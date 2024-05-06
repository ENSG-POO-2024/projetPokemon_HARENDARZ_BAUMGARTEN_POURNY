# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:48:22 2024

@author: romai
"""

import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt
from PIL import Image
import numpy as np
from PyQt5 import QtCore, QtWidgets, QtMultimedia

import carte as c
import deplacement as d
import random as rd




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
new_image.save("game.png")

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


def affiche_id(pid):
    idd = str(pid)
    nb_0 = 3 - len(idd)
    nom = ""
    for i in range(nb_0):
        nom = nom + "0"
    return nom + idd

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.son()
        

    def initUI(self):
        super(MainWindow, self).__init__()
        self.title = "Pykémon"
        self.setWindowTitle(self.title)
        label = QLabel(self)
        pixmap = QPixmap("game.png")
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
        if e.key() == Qt.Key_Up:
            j1.deplacement("up")
            img0 = Image.open("..\code\gui\Safari_Zone_entrance_RBY.png")
            img1 = Image.open("..\code\gui\Safari_Zone_area_1_RBY.png")
            img2 = Image.open("..\code\gui\Safari_Zone_area_2_RBY.png")
            img3 = Image.open("..\code\gui\Safari_Zone_area_3_RBY.png")
            img4 = Image.open("..\code\gui\player_back.png")
            all_img = [img0,img1,img2,img3]
            new_image = all_img[j1.case.area_id]
            new_image.paste(img4, (j1.case.y * 8, j1.case.x * 8), mask = img4)
            if j1.case.type_case(j1.map) == "Herbe":
                id_Poke = rd.randint(1, 1000)
                if id_Poke <= 151:
                    print(Pokedex[id_Poke].name) ### A modifier pour lancer le combat
                    img5 = Image.open("..\code\gui\spr_rb-supgb_" + affiche_id(id_Poke) + ".png")
                    new_image.paste(img5, (j1.case.y * 8, j1.case.x * 8))
            new_image.save("game.png")
            label = QLabel(self)
            pixmap = QPixmap("game.png")
            label.setPixmap(pixmap)
            label.setScaledContents(True)
            self.setCentralWidget(label)
        if e.key() == Qt.Key_Down:
            j1.deplacement("down")
            img0 = Image.open("..\code\gui\Safari_Zone_entrance_RBY.png")
            img1 = Image.open("..\code\gui\Safari_Zone_area_1_RBY.png")
            img2 = Image.open("..\code\gui\Safari_Zone_area_2_RBY.png")
            img3 = Image.open("..\code\gui\Safari_Zone_area_3_RBY.png")
            img4 = Image.open("..\code\gui\player_front.png")
            all_img = [img0,img1,img2,img3]
            new_image = all_img[j1.case.area_id]
            new_image.paste(img4, (j1.case.y * 8, j1.case.x * 8), mask = img4)
            if j1.case.type_case(j1.map) == "Herbe":
                id_Poke = rd.randint(1, 1000)
                if id_Poke <= 151:
                    print(Pokedex[id_Poke].name) ### A modifier pour lancer le combat
                    img5 = Image.open("..\code\gui\spr_rb-supgb_" + affiche_id(id_Poke) + ".png")
                    new_image.paste(img5, (j1.case.y * 8, j1.case.x * 8))
            new_image.save("game.png")
            label = QLabel(self)
            pixmap = QPixmap("game.png")
            label.setPixmap(pixmap)
            label.setScaledContents(True)
            self.setCentralWidget(label)
        if e.key() == Qt.Key_Left:
            j1.deplacement("left")
            img0 = Image.open("..\code\gui\Safari_Zone_entrance_RBY.png")
            img1 = Image.open("..\code\gui\Safari_Zone_area_1_RBY.png")
            img2 = Image.open("..\code\gui\Safari_Zone_area_2_RBY.png")
            img3 = Image.open("..\code\gui\Safari_Zone_area_3_RBY.png")
            img4 = Image.open("..\code\gui\player_left.png")
            all_img = [img0,img1,img2,img3]
            new_image = all_img[j1.case.area_id]
            new_image.paste(img4, (j1.case.y * 8, j1.case.x * 8), mask = img4)
            if j1.case.type_case(j1.map) == "Herbe":
                id_Poke = rd.randint(1, 1000)
                if id_Poke <= 151:
                    print(Pokedex[id_Poke].name) ### A modifier pour lancer le combat
                    img5 = Image.open("..\code\gui\spr_rb-supgb_" + affiche_id(id_Poke) + ".png")
                    new_image.paste(img5, (j1.case.y * 8, j1.case.x * 8))
            new_image.save("game.png")
            label = QLabel(self)
            pixmap = QPixmap("game.png")
            label.setPixmap(pixmap)
            label.setScaledContents(True)
            self.setCentralWidget(label)
        if e.key() == Qt.Key_Right:
            j1.deplacement("right")
            img0 = Image.open("..\code\gui\Safari_Zone_entrance_RBY.png")
            img1 = Image.open("..\code\gui\Safari_Zone_area_1_RBY.png")
            img2 = Image.open("..\code\gui\Safari_Zone_area_2_RBY.png")
            img3 = Image.open("..\code\gui\Safari_Zone_area_3_RBY.png")
            img4 = Image.open("..\code\gui\player_right.png")
            all_img = [img0,img1,img2,img3]
            new_image = all_img[j1.case.area_id]
            new_image.paste(img4, (j1.case.y * 8, j1.case.x * 8), mask = img4)
            if j1.case.type_case(j1.map) == "Herbe":
                id_Poke = rd.randint(1, 1000)
                if id_Poke <= 151:
                    print(Pokedex[id_Poke].name) ### A modifier pour lancer le combat
                    img5 = Image.open("..\code\gui\spr_rb-supgb_" + affiche_id(id_Poke) + ".png")
                    new_image.paste(img5, (j1.case.y * 8, j1.case.x * 8))
            new_image.save("game.png")
            label = QLabel(self)
            pixmap = QPixmap("game.png")
            label.setPixmap(pixmap)
            label.setScaledContents(True)
            self.setCentralWidget(label)
            
            
                
            
        

app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())





