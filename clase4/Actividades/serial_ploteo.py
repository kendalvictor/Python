# -*- coding: utf-8 -*-
"""
Created on Sun May 07 01:54:57 2017

@author: Francisco
"""


import serial
from time import sleep
import numpy as np
y=[] 
i=1
import matplotlib.pyplot as plt 
#Comando: variable=serial.Serial (#
# de puerto, baudrate,bytezise,parity,stopbits)
#puerto=raw_input('Ingrese puerto: ')
comuni = serial.Serial('COM3', 9600)
comuni.timeout = 2
cuenta = 0
sleep(2)
data = " x: -58 y: -16 z: -87 "
print len(data)
cont=0

def ploteo(dato,n):
    global y
     
    #dato=float(dato)
    y.append(dato)
    
    x=range(n)   
    
   
    print "El valor es :",dato
    
  
    
   
    plt.xlim(0,n+1) 
    plt.plot(x,y,'r')
    plt.draw()
        
       
    plt.show(block=False)
    plt.pause(0.05)
 
while i<=100:
    data = comuni.readline()
    data=data[:5]     
    print len(data)
    ploteo(data,i)
    i=i+1 
print "termino"
comuni.close()

 