
texto_usuario = input("Introduce una frase: ")

espacio = " "
punto = "."
coma = ","

n_espacio = 0
n_punto = 0
n_coma = 0

for letra in texto_usuario:
    if letra in espacio:
        n_espacio += 1
    if letra in punto:
        n_punto += 1
    if letra in coma:
        n_coma += 1

print("El numero de espacios es {}".format(n_espacio))
print("El numero de puntos es {}".format(n_punto))
print("El numero de comas es {}".format(n_coma))