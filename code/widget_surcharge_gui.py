# Widget surcharge

from PyQt5.QtWidgets import  QWidget, QGraphicsOpacityEffect
from PyQt5.QtCore import QEventLoop, QPropertyAnimation, QRect, QSize, Qt
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QAction,  QGraphicsOpacityEffect, QWidget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # quit_action = QAction(self.tr("E&xit"), self)
        # quit_action.setShortcut(self.tr("Ctrl+Q"))
        # quit_action.triggered.connect(self.close)
        # self.addAction(quit_action)

        self.effect = QGraphicsOpacityEffect(self, opacity=1.0)
        self.setGraphicsEffect(self.effect)
        self._animation = QPropertyAnimation(
            self,
            propertyName=b"opacity",
            targetObject=self.effect,
            duration=500,
            startValue=0.0,
            endValue=1.0,
        )

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

class Widget2(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setAutoFillBackground(True)

    def centerWidget(self, s_width, s_height):
        width, height = self.width(), self.height()
        new_x = int((s_width-width)/2)
        new_y = int((s_height-height)/2)
        self.setGeometry(QRect(new_x, new_y, width, height))

    def widgetHide(self):
        self.setEnabled(False)
        self.setVisible(False)

    def widgetShow(self):
        self.setEnabled(True)
        self.setVisible(True)
        
        