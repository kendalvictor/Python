# -*- coding: utf-8 -*-
"""
Created on Sat Sep 02 17:20:45 2017

@author: labotec
"""
"""
Las propiedades son exclusivos del class lista
estructura:
nombre_de_lista.(funciona ejecutar)(arg)
"""

#%%
#for variable in (lista) :
    #sentencia
for x in [1,2,1,4,"hola","dos"]:
    print 4
#%%
sal=1    
for x in range(1,input()+1):
    sal=sal*x
print sal

#%%
for i in range(5):
    print i**2

#%%
contener=[]
for i in range(1,4):
    contener.append( i**2)
print contener

#%%
contener=[x**2 for x in range(5)]
print contener

#%%
[x for x in range(10) if x>5]
print x