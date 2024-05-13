# Game launcher

from main_gui import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
import sys

app = QtWidgets.QApplication(sys.argv)
Pyk_MainWindow = MainWindow(app)


# Pyk_MainWindow.blackBackground = QWidget(Pyk_MainWindow.centralwidget)
# Pyk_MainWindow.gridLayout.addWidget(Pyk_MainWindow.blackBackground, 0, 0, 1, 1)
# Pyk_MainWindow.blackBackground.setStyleSheet("background-color: rgb(0, 0, 255);")
# Pyk_MainWindow.blackBackground.setGeometry(QtCore.QRect(0, 0, Pyk_MainWindow.max_width, Pyk_MainWindow.max_height))
# Pyk_MainWindow.blackBackground.setObjectName("blackBackground")
# Pyk_MainWindow.blackBackground.animation = QtCore.QPropertyAnimation(Pyk_MainWindow.blackBackground, b'windowOpacity')
# Pyk_MainWindow.blackBackground.animation.setDuration(4000)
# try:
#     Pyk_MainWindow.blackBackground.animation.finished.disconnect(Pyk_MainWindow.blackBackground.close)
# except:
#     pass
# Pyk_MainWindow.blackBackground.animation.stop()
# Pyk_MainWindow.blackBackground.animation.setStartValue(0)
# Pyk_MainWindow.blackBackground.animation.setEndValue(1)
# Pyk_MainWindow.blackBackground.animation.start()
# Pyk_MainWindow.blackBackground.black_to_visible()

# Execution
Pyk_MainWindow.show()
app.exec_()


