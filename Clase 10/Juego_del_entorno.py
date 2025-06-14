'''
Clase:        Numero 9
Tema:         Manejo de Matrices
Ejercicio:    10.3.2. Juego del entorno
Descripción:  Dada una matriz binaria ingresada por el
usuario, verifica para cada celda de una
matriz binaria cuántos elementos con valor
de 1 hay en las celdas vecinas (arriba, abajo,
izquierda, derecha, diagonales).

Autor:        Rodrigo Jose Marroquin Quijada
Fecha:        2025-06-14
Estado:       [ En progreso | Terminado ]
'''

N = int(input("Ingrese el número de filas: "))
M = int(input("Ingrese el número de columnas: "))


matriz = []
for _ in range(N):
    fila = list(map(int, input().split(',')))
    matriz.append(fila)


x = [-1, -1, -1, 0, 0, 1, 1, 1]
y = [-1, 0, 1, -1, 1, -1, 0, 1]


resultado = []

for i in range(N):
    fila_resultado = []
    for j in range(M):
        contador = 0
        for k in range(8):
            ni, nj = i + x[k], j + y[k]
            if 0 <= ni < N and 0 <= nj < M and matriz[ni][nj] == 1:
                contador += 1
        fila_resultado.append(contador)
    resultado.append(fila_resultado)

# Imprimir resultado
for fila in resultado:
    print(fila)
