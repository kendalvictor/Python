# -*- coding: utf-8 -*-
"""
 

@author: Francixco
"""
#%%
#%reto
import getpass

#palabra="manzana"
palabra1 = getpass.getpass("Ingrese Palabra: ")
palabra1=range(len(palabra))
 
for i in range(len(palabra)):
     palabra1[i]="_"


 
 
print "Adivine la palabra "
for n in range(10):
    val=raw_input("Ingrese letra : ")
    val=val[0]
    if (val in palabra):
        for m in range(len(palabra)):
            if(palabra[m]==val):
                palabra1[m]=val
        print palabra1
        
    else:
        print palabra1
    if "_"  not in  palabra1:
        print "Usted Gana"
        print "Intento numero : ", n+1
        break
if n==9:
    print "Perdio"
print "Fin"    
    
