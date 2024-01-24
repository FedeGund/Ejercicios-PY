import msvcrt

print("Este programa recibe un numero entero positivo e indica si es múltiplo de 5")
while True:
    try:
        numero = int(input("Ingrese un número entero (o ingrese 0 para salir): "))
        if numero == 0:
            print("Saliendo del programa, hasta luego!")
            break
        if numero > 0:
            prueba = numero % 5
            if prueba == 0 :
                print("El número es múltiplo de 5")
            else:
                print("El número no es múltiplo de 5")
        else:
            print("Por favor, ingrese un entero positivo.")
    except ValueError:
        print("Error: Ingerese un valor entero válido.")
msvcrt.getch()