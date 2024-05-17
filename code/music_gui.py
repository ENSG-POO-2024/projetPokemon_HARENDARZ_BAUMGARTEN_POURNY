# Music player definition

from PyQt5.QtCore import QUrl, QDir
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import *
import os

path = os.getcwd()

#####################
##  Music jukebox  ##
#####################

class MusicJukebox(QMediaPlayer):
    def __init__(self):
        super().__init__()
        self.currentVolume = 50
        self.setVolume(self.currentVolume)
        self.songs_available = {'MainMenu': './gui/music/gta_3_theme.mp3', 'Exploration': './gui/music/poke_diamond_pearl_great_marsh.mp3', 'Combat1': './gui/music/poke_black_white_battle.mp3', 'Combat2': './gui/music/cat_mario.mp3'}
        self.play_song()


    def play_song(self, name='MainMenu'):
        if self.state() == QMediaPlayer.StoppedState:
            song_path = QDir.current().absoluteFilePath(self.songs_available[name])
            song = QMediaContent(QUrl.fromLocalFile(song_path))
            self.setMedia(song)
            self.play()

    def pause_and_unpause(self):
        if self.state() == QMediaPlayer.PlayingState:
            self.pause()
        else:
            self.play()

    def stop_song(self):
        self.stop()



