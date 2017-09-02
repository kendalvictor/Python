# -*- coding: utf-8 -*-
"""
 

@author: Francixco
"""

#metodo burbuja
print "metodo burbuja"
i=1
a=[]
n=5
while(i<=n):
    temp=input( "Ingrese numero : ")
    a+=[temp]
    i+=1
op=raw_input("Ingrese operacion 'mayor' o  'menor' : ")
i=0

if(op=="mayor"):
    while(i<n-1):
        j=0
        while(j<n-1):
            if(a[j]<=a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
            print a,j
            j+=1       
        i+=1
        
    print a    


elif(op=="menor"):
    while(i<n-1):
        j=0
        while(j<n-1):
            if(a[j]>=a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
            print a,j
            j+=1       
        i+=1
        
    print a    

else:   
    print "Error al ingresar operacion"

