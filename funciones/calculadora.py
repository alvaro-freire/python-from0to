#!/usr/bin/env python
#_*_ coding: utf8 _*_


def despedida():
    print("Adiós!\n")

def multiply(v1, v2):
    print("\nResultado: {}\n".format(v1*v2))

def divide(v1, v2):
    print("\nResultado: {}\n".format(v1/v2))

def add(v1, v2):
    print("\nResultado: {}\n".format(v1+v2))

def sub(v1, v2):
    print("\nResultado: {}\n".format(v1-v2))

def main():
    print("Hola\n")
    list = [1, 2, 3, 4]
    while True:
        print("1.- Suma dos enteros")
        print("2.- Resta dos enteros")
        print("3.- Divide dos enteros")
        print("4.- Multiplica dos enteros")
        print("5.- Salir")
        opcion = int(input("Opción: "))

        if opcion == 5:
            despedida()
            exit()

        if not list.__contains__(opcion):
            print("Opción inválida")
        else:
            v1 = int(input("Valor 1: "))
            v2 = int(input("Valor 2: "))
            if opcion == 1:
                add(v1, v2)
            elif opcion == 2:            
                sub(v1, v2)
            elif opcion == 3:
                divide(v1, v2)
            elif opcion == 4:
                multiply(v1, v2)
            


if __name__ == '__main__':
    main()