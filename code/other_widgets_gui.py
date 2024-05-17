# Other widgets gui

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

class menuUi_class(Widget2):
    def __init__(self, width, height, parent=None):
        super().__init__(parent)
        self.label = QLabel(self)
        pixmap = QPixmap("gui\logos\Retropix.png")
        pixmap = pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.setGeometry(QtCore.QRect(0, 0, width, height))
        self.lower()
    

class carteUi_class(Widget2):
    def __init__(self, width, height, parent=None):
        super().__init__(parent)
        self.label = QLabel(self)
        pixmap = QPixmap("gui\maps\game.png")
        pixmap = pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.setGeometry(QtCore.QRect(0, 0, width, height))
        self.lower()

    def reloadPixmap(self, width, height):
        pixmap = QPixmap("gui\maps\game.png")
        pixmap = pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)

class inventraireUi_class(Widget2):
    def __init__(self, width, height, parent=None):
        super().__init__(parent)
        self.label = QLabel(self)
        pixmap = QPixmap("inventory_poke.png")
        pixmap = pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.setGeometry(QtCore.QRect(0, 0, width, height))
        self.lower()
    
    def reloadPixmap(self, width, height):
        pixmap = QPixmap("inventory_poke.png")
        pixmap = pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)

class combatUi_class(Widget2):
    def __init__(self, width, height, parent=None):
        super().__init__(parent)
        self.label = QLabel(self)
        pixmap = QPixmap("fight.png")
        pixmap = pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.setGeometry(QtCore.QRect(0, 0, width, height))
        self.lower()

    def reloadPixmap(self, width, height):
        pixmap = QPixmap("fight.png")
        pixmap = pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)

class introUi_class(Widget2):
    def __init__(self, width, height, parent=None):
        super().__init__(parent)
        self.label = QLabel(self)
        pixmap = QPixmap("oak_intro2.png")
        pixmap = pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.setGeometry(QtCore.QRect(0, 0, width, height))
        self.lower()

    def reloadPixmap(self, width, height):
        pixmap = QPixmap("oak_intro2.png")
        pixmap = pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)

