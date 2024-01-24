import msvcrt

print("Este programa calcula la suma de los enteros del 1 al 100")

suma_total = 0
x = 1
#Otra forma de hacerlo, borro el x=1 pero dejo el suma total
#for numero in range (1, 101): 
#    suma_total += numero
#
while x <= 100 :
    suma_total += x
    x += 1



print("La suma de los enteros del 1 al 100 es: ", suma_total)

msvcrt.getch()