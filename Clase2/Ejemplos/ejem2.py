# -*- coding: utf-8 -*-
"""
 

@author: Francixco
"""
#%%
#for variable in (lista) :
    #sentencia


#%%
contener=[]
for i in range(1,4):
    contener.append( i**2)
print contener

#%%
contener=[x**2 for x in range(5)]
print contener

#%%
[x for x in range(10) if x>5]
print x