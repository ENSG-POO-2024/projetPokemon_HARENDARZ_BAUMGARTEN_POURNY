# Music player definition

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import *
import os

path = os.getcwd()

#####################
##  Music jukebox  ##
#####################

class MusicJukebox(QMediaPlayer):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.current_songs = []
        self.currentVolume = 50
        self.setVolume(self.currentVolume)
        self.songs_available = {'Main': 'gta_3_theme.mp3'}


    def play_song(self, name='Main'):
        song_path = path+'\\Music\\'+self.songs_available[name]
        print(song_path)
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
