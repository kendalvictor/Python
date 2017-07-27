# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:24:20 2017

@author: Francisco
"""

import serial
import time
import numpy as np #libreria que nos permite trabajar con vectores y matrices
gx=0
gy=0
gz=0 
#INCIO DE LA COMUNICACION SERIAL 
comuni=serial.Serial('COM5',9600,timeout=1)
time.sleep(1.8) #PAUSA DE 1.8 SEGUNDOS
 
def  acelerometro(data1):
    salida=[0,0,0]    
    data=data1[1:4]
    salida[0]=round(float(data[0])*9.81/16384,2)
    salida[1]=round(float(data[1])*9.81/16384,2)
    salida[2]=round(float(data[2])*9.81/16384,2)
    return salida
"""    
def giroscopio(data):
  global gx,gy,gz
  print data
  salida=[0,0]
  ay=np.arctan2(float(data[1]),np.sqrt(float(data[2])**2+float(data[3])**2)) *180/np.pi
 
  ax=np.arctan2(float(data[1]),np.sqrt(float(data[1])**2+float(data[3])**2))*180/np.pi        
  
  gx = gx + float(data[4]) / 30.0
  gy = gy - float(data[5]) / 30.0
  gz = gz + float(data[6]) / 30.0

 
 
  gx = gx * 0.96 + ax * 0.04
  
  gy = gy * 0.96 + ay * 0.04
   
  salida[0]=gx
  salida[1]=gy
  
  return salida
"""  
for i in range(15): #se repetira 100 veces
    comuni.write('x')
    data=comuni.readline()
    data=data.split()  #separa la cadena en elementos
 
     
    time.sleep(0.1) #time.sleep(segundos)
    acelerometro=acelerometro(data)
    #funcion giroscopio
    ay=np.arctan2(float(data[1]),np.sqrt(float(data[2])**2+float(data[3])**2)) *180/np.pi
 
    ax=np.arctan2(float(data[1]),np.sqrt(float(data[1])**2+float(data[3])**2))*180/np.pi        
  
    gx = gx + float(data[4]) / 30.0
    gy = gy - float(data[5]) / 30.0
    gz = gz + float(data[6]) / 30.0

 
 
    gx = gx * 0.96 + ax * 0.04
  
    gy = gy * 0.96 + ay * 0.04  
    
    print gx," ",gy
    
    time.sleep(1)
       
comuni.close()
print "Termino" 


 