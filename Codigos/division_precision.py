a = int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))
k = int(input("Ingresa el número de decimales k: "))

result = a / b
truncated_result = str(result)[:k + 2] 

print("Resultado:", truncated_result)