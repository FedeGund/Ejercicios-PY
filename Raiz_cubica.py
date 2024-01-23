import msvcrt

numero = float(input("Ingrese un número para conocer su raíz cúbica: "))
rc = (numero)**1/3
print(f"La raíz cubica de {numero} es {rc}")

msvcrt.getch()
