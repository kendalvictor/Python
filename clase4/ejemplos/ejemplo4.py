# -*- coding: utf-8 -*-
 

 

import serial
from time import sleep

def ploteo(punto):
    data=list()
    data.append(punto)
    x.append(x[-1]+1)
    plt.plot(x,data)
    plt.show(block=False)
    plt.pause(0.05)
    plt.draw()
    
#Comando: variable=serial.Serial (#
# de puerto, baudrate,bytezise,parity,stopbits)
comuni = serial.Serial('COM23', 9600)
comuni.timeout = 2
cuenta = 0
sleep(2) #tiempo de espera
data = " x: -58 y: -16 z: -87 "
print len(data)
x=[0]
cont=0
 
while int(len(data))>=19:
    data = comuni.readline()
    print data    
    print len(data)
     
print "termino"
comuni.close()



#%%parity= serial.PARITY_EVEN(par)   odd(impar) 