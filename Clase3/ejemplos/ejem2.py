# -*- coding: utf-8 -*-
"""
 

@author: Francisco
"""
#%%
#definimos funciones

def mostrar(c,*a):
    print c
    print a
    
mostrar(1,2,3,4 )    



#%%
def serie(tabla=[],sentido="normal"):
    tabla.sort()
    if sentido=="reverso":
        tabla.reverse()
    print tabla

serie([1,5,4,8,6,3],"reverso")        




#%%
def cuadrado(a,*arg):
    cont=list()
    print arg
    for i in arg:
        cont.append(i**2)
    print a    
    return cont
    
data= range(50)
print cuadrado("Hola",data)        




#%%


def arbitrarios(parametro_fijo, *args, **kwords): 
    print parametro_fijo 
    for i in args: 
        print i 
 
    #** parametros arbitaratios,tipo diccionarios
    for clave in kwords: 
        print "El valor de", clave, "es", kwords[clave]
 
arbitrarios("Hola", "args 1", "args 2", "args 3"
, clave1="valor uno", clave2="valor dos")




#%%


def operacion(a, b): 
    print a
    print b
    return a - (a * b / 100) 
 
datos = {"b": 30, "a": 200} 
print operacion(**datos)


#%%% Polimorfismo:usar distintos tipos de datos e n una interfaz comun
def repetidos(data):
    
   
    rept = {}
 
    for i in data:
        rept[i] = rept.get(i, 0) + 1
    return rept
data=["hola","hola","mundo"]    
print repetidos(data)
