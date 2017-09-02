# -*- coding: utf-8 -*-
"""
 

@author: Francixco
"""

a,b,c ="hola" ,2 , 0.2
print a,b,c

def fun():
    print "Ingrese los parametros de la ecuacion "

def variables():
    x=input("Ingrese valor de a: ")
    y=input("Ingrese valor de b: ")
    z=input("Ingrese valor de c: ")
    return x,y,z

def delta(a,b,c):
    return b**2-4*a*c
def resultado(v_delta):
    if(v_delta>=0):
        x1=(-b+(v_delta)**0.5)/(2*a)
        x2=(-b-(v_delta)**0.5)/(2*a)
        print "La soluciones son x1=%.2f y x2=%.2f "%(x1,x2)  
    else:
        print "La solucion es compleja " 
        
def vacio():
    pass

def salida():
    print"Fin"

##INICIO
fun()
a,b,c=variables()
result=delta(a,b,c)    
resultado(result)    
salida()
