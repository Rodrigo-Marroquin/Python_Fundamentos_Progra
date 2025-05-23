
nombre_completo = input("Ingresa tu nombre completo (2 nombres y 2 apellidos): ")


partes = nombre_completo.strip().split()


primer_nombre = partes[0].lower()
primer_apellido = partes[2].lower()


correo = f"{primer_nombre}.{primer_apellido}@keyinstitute.edu.sv"

print(f"\nEl correo que se debe asignar al usuario ingresado es: {correo}")