import msvcrt

def contar_vocales(frase):
    conteo_vocales = {"a" : 0, "e": 0, "i" : 0, "o" : 0, "u" : 0}
    frase = frase.lower()

    for caracter in frase:
        if caracter in "aeiou":
            conteo_vocales[caracter] += 1
    return conteo_vocales

frase_usuario = input("Ingrese una frase: ")

resultado = contar_vocales(frase_usuario)

print("Conteo de vocales en la frase:")
for vocal, cantidad in resultado.items():
    print(f"{vocal}: {cantidad}")
msvcrt.getch()