# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:25:58 2024

@author: romai
"""


from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from PIL import Image, ImageDraw, ImageFont
import nouveau_combat as nc
import combat as co


import affichage_deplacement as de
import utilitaire

def affiche_combat(self,mode, id_Poke,Equipe,Pokedex,e,phase,collection,environnement,poke_combattant = None):
    """
    

    Parameters
    ----------
    mode : int
        chaque action ne peut que s'effectuer dans le bon mode
    id_Poke : int
        id du Pokemon ennemie
    Equipe : dict
        dictionnaire contenat les Pokemon de notre équipe
    Pokedex : dict
        dictionnaire de tout les Pokemon
    e : PyQt5.QtGui.QKeyEvent
        correspond à l'input de l'utilisateur
    phase : str
        nom de la phase de combat dans laquelle ous sommes permet de limiter les inputs et d'afficher correctement le combat
    collection : dict
        dictionnaire des Pokemon de notre inventaire
    environnement : dict
        dictionnaire des Pokemon sauvages
    poke_combattant : Pokemon, optional
        Pokemon du joueur en combat. The default is None.

    Returns
    -------
    mode : int
        chaque action ne peut que s'effectuer dans le bon mode
    phase : str
        nom de la phase de combat dans laquelle ous sommes permet de limiter les inputs et d'afficher correctement le combat
    Poke_player : Pokemon
        Pokemon du joueur en combat.

    """
    if (e.key() == Qt.Key_Space and phase == "intro") or (e.key() == Qt.Key_Space and phase =="tour_suivant"):
        if phase == "intro":
            Poke_player = nc.choix_pokemon(Equipe)
        else:
            Poke_player = poke_combattant
        phase = "choix_action_fight"
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
        draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
        draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
        img_fight.save("fight.png")
        label = QLabel(self)
        pixmap = QPixmap("fight.png")
        label.setPixmap(pixmap) 
        label.setScaledContents(True)
        self.setCentralWidget(label)
        self.show()
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
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
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
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
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
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
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
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "choix_action_fight"
            return mode, phase, Poke_player
    
        if e.key() == Qt.Key_Space:
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_result.png')
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
            n = 0
            for cle in Equipe:
                txt_poke = Equipe[cle].name
                if n > 2:
                    draw.text((85, 105 + 10 * (n-3)), txt_poke, font = fnt, fill =(0, 0, 0))
                else:
                    draw.text((20, 105 + 10 * n), txt_poke, font = fnt,fill =(0, 0, 0))
                n += 1 
            txt_icon = ">"
            draw.text((15, 105), txt_icon, font = fnt, fill =(0, 0, 0))
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "choix_poke1"
            return mode, phase, Poke_player
        
        
        else:
            return mode, phase, poke_combattant
        
    if phase == "choix_poke1":
        if e.key() == Qt.Key_Down:
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_result.png')
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
            n = 0
            for cle in Equipe:
                txt_poke = Equipe[cle].name
                if n > 2:
                    draw.text((85, 105 + 10 * (n-3)), txt_poke, font = fnt, fill =(0, 0, 0))
                else:
                    draw.text((20, 105 + 10 * n), txt_poke, font = fnt, fill =(0, 0, 0))
                n += 1 
            txt_icon = ">"
            draw.text((15, 115), txt_icon, font = fnt, fill =(0, 0, 0))
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "choix_poke2"
            return mode, phase, Poke_player
        
        if e.key() == Qt.Key_Right:
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_result.png')
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
            n = 0
            for cle in Equipe:
                txt_poke = Equipe[cle].name
                if n > 2:
                    draw.text((85, 105 + 10 * (n-3)), txt_poke, font = fnt, fill =(0, 0, 0))
                else:
                    draw.text((20, 105 + 10 * n), txt_poke, font = fnt, fill =(0, 0, 0))
                n += 1 
            txt_icon = ">"
            draw.text((80, 105), txt_icon, font = fnt, fill =(0, 0, 0))
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "choix_poke4"
            return mode, phase, Poke_player
        
        if e.key() == Qt.Key_Space:
            cle = list(Equipe.keys())
            if len(cle) >= 1 and Equipe[cle[0]].etat:
                Poke_player = Equipe[cle[0]]
                phase = "ennemie_turn"
                img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
                img_fond = Image.open('attack_result.png')
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
                fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 8)
                txt_icon = Poke_player.name + " I choose you !"
                draw.text((10, 110), txt_icon, font = fnt, fill =(0, 0, 0))
                draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
                draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
                img_fight.save("fight.png")
                label = QLabel(self)
                pixmap = QPixmap("fight.png")
                label.setPixmap(pixmap) 
                label.setScaledContents(True)
                self.setCentralWidget(label)
                self.show()
            else:
                Poke_player = poke_combattant
            return mode, phase, Poke_player
        
        
        else:
            return mode, phase, poke_combattant
        
    if phase == "choix_poke2":
        if e.key() == Qt.Key_Down:
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_result.png')
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
            n = 0
            for cle in Equipe:
                txt_poke = Equipe[cle].name
                if n > 2:
                    draw.text((85, 105 + 10 * (n-3)), txt_poke, font = fnt, fill =(0, 0, 0))
                else:
                    draw.text((20, 105 + 10 * n), txt_poke, font = fnt, fill =(0, 0, 0))
                n += 1 
            txt_icon = ">"
            draw.text((15, 125), txt_icon, font = fnt, fill =(0, 0, 0))
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "choix_poke3"
            return mode, phase, Poke_player
        
        if e.key() == Qt.Key_Up:
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_result.png')
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
            n = 0
            for cle in Equipe:
                txt_poke = Equipe[cle].name
                if n > 2:
                    draw.text((85, 105 + 10 * (n-3)), txt_poke, font = fnt, fill =(0, 0, 0))
                else:
                    draw.text((20, 105 + 10 * n), txt_poke, font = fnt, fill =(0, 0, 0))
                n += 1 
            txt_icon = ">"
            draw.text((15, 105), txt_icon, font = fnt, fill =(0, 0, 0))
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "choix_poke1"
            return mode, phase, Poke_player
        
        if e.key() == Qt.Key_Right:
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_result.png')
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
            n = 0
            for cle in Equipe:
                txt_poke = Equipe[cle].name
                if n > 2:
                    draw.text((85, 105 + 10 * (n-3)), txt_poke, font = fnt, fill =(0, 0, 0))
                else:
                    draw.text((20, 105 + 10 * n), txt_poke, font = fnt, fill =(0, 0, 0))
                n += 1 
            txt_icon = ">"
            draw.text((80, 115), txt_icon, font = fnt, fill =(0, 0, 0))
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "choix_poke5"
            return mode, phase, Poke_player
        
        if e.key() == Qt.Key_Space:
            cle = list(Equipe.keys())
            if len(cle) >= 2 and Equipe[cle[1]].etat:
                Poke_player = Equipe[cle[1]]
                phase = "ennemie_turn"
                img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
                img_fond = Image.open('attack_result.png')
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
                fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 8)
                txt_icon = Poke_player.name + " I choose you !"
                draw.text((10, 110), txt_icon, font = fnt, fill =(0, 0, 0))
                draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
                draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
                img_fight.save("fight.png")
                label = QLabel(self)
                pixmap = QPixmap("fight.png")
                label.setPixmap(pixmap) 
                label.setScaledContents(True)
                self.setCentralWidget(label)
                self.show()
            else:
                Poke_player = poke_combattant
            return mode, phase, Poke_player
        
        else:
            return mode, phase, poke_combattant
        
    if phase == "choix_poke3":
        if e.key() == Qt.Key_Up:
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_result.png')
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
            n = 0
            for cle in Equipe:
                txt_poke = Equipe[cle].name
                if n > 2:
                    draw.text((85, 105 + 10 * (n-3)), txt_poke, font = fnt, fill =(0, 0, 0))
                else:
                    draw.text((20, 105 + 10 * n), txt_poke, font = fnt, fill =(0, 0, 0))
                n += 1 
            txt_icon = ">"
            draw.text((15, 115), txt_icon, font = fnt, fill =(0, 0, 0))
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "choix_poke2"
            return mode, phase, Poke_player
        
        if e.key() == Qt.Key_Right:
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_result.png')
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
            n = 0
            for cle in Equipe:
                txt_poke = Equipe[cle].name
                if n > 2:
                    draw.text((85, 105 + 10 * (n-3)), txt_poke, font = fnt, fill =(0, 0, 0))
                else:
                    draw.text((20, 105 + 10 * n), txt_poke, font = fnt, fill =(0, 0, 0))
                n += 1 
            txt_icon = ">"
            draw.text((80, 125), txt_icon, font = fnt, fill =(0, 0, 0))
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "choix_poke6"
            return mode, phase, Poke_player
        
        if e.key() == Qt.Key_Space:
            cle = list(Equipe.keys())
            if len(cle) >= 3 and Equipe[cle[2]].etat:
                Poke_player = Equipe[cle[2]]
                phase = "ennemie_turn"
                img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
                img_fond = Image.open('attack_result.png')
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
                fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 8)
                txt_icon = Poke_player.name + " I choose you !"
                draw.text((10, 110), txt_icon, font = fnt, fill =(0, 0, 0))
                draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
                draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
                img_fight.save("fight.png")
                label = QLabel(self)
                pixmap = QPixmap("fight.png")
                label.setPixmap(pixmap) 
                label.setScaledContents(True)
                self.setCentralWidget(label)
                self.show()
            else:
                Poke_player = poke_combattant
            return mode, phase, Poke_player
        
        
        else:
            return mode, phase, poke_combattant
        
    if phase == "choix_poke4":
        if e.key() == Qt.Key_Down:
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_result.png')
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
            n = 0
            for cle in Equipe:
                txt_poke = Equipe[cle].name
                if n > 2:
                    draw.text((85, 105 + 10 * (n-3)), txt_poke, font = fnt, fill =(0, 0, 0))
                else:
                    draw.text((20, 105 + 10 * n), txt_poke, font = fnt, fill =(0, 0, 0))
                n += 1 
            txt_icon = ">"
            draw.text((80, 115), txt_icon, font = fnt, fill =(0, 0, 0))
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "choix_poke5"
            return mode, phase, Poke_player
        
        if e.key() == Qt.Key_Left:
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_result.png')
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
            n = 0
            for cle in Equipe:
                txt_poke = Equipe[cle].name
                if n > 2:
                    draw.text((85, 105 + 10 * (n-3)), txt_poke, font = fnt, fill =(0, 0, 0))
                else:
                    draw.text((20, 105 + 10 * n), txt_poke, font = fnt, fill =(0, 0, 0))
                n += 1 
            txt_icon = ">"
            draw.text((15, 105), txt_icon, font = fnt, fill =(0, 0, 0))
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "choix_poke1"
            return mode, phase, Poke_player
        
        if e.key() == Qt.Key_Space:
            cle = list(Equipe.keys())
            if len(cle) >= 4 and Equipe[cle[3]].etat:
                Poke_player = Equipe[cle[3]]
                phase = "ennemie_turn"
                img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
                img_fond = Image.open('attack_result.png')
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
                fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 8)
                txt_icon = Poke_player.name + " I choose you !"
                draw.text((10, 110), txt_icon, font = fnt, fill =(0, 0, 0))
                draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
                draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
                img_fight.save("fight.png")
                label = QLabel(self)
                pixmap = QPixmap("fight.png")
                label.setPixmap(pixmap) 
                label.setScaledContents(True)
                self.setCentralWidget(label)
                self.show()
            else:
                Poke_player = poke_combattant
            return mode, phase, Poke_player
        
        
        else:
            return mode, phase, poke_combattant
        
    if phase == "choix_poke5":
        if e.key() == Qt.Key_Down:
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_result.png')
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
            n = 0
            for cle in Equipe:
                txt_poke = Equipe[cle].name
                if n > 2:
                    draw.text((85, 105 + 10 * (n-3)), txt_poke, font = fnt, fill =(0, 0, 0))
                else:
                    draw.text((20, 105 + 10 * n), txt_poke, font = fnt, fill =(0, 0, 0))
                n += 1 
            txt_icon = ">"
            draw.text((80, 125), txt_icon, font = fnt, fill =(0, 0, 0))
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "choix_poke6"
            return mode, phase, Poke_player
        
        if e.key() == Qt.Key_Up:
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_result.png')
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
            n = 0
            for cle in Equipe:
                txt_poke = Equipe[cle].name
                if n > 2:
                    draw.text((85, 105 + 10 * (n-3)), txt_poke, font = fnt, fill =(0, 0, 0))
                else:
                    draw.text((20, 105 + 10 * n), txt_poke, font = fnt, fill =(0, 0, 0))
                n += 1 
            txt_icon = ">"
            draw.text((80, 105), txt_icon, font = fnt, fill =(0, 0, 0))
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "choix_poke4"
            return mode, phase, Poke_player
        
        if e.key() == Qt.Key_Left:
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_result.png')
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
            n = 0
            for cle in Equipe:
                txt_poke = Equipe[cle].name
                if n > 2:
                    draw.text((85, 105 + 10 * (n-3)), txt_poke, font = fnt, fill =(0, 0, 0))
                else:
                    draw.text((20, 105 + 10 * n), txt_poke, font = fnt, fill =(0, 0, 0))
                n += 1 
            txt_icon = ">"
            draw.text((15, 115), txt_icon, font = fnt, fill =(0, 0, 0))
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "choix_poke2"
            return mode, phase, Poke_player
        
        if e.key() == Qt.Key_Space:
            cle = list(Equipe.keys())
            if len(cle) >= 5 and Equipe[cle[4]].etat:
                Poke_player = Equipe[cle[4]]
                phase = "ennemie_turn"
                img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
                img_fond = Image.open('attack_result.png')
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
                fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 8)
                txt_icon = Poke_player.name + " I choose you !"
                draw.text((10, 110), txt_icon, font = fnt, fill =(0, 0, 0))
                draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
                draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
                img_fight.save("fight.png")
                label = QLabel(self)
                pixmap = QPixmap("fight.png")
                label.setPixmap(pixmap) 
                label.setScaledContents(True)
                self.setCentralWidget(label)
                self.show()
            else:
                Poke_player = poke_combattant
            return mode, phase, Poke_player
        
        else:
            return mode, phase, poke_combattant
        
    if phase == "choix_poke6":
        if e.key() == Qt.Key_Up:
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_result.png')
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
            n = 0
            for cle in Equipe:
                txt_poke = Equipe[cle].name
                if n > 2:
                    draw.text((85, 105 + 10 * (n-3)), txt_poke, font = fnt, fill =(0, 0, 0))
                else:
                    draw.text((20, 105 + 10 * n), txt_poke, font = fnt, fill =(0, 0, 0))
                n += 1 
            txt_icon = ">"
            draw.text((80, 115), txt_icon, font = fnt, fill =(0, 0, 0))
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "choix_poke5"
            return mode, phase, Poke_player
        
        if e.key() == Qt.Key_Left:
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_result.png')
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
            n = 0
            for cle in Equipe:
                txt_poke = Equipe[cle].name
                if n > 2:
                    draw.text((85, 105 + 10 * (n-3)), txt_poke, font = fnt, fill =(0, 0, 0))
                else:
                    draw.text((20, 105 + 10 * n), txt_poke, font = fnt, fill =(0, 0, 0))
                n += 1 
            txt_icon = ">"
            draw.text((15, 125), txt_icon, font = fnt, fill =(0, 0, 0))
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "choix_poke3"
            return mode, phase, Poke_player
        
        if e.key() == Qt.Key_Space:
            cle = list(Equipe.keys())
            if len(cle) >= 6 and Equipe[cle[5]].etat:
                Poke_player = Equipe[cle[5]]
                phase = "ennemie_turn"
                img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
                img_fond = Image.open('attack_result.png')
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
                fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 8)
                txt_icon = Poke_player.name + " I choose you !"
                draw.text((10, 110), txt_icon, font = fnt, fill =(0, 0, 0))
                draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
                draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
                img_fight.save("fight.png")
                label = QLabel(self)
                pixmap = QPixmap("fight.png")
                label.setPixmap(pixmap) 
                label.setScaledContents(True)
                self.setCentralWidget(label)
                self.show()
            else:
                Poke_player = poke_combattant
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
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
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
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_result.png')
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
            fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 8)
            txt_icon = "You flee !"
            draw.text((20, 110), txt_icon, font = fnt, fill =(0, 0, 0))
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "return_carte"
            return mode,phase,Poke_player
            
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
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "attack_choice_sp"
            return mode, phase, Poke_player
        
        if e.key() == Qt.Key_Space:
            co.tour_joueur(poke_combattant, Pokedex[id_Poke], 'normale')
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_result.png')
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
            fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 8)
            txt_icon = "You use normal attack"
            draw.text((20, 110), txt_icon, font = fnt, fill =(0, 0, 0))
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            if Pokedex[id_Poke].pv <= 0:
                phase = "victory"
            else:
                phase = "ennemie_turn"
            
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
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "attack_choice_n"
            return mode, phase, Poke_player
        
        if e.key() == Qt.Key_Space:
            co.tour_joueur(poke_combattant, Pokedex[id_Poke], 'speciale')
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_result.png')
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
            fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 8)
            txt_icon = "You use special attack"
            draw.text((20, 110), txt_icon, font = fnt, fill =(0, 0, 0))
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            if Pokedex[id_Poke].pv <= 0:
                phase = "victory"
            else:
                phase = "ennemie_turn"
            
            return mode, phase, Poke_player
        
        else:
            return mode, phase, poke_combattant
        
        
        
    if phase == "ennemie_turn":
        if e.key() == Qt.Key_Space:
            co.tour_environnement(Pokedex[id_Poke],poke_combattant)
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_result.png')
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
            fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 8)
            txt_icon = "The ennemie Pokemon attack"
            draw.text((10, 110), txt_icon, font = fnt, fill =(0, 0, 0))
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            if poke_combattant.pv <= 0:
                for cle in Equipe:
                    if Equipe[cle].etat:
                        phase = "poke_mort"
                        return mode, phase, Poke_player
                phase = "game_over"
                return mode, phase, Poke_player
            else:
                phase = "tour_suivant"
            return mode, phase, Poke_player
        
        else:
            return mode, phase, poke_combattant
        
    if phase == "poke_mort":
        if e.key() == Qt.Key_Space:
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_result.png')
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
            n = 0
            for cle in Equipe:
                txt_poke = Equipe[cle].name
                if n > 2:
                    draw.text((85, 105 + 10 * (n-3)), txt_poke, font = fnt, fill =(0, 0, 0))
                else:
                    draw.text((20, 105 + 10 * n), txt_poke, font = fnt, fill =(0, 0, 0))
                n += 1 
            txt_icon = ">"
            draw.text((15, 105), txt_icon, font = fnt, fill =(0, 0, 0))
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "choix_poke1"
            return mode, phase, Poke_player
        else:
            return mode, phase, poke_combattant
    
    if phase == "victory":
        if e.key() == Qt.Key_Space:
            co.fin_combat(Equipe, collection, Pokedex[id_Poke], environnement)
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_result.png')
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
            fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 8)
            txt_icon = "You win the fight !"
            draw.text((20, 110), txt_icon, font = fnt, fill =(0, 0, 0))
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "return_carte"
            return mode, phase, Poke_player
    
    if phase == "game_over":
        if e.key() == Qt.Key_Space:
            co.fin_combat(Equipe, collection, Pokedex[id_Poke], environnement)
            Poke_player = poke_combattant
            img_Poke_ennemie = Image.open("..\code\gui\spr_rb-supgb_" + de.affiche_id(id_Poke) + ".png")
            img_fond = Image.open('attack_result.png')
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
            fnt = ImageFont.truetype("gui/Retro_Gaming.ttf", 8)
            txt_icon = Pokedex[id_Poke].name + " defeat you !"
            draw.text((20, 110), txt_icon, font = fnt, fill =(0, 0, 0))
            draw.rectangle([(Poke_player.pv / Poke_player.pv_totaux * 47 + 95, 73), (142, 74)] )
            draw.rectangle([(Pokedex[id_Poke].pv / Pokedex[id_Poke].pv_totaux * 47 + 31, 17), (78, 18)] )
            img_fight.save("fight.png")
            label = QLabel(self)
            pixmap = QPixmap("fight.png")
            label.setPixmap(pixmap) 
            label.setScaledContents(True)
            self.setCentralWidget(label)
            self.show()
            phase = "return_carte"
            return mode, phase, Poke_player
        else:
            return mode, phase, poke_combattant
        
    if phase == "return_carte":
        if e.key() == Qt.Key_Space:
            utilitaire.soin(Equipe)
            mode = 1
            phase = "intro"
            self.hide()
            self.carteUI()
            return mode,phase,poke_combattant
            
            
    
    else:
        return mode, phase, poke_combattant
   

            
            
            
            
            
            
            
            
        
    