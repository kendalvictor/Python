# -*- coding: utf-8 -*-
"""
 

@author: Francixco
"""
#%%
#diccionarios
#agrupacion de listas, y metodos
dicciona = {}
dicciona[5] = ["hola", 7540]
dicciona[4] = [6201]
dicciona[3] = "hola"

dicciona["d"] = []
dicciona["e"] = 10
print dicciona.keys()
print dicciona.values()
print dicciona["e"]
print dir(dict())
#%%
d={1:'one',2:'two',3:'three'}
print 'd.items():'
for k,v in d.items():
   if d[k] is v: print 'Lo Hizo' 
   else: print 'Lo Hizo '
#dict
#%%
usuario={"Luis":1234,"Carlos": 4321}

print "Bienvenido"
usu=raw_input("Ingrese su nombre de usuario: ")
clave=raw_input("Ingrese su contraseña: ")
if(usu in usuario):
   
    if clave==usuario[usu]:
        print "SEsion iniciada"
    else:
        print "error"
else:
    print" Usuario no existe  "  

#%%
registro={}
print "Bienvenido"
usu=raw_input("Ingrese su nombre de usuario: ")
clave1=raw_input("Ingrese su contraseña: ")
clave2=raw_input("Confirme su contraseña: ")
if(clave1==clave2): 
    registro[usu]=clave1
    print "registro completo"
else:    
    print"Clave incorrecta"
        
    
 