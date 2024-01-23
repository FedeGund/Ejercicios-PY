import msvcrt

numero = float(input("Ingrese un número para conocer su raíz: "))
raiz = int(input("Ingerese que raíz desea conocer: "))
rc = (numero)**(1/(raiz))
print(f"La raíz cubica de {numero} es {rc}")

msvcrt.getch()
