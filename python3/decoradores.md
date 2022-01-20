## @classmethod:
### Nos ayuda a usar una función sin que antes la clase sea atribuída a un objeto.
> ejemplo:
```python
class clase(object):
    def __init__(self):
        pass

    @classmethod
    def saludo(cls, nombre):
        print('Hola {}'.format(nombre))

def main():
    nombre = input("Nombre: ")
    clase.saludo(nombre)

if __name__ == '__main__':
    main()
```

## @staticmethod
### Nos ayuda a usar una función dentro de una clase sin que esta reciba argumentos.
> ejemplo:
```python
class clase(object):
    def __init__(self):
        pass

    @staticmethod
    def saludo_static():
        print('Hola!')

def main():
    c = clase()
    c.saludo_static()

if __name__ == '__main__':
    main()
```

## @property
### Nos ayuda a usar una función como si fuera una variable.
> ejemplo:
```python
class clase(object):
    def __init__(self, radio):
        self.radio = radio

    @property
    def area_circulo(self):
        return 3.14159*(self.radio**2)

def main():
    c = clase(5)
    area = c.area_circulo
    print(area)


if __name__ == '__main__':
    main()
```