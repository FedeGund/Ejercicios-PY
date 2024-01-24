import msvcrt

from random import randint

print("Bienvenido a adivina el número!")
n = randint(1,10)
k = 1

while True:
    x = int(input("Ingrese un número entero entre 1 y 10: "))
    if x == n:
        print(f"Has adivinado despues de {k} intentos")
        break
    else:
        print(f"{x} no es el número, intenta nuevamene\n")
    k += 1

msvcrt.getch()