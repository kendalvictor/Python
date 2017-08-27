# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 17:38:27 2017

@author: Labotec
"""

estado=True

print 2>3 

print 2==5 #2 es igual a 5? 

print True and False #and si los 2 son verdaderos result  V

print 2<3 or 4==5 #or si los 2 son Falsos resul F 


a,b,c=input("Ingrese valor a,b,c: ")

print a<b," ", b==c, " ",a>c

#%%
a,b=input("ingrese numero a,b:")

if a<b:  #estructura del if
    print "a es menor"
    print "a sigue siendo menor "
else:
    print "b es mayor"
    print "b todavia no termina"
print "termino"    

