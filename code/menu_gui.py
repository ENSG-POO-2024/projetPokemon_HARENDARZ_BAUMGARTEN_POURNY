# Menu gui

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from widget_surcharge_gui import Widget, Widget2

###################
##  Menu button  ##
###################

class Ui_LateralMenuButton(QtWidgets.QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(40, 40, 70, 70))
        self.setMaximumSize(70, 70)
        self.setStyleSheet("color: rgba(255, 255, 255, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Hamburger_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(70, 70))



####################
##  Options Menu  ##
####################

class optionsMenu(Widget2):
    def __init__(self, parent):
        super().__init__(parent)
        # self.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(203, 159, 1, 255), stop:1 rgba(255, 204, 3, 255));")
        self.setStyleSheet("background-color: rgba(0, 255, 255, 255);")
        self.setGeometry(QtCore.QRect(100, 100, 400, 340))
        self.setAutoFillBackground(True)

        self.volumeHorizontalSlider = QtWidgets.QSlider(self)
        self.volumeHorizontalSlider.setGeometry(QtCore.QRect(150, 50, 191, 22))
        self.volumeHorizontalSlider.setSliderPosition(50)
        self.volumeHorizontalSlider.setTracking(True)
        self.volumeHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeHorizontalSlider.setObjectName("volumeHorizontalSlider")

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily('Retro Gaming')

        self.hide()

        self.labelVolume = QtWidgets.QLabel(self)
        self.labelVolume.setGeometry(QtCore.QRect(50, 50, 81, 21))
        self.labelVolume.setFont(font)
        self.labelVolume.setStyleSheet("background-color: rgb(56, 106, 187); color: rgb(255, 255, 255);")
        self.labelVolume.setAlignment(QtCore.Qt.AlignCenter)
        self.labelVolume.setObjectName("labelVolume")

        self.saveButton = QtWidgets.QPushButton(self)
        self.saveButton.setGeometry(QtCore.QRect(50, 110, 291, 41))
        self.saveButton.setFont(font)
        self.saveButton.setStyleSheet("background-color: rgb(56, 106, 187);")
        self.saveButton.setObjectName("saveButton")

        self.loadButton = QtWidgets.QPushButton(self)
        self.loadButton.setGeometry(QtCore.QRect(50, 160, 291, 41))
        self.loadButton.setFont(font)
        self.loadButton.setStyleSheet("background-color: rgb(56, 106, 187);")
        self.loadButton.setObjectName("loadButton")

        self.commandsButton = QtWidgets.QPushButton(self)
        self.commandsButton.setGeometry(QtCore.QRect(50, 210, 291, 41))
        self.commandsButton.setFont(font)
        self.commandsButton.setStyleSheet("background-color: rgb(56, 106, 187);")
        self.commandsButton.setObjectName("commandsButton")

        self.closeButton = QtWidgets.QPushButton(self)
        self.closeButton.setGeometry(QtCore.QRect(50, 260, 291, 41))
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("background-color: rgb(56, 106, 187);")
        self.closeButton.setObjectName("closeButton")

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Form"))
        self.labelVolume.setText(_translate("self", "Volume"))
        self.saveButton.setText(_translate("self", "SAVE GAME"))
        self.loadButton.setText(_translate("self", "LOAD GAME"))
        self.commandsButton.setText(_translate("self", "COMMANDS"))
        self.closeButton.setText(_translate("self", "EXIT TO DESKTOP"))

    def show(self):
        self.setVisible(True)
        self.setEnabled(True)

    def hide(self):
        self.setVisible(False)
        self.setEnabled(False)

    def test_for_hiding(self):
        if self.isVisible() == True:
            self.hide()
        else:
            self.show()
