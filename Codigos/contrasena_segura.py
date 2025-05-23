'''
Clase:        Numero 2
Tema:         Condicionales
Ejercicio:    Contrasena Segura
Descripción:  Contrasena Segura

Autor:        Rodrigo Marroquin
Fecha:        2025-05-16
Estado:       [ En progreso ]
'''

pregunta = input("Introduce una contraseña: ")
print(pregunta)


if len(pregunta) < 8:
    print("Contrasena no segura")

elif not any(char.isupper() for char in pregunta):
    print("Contrasena no segura")

elif not any(char.isdigit() for char in pregunta):
    print("Contrasena no segura")
else:
    print("contrasena segura")