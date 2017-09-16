# -*- coding: utf-8 -*-
 

#Herencia
#%%
class Miclase:
    """Simple clase de ejemplo"""
    i = 24 #atributos
    def f(self):  #funcion-metodo
        return 'hola mundo  '
class Copi(Miclase):
    a=2
    

alumno=Copi()#instancia
print alumno.f()    

#%%

#Herencia
class persona:
    def __init__(self,edad,peso):
        self.edad=edad
        self.peso=peso        
        
    
        
class agilidad(persona):
       habilidad="velocidad" 
       def suma(self,num1,num2):
           print "la suma es: ",num1+num2
           
  
class fuerza(persona):
       habilidad="resistencia"
       def mul(self,num1,num2):
           print "el producto es: ",num1*num2
           

alumno1=agilidad(15,20)#instancia
alumno2=fuerza(16,40) #instanciar
print alumno1.habilidad,
print alumno1.edad
print alumno1.suma(1,2)
print alumno2.habilidad,
print alumno2.edad  
print alumno2.mul(2,3)
