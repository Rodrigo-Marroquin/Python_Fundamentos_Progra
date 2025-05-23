unidades = int(input("Introduce las unidades consumidas: "))


if unidades <= 100:
    impuesto = 0
elif unidades <= 200:
    impuesto = (unidades - 100) * 0.5
else:
    impuesto = (100 * 0.5) + ((unidades - 200) * 0.7)


print(f"Impuesto aplicado ($): {impuesto}")