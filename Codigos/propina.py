
total_cuenta = float(input("Ingresa el total de la cuenta: $"))

porcentaje_propina = float(input("Ingresa el porcentaje de propina (por ejemplo, 10 para 10%): "))

propina = total_cuenta * (porcentaje_propina / 100)
total_con_propina = total_cuenta + propina

print(f"\nTotal de la cuenta: ${total_cuenta:.2f}")
print(f"Propina: ${propina:.2f}")
print(f"Total de la cuenta con propina ({porcentaje_propina}%): ${total_con_propina:.2f}")