# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pykemon(object):
    def setupUi(self, Pykemon):
        Pykemon.setObjectName("Pykemon")
        Pykemon.setEnabled(True)
        Pykemon.resize(480, 436)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Pykemon.sizePolicy().hasHeightForWidth())
        Pykemon.setSizePolicy(sizePolicy)
        Pykemon.setMinimumSize(QtCore.QSize(480, 436))
        Pykemon.setMaximumSize(QtCore.QSize(2880, 2616))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logos/py_symbol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Pykemon.setWindowIcon(icon)
        Pykemon.setWindowOpacity(1.0)
        Pykemon.setAutoFillBackground(False)
        Pykemon.setStyleSheet("background-color: rgb(37, 70, 124);")
        Pykemon.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(Pykemon)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        Pykemon.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Pykemon)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 26))
        self.menubar.setObjectName("menubar")
        Pykemon.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Pykemon)
        self.statusbar.setObjectName("statusbar")
        Pykemon.setStatusBar(self.statusbar)

        self.retranslateUi(Pykemon)
        QtCore.QMetaObject.connectSlotsByName(Pykemon)

    def retranslateUi(self, Pykemon):
        _translate = QtCore.QCoreApplication.translate
        Pykemon.setWindowTitle(_translate("Pykemon", "Pykémon : Attrapy-les tous !"))
        self.label.setText(_translate("Pykemon", "<html><head/><body><p><img src=\":/logos/main_logo.png\"/>111</p></body></html>"))
        self.label_2.setText(_translate("Pykemon", "TextLabel"))
import gui_resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pykemon = QtWidgets.QMainWindow()
    ui = Ui_Pykemon()
    ui.setupUi(Pykemon)
    Pykemon.show()
    sys.exit(app.exec_())