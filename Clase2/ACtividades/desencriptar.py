# -*- coding: utf-8 -*-
"""
 

@author: Francisco
"""

texto = raw_input("Ingrese cadena para ser desencriptada : ")
n     = input("Ingrese el valor de encriptacion  : ") 
 

salida=""
for i in texto:
    #a  z    97  122
    #A  Z   65  90
    #0  9   48  57
    temp=ord(i)
    if temp>=97 and temp<=122:
        valor=temp - 97 -n
        while valor<0:
                valor=valor+26
        salida=salida+chr(97+valor)  
        
        
    if temp>=65 and temp<=90:
        valor=temp - 65 -n
        while valor <0:
            valor=valor+26
        salida=salida+chr(65+valor) 
        
    if temp>=48 and temp<=57:
        valor=temp - 48 -n
        while valor <0:
            valor=valor+10
        salida=salida+chr(48+valor)     
        

print "El codigo desencriptado es: ", salida