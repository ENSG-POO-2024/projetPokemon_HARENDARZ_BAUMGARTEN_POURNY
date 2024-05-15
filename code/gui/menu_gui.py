# Menu gui

from PyQt5 import QtCore, QtGui, QtWidgets
from widget_surcharge_gui import Widget

###################
##  Menu button  ##
###################

class Ui_LateralMenuButton(QtWidgets.QPushButton):
    def __init__(self, parent):
        super().__init__()
        self.setGeometry(QtCore.QRect(40, 40, 70, 70))
        self.setMaximumSize(70, 70)
        self.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Hamburger_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(70, 70))

        QtCore.QMetaObject.connectSlotsByName(parent)


############
##  Menu  ##
############

class optionsMenu(Widget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(0, 0, 70, 70))
