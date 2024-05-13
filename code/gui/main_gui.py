# GUI main window and widgets definition


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QGraphicsOpacityEffect
import gui_resources
import sys

##################
##  MainWindow  ##
##################

class MainWindow(QMainWindow):  
    def __init__(self, app):
        QMainWindow.__init__(self)
        QtGui.QFontDatabase.addApplicationFont("fonts/Retro_Gaming.ttf")
        a = self.startup_ratio(app)
        self.max_width = a[0]
        self.max_height = a[1]
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logos/py_symbol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setAnimated(True)
        self.setEnabled(True)
        self.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.setMinimumSize(QtCore.QSize(1280, 720))
        self.setMaximumSize(QtCore.QSize(self.max_width, self.max_height))

        self.centralwidget = QWidget(self)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)

        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        menubar = QtWidgets.QMenuBar(self)
        menubar.setGeometry(QtCore.QRect(0, 0, 1217, 21))
        menubar.setObjectName("menubar")
        self.setMenuBar(menubar)
        
        statusbar = QtWidgets.QStatusBar(self)
        statusbar.setObjectName("statusbar")
        self.setStatusBar(statusbar)

        QtCore.QMetaObject.connectSlotsByName(self)
        self.retranslateUi()
        self.screen_resize(self.max_width, self.max_height)
        
        self.opacity = QGraphicsOpacityEffect(self)
        self.opacity.setOpacity(1)
        self.blackBackground = QWidget(self.centralwidget)
        self.blackBackground.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.blackBackground.setGraphicsEffect(self.opacity)
        # self.blackBackground.setAutoFillBackground(True)

        # self.animation = QtCore.QPropertyAnimation(self.blackBackground, b'opacity')
        # self.animation.setDuration(4000)
        # self.animation.stop()
        # self.animation.setStartValue(0)
        # self.animation.setEndValue(1)
        # self.animation.start()

        self.gridLayout.addWidget(self.blackBackground, 0, 0, 1, 1)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Pykemon_MainWindow", "Pykémon : Attrapy-les tous !"))

    def screen_resize(self, width, height):
        self.resize(width, height)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.showMaximized()
    
    def startup_ratio(self, app):
        screen = app.primaryScreen()
        size = screen.size()
        self.ratio = size.width()/1920
        return [size.width(), size.height()]
    

###############################
##  Black background widget  ##
###############################

# class QWidget():
#     def black_to_visible(self):
#         self.animation = QtCore.QPropertyAnimation(self, b'windowOpacity')
#         self.animation.setDuration(1000)
#         try:
#             self.animation.finished.disconnect(self.close)
#         except:
#             pass
#         self.animation.stop()
#         self.animation.setStartValue(0)
#         self.animation.setEndValue(1)
#         self.animation.start()

# A regarder : https://stackoverflow.com/questions/57828052/qpropertyanimation-not-working-with-window-opacity
    


    



