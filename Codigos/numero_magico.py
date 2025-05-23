n = int(input("Introduce un entero n: "))


if n % 7 == 0 and n % 5 != 0:
    print("Mágico")
else:
    print("Normal")