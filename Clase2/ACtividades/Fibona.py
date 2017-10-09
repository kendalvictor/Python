# -*- coding: utf-8 -*-
"""
 

@author: Francixco
"""

#serie de Fibonacci
print "Mi primer reto"
n=input("Ingrese cantidad de terminos a mostrar: ")
i=1
num_ant=0
num_act=1
print num_ant
print num_act
while i<=n:
   
   
    temp=num_act
    num_act=num_act+num_ant
    num_ant=temp
    print num_act
    i+=1
print "El valor es :",num_act
    
    
    
    #0 1 1 2 3 5
