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
import nouveau_combat as nc
import combat as co

import carte as c
import deplacement as d
import random as rd
import affichage_deplacement as de
import pokemon as p

def affiche_combat(self,mode, id_Poke,Equipe,Pokedex,e,phase,collection,environnement,poke_combattant = None,):
    if e.key() == Qt.Key_Space and phase == "intro":
        phase = "choix_action_fight"
        Poke_player = nc.choix_pokemon(Equipe)
        img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
        img_fond = Image.open('action_choice.png')
        img_fight = img_fond 
        fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 8)
        img_fight.paste(img_Poke_ennemie, (100,5))
        img_poke_player = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(Poke_player.id) + ".png")
        img_fight.paste(img_poke_player, (10,40))
        draw = ImageDraw.Draw(img_fight)
        txt_ennemie = Pokedex[id_Poke].name
        draw.text((25, 2), txt_ennemie, font = fnt, fill =(0, 0, 0))
        txt_player = Poke_player.name
        draw.text((90, 60), txt_player, font = fnt, fill =(0, 0, 0))
        txt_pv_actu = str(Poke_player.pv)
        draw.text((90, 78), txt_pv_actu, font = fnt, fill =(0, 0, 0))
        txt_pv_max = str(Poke_player.pv_totaux)
        draw.text((120, 78), txt_pv_max, font = fnt, fill =(0, 0, 0))
        txt_icon = ">"
        draw.text((72, 109), txt_icon, font = fnt, fill =(0, 0, 0))
        img_fight.save("fight.png")
        label = QLabel(self)
        pixmap = QPixmap("fight.png")
        label.setPixmap(pixmap) 
        label.setScaledContents(True)
        self.setCentralWidget(label)
        self.show()
        print(Poke_player.name)
        return mode, phase, Poke_player
    
    
    if phase == "choix_action_fight":
        if e.key() == Qt.Key_Right:
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('action_choice.png')
            img_fight = img_fond 
            fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 8)
            img_fight.paste(img_Poke_ennemie, (100,5))
            img_poke_player = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(Poke_player.id) + ".png")
            img_fight.paste(img_poke_player, (10,40))
            draw = ImageDraw.Draw(img_fight)
            txt_ennemie = Pokedex[id_Poke].name
            draw.text((25, 2), txt_ennemie, font = fnt, fill =(0, 0, 0))
            txt_player = Poke_player.name
            draw.text((90, 60), txt_player, font = fnt, fill =(0, 0, 0))
            txt_pv_actu = str(Poke_player.pv)
            draw.text((90, 78), txt_pv_actu, font = fnt, fill =(0, 0, 0))
            txt_pv_max = str(Poke_player.pv_totaux)
            draw.text((120, 78), txt_pv_max, font = fnt, fill =(0, 0, 0))
            txt_icon = ">"
            draw.text((120, 109), txt_icon, font = fnt, fill =(0, 0, 0))
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "choix_action_poke"
            return mode, phase, Poke_player
        
        if e.key() == Qt.Key_Space:
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_choice.png')
            img_fight = img_fond 
            fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 8)
            img_fight.paste(img_Poke_ennemie, (100,5))
            img_poke_player = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(Poke_player.id) + ".png")
            img_fight.paste(img_poke_player, (10,40))
            draw = ImageDraw.Draw(img_fight)
            txt_ennemie = Pokedex[id_Poke].name
            draw.text((25, 2), txt_ennemie, font = fnt, fill =(0, 0, 0))
            txt_player = Poke_player.name
            draw.text((90, 60), txt_player, font = fnt, fill =(0, 0, 0))
            txt_pv_actu = str(Poke_player.pv)
            draw.text((90, 78), txt_pv_actu, font = fnt, fill =(0, 0, 0))
            txt_pv_max = str(Poke_player.pv_totaux)
            draw.text((120, 78), txt_pv_max, font = fnt, fill =(0, 0, 0))
            txt_icon = ">"
            draw.text((39, 103), txt_icon, font = fnt, fill =(0, 0, 0))
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "attack_choice_n"
            return mode, phase, Poke_player
        else:
            return mode, phase, poke_combattant
        
        
    if phase == "choix_action_poke":
        if e.key() == Qt.Key_Down:
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('action_choice.png')
            img_fight = img_fond 
            fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 8)
            img_fight.paste(img_Poke_ennemie, (100,5))
            img_poke_player = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(Poke_player.id) + ".png")
            img_fight.paste(img_poke_player, (10,40))
            draw = ImageDraw.Draw(img_fight)
            txt_ennemie = Pokedex[id_Poke].name
            draw.text((25, 2), txt_ennemie, font = fnt, fill =(0, 0, 0))
            txt_player = Poke_player.name
            draw.text((90, 60), txt_player, font = fnt, fill =(0, 0, 0))
            txt_pv_actu = str(Poke_player.pv)
            draw.text((90, 78), txt_pv_actu, font = fnt, fill =(0, 0, 0))
            txt_pv_max = str(Poke_player.pv_totaux)
            draw.text((120, 78), txt_pv_max, font = fnt, fill =(0, 0, 0))
            txt_icon = ">"
            draw.text((120, 125), txt_icon, font = fnt, fill =(0, 0, 0))
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "choix_action_fuite"
            return mode, phase, Poke_player
        
        if e.key() == Qt.Key_Left:
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('action_choice.png')
            img_fight = img_fond 
            fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 8)
            img_fight.paste(img_Poke_ennemie, (100,5))
            img_poke_player = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(Poke_player.id) + ".png")
            img_fight.paste(img_poke_player, (10,40))
            draw = ImageDraw.Draw(img_fight)
            txt_ennemie = Pokedex[id_Poke].name
            draw.text((25, 2), txt_ennemie, font = fnt, fill =(0, 0, 0))
            txt_player = Poke_player.name
            draw.text((90, 60), txt_player, font = fnt, fill =(0, 0, 0))
            txt_pv_actu = str(Poke_player.pv)
            draw.text((90, 78), txt_pv_actu, font = fnt, fill =(0, 0, 0))
            txt_pv_max = str(Poke_player.pv_totaux)
            draw.text((120, 78), txt_pv_max, font = fnt, fill =(0, 0, 0))
            txt_icon = ">"
            draw.text((72, 109), txt_icon, font = fnt, fill =(0, 0, 0))
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "choix_action_fight"
            return mode, phase, Poke_player
        else:
            return mode, phase, poke_combattant
        
        
    if phase == "choix_action_fuite":
        if e.key() == Qt.Key_Up:
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('action_choice.png')
            img_fight = img_fond 
            fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 8)
            img_fight.paste(img_Poke_ennemie, (100,5))
            img_poke_player = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(Poke_player.id) + ".png")
            img_fight.paste(img_poke_player, (10,40))
            draw = ImageDraw.Draw(img_fight)
            txt_ennemie = Pokedex[id_Poke].name
            draw.text((25, 2), txt_ennemie, font = fnt, fill =(0, 0, 0))
            txt_player = Poke_player.name
            draw.text((90, 60), txt_player, font = fnt, fill =(0, 0, 0))
            txt_pv_actu = str(Poke_player.pv)
            draw.text((90, 78), txt_pv_actu, font = fnt, fill =(0, 0, 0))
            txt_pv_max = str(Poke_player.pv_totaux)
            draw.text((120, 78), txt_pv_max, font = fnt, fill =(0, 0, 0))
            txt_icon = ">"
            draw.text((120, 109), txt_icon, font = fnt, fill =(0, 0, 0))
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "choix_action_poke"
            return mode, phase, Poke_player
        
        if e.key() == Qt.Key_Space:
            co.fin_combat(Equipe, collection, Pokedex[id_Poke], environnement)
            mode = 1
            phase = "intro"
            self.hide()
            self.carteUI()
            return mode,phase,poke_combattant
            
        
        else:
            return mode, phase, poke_combattant
    if phase == "attack_choice_n":
        if e.key() == Qt.Key_Down:
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_choice.png')
            img_fight = img_fond 
            fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 8)
            img_fight.paste(img_Poke_ennemie, (100,5))
            img_poke_player = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(Poke_player.id) + ".png")
            img_fight.paste(img_poke_player, (10,40))
            draw = ImageDraw.Draw(img_fight)
            txt_ennemie = Pokedex[id_Poke].name
            draw.text((25, 2), txt_ennemie, font = fnt, fill =(0, 0, 0))
            txt_player = Poke_player.name
            draw.text((90, 60), txt_player, font = fnt, fill =(0, 0, 0))
            txt_pv_actu = str(Poke_player.pv)
            draw.text((90, 78), txt_pv_actu, font = fnt, fill =(0, 0, 0))
            txt_pv_max = str(Poke_player.pv_totaux)
            draw.text((120, 78), txt_pv_max, font = fnt, fill =(0, 0, 0))
            txt_icon = ">"
            draw.text((39, 123), txt_icon, font = fnt, fill =(0, 0, 0))
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "attack_choice_sp"
            return mode, phase, Poke_player
        else:
            return mode, phase, poke_combattant
    
    if phase == "attack_choice_sp":
        if e.key() == Qt.Key_Up:
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_choice.png')
            img_fight = img_fond 
            fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 8)
            img_fight.paste(img_Poke_ennemie, (100,5))
            img_poke_player = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(Poke_player.id) + ".png")
            img_fight.paste(img_poke_player, (10,40))
            draw = ImageDraw.Draw(img_fight)
            txt_ennemie = Pokedex[id_Poke].name
            draw.text((25, 2), txt_ennemie, font = fnt, fill =(0, 0, 0))
            txt_player = Poke_player.name
            draw.text((90, 60), txt_player, font = fnt, fill =(0, 0, 0))
            txt_pv_actu = str(Poke_player.pv)
            draw.text((90, 78), txt_pv_actu, font = fnt, fill =(0, 0, 0))
            txt_pv_max = str(Poke_player.pv_totaux)
            draw.text((120, 78), txt_pv_max, font = fnt, fill =(0, 0, 0))
            txt_icon = ">"
            draw.text((39, 103), txt_icon, font = fnt, fill =(0, 0, 0))
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "attack_choice_n"
            return mode, phase, Poke_player
        else:
            return mode, phase, poke_combattant
            
    
    else:
        return mode, phase, poke_combattant
   

            
            
            
            
            
            
            
            
        
    