# -*- coding: utf-8 -*-
"""
Created on Fri Dec 09 22:14:05 2016

@author: Francixco
"""

#%%Numero primo
#Saber si un numero es par
def par(num):
    if num<=1:
        return 0 
    if num%2!=0:
        num=num-1
    print  num
    par(num-2)            
    return num
 
num=input("Ingrese numero: ")
par(num)
#%%
def invertir(  texto):
    if len(texto)==1:
        print texto.pop()
        print"\n"
        return
     
    print texto.pop(),
    #print len(texto)
    
    invertir(texto)
     
    return texto
    


 
t1=list(raw_input("Ingrese texto: "))
print len(t1) 
invertir(t1)


#%%



