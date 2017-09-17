# -*- coding: utf-8 -*-
 

#convertir romanos a enteros

 
 
class Roman_to_int():
    
    
    def __init__():
        pass
    
    
    
texto="CDXLVIII"    
texto="MMMM"
notacion = { "I":1 ,"V":5,"X":10, "L" : 50 , "C" : 100 , "D" : 500 , "M":1000 ,"0":0}
orden="IVXLCDM"

def convertir(texto):
    texto+="0"    
    cont=list()
    
    for i in range(len(texto)-1) :
        print i
        if notacion[texto[i]] >= notacion[texto[i+1] ]:
            cont.append(notacion[texto[i]])
        else:
            cont.append(-notacion[texto[i]])
    print cont  
    print sum(cont)
    
            
            

convertir=convertir(texto)    

 
















"""
class py_solution:
    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

print(py_solution().roman_to_int('CDXLVIII'))
print(py_solution().roman_to_int('MMMM'))
"""