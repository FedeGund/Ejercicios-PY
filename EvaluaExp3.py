import msvcrt

print("Este es un programa que evalúa la expresión: ")
print("5+(1/(1-(1/(5^0.35))))")

x = float(5+(1/(1-(1/(5**0.35)))))
print("El resultado de la expresión es: ",x)

msvcrt.getch()
