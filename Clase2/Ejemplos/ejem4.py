# -*- coding: utf-8 -*-
"""
 

@author: Francixco
"""
#%%
#leer archivos
# Primero ,abrimos el fichero a leer
 
archivo = open('prueba.txt', 'r')#r para leer archivo
# Mostramos por pantalla lo que leemos desde el archivo
print('Leido')
print(archivo.read())
# Cerramos el fichero.
archivo.close()


#%%Leer cantidad limitada de informacion
 
#Abrimos el archivo
archivo = open('prueba.txt', 'r')
# Mostramos por pantalla lo que leemos desde el archivo
print("Lectura limitada")
print(archivo.read(38) + '\n')
archivo.close()# Cerramos el archivo.

#%%
 
archivo = open('prueba.txt', 'r')
 
 #leemos una linea de codigo
print(archivo.readline())
 
archivo.close()

#%%Imprimir todas la lineas
i=1 
#abrimos el archivo
archivo = open('prueba.txt', 'r')

#Bucle for para leer las lineas 
for linea in archivo:
    print(linea)
    print i
    i=i+1
 
archivo.close()

#%%Ahora si!!!,Sobreescritura 
 # cambiamos el parametro 'r' por 'w'
archivo = open('prueba1.txt', 'w')
archivo.write("Python es una muy buena herramienta.\n")
archivo.close()
# Listo, ahora lo leemos
archivo = open('prueba1.txt', 'r')
print(archivo.read())
# Cerramos el archivo
archivo.close()

#%% Agregar 
#ponemos "a"
archivo = open('prueba2.txt', 'a')  
archivo.write("Python es una muy buena herramienta+2.\n")
archivo.close()
# Verificamos si el archivo se grabo
archivo = open('prueba2.txt', 'r')
 
print(archivo.read())
# Cerramos el archivo.
archivo.close()



