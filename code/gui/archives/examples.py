# Examples of mechanisms for other devs

###################################
##  Test from class documents    ##
###################################

# import sys
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QMainWindow, QGridLayout
# from PyQt5.QtWidgets import QWidget
# from PyQt5.QtWidgets import QPushButton, QMessageBox
# from PyQt5.QtCore import QSize

# class BoutonWindow(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)

#         self.setMinimumSize(QSize(300,300))
#         self.setWindowTitle("Exemple 1")

#         centralWidget = QWidget(self)
#         self.setCentralWidget(centralWidget)

#         gridLayout = QGridLayout(self)
#         centralWidget.setLayout(gridLayout)

#         boutonAfficher = QPushButton("Test !")
#         gridLayout.addWidget(boutonAfficher, 0, 0)
#         boutonAfficher.clicked.connect(self.affiche)

#     def affiche(self):
#         print("Ça marche")
#         QMessageBox.information(self, "Info", "Mission réussie !")

# if __name__ == "__main__":
#     def run_app():
#         app = QtWidgets.QApplication(sys.argv)
#         mainWin = BoutonWindow()
#         mainWin.show()
#         app.exec_()
#     run_app()

######################
##  Real version    ##
######################

from main_window import Ui_Pykemon

