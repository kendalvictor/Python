# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)#Inicializamos la aplicacion

ventana = QtGui.QWidget()#generamos la ventana
ventana.show() #mostramos la ventana,con los componentes agregados en ella

sys.exit(app.exec_())  #mantiene abierta la ventana hasta que se cierra
#Enters the main event loop and waits until exit() is called, 
 
 
""" 
from PyQt4 import QtCore, QtGui
import sys

class MiVentana(QtGui.QWidget): #qtwidget hereda  la clase mi ventana,
    def __init__(self, padre = None):
        super(MiVentana, self).__init__(padre)
        self.button = QtGui.QPushButton("Hola",self)
        self.connect(self.button, QtCore.SIGNAL("clicked()"), self.say_hello)
        self.show()
    def say_hello(self,**kwargs):
        print "hola mundo!"

app = QtGui.QApplication(sys.argv)
v = MiVentana()
app.exec_()
"""