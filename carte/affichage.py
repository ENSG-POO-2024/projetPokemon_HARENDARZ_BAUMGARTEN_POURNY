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

import carte as c
import deplacement as d



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

def nouv_j(j):
    re = j.deplacement("Up")
    return re
 
jsp = nouv_j(j1)    

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        super(MainWindow, self).__init__()
        self.title = "Image Viewer"
        self.setWindowTitle(self.title)
        label = QLabel(self)
        pixmap = QPixmap("game.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        self.setCentralWidget(label)
        self.show()
    
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
            new_image.save("game.png")
            label = QLabel(self)
            pixmap = QPixmap("game.png")
            label.setPixmap(pixmap)
            label.setScaledContents(True)
            self.setCentralWidget(label)
        if e.key() == Qt.Key_Down:
            j1.deplacement("down").case.x
            img0 = Image.open("..\code\gui\Safari_Zone_entrance_RBY.png")
            img1 = Image.open("..\code\gui\Safari_Zone_area_1_RBY.png")
            img2 = Image.open("..\code\gui\Safari_Zone_area_2_RBY.png")
            img3 = Image.open("..\code\gui\Safari_Zone_area_3_RBY.png")
            img4 = Image.open("..\code\gui\player_front.png")
            all_img = [img0,img1,img2,img3]
            new_image = all_img[j1.case.area_id]
            new_image.paste(img4, (j1.case.y * 8, j1.case.x * 8), mask = img4)
            new_image.save("game.png")
            label = QLabel(self)
            pixmap = QPixmap("game.png")
            label.setPixmap(pixmap)
            label.setScaledContents(True)
            self.setCentralWidget(label)
        if e.key() == Qt.Key_Left:
            j1.deplacement("left").case.x
            img0 = Image.open("..\code\gui\Safari_Zone_entrance_RBY.png")
            img1 = Image.open("..\code\gui\Safari_Zone_area_1_RBY.png")
            img2 = Image.open("..\code\gui\Safari_Zone_area_2_RBY.png")
            img3 = Image.open("..\code\gui\Safari_Zone_area_3_RBY.png")
            img4 = Image.open("..\code\gui\player_front.png")
            all_img = [img0,img1,img2,img3]
            new_image = all_img[j1.case.area_id]
            new_image.paste(img4, (j1.case.y * 8, j1.case.x * 8), mask = img4)
            new_image.save("game.png")
            label = QLabel(self)
            pixmap = QPixmap("game.png")
            label.setPixmap(pixmap)
            label.setScaledContents(True)
            self.setCentralWidget(label)
        if e.key() == Qt.Key_Right:
            j1.deplacement("right").case.x
            img0 = Image.open("..\code\gui\Safari_Zone_entrance_RBY.png")
            img1 = Image.open("..\code\gui\Safari_Zone_area_1_RBY.png")
            img2 = Image.open("..\code\gui\Safari_Zone_area_2_RBY.png")
            img3 = Image.open("..\code\gui\Safari_Zone_area_3_RBY.png")
            img4 = Image.open("..\code\gui\player_front.png")
            all_img = [img0,img1,img2,img3]
            new_image = all_img[j1.case.area_id]
            new_image.paste(img4, (j1.case.y * 8, j1.case.x * 8), mask = img4)
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




