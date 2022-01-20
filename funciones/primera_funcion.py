#!/usr/bin/env python
#_*_ coding: utf8 _*_


# __name__
# main()

# argumentos:

def despedida(nombre):
    print("Adiós, {}!".format(nombre))

def saludo(nombre, edad):
    print("Hola {}, tienes {} años".format(nombre, edad))

def main():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    segundo_nombre = input("Segundo nombre: ")
    saludo(nombre, edad)
    despedida(segundo_nombre)

if __name__ == '__main__':
    main()