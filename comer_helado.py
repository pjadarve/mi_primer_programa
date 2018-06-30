

apetece_helado_input = input("¿Te apetece un helado? (Si/No):").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("LA RESPUESTA ES INCORRECTA, CONTARÉ COMO QUE NO")
    apetece_helado = False


tiene_dinero_input=input("¿Tienes dineros? (Si/No): ").upper()
esta_el_senor_helados_input=input("¿Esta el señor de los helados? (Si/No): ").upper()
esta_su_tia_input = input("¿Estas con tu tia? (Si/No): ").upper()



apetece_helado = apetece_helado_input == "SI"
tiene_dinero = tiene_dinero_input == "SI"
esta_su_tia = esta_su_tia_input == "SI"
puede_permitirselo = tiene_dinero or esta_su_tia
esta_el_senor_helados = esta_el_senor_helados_input == "SI"

if apetece_helado and puede_permitirselo and esta_el_senor_helados:
    print("Pues comete el helado")
else:
    print("Pues nada")


