'''
Clase:        Numero 9
Tema:         Manejo de Matrices
Ejercicio:    Diagonal principal y secundaria 10.2.1
Descripción:  Dada una matriz cuadrada ingresada por el
usuario, crea dos listas, una con los
elementos de la diagonal principal y la otra
con los elementos de la diagonal
secundaria.

Autor:        Rodrigo Jose Marroquin Quijada
Fecha:        2025-06-09
Estado:       [ En progreso | Terminado ]
'''

N = int(input("Ingrese el tamaño de la matriz: "))

matriz = []
for _ in range(N):
    fila = list(map(int, input().split(',')))  
    matriz.append(fila)


diagonal_principal = [matriz[i][i] for i in range(N)]
diagonal_secundaria = [matriz[i][N - 1 - i] for i in range(N)]

print("Diagonal principal:", diagonal_principal)
print("Diagonal secundaria:", diagonal_secundaria)
