# -*- coding: utf-8 -*-
 
"""
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)#Inicializamos la aplicacion

ventana = QtGui.QWidget()#generamos la ventana

layout=QtGui.QHBoxLayout()
boton = QtGui.QPushButton(ventana)
boton1 = QtGui.QPushButton(ventana)
layout.addWidget(boton)
layout.addWidget(boton1)
ventana.setLayout(layout)
boton.setText("Presiona")
boton1.setText("Salir")
ventana.show() #mostramos la ventana,con los componentes agregados en ella
sys.exit(app.exec_())  #mantiene abierta la ventana hasta que se cierra
#Enters the main event loop and waits until exit() is called, 


""" 

from PyQt4 import QtCore, QtGui
import sys



class Ventana(QtGui.QWidget):
    def __init__(self):
        super(Ventana,self).__init__()
        self.setWindowTitle("Hola mundo")
        self.boton=QtGui.QPushButton(self)
        self.boton.setText("HOla")





app = QtGui.QApplication(sys.argv)#Inicializamos la aplicacion

ventana =Ventana()#generamos la ventana

 
ventana.show() #mostramos la ventana,con los componentes agregados en ella
sys.exit(app.exec_())  #mantiene abierta la ventana hasta que se cierra
#Enters the main event loop and waits until exit() is called, 

