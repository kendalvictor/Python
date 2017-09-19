#Esto es un comentario
"""
Esto es un comentario
que no se
ejecutara
"""

"""
print ("Mi nombre es: Francisco ")
#print: nos permite mostrar

#asginacion de valores
a      = 15        #asignamos valor entero a una variable
b      = 20.5      #asignamos valor flotante a una variable
texto  = "Labotec" #asignamos valor cadena a una variable
estado = False      #False, asignamos valor bool a una variable


#Mostrar variables y observar tipos de datos
print (a , type(a))
print (b , type(b))
print (texto,type(texto))
print (estado,type(estado))
#Ingreso de datos con input
nombre = input ("Ingrese su nombre: ")
print (type(nombre))
print ("Mi nombre es : ",nombre)
#Operadores
# + - X
#
"""
"""
num1 = input("Ingrese un numero : ")
num2 = input("Ingrese un numero : ")

suma = float(num1) +  int(num2)
mul  = int(num1)   *  int(num2)
div  = int(num1)   /  int(num2)
pot  = int(num1)  **  int(num2)

print(suma)
print (mul)
print (div)
print (pot)
"""
#Valores logico
#  > mayor que
#  < menor que
"""
print (True )
print (False)
print (2 >  3)
print (5 <  1)
print (2 >= 2)# <= menor igual
print (1 != 1)# == igualdad
print (2>4  and 3<2 ) #V,si las dos condiciones de son V
print (7<3  or 4<2 )  #V,si una de las condiciones es V
"""
"""
#if condicion :
#     Verdadero
#else:
#     Falso
num = input ("Ingrese numero")
print (type(num))#str

if 2>3 or int(num)>7 :
    print ("Verdadero")
    print (2)
else:
    print ("Falso")
    
"""
"""
num1 = input("Ingrese numero : ")
num2 = input("Ingrese numero : ")

if num1 > num2 :
    print (num1 ,"es mayor que",num2)
else:
    print (num1 ,"no es mayor que",num2)

##INgresmos 3 numeros     

"""
"""
num1 = input("Ingrese numero : " )
num2 = input("Ingrese numero : " )
num3 = input("Ingrese numero : " )

if num1 > num2 :
    if num1>num3:
        print (num1) #el numero mayor
        if num2>num3:
            print num3 #el numero menor
        else:
            print num2
    else:
        print (num3)
        print (num2)
#else:
"""
"""
#ejemplo aplicando  if ,elif,else
#Ingresamoss un numero  ,
#evaluamos si es multiplo de 6
#Sino evaluamos si es par
#Mostramos
        
num=int(input("Ingrese un numero"))
#multiplo de 6
if num%6==0:
    print("El numero es multiplo de 6")
elif num%2==0:
    print("El numero es par")
else:
    print ("El numero es impar")
"""
"""
num=int(input("INgrese numero"))

i=0

while( i <= num):
    print (i)
    i = i + 1
print ("Termino")
    
"""
#Mayor de 3 numeroes

#a , b , c = 2 , 4 , 5
"""
num1=input("Ingrese numero")
num2=input("Ingrese numero")
if num1>num2:
    mayor=num1
    menor=num2
else:
    menor=num1
    mayor=num2
"""

"""
cond="si"
while cond=="si":#si la condicion es verdadera se seguira ejecutara
    mayor = 0 #asignamos el valor 0 a la variable mayor
    i=1 #contador

    num =int(input("Cantidad de numeros: "))

    while i<=num:
        num3=int(input("Ingrese numero: "))
        if num3 > mayor:
            mayor = num3#mayor almacenara el valor de num3
        i = i + 1 
        
        #if i==num+1:
        #   cond=input("Desea continuar : ")
        #   if cond=="si":
        #     num =int(input("Cantidad de numeros: "))
        #     i=1
        
    print ("El mayor es: ",mayor)        
    cond=input("Desea continuar : ")
print ("Programa terminado")    

"""

#while ,if ,else,elif,print, input

"""

#num =int(input("Cantidad de numeros: "))
i=1#contador de iteracion
mayor=0
menor=999
while i<=3:
        num=int(input("Ingrese numero: "))
        if num > mayor:
            mayor = num3#mayor almacenara el valor de num3
        if menor > num:
            menor = num
        i = i + 1 
        
        #if i==num+1:
        #   cond=input("Desea continuar : ")
        #   if cond=="si":
        #     num =int(input("Cantidad de numeros: "))
        #     i=1
"""        
#algoritmo solo devuelve valores el valor mayor o menor de
#de los datos ingresados,y la informacion de los elementos pierde
n=5 #cantidad de elementos
i=0
lista=[12,343, 1, 3 , 5]
#lista=[0 , 1 , 2, 3 , 4]   #lista de 5 elemneots
lista=list(range(5))#lista de 5 elementos
while i<n:
    num=int(input("Ingrese numero : "))
    lista[i]=num
    i= i+1
print(lista)











        


















    









        



































