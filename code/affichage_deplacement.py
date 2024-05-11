# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:00:24 2024

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
import affichage as a




import csv
import numpy as np

def affiche_id(pid):
    idd = str(pid)
    nb_0 = 3 - len(idd)
    nom = ""
    for i in range(nb_0):
        nom = nom + "0"
    return nom + idd

def affiche_deplacement(self,j1,e,Pokedex,environnement):
    global id_Poke
    mode = 1
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
                if id_Poke in environnement:
                    mode = 2
                    img5 = Image.open("..\code\gui\spr_rb-supgb_" + affiche_id(id_Poke) + ".png")
                    new_image.paste(img5, (j1.case.y * 8, j1.case.x * 8))
                    new_image.save("gui\maps\game.png")
                    return mode,id_Poke
        new_image.save("gui\maps\game.png")
        label = QLabel(self)
        pixmap = QPixmap("gui\maps\game.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        self.setCentralWidget(label)
        return mode,0
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
                if id_Poke in environnement:
                    mode = 2
                    img5 = Image.open("..\code\gui\spr_rb-supgb_" + affiche_id(id_Poke) + ".png")
                    new_image.paste(img5, (j1.case.y * 8, j1.case.x * 8))
                    new_image.save("gui\maps\game.png")
                    return mode,id_Poke
        new_image.save("gui\maps\game.png")
        label = QLabel(self)
        pixmap = QPixmap("gui\maps\game.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        self.setCentralWidget(label)
        return mode,0
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
                if id_Poke in environnement:
                    mode = 2
                    img5 = Image.open("..\code\gui\spr_rb-supgb_" + affiche_id(id_Poke) + ".png")
                    new_image.paste(img5, (j1.case.y * 8, j1.case.x * 8))
                    new_image.save("gui\maps\game.png")
                    return mode,id_Poke
        new_image.save("gui\maps\game.png")
        label = QLabel(self)
        pixmap = QPixmap("gui\maps\game.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        self.setCentralWidget(label)
        return mode,0
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
                if id_Poke in environnement:
                    mode = 2
                    img5 = Image.open("..\code\gui\spr_rb-supgb_" + affiche_id(id_Poke) + ".png")
                    new_image.paste(img5, (j1.case.y * 8, j1.case.x * 8))
                    new_image.save("gui\maps\game.png")
                    return mode,id_Poke
        new_image.save("gui\maps\game.png")
        label = QLabel(self)
        pixmap = QPixmap("gui\maps\game.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        self.setCentralWidget(label)
        return mode,0
    else:
        return mode,0
    