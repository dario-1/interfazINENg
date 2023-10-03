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
class SubVentana(QtWidgets.QDialog):
    def __init__(self,seleccion_lab):
        super().__init__()
        self.setWindowTitle("Subventana Personalizada")
        loadUi('D:/ESPE/Practicas INEN/InterfazINEN/ventana.ui',self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.frame_top2.mouseMoveEvent=self.mover_ventana
        self.bt_close.clicked.connect(lambda: self.close())
        self.var=seleccion_lab
        self.labinfo.setText(self.var)
        
        
        
    
    def mousePressEvent(self,event):
        self.click_position=event.globalPos()

    def mover_ventana(self,event):
        if self.isMaximized()==False:
            if event.buttons()==QtCore.Qt.LeftButton:
                self.move(self.pos()+event.globalPos()-self.click_position)
                self.click_position=event.globalPos()
                event.accept()
    
    @QtCore.pyqtSlot(str)
    def actualizar_info(self, mensaje):
        self.label_info.setText(mensaje)
        



class rooti(QMainWindow):
    def __init__(self):
        super(rooti,self).__init__()
        loadUi('D:/ESPE/Practicas INEN/InterfazINEN/interfazinen2.ui',self)
        #oculatar boton normal
        self.bt_normal.hide()
        self.frame_top.mouseMoveEvent=self.mover_ventana
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
        #botones buscar, reporte y actualizar
        self.bt_buscar.clicked.connect(self.buscar)
        #self.bt_reporte.clicked.connect()
        #self.bt_actualizar.connect()
        #botones de detalles
        self.bt_tem1.clicked.connect(self.mostrar_subventana)
        self.bt_tem2.clicked.connect(self.mostrar_subventana)
        self.bt_humedad.clicked.connect(self.mostrar_subventana)
        self.bt_presion.clicked.connect(self.mostrar_subventana)
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
    #===========Funciones detalles====
    def mostrar_subventana(self):
        subventana = SubVentana(self.seleccion_lab.currentText())
        subventana.exec_()
    
    #def detalletem1(self):
         #QMessageBox.warning(self, 'Advertencia', 'No se seleccionó ningún archivo.')
    def detalletem2(self):
         QMessageBox.warning(self, 'Advertencia', 'No se seleccionó ningún archivo.')
    def detallehume(self):
         QMessageBox.warning(self, 'Advertencia', 'No se seleccionó ningún archivo.')
    def detallepresi(self):
         QMessageBox.warning(self, 'Advertencia', 'No se seleccionó ningún archivo.')
    #====Funcion  buscar====
    def buscar(self):
        if self.seleccion_lab.currentText()=="Seleccioné una Opción":
            self.nombre_lab.setText("No se ha seleccionado un lab ") 
            QMessageBox.warning(self, 'Advertencia', 'No se seleccionó un laboratorio.')
             
        else: 
            lab_seleccionado = self.seleccion_lab.currentText()
            self.nombre_lab.setText("Laboratorio de "+lab_seleccionado)
            #==variable de la fecha==aquí se captura de la base de datos la fecha:
            fecha="03/10/2023"# cambiar el valor por la variable que se captura del SQL
            self.fecha.setText(fecha)
            #==variable de la hora==aquí se captura de la base de datos la hora:
            hora="15:30"
            self.hora.setText(hora)
        #======Función actualizar y reporte
        def report(self):
            archivo=''#aquí se debería colocar el archivo del reporte
        def actual(self):
            refresh=''
            
     #=========mover ventana====
    def mover_ventana(self,event):
        if self.isMaximized()==False:
            if event.buttons()==QtCore.Qt.LeftButton:
                self.move(self.pos()+event.globalPos()-self.click_position)
                self.click_position=event.globalPos()
                event.accept()
        if event.globalPos().y()<=10:
            self.showMaximized()
            self.bt_maximizar.hide()
            self.bt_normal.show()
        else:
            self.showNormal()
            self.bt_maximizar.show()
            self.bt_normal.hide()
        

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