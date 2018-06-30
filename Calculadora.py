
operacion_elegida = input("¿Qué operación quieres realizar? (multiplicar/dividir/sumar/restar): ")
primer_numero = int(input("Primer Número: "))
segundo_numero = int(input("Segundo Número: "))

if operacion_elegida == "multiplicar":
    resultado_multiplicar = primer_numero * segundo_numero
    print("El resultado es {}".format(resultado_multiplicar))
elif operacion_elegida == "dividir":
    resultado_dividir = primer_numero / segundo_numero
    print("El resultado es {}".format(resultado_dividir))
elif operacion_elegida == "sumar":
    resultado_sumar = primer_numero + segundo_numero
    print("El resultado es {}".format(resultado_sumar))
elif operacion_elegida == "restar":
    resultado_restar = primer_numero - segundo_numero
    print("El resultado es {}".format(resultado_restar))