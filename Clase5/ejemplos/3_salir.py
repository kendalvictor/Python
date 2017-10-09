# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\salir.ui'
#
# Created: Fri Sep 22 02:29:48 2017
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
        Form.resize(400, 300)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(115, 130, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Salir", None))


"""
#lanzador 1 
import sys
class Plantilla(QtGui.QWidget,Ui_Form):
    def __init__(self):
        super(Plantilla,self).__init__()
        self.setupUi(self)
"""        
    

 
#Lanzador 2
import sys

class Plantilla(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        
        self.tiempo=QtCore.QTimer() 
        self.tiempo.timeout.connect(self.contar)
        self.tiempo.start(500)
    
        
if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=Plantilla()
        
    myapp.show()
       
    sys.exit(app.exec_())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    