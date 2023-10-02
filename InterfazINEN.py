# -*- coding: latin-1 -*-
import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QMainWindow, QVBoxLayout, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation,QEasingCurve
from PyQt5.QtGui import QColor
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot

class rooti(QMainWindow):
    def __init__(self):
        super(rooti,self).__init__()
        loadUi('D:/ESPE/Practicas INEN/InterfazINEN/interfazinen.ui',self)
        #oculatar boton normal
        self.bt_normal.hide()
         #eliminar la ventana del main
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        #SizeGrip
        self.gripSize=10
        self.grip=QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize,self.gripSize)
        #botones barra de titulo
        self.bt_maximizar.clicked.connect(self.maximizar)
        self.bt_normal.clicked.connect(self.normal)
        self.bt_minimizar.clicked.connect(self.minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())
        #botones de detalles
        self.bt_tem1.clicked.connect(self.detalletem1)
        self.bt_tem2.clicked.connect(self.detalletem2)
        self.bt_humedad.clicked.connect(self.detallehume)
        self.bt_presion.clicked.connect(self.detallepresi)

    #======================FUNCIONES=========
    def minimizar(self):
        self.showMinimized()
    def normal(self):
        self.showNormal()
        self.bt_normal.hide()
        self.bt_maximizar.show()
    def maximizar(self): 
        self.showMaximized()
        self.bt_normal.show()
        self.bt_maximizar.hide()
    def mousePressEvent(self,event):
        self.click_position=event.globalPos()
    #===========Fuenciones detalles====
    def detalletem1(self):
         QMessageBox.warning(self, 'Advertencia', 'No se seleccionó ningún archivo.')
    def detalletem2(self):
         QMessageBox.warning(self, 'Advertencia', 'No se seleccionó ningún archivo.')
    def detallehume(self):
         QMessageBox.warning(self, 'Advertencia', 'No se seleccionó ningún archivo.')
    def detallepresi(self):
         QMessageBox.warning(self, 'Advertencia', 'No se seleccionó ningún archivo.')
        
        
        
          

        
if __name__=="__main__":
    app=QApplication(sys.argv)
    mi_app=rooti()
    mi_app.show()
    sys.exit(app.exec_())