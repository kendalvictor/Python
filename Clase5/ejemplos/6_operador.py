# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\contador.ui'
#
# Created: Fri Sep 22 04:41:34 2017
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
        Form.resize(751, 549)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(645, 495, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(65, 30, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(220, 45, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(495, 205, 171, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_1 = QtGui.QLineEdit(Form)
        self.lineEdit_1.setGeometry(QtCore.QRect(85, 170, 171, 20))
        self.lineEdit_1.setObjectName(_fromUtf8("lineEdit_1"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(85, 230, 171, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(325, 190, 69, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(325, 165, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 265, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(495, 175, 61, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 130, 101, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Salir", None))
        self.pushButton_2.setText(_translate("Form", "Contar", None))
        self.label.setText(_translate("Form", " ", None))
        self.label_2.setText(_translate("Form", "Operador", None))
        self.pushButton_3.setText(_translate("Form", "Operar", None))
        self.label_3.setText(_translate("Form", "Resultado", None))
        self.label_4.setText(_translate("Form", "Ingrese Numero", None))


import sys

class Plantilla(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.data=["+", "-", "*", "/"]
        self.ui.comboBox.addItems(self.data)
        #self.ui.comboBox.activated.connect(self.mostrar)
        self.ui.pushButton_3.clicked.connect(self.operar)
        self.ui.pushButton.clicked.connect(self.cerrar)
    def mostrar(self):
        print self.ui.comboBox.currentText()
    
    def contar(self):
        pass
    def operar(self):
        a=str(self.ui.lineEdit_1.text()) #obtenemos el texto
        b=str(self.ui.lineEdit_2.text())
        op=str(self.ui.comboBox.currentText())
        self.ui.lineEdit_3.setText(str(eval(a+op+b)))
    def cerrar(self):
        self.close()
        
if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=Plantilla()
        
    myapp.show()
       
    sys.exit(app.exec_())
    
    
    
