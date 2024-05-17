# GUI main window and widgets definition


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QGraphicsOpacityEffect
from PyQt5.QtCore import QEasingCurve, QEventLoop, QPropertyAnimation, QRect, QSize, Qt
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QAction, QApplication, QGraphicsOpacityEffect, QWidget, QPushButton
import gui_resources
import sys
from time import *
from menu_gui import *
from music_gui import *
from widget_surcharge_gui import Widget

##################
##  MainWindow  ##
##################

class MainWindow(QMainWindow, Widget):  
    def __init__(self, app):
        super().__init__()
        QtGui.QFontDatabase.addApplicationFont("fonts/Retro_Gaming.ttf")
        a = self.startup_ratio(app)
        self.max_width = a[0]
        self.max_height = a[1]
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logos/py_symbol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setAnimated(True)
        self.setEnabled(True)
        # self.setStyleSheet("background-color: rgb(127, 255, 255);")
        self.setMinimumSize(QtCore.QSize(1280, 720))
        self.setMaximumSize(QtCore.QSize(self.max_width, self.max_height))
        self.retranslateUi()
        self.screen_resize(self.max_width, self.max_height)
        

        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
       
        self.player = MusicJukebox()
        
        self.lateralMenu = optionsMenu(self.centralwidget)
        self.lateralMenu.centerWidget(self.max_width, self.max_height)
        self.lateralMenuButton = Ui_LateralMenuButton(self.centralwidget)
        self.lateralMenuButton.clicked.connect(self.lateralMenu.test_for_hiding)
        
        self.lateralMenu.volumeHorizontalSlider.valueChanged.connect(self.changeVolume)
        self.lateralMenu.closeButton.clicked.connect(sys.exit)
        

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Pykemon_MainWindow", "Pykémon : Attrapy-les tous !"))

    def screen_resize(self, width, height):
        self.setGeometry(QtCore.QRect(0, 0, width, height))
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)     
    
    def startup_ratio(self, app):
        screen = app.primaryScreen()
        size = screen.size()
        self.ratio = size.width()/1920
        return [size.width(), size.height()]
    
    def closeEvent(self, event):
        # fade out
        self.fade_out()
        self.player.stop_song()
        super().closeEvent(event)

    def changeVolume(self):
        self.player.setVolume(self.lateralMenu.volumeHorizontalSlider.value())



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = MainWindow(app)
    w.show()

    app.exec_()
    


    



