# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:25:58 2024

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
import affichage_deplacement as de

def affiche_combat(id_Poke,Equipe)v