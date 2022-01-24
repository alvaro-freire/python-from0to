# El problema de Monty Hall

import random

#1. Implementar la clase puerta
class Puerta(object):
# Inicializador / Atributos de Instancia.
    def __init__(self, premio):
        self.premio = premio

    def abrir(self):
        return self.premio


def inicializar_puertas():
    coche = 'coche'
    cabra = 'cabra'
    puertas = []

    #2. Crear un listado de puertas con 3 premios
    coche = Puerta(coche)
    cabra = Puerta(cabra)

    objects = [coche, cabra, cabra]

    i = 2
    for j in range(3):
        x = random.randint(0, i)
        puertas.append(objects[x])
        objects.pop(x)
        i -= 1

    return puertas

def choose_door(puertas):
    n = random.randint(0, 2)

    return n # simplemente devolvemos el index de la puerta escogida

def open_door(first_choice, puertas):
    i = 0
    for puerta in puertas: # para cada elemento puerta
        if puerta.abrir() == 'cabra' and i != first_choice:
            puertas.remove(puerta)
            break # romper el bucle for, ya hizo su trabajo
        i += 1

def change_door(choice, puertas):
    # Se devuelve el objeto que no habíamos escogido
    for puerta in puertas:
        if puerta != choice:
            return puerta

def juego():
    # inicializamos las 3 puertas de forma aleatoria  
    puertas = inicializar_puertas()

    # Concursante elige puerta aleatoriamente.
    first_choice = choose_door(puertas) # guardamos el index
    mydoor = puertas[first_choice] # guardamos el objeto

    # El presentador abre una de las puertas restantes con una cabra.
    open_door(first_choice, puertas)

    # Quedan 2 puertas !

    # Cambiamos de opción:    
    mydoor = change_door(mydoor, puertas)

    # Si la puerta esconde el coche, sumamos una "victoria"
    if mydoor.abrir() == "coche":
        return 1
    else: 
        return 0

def main():  
    n = 1000
    victorias = 0
    
    # Lo repetimos n (mil) veces
    for i in range(n):
        victorias += juego()

    print("De {} juegos, has ganado {}".format(n, victorias))

if __name__ == '__main__':
    main()