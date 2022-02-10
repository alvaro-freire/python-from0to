#!/usr/bin/env python
#_*_ coding: utf8 _*_

import mod_calc as calc

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
            calc.despedida()
            exit()

        if not list.__contains__(opcion):
            print("Opción inválida")
        else:
            v1 = int(input("Valor 1: "))
            v2 = int(input("Valor 2: "))
            if opcion == 1:
                calc.add(v1, v2)
            elif opcion == 2:            
                calc.sub(v1, v2)
            elif opcion == 3:
                calc.divide(v1, v2)
            else:
                calc.multiply(v1, v2)
            


if __name__ == '__main__':
    main()
