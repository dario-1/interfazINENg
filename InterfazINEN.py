# -*- coding: latin-1 -*-
import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QMainWindow, QVBoxLayout, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation,QEasingCurve
from PyQt5.QtGui import QColor
import numpy as np
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as figure
import matplotlib.pyplot as plt



class rooti(QMainWindow):
    def __init__(self):
        super(rooti,self).__init__()
        loadUi('D:/ESPE/Practicas INEN/InterfazINEN/interfazinen2.ui',self)
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
        #condiciones iniciales del combobox seleccion_lab
        self.seleccion_lab.model().item(0).setEnabled(False)
        #====gráficas=====
        self.init_graph()  
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
     #====funcion de las gráficas=====
    def init_graph(self):
        self.grafica1 = Canvas_tempe1('temperatura')
        self.tempe1.addWidget(self.grafica1)
        self.grafica2 = Canvas_tempe2('temperatura 2')
        self.temp2.addWidget(self.grafica2)
        self.grafica3=Canvas_hume1('humedad')
        self.humedad2.addWidget(self.grafica3)
        self.grafica4=Canvas_presion2('presion')
        self.presion2.addWidget(self.grafica4)
#========Clasese graficas====
class Canvas_tempe1(figure):
        def __init__(self,temperatura,parent=None):
            self.fig,self.ax=plt.subplots(1,dpi=100,figsize=(5,5),
                sharey=True,facecolor='White')
            super().__init__(self.fig)
            self.ax.grid()
            self.ax.margins(x=0)
            self.nivel1 = 10
            self.nivel2 = 1
            self.grafica_datos()
        def grafica_datos(self):
             plt.title("Temperatura en °C", fontsize=8)
             plt.grid(True, color='blue')
             # Configurar el tamaño de fuente en los ejes (por ejemplo, 10 puntos)
             plt.xticks(fontsize=6)
             plt.yticks(fontsize=6)
             x = np.arange(-np.pi, 10*np.pi, 0.01) 
             line, = self.ax.plot(x, self.nivel1*np.sin(self.nivel2*x), color='black',linewidth=0.5)
             self.draw()     
             line.set_ydata(np.sin(x)+24)
             QtCore.QTimer.singleShot(10, self.grafica_datos)

class Canvas_tempe2(figure):
        def __init__(self,temperatura,parent=None):
            self.fig,self.ax=plt.subplots(1,dpi=100,figsize=(5,5),
                sharey=True,facecolor='White')
            super().__init__(self.fig)
            self.ax.grid()
            self.ax.margins(x=0)
            self.nivel1 = 10
            self.nivel2 = 1
            self.grafica_datos()
        def grafica_datos(self):
             plt.title("Temperatura 2 en °C", fontsize=8)
             plt.grid(True, color='blue')
             # Configurar el tamaño de fuente en los ejes (por ejemplo, 10 puntos)
             plt.xticks(fontsize=6)
             plt.yticks(fontsize=6)
             x = np.arange(-np.pi, 10*np.pi, 0.01) 
             line, = self.ax.plot(x, self.nivel1*np.sin(self.nivel2*x), color='black',linewidth=0.5)
             self.draw()     
             line.set_ydata(np.sin(x)+24)
             QtCore.QTimer.singleShot(10, self.grafica_datos)

class Canvas_hume1(figure):
        def __init__(self,humedad,parent=None):
            self.fig,self.ax=plt.subplots(1,dpi=100,figsize=(5,5),
                sharey=True,facecolor='White')
            super().__init__(self.fig)
            self.ax.grid()
            self.ax.margins(x=0)
            self.nivel1 = 10
            self.nivel2 = 1
            self.grafica_datos()
        def grafica_datos(self):
             plt.title("Humedad en %HR", fontsize=8)
             plt.grid(True, color='blue')
             # Configurar el tamaño de fuente en los ejes (por ejemplo, 10 puntos)
             plt.xticks(fontsize=6)
             plt.yticks(fontsize=6)
             x = np.arange(-np.pi, 10*np.pi, 0.01) 
             line, = self.ax.plot(x, self.nivel1*np.sin(self.nivel2*x), color='black',linewidth=0.5)
             self.draw()     
             line.set_ydata(np.sin(x)+24)
             QtCore.QTimer.singleShot(10, self.grafica_datos)

class Canvas_presion2(figure):
        def __init__(self,temperatura,parent=None):
            self.fig,self.ax=plt.subplots(1,dpi=100,figsize=(5,5),
                sharey=True,facecolor='White')
            super().__init__(self.fig)
            self.ax.grid()
            self.ax.margins(x=0)
            self.nivel1 = 10
            self.nivel2 = 1
            self.grafica_datos()
        def grafica_datos(self):
             plt.title("Presión en kPa", fontsize=8)
             plt.grid(True, color='blue')
             # Configurar el tamaño de fuente en los ejes (por ejemplo, 10 puntos)
             plt.xticks(fontsize=6)
             plt.yticks(fontsize=6)
             x = np.arange(-np.pi, 10*np.pi, 0.01) 
             line, = self.ax.plot(x, self.nivel1*np.sin(self.nivel2*x), color='black',linewidth=0.5)
             self.draw()     
             line.set_ydata(np.sin(x)+24)
             QtCore.QTimer.singleShot(10, self.grafica_datos)
            
        
          

        
if __name__=="__main__":
    app=QApplication(sys.argv)
    mi_app=rooti()
    mi_app.show()
    sys.exit(app.exec_())