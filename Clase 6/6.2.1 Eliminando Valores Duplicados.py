'''
Clase:        Numero 6
Tema:         Manejo de Listas
Ejercicio:    6.2.1 Eliminando Valores Duplicados
Descripción:  Dada una lista ingresada por el usuario, elimina los elementos duplicados
manteniendo la primera aparición de cada número.

Autor:        Rodrigo Jose Marroquin Quijada
Fecha:        2025-05-30
Estado:       [ En progreso | Terminado ]
'''


numeros = input("ingrese los datos para la lista")

lista = []
for a in numeros.split():
    lista.append(int(a))
 
sin_repetir = []
for num in lista:
    if num not in sin_repetir:
        sin_repetir.append(num)

resultado = ""
for num in sin_repetir:
    resultado += str(num) + " "
print(f"los numeros serian {resultado}")