# -*- coding: utf-8 -*-



 
#%%
#clase
class Miclase:
    #Simple clase de ejemplo
    i = 24 #atributos
    def f(self):  #funcion-metodo
        return 'hola mundo  '
#%%
 
 
a=Miclase() #instanciar   
print a.i   #obtenemos el valor de i
print "termino"
#%% objetos

 
class Ope:
         
    def __init__(self,num1,num2): #se inicia al ser instanciado
        self.x=num1
        self.y=num2
    def suma(self):
        print "suma es ",self.x +self.y
a=Ope(4,5)  #instanciamos
a.suma()      


#%%








#%%
class yo:
    pass

carlos = yo()   

# Llenar los campos del registro
carlos.nick = 'Ember Spirit'
carlos.edad = 25
carlos.signo = "Tauro"
print carlos.signo

#%%

 


