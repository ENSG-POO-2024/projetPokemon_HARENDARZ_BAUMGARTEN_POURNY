# Game launcher

from main_gui import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
import sys

app = QtWidgets.QApplication(sys.argv)
Pyk_MainWindow = MainWindow(app)

# Execution
Pyk_MainWindow.show()
app.exec_()


