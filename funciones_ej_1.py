
def numero_mayor_entre_tres(primero, segundo, tercero):
    numer_mayor = max(primero, segundo, tercero)
    return numer_mayor


n_1 = input("Dime un numero: ")
n_2 = input("Dime un numero: ")
n_3 = input("Dime un numero: ")

print(numero_mayor_entre_tres(n_1, n_2, n_3))