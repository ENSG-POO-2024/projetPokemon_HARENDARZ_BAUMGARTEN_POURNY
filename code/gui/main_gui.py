# GUI main window and widgets definition


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QGraphicsOpacityEffect
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
        self.setStyleSheet("background-color: rgb(120, 0, 0);")
        self.setMinimumSize(QtCore.QSize(1280, 720))
        self.setMaximumSize(QtCore.QSize(self.max_width, self.max_height))

        self.centralwidget = QWidget(self)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)

        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        QtCore.QMetaObject.connectSlotsByName(self)
        self.retranslateUi()
        self.screen_resize(self.max_width, self.max_height)
        
        # self.opacity = QGraphicsOpacityEffect(self)
        # self.opacity.setOpacity(1)
        self.LateralMenuButton = Ui_LateralMenuButton(self.centralwidget)
        self.transparent = Widget()
        self.transparent.resize(QSize(2490, 1370))
        self.transparent.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.gridLayout.addWidget(self.LateralMenuButton, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.transparent, 1, 1, 1, 1)
        # self.gridLayout.setColumnStretch(1, 100)
        # self.gridLayout.setRowStretch(1, 10)
        # self.blackBackground = QWidget(self.centralwidget)
        # self.blackBackground.setStyleSheet("background-color: rgb(0, 0, 255);")
        # self.blackBackground.setGraphicsEffect(self.opacity)

        self.player = MusicJukebox()

        # self.gridLayout.addWidget(self.blackBackground, 0, 0, 1, 1)

        
        #self.LateralMenuButton.clicked.connect(print("C'est bon !"))

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Pykemon_MainWindow", "Pykémon : Attrapy-les tous !"))

    def screen_resize(self, width, height):
        self.resize(width, height)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.showMaximized()
    
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


########################
##  Widget surcharge  ##
########################



###

# class MainWidget(Widget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         gridLayout = QGridLayout(self)
#         self.setLayout(gridLayout)
#         boutonAfficher = QPushButton("Test !")

#         gridLayout.addWidget(boutonAfficher, 0, 0)
#         boutonAfficher.clicked.connect(self.fade_out)
#         LateralMenuButton = Ui_LateralMenuButton(self)
#         LateralMenuButton.clicked.connect(self.fade_out)
#         gridLayout.addWidget(LateralMenuButton, 0, 1)

#         self.player = MusicJukebox()

    def closeEvent(self, event):
        # fade out
        self.fade_out()
        self.player.stop_song()
        super().closeEvent(event)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = MainWindow(app)
    w.show()

    sys.exit(app.exec_())
    


    



