# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 16:52:09 2016

@author: Josue
"""
#Importar archivos py nos permite,emplear o reutilizar
#las posibles funciones o clases
import texto
import saludo
import primo
#Instanciamos del modulo texto la clase saludo
juan=texto.saludo()
 
#condicion que nos permite ejecutar instrucciones
#siempre que inicialicemos el mismo archivo
#No funciona cuando es importado por otro archivo.py  
if __name__=="__main__":
    print "yo"

 