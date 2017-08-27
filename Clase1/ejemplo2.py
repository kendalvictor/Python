# -*- coding: utf-8 -*-
"""
#el mayor de 3 numeros

a,b,c=input("Ingrese numero :")

if a>b:
    if a>c:
        res=a
    else:
        res=c
else: 
    if b>c:
        res=b
    else:
        res=c
            

print "el mayor es ", res   
"""
a,b,c=input("Ingrese numero :")

if a>b:
    if a>c:
        res=a
    else:
        res=c
elif b>c:
        res=b
else:
        res=c
            

print "el mayor es ", res   
#%%
#calculadora (elif)
num1=input("Ingrese numero 1: ")

num2=input("Ingrese numero 2: ")
param=raw_input("Ingrese operador: ")

if (param=='+'):
    print num1+num2
elif (param=='-'):
    print num1-num2

elif param=='*':
    print num1* num2
elif param=='/':
    print float(num1)/float(num2)    
#  /  //   %    

     