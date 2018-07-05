
def input_con_confirmacion(pregunta):
    confirmacion = False
    while not confirmacion:
        dato_usuario = input(pregunta)
        seguro = input("Has dicho {}, ¿Estás seguro? [si/no]: ".format(dato_usuario))
        if seguro == "si":
            confirmacion = True
    return dato_usuario


nombre = input_con_confirmacion("¿Cómo te llamas?: ")
print("Has confirmado que tu nombre es {}".format(nombre))

edad = input_con_confirmacion("Dime tu edad: ")
print("Has confirmado que tu edad es {}".format(edad))

print("Tu nombre es {} y tu edad es de {} años".format(nombre, edad))