# -*- coding: utf-8 -*-
 

import datetime # Modulos fecha

class Person:

    def __init__(self, nombre, apellido, naci, direcc, telefono, correo):#\constructor
        self.nombre = nombre
        self.apellido = apellido
        self.cumpleanos = naci

        self.direccion = direcc
        self.telefono = telefono
        self.correo = correo

    def age(self):
        hoy = datetime.date.today()
        age = hoy.year - self.cumpleanos.year

        if hoy < datetime.date(hoy.year, self.cumpleanos.month, self.cumpleanos.day):
            age -= 1

        return age

person = Person(
    "Jose",
    "Martinez",
    datetime.date(1995, 5, 12), # year, month, day
    "Salaverrry",
    "988 522 230",
    "josemartinez@gmail.com"
)

print(person.nombre)
print(person.correo)
print(person.age())
print dir (Person)