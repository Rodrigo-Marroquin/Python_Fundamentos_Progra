'''
Clase:        Numero 7
Tema:         NumPy
Ejercicio:    Introduccion a NumpY
Descripción:  

Autor:        Rodrigo Jose Marroquin Quijada
Fecha:        2025-06-02
Estado:       [ En progreso | Terminado ]
'''

import numpy as np

my_list = [1, 2, 3, 4, 5]
arr = np.array(my_list)
print(arr)

zeros = np.zeros(5)
print(zeros)

ones = np.ones(5)
print(ones)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
resultado = arr1 + arr2
print(resultado)

arr3 = np.array([1, 2, 3])
arr4 = np.array([4, 5, 6])
resultado1 = arr3 * arr4
print(resultado1)

#Ejemplos de Broadcasting

#Ejemplo 1: Broadcasting con un escalar
#En este ejemplo, NumPy difunde el escalar 5 para que coincida con la forma del array arr, lo que resulta en [6, 7, 8].
arr = np.array([1, 2, 3])
result = arr + 5

#Ejemplo 2: Difusión de matrices unidimensionales y bidimensionales*
#Aquí, NumPy difunde la matriz unidimensional arr1 para que coincida con la forma de la matriz bidimensional arr2, 
# lo que resulta en una matriz bidimensional [[11, 12, 13], [21, 22, 23], [31, 32, 33]].
#El Broadcasting simplifica muchas operaciones, eliminando la necesidad de bucles explícitos o la remodelación de matrices.
arr1 = np.array([1, 2, 3])
arr2 = np.array([[10], [20], [30]])
result = arr1 + arr2

#Tecnicas avanzadas de numpy

arr = np.array([1, 2, 3, 4, 5])
slice = arr[1:4]
# Recupera los elementos 2, 3 y 4

# Indexación booleana
arr = np.array([1, 2, 3, 4, 5])
mask = arr > 2
result = arr[mask]
# Recupera los elementos donde la condición es verdadera: [3, 4, 5]

arr = np.array([1, 2, 3, 4, 5])
indices = np.array([0, 2, 4])
result = arr[indices] 
# Recupera los elementos en los índices especificados: [1, 3, 5]

#Concatenación
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated = np.concatenate((arr1, arr2))

#División
arr = np.array([1, 2, 3, 4, 5, 6])
split = np.split(arr, 3) # Divide la matriz en 3 partes iguales

consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

#Exploracion de datos
print ("Dimensiones:", consumo.ndim) #2 (flilas y columnas)
print ("Forma:", consumo.shape) #(10, 7) -- 10 filas y 7 columnas
print ("Tipo de datos:", consumo.dtype) #float64 (numeros decimales)
print ("Consumo primer hogar:", consumo[0]) #todos los datos de la fila 0
print ("Consumo el miercoles (dia 3):", consumo[:, 2]) #todos los datos de la columna 2

'''
ndim: muestra cuántas dimensiones tiene la matriz. En este caso, 2 (filas y columnas).

shape: indica el número de filas y columnas. (10, 7) significa 10 hogares y 7 días.

dtype: muestra el tipo de datos. float64 son números con decimales.

consumo[0]: devuelve toda la fila 0 (consumo del primer hogar durante la semana).

consumo[:, 2]: El símbolo : significa "todos los hogares", y el 2 es la tercera columna (miércoles, porque Python cuenta desde 0).
'''

#Calculo de promedios y sumas

#Promedio de consumo por hogar
promedio_por_hogar = np.mean(consumo, axis=1)

#Promedio de consumo diario de todos los hogares
promedio_por_dia = np.mean(consumo, axis=0)

#Suma total de consumo en la semana de los 10 hogares
total_consumo = np.sum (consumo)

print(promedio_por_hogar)
print(promedio_por_dia)
print(total_consumo)

'''
np.mean: calcula el promedio. el valor axis=1: promedia por fila (cada hogar). 
Resultado: un array con 10 valores (uno por hogar). Por otro lado, axis=0: promedia por columna 
(cada día). Resultado: un array con 7 valores (uno por día).

np.sum: suma todos los valores de la matriz.
'''

#Minimos, Maximos y Desviacion

#Maximo por hogar
maximos = np.max(consumo, axis=1)

#Minimo por dia
minimos = np.min (consumo, axis=0)

#Desviacion estandar global
desviacion = np.std(consumo)

print(maximos)
print(minimos)
print(desviacion)

'''
Máximos por hogar (axis=1): el valor más alto que alcanzó cada hogar en la semana.

Mínimos por día (axis=0): el valor más bajo registrado entre todos los hogares en un día específico.

Desviación estándar (np.std): mide cuánto varían los datos respecto al promedio. 
Un valor alto indica que hay hogares con consumos muy distintos.
'''

#Comparacion de Hogares

#Suma por hogar (semana)
consumo_total_hogar = np.sum (consumo, axis =1)

#Indice del hogar con mayor consumo
hogar_mayor_consumo = np.argmax (consumo_total_hogar)

#Indice del hogar con mejor consumo
hogar_mas_eficiente = np.argmin(consumo_total_hogar)

'''
np.sum(axis=1): Suma el consumo de cada hogar durante los 7 días.

np.argmax y np.argmin: Encuentran la posición (índice) del hogar que consumió más y menos energía en la semana.
'''

#Suma por hogar(Semana)
consumo_total_hogar = np.sum(consumo, axis=1)
print(f"consumo total de cada hogar derante la semana:{consumo_total_hogar}")

#Compara cada hogar con un valor mayor a 100
altos = consumo_total_hogar > 100

#Filtrando hogares que cumplen la condicion:
consumo_mayor_100 = np.where (altos)[0]

print (f"ids de hogares con consumo mayor a 100: {consumo_mayor_100}")

#Aplicando normalizacion MinMax al conjunto de datos
consumo_normalizado = (consumo - consumo.min()) / (consumo.max() - consumo.min())

#resultado
print (consumo_normalizado)

#1. ¿Cuál es el consumo del hogar 5 el viernes (día 5)?
consumo_hogar5_viernes = consumo[4, 4]
print(f"Consumo del hogar 5 el viernes: {consumo_hogar5_viernes}")


#2. Usando indexación, muestra el consumo de los últimos 3 hogares el domingo.
consumo_ultimos3_domingo = consumo[-3:, 6]
print(f"Consumo de los últimos 3 hogares el domingo: {consumo_ultimos3_domingo}")

#3. Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
promedio_fin_de_semana = np.mean(consumo[:, 5:7])
print(f"Promedio de consumo en fines de semana: {promedio_fin_de_semana}")

#4. ¿Qué día de la semana tiene la mayor desviación estándar entre hogares? Explica qué indica esto.
desviaciones_de_dia = np.std(consumo, axis=0)
dia_de_mayor_desviacion = np.argmax(desviaciones_dia)
print(f"Día con mayor desviación estándar: {dia_de_mayor_desviacion} (0=Lunes, 6=Domingo)")
print(f"Desviaciones estándar por día: {desviaciones_de_dia}")


#5. Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.
consumo_total_hogar = np.sum(consumo, axis=1)

indices_menor_consumo = np.argsort(consumo_total_hogar)[:3]
valores_menor_consumo = consumo_total_hogar[indices_menor_consumo]
print(f"Índices de los 3 hogares con menor consumo: {indices_menor_consumo}")
print(f"Valores: {valores_menor_consumo}")


#6. Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?
consumo_hogar3 = consumo[2]
consumo_aumentado = consumo_hogar3 * 1.10
nuevo_total_hogar3 = np.sum(consumo_aumentado)
print(f"Nuevo consumo total semanal del hogar 3 con aumento del 10% diario: {nuevo_total_hogar3}")
