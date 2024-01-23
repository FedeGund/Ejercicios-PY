import msvcrt

print("Este es un programa que evalua la expresion:")
print("10^(0.375)-30^(0.25)+((2^2+10^2)/10^3)")

x = float((10**0.375)-(30**0.25)+((2**2+10**2)/10**3))
print("La respuesta a la expresion evaluada es: ",x)

msvcrt.getch()
