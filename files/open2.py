#!/usr/bin/env python
#_*_ coding: utf8 _*_

# r = read

archivo = open("wordlist.lst", 'r')

# print(archivo.readlines())

# read lines of a file: (op1)
#
# for l in archivo.read().split('\n'):
#     print(l)


# (op2)
lista = archivo.read().split('\n')
print(len(lista))

for n in lista:
    print(n)

archivo.close()