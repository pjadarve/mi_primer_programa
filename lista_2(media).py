
lista = []

numero_usuario = input("Introduce un numero: ")

while len(lista) < 10:
    while not numero_usuario.isdigit():
        numero_usuario = input("Introduce un numero: ")
    lista.append(int(numero_usuario))
    numero_usuario = ""
    print("¡Numero añadido!")

media = (lista[0] + lista[1] + lista[2] + lista[3] + lista[4] +  lista[5] + lista[6] + lista[7] + lista[8] + lista[9]) / 10

print("La media es {}".format(media))






