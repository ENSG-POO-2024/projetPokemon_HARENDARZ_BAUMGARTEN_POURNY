# Widget surcharge

from PyQt5.QtWidgets import  QWidget, QGraphicsOpacityEffect
from PyQt5.QtCore import QEventLoop, QPropertyAnimation, QRect, QSize, Qt
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QAction,  QGraphicsOpacityEffect, QWidget

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        # self.resize(QSize(300, 300))
        # # self.setWindowOpacity(1)
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setContextMenuPolicy(Qt.ActionsContextMenu)

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

    # def paintEvent(self, event):
    #     qp = QPainter(self)
    #     qp.setRenderHint(QPainter.Antialiasing, True)
    #     qp.setBrush(QColor().fromRgb(2, 106, 194))
    #     qp.setPen(QColor().fromRgb(2, 106, 194))
    #     qp.drawRoundedRect(QRect(0, 0, 300, 300), 16, 8)

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