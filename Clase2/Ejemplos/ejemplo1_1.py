# -*- coding: utf-8 -*-
"""
Created on Sat Sep 02 16:46:31 2017

@author: labotec
"""
#%%Propiedades de las listas

num = input("Ingrese numero : ")
salida=[]#genero variable tipo lista
for i in range(1,num+1):
    salida.append(i**2)
print salida    

#%%Contar
texto=["hola"]
texto=texto*6
print texto
num1=[1,1,2,3,3,3,3,4,5]
print num1.count(3)
print texto.count("hola")

#%%extend,unir listas
lista=[1,2,3]
lista1=[6,5,4]
lista.extend(lista1)
print lista


#%%insert() insertamos un elemento
num=range(5)
num.insert(2,90)#num.insert(orden de la lista,valora insertar)
print num

#%%index,busca el valor en la lista y devuelve su orden
num=range(4,23)
print num.index(9)


#%%pop elmina un valor y lo imprime

num=[1,23,5,6,3,15,2,15,15]
num.pop(4)
print num

#%%remove elmiman un valor de la lista(valor)
num=[1,23,5,6,3,15,2,15,15]
num.remove(15)
print num

#%%sort() ordena los elemenots de mayor a menor
num=[4,3,56,9,13,11,1]
print num
num.sort(reverse=True)
print num
#num.sort(reverse=True)


