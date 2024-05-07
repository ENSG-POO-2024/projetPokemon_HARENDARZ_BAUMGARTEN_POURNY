# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_carte.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Pykemon_MainWindow(object):
    def setupUi(self, Pykemon_MainWindow):
        Pykemon_MainWindow.setObjectName("Pykemon_MainWindow")
        Pykemon_MainWindow.resize(640, 640)
        Pykemon_MainWindow.setMinimumSize(QtCore.QSize(640, 640))
        Pykemon_MainWindow.setMaximumSize(QtCore.QSize(640, 640))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logos/py_symbol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Pykemon_MainWindow.setWindowIcon(icon)
        Pykemon_MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        Pykemon_MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(Pykemon_MainWindow)
        self.centralwidget.setEnabled(False)
        self.centralwidget.setObjectName("centralwidget")
        self.MainMenu = QtWidgets.QWidget(self.centralwidget)
        self.MainMenu.setGeometry(QtCore.QRect(0, 0, 640, 640))
        self.MainMenu.setObjectName("MainMenu")
        self.MainMenu_Logo = QtWidgets.QLabel(self.MainMenu)
        self.MainMenu_Logo.setGeometry(QtCore.QRect(0, 150, 640, 211))
        self.MainMenu_Logo.setObjectName("MainMenu_Logo")
        self.MainMenu_ClickToStart = QtWidgets.QLabel(self.MainMenu)
        self.MainMenu_ClickToStart.setGeometry(QtCore.QRect(0, 350, 640, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.MainMenu_ClickToStart.setFont(font)
        self.MainMenu_ClickToStart.setObjectName("MainMenu_ClickToStart")
        self.MainMenu_PushButton = QtWidgets.QPushButton(self.MainMenu)
        self.MainMenu_PushButton.setEnabled(False)
        self.MainMenu_PushButton.setGeometry(QtCore.QRect(0, -20, 640, 640))
        self.MainMenu_PushButton.setStyleSheet("color: rgba(255, 255, 255, 0);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.MainMenu_PushButton.setObjectName("MainMenu_PushButton")
        self.carte = QtWidgets.QWidget(self.MainMenu)
        self.carte.setGeometry(QtCore.QRect(-20, -60, 641, 671))
        self.carte.setObjectName("carte")
        self.label = QtWidgets.QLabel(self.carte)
        self.label.setGeometry(QtCore.QRect(20, 30, 641, 641))
        self.label.setObjectName("label")
        self.MainMenu_ClickToStart.raise_()
        self.MainMenu_Logo.raise_()
        self.MainMenu_PushButton.raise_()
        self.carte.raise_()
        Pykemon_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Pykemon_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        Pykemon_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Pykemon_MainWindow)
        self.statusbar.setObjectName("statusbar")
        Pykemon_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(Pykemon_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Pykemon_MainWindow)

    def retranslateUi(self, Pykemon_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Pykemon_MainWindow.setWindowTitle(_translate("Pykemon_MainWindow", "Pykémon : Attrapy-les tous !"))
        self.MainMenu_Logo.setText(_translate("Pykemon_MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/logos/main_logo.png\"/></p></body></html>"))
        self.MainMenu_ClickToStart.setText(_translate("Pykemon_MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#386abb;\">CLICK ON THE WINDOW TO START</span></p></body></html>"))
        self.MainMenu_PushButton.setText(_translate("Pykemon_MainWindow", "PushButton"))
        self.label.setText(_translate("Pykemon_MainWindow", "<html><head/><body><p><img src=\":/maps/game.png\"/></p></body></html>"))
        
    def change_screen(self):
        self.carte.setVisible(True)
        self.MainMenu.setVisible(False)


import gui_resources

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pykemon_MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Pykemon_MainWindow()
    ui.setupUi(Pykemon_MainWindow)
    ui.carte.setVisible(False)
    ui.MainMenu_PushButton.clicked.connect(ui.change_screen)
    
    Pykemon_MainWindow.show()
    app.exec()

