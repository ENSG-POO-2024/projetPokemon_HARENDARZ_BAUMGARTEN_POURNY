# Menu gui

from PyQt5 import QtCore, QtGui, QtWidgets

###################
##  Menu button  ##
###################

class Ui_LateralMenuButton(QtWidgets.QPushButton):
    def __init__(self, parent):
        super().__init__()
        self.setGeometry(QtCore.QRect(0, 0, 70, 70))
        self.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Hamburger_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(70, 70))

        QtCore.QMetaObject.connectSlotsByName(parent)