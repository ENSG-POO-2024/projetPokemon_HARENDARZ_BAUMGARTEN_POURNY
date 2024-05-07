# -*- coding: utf-8 -*-

from pyproj import Transformer
import sys

from addCRS import Ui_Dialog
from TransformWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.uic import loadUi


class TransformWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(TransformWindow, self).__init__(parent)
        self.setupUi(self)
        
        # Rendre non modifiable
        self.xField.setEnabled(False)
        self.yField.setEnabled(False)
        
        self.listInputCrs.setEnabled(True)
        self.listInputCrs.addItem("EPSG:4326 WGS 84")
        
        self.xField.setStyleSheet("color: red;")
        self.yField.setStyleSheet("color: red;")
            
        # Ajouter les actions sur le bouton 
        self.listeCRS.addItem("EPSG:3857 WGS 84 / Pseudo-Merself.transformBouton.clicked.connect(self.transforme)cator")
        self.listeCRS.addItem("EPSG:2154 RGF93 v1 / Lambert-93")
        self.listeCRS.addItem("EPSG:3387 KKJ / Finland zone 5")

        self.transformBouton.clicked.connect(self.transforme)
        self.addBouton.clicked.connect(self.addCRS)
        
        # 
        self.pasteBouton.clicked.connect(self.copy)
        self.pressPaper = QApplication.clipboard()
    
    def transforme(self):
        
        # On récupère les coordonnées lon et lat
        lon = float(self.lonField.text())
        lat = float(self.latField.text())
        
        # On récupère les systèmes de référence
        crsText = self.listInputCrs.currentText().split(" ")[0][5:]
        destCrsText = self.listeCRS.currentText().split(" ")[0][5:]
        
        proj = Transformer.from_crs(int(crsText), int(destCrsText), always_xy=True)
        (x, y) = proj.transform(lon, lat)
        
        self.xField.setText(str(x))
        self.yField.setText(str(y))
        
    def addCRS(self):
        dlg = CrsDlg(self)
        dlg.exec()
        
    def copy(self):
        x = self.xField.text()
        y = self.yField.text()
        
        self.pressPaper.setText(x + ";" + y)
        
        
class CrsDlg(QDialog):
    
    """CRS dialog."""
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)   
        
    def accept(self):
        crsTxt = self.ui.crs.text()
        self.parent().listeCRS.addItem(crsTxt)
        super().accept()
    
        
if __name__ == "__main__":
    def run_app():
        app = QApplication(sys.argv)
        mainWin = TransformWindow()
        mainWin.show()
        app.exec_()
    run_app()