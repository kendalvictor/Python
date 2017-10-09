texto = raw_input("Ingrese cadena para ser encriptada : ")
n     = input("Ingrese el valor de n : ") 
salida=""
 
for i in texto:
    #a  z    97  122
    #A  Z   65  90
    #0  9   48  57
    temp=ord(i)
    if temp>=97 and temp<=122:
        valor=temp - 97 +n
        while valor>=26:
                valor=valor-26
        salida=salida+chr(97+valor)  
        
        
    if temp>=65 and temp<=90:
        valor=temp - 65 +n
        while valor >=26:
            valor=valor-26
        salida=salida+chr(65+valor) 
        
    if temp>=48 and temp<=57:
        valor=temp - 48 +n
        while valor >=10:
            valor=valor-10
        salida=salida+chr(48+valor)     
        

print "El codigo encriptado es: ", salida