#!/usr/bin/env python
#_*_ coding: utf8 _*_

# a = append

archivo = open('archivo1.txt', 'a')

dedicacion = input("Dedicación: ")
empresa = input("Empresa: ")
idioma = input("Idioma: ")

archivo.write(dedicacion)
archivo.write("\n")
archivo.write(empresa)
archivo.write("\n")
archivo.write(idioma)
archivo.write("\n")

archivo.close()