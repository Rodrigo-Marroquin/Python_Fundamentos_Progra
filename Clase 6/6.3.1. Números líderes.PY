'''
Clase:        Numero 6
Tema:         Manejo de Listas
Ejercicio:    6.3.1 Numeros Lideres
Descripción:  Un número en una lista es "líder" si es
estrictamente mayor que todos los
elementos a su derecha. Dada una lista de
números ingresada por el usuario, imprime
todos los números líderes.

Autor:        Rodrigo Jose Marroquin Quijada
Fecha:        2025-06-01
Estado:       [ En progreso | Terminado ]
'''

num_lideres = input("Ingrese los datos a continuación: ")

num = num_lideres.split()
for i in range(len(num)):
    num[i] = int(num[i])

lider = []

mayor = num[-1]

for i in range(len(num) - 1, -1, -1):
    if num[i] > mayor:
        lider.append(num[i])
        mayor = num[i]
    elif i == len(num) - 1:
        lider.append(num[i])

lider.reverse()

print("Números líderes:")
for n in lider:
    print(n, end=" ")

