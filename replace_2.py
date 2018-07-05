
texto_usuario = input(str("Introduce una frase: "))

while texto_usuario.isdigit():
    print("Repite")
    texto_usuario = input(str("Introduce una frase: "))
if not texto_usuario.isdigit():
    texto_cambiado = texto_usuario.replace("a", "i")

print(texto_cambiado)