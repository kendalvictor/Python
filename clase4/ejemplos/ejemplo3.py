# -*- coding: utf-8 -*-
 

#Porgramacion Orientada a Objetos
#%%
class Personaje():
    def __init__(self,sexo,color):#inicializar
        self.sexo=sexo
        self.color=color
        print "Inicializo la clase personaje"
    def stats(self):
        print "Inicializo el metodo Stats"

class Agilidad(Personaje):
    def poder(self):
        print self.sexo
        print "velocidad de ataque"


class Fuerza(Personaje): 
    def __init__(self):#si construimos el init ya no lee el de la class base
        print "Inicializo la clase fuerza"
       
    def poder(self):
        print "Se ejecuto el metodo poder"



class Inteligencia(Personaje):     
    def poder(self):
        print "mas energia"

"""tener en cuenta que podemos poner al crear una clase sin herencia el parametro 
"object" , lo cual permite heredadr la clase base de python
clase  yo(Object)


"""
#instanciamos
a=Personaje("hombre","gringo")

Maya=Agilidad("Mujer","azul")
Salvador=Fuerza()
 

Maya.poder()
#%%   Metodo burbuja con clases     
class Burbuja():
    def __init__(self,lista):
        self.lista=lista

    def mayor(self):
        self.lista
        
        
        
        

#%%
 


 






        