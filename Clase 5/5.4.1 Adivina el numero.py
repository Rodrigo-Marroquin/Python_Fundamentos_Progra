'''
Clase:        Numero 5
Tema:         Bucles While y For
Ejercicio:    5.4.1 Adivina el numero
Descripción:  Genera un número aleatorio entre 1 y 100 y pide al usuario que lo adivine.
El programa debe seguir pidiendo números hasta que acierte. En cada
intento fallido el programa notificará al usuario si el número secreto es
mayor o menor al último valor ingresado

Autor:        Rodrigo Jose Marroquin Quijada
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

import random

num_secreto = random.randint(1, 100)

while True:
    intento = int(input("Ingresa un numero entre 1 y 100: "))
    
    if intento < num_secreto:
        print("El número secreto es mayor")
    elif intento > num_secreto:
        print("El número secreto es menor")
    else:
        print(f"¡Felicidades! Has adivinado el número secreto: {num_secreto}")
        print("Fin del juego")
        break
