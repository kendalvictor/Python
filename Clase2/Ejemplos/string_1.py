# -*- coding: utf-8 -*-
"""
 

@author: Francixco
"""
#%%
texto="hola mundo"
print type(texto)  #muestra el tipo de dato

#%% concatenacion
text1="hola"
text2="mundo"
print text1+" "+text2
 
#%%
print "hola \b\b\b\bmundo"  #retroceso
print "python  \n python xy" #salto de linea
print " segundo \rprimero" #retroceso
 
 
 
#%% formato print
res=2.75
num=121
num1=-15214
text="lucho"
print "mostrando numero %u " %(num1)
print "hola soy %c"%(num)
print "el numero eso  : %.2e " % (res)

#%%
print "Usuario: %s  numero de espera : %i " % ('Luis', 16) 
 
 
#%%

print " "
import string as s
a="hola mundo"
print s.upper(a)
#%%
b="Hola Mundo"
print b.istitle() #devuleve V o F si la cadena cada palabra de la cadena es mayuscula
b="AAAAAAAHola mundo1 holaAAAAA"
print b.strip('A') #Elimina el parametro de una cadena solo los extremos
print b.replace("mundo","onda") 
print b.find("ola",2,20)
print b.split()
#%%



#%%
a=-2
print "hola %u "% (a)







 