# -*- coding: utf-8 -*-
"""
 

@author: Francixco
"""

#Recursion
#usar una misma funcion dentro de otra es decir dentro
# de l a funcion declarada, volver a llaamr a la mimsa funcion



#%%

def repetir(TEXTO,n):
    if n==0:
        return
    print (TEXTO)
    repetir(TEXTO,n-1)
palabra=input("Ingrese texto o palabra: ")    
repetir(palabra,5)

#%%
def numero(n):
    if n==0:
        return
    print n
    numero(n-1)
numero( 5)




#%%
#potencia
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    sol  =fib(n-1) + fib(n-2)  
    return sol
    print sol


num=input("Ingrese la cantidad de elementos a emplear por fibonacci : ")
fib(num)

#mostrar todos los elementos de fibonacci


#%%
# factorial de un nuemro o series 
def fact(num):
    if num==1:
        return 1 
    else:
        sol=num * fact(num-1)   
        print sol       
        return sol    

numero=input("Ingrese numero para hallar factorial: ")
print(fact(numero))
    
 
 #%%







 