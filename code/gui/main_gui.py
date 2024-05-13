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


########################
##  Widget surcharge  ##
########################

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(QSize(300, 300))
        # self.setWindowOpacity(1)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setContextMenuPolicy(Qt.ActionsContextMenu)

        quit_action = QAction(self.tr("E&xit"), self)
        quit_action.setShortcut(self.tr("Ctrl+Q"))
        quit_action.triggered.connect(self.close)
        self.addAction(quit_action)

        effect = QGraphicsOpacityEffect(self, opacity=1.0)
        self.setGraphicsEffect(effect)
        self._animation = QPropertyAnimation(
            self,
            propertyName=b"opacity",
            targetObject=effect,
            duration=500,
            startValue=0.0,
            endValue=1.0,
        )

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.Antialiasing, True)
        qp.setBrush(QColor().fromRgb(2, 106, 194))
        qp.setPen(QColor().fromRgb(2, 106, 194))
        qp.drawRoundedRect(QRect(0, 0, 300, 300), 16, 8)

    def fade_in(self):
        self._animation.setDirection(QPropertyAnimation.Forward)
        self._animation.start()

    def fade_out(self):
        loop = QEventLoop()
        self._animation.finished.connect(loop.quit)
        self._animation.setDirection(QPropertyAnimation.Backward)
        self._animation.start()
        loop.exec_()

    def showEvent(self, event):
        super().showEvent(event)
        self.fade_in()

    def closeEvent(self, event):
        # fade out
        self.fade_out()
        super().closeEvent(event)

    def hideEvent(self, event):
        # fade out
        self.fade_out()
        super().hideEvent(event)

###

class MainWidget(Widget):
    def __init__(self, parent=None):
        super().__init__(parent)
        gridLayout = QGridLayout(self)
        self.setLayout(gridLayout)
        boutonAfficher = QPushButton("Test !")

        gridLayout.addWidget(boutonAfficher, 0, 0)
        boutonAfficher.clicked.connect(self.fade_out)
        LateralMenuButton = Ui_LateralMenuButton(self)
        print(type(LateralMenuButton))
        LateralMenuButton.clicked.connect(self.fade_out)
        gridLayout.addWidget(LateralMenuButton, 0, 1)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = MainWidget()
    w.show()

    sys.exit(app.exec_())
    


    



