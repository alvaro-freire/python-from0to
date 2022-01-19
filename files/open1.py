#!/usr/bin/env python
#_*_ coding: utf8 _*_

# w = write

archivo = open("archivo1.txt", "w")
nombre = input("Nombre: ")
edad = input("Edad: ")
pais = input("País: ")

archivo.write(nombre)
archivo.write("\n")
archivo.write(edad)
archivo.write("\n")
archivo.write(pais)
archivo.write("\n")

print("He escrito los datos.")

archivo.close()