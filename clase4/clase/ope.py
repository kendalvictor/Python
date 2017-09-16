# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 18:28:13 2016

@author: Josue
"""
import texto
class Ope(object):#Heredamos la clase primaria de python
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print "Operacion"
    def suma(self):
        print self.num1+self.num2
        
    def multi(self):
        print self.num1*self.num2
        
if __name__=="__main__":
    texto=texto.saludo()