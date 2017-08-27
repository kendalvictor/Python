# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 19:30:17 2017

@author: Labotec
"""

"""
#mi primer bucle
i=0
while (i<20):
    print "Numero",i
    i+=1 #i=i+1
    if i==10:
        pass
"""    
#num primo tiene 2  divisores
i=2
num=12
while i<num:
    if num%i==0:
        print "el numero no es primo"
        break
    #if i==num-1:
    #if num%i==2:   
    i+=1    

print "numero primo"        

#%%
i=0
while(i<10): 
    
    i+=1
    if i<5:
        continue
    print i
       
#%% completar
contenedor=[15]
print type(contenedor)       
num1=input("INgrese un valor: ")
i=0                
while i<4:
    temp=input("Ingrese numero : ")
    if num1>temp:
        contenedor[i]=num1
        contenedor[i+1]=temp
    else:
        contenedor[i]=temp
        contenedor[i+1]=num1
    num1=temp    
    i+=1


#%%
i=0
t=[]
while(i<5):
    a=input("num: ")
    t.append(a)
    i+=1

t.sort()
print t














    