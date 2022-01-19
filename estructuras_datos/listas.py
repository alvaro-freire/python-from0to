# lista = [1, 2, 1 < 2, 4, 5, 'a']

lista = ['h', 'o', 'l', 'a']
# lista = ''.join(lista)

# print(lista[len(lista) - 1])

# for l in lista:
#     print(l)

print(lista[0 : len(lista)])

lista.pop()
print(lista)

del lista[len(lista) - 1]
print(lista)

for n in range(98, 100):
    lista.append(n)
print(lista)

lista.append('z')
print(lista)