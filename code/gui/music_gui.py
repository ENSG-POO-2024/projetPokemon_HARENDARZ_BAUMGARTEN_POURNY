# Music player definition

from PyQt5.QtCore import QUrl, QDir
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import *
import os
import sys

path = os.getcwd()

#####################
##  Music jukebox  ##
#####################

class MusicJukebox(QMediaPlayer):
    def __init__(self):
        super().__init__()
        self.currentVolume = 50
        self.setVolume(self.currentVolume)
        self.songs_available = {'Main': './music/gta_3_theme.mp3'}
        self.play_song()


    def play_song(self, name='Main'):
        song_path = QDir.current().absoluteFilePath(self.songs_available[name])
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

