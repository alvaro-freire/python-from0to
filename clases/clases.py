#!/usr/bin/env python
#_*_ coding: utf8 _*_

from socket import CAN_RAW


class Coche(object):
    def __init__(self, m):
        self.color = "Rojo"
        self.marca = "Audi"
        self.ano = 2012
        self.m = m

    def movilidad(self):
        if self.m == True:
            print("Acelerar")
        else:
            print("Frenar")


def main():

    print("1.- Acelera")
    print("2.- Frena")
    valor = int(input("> "))
    if valor == 1:
        c = Coche(True)
    else:
        c = Coche(False)
    c.movilidad()

    # print(c.marca)
    # print(c.color)
    # print(c.ano)

if __name__ == '__main__':
    main()