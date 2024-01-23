import msvcrt

print("Este es un programa que evalúa la expresion: ")
print("(7+(6+(5)^1/2)^1/2)^1/2")

x = (7+(6+(5**0.5))**0.5)**0.5
print("El resultado de la expresión es: ",x)

msvcrt.getch()
