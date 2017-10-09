# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\plot_leer.ui'
#
# Created: Fri Sep 22 05:13:10 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(747, 537)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 30, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(530, 140, 71, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.mplwidget = MatplotlibWidget(Form)
        self.mplwidget.setGeometry(QtCore.QRect(30, 110, 441, 291))
        self.mplwidget.setObjectName(_fromUtf8("mplwidget"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(620, 140, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(480, 140, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 170, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 470, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(530, 170, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "TextLabel", None))
        self.pushButton.setText(_translate("Form", "Abrir Puerto", None))
        self.label_2.setText(_translate("Form", "Puertos", None))
        self.pushButton_2.setText(_translate("Form", "Cerrar Puerto", None))
        self.pushButton_3.setText(_translate("Form", "Salir", None))
        self.pushButton_4.setText(_translate("Form", "Actualizar", None))

from matplotlibwidget import MatplotlibWidget
"""
import sys

class Plantilla(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
              
        
if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=Plantilla()
        
    myapp.show()
       
    sys.exit(app.exec_())
"""    
import sys  
 
from PyQt4.QtCore import QTimer,SIGNAL,QObject
from PyQt4.QtGui import QPixmap
import time
import threading 
import serial
class paralel(threading.Thread):
    def __init__(self,estado):
        threading.Thread.__init__(self)
        self.puerto=" "
        self.estado=estado
    def run(self): #run es el metodo que funciona con start
        pass 
        
def  acel(data):
          
        data=data[1:4]
        salida=[round(float(i)*2*9.81/16384,2)  for i in data ]
       
        return salida
            
      
 
def buscar_puertos():
    salida=[]
    for i in range(50):
        try:
            com = serial.Serial("COM"+str(i),9600)
            salida.append("COM"+str(i))
            com.close()
        except serial.SerialException:
            pass
    del com    
    return salida      
    
class Formulario(QtGui.QWidget ):
    def __init__(self,parent=None):    
         
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Form()
         
         
        self.ui.setupUi(self)
        self.data=[0,0,0,0,0,0]
        self.show()
        self.inc=0  #incrementadors
        self.data_base_ploteo=[]
        self.plotx=[]
        self.ploty=[]
        self.plotz=[]
        self.tiempo=QtCore.QTimer()
        self.estado=True #True Acelerometro  
        self.ui.pushButton.clicked.connect(self.abrir)
        self.ui.pushButton_3.clicked.connect(self.salir)   
        self.ui.pushButton_4.clicked.connect(self.refresh) 
        self.ui.pushButton_2.clicked.connect(self.cerrar) 
         
         
        print "lo hizo gGWP"
        
        #solucion presente para evitar timer es grabar el dato en un labol no visible y hacer evento de cambio de texto :)
        QObject.connect(self.tiempo,SIGNAL("timeout()"),self.adquirir_senal)
        #QObject.connect(self.valor,SIGNAL("valueChanged()"),self.ploteo) 
    def adquirir_senal(self):
        print "entor"
        self.con.write('x')#enviamos
        print "enviado"
        self.data = self.con.readline()
        self.data = self.data.split()
       
  
        self.ploteo()
       
        
    def abrir(self):
        #self.serial.port(self.ui.comboBox.currentText())
        self.con=serial.Serial(str(self.ui.comboBox.currentText()),9600)
        self.con.timeout = 2
        time.sleep(1.8)
        print "Puerto Abierto"
        self.ui.pushButton_2.setEnabled(True)
        
        self.tiempo.start(350)  
        print "conectado"
        
    def cerrar(self): 
        self.con.close()
        print "cerrado"
        self.tiempo.stop()
        
     

        
   
    def salir(self):
        self.close()
    def hola(self)  :
        print "hola1"

           
    def ploteo(self):
        
        a=acel(self.data)
        print a
        self.data_base_ploteo.append(self.inc)
        self.plotx.append(a[0])
        self.ploty.append(a[1])
        self.plotz.append(a[2])
         
         
        #self.ui.mplwidget.axes.plot(self.data_base_ploteo,a[0],'r-',self.data_base_ploteo,a[1],'g-',self.data_base_ploteo,a[2],'b-') 
        self.ui.mplwidget.axes.plot(self.data_base_ploteo,self.plotx,'r-',self.data_base_ploteo,self.ploty,'g-',self.data_base_ploteo,self.plotz,'b-') 
        self.inc+=1
        self.ui.mplwidget.draw()        
        
        
    
    def refresh(self):
        #cargar puertos serie con try y catch :)
        
        self.ui.comboBox.clear()
       
        self.ui.comboBox.addItems(buscar_puertos())   
        
        
if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=Formulario()
     
    sys.exit(app.exec_())    
 