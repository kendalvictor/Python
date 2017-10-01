# -*- coding: utf-8 -*-
"""
Created on Thu Sep 07 06:11:13 2017

@author: Francisco
"""
"""
from modulo import  (nombre de la funcion)

(nombre de la funcion)(parametros)

"""
"""
import numpy as np

a = np.arange(5)
print a
#%%
#Libreria numpy
def get_corazon_coords(da, db,cor,ang_i=0,ang_f=360,ruta=0 ):
    pts = np.zeros((ang_f+1, 2))
    alpha = np.radians(np.r_[ang_i:ang_f:1j*(ang_f+1)])
    pts[:, 0] = cor[0] +     da*np.sin(alpha)**3 
    pts[:, 1] = cor[1] +  ( (db*np.cos(alpha)-(db*0.5)*np.cos(2*alpha)-10*np.cos(3*alpha)-3*np.cos(5*alpha) ))  #b=2ahora es 4
    if ruta==1:
        pts[:,:]=np.fliplr([pts[:,:]]) #da reversa a una columna
         
    return pts

#%%
import time

time.sleep(1)
"""
#%%
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(100)
y=x**2
print ("listo")
#x=range(5)
plt.figure("nuevo ARchivo") 
plt.xlabel("eje x ")
plt.xlim( xmin=1, xmax=100 )  
plt.ylabel(" ejey") 
plt.title("Ecuacion cuadratica")
plt.plot(x,y,x,-y)
plt.show()
#%%
 


