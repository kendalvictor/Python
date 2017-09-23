# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\contador.ui'
#
# Created: Fri Sep 22 04:15:37 2017
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
        Form.resize(409, 230)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(305, 185, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(75, 40, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(220, 45, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Salir", None))
        self.pushButton_2.setText(_translate("Form", "Contar", None))
        self.label.setText(_translate("Form", " ", None))

import sys


class Lanzador(QtGui.QWidget,Ui_Form):
    def __init__(self,parent=None):
        super(Lanzador,self).__init__() 
        self.setupUi(self)
        self.cont=0
        self.pushButton_2.clicked.connect(self.contar)
        self.pushButton.clicked.connect(self.salir)
        
        
    def contar(self):
        self.cont+=1
        self.label.setText(str(self.cont))
    
    def salir(self):
        self.close()
              


if __name__=="__main__":     
    app=QtGui.QApplication(sys.argv)
    myapp=Lanzador()
    myapp.show()
    sys.exit(app.exec_())