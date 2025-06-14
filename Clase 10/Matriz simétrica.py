'''
Clase:        Numero 9
Tema:         Manejo de Matrices
Ejercicio:    10.3.1. Matriz simétrica
Descripción:  Dada una matriz cuadrada ingresada por el
usuario, comprueba si la matriz cuadrada es
simétrica respecto a su diagonal principal.

Autor:        Rodrigo Jose Marroquin Quijada
Fecha:        2025-06-14
Estado:       [ En progreso | Terminado ]
'''

N = int(input("Ingrese el tamaño de la matriz: "))

matriz = []
for _ in range(N):
    fila = list(map(int, input().split(',')))
    matriz.append(fila)

simetrica = True
for i in range(N):
    for j in range(N):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
            break

if simetrica:
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")
