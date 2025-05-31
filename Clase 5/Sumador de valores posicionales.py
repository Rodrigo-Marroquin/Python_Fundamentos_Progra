'''
Clase:        Numero 5
Tema:         Bucles While y For
Ejercicio:    5.4.2 Sumador de valores posicionales
Descripción:  Pide un número al usuario y suma sus dígitos hasta que quede un solo dígito. Ejemplo:
Si el usuario ingresa 9875, entonces: 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2

Autor:        Rodrigo Jose Marroquin Quijada
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

num = int(input("Ingresa un número: "))

print("Proceso de reducción para", num, ":")

while num > 9:
    suma = 0
    for digito in str(num):
        suma = suma + int(digito)
    print(num, "=", suma)
    num = suma

print(f"El resultado final es: {num}")
