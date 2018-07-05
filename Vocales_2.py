
texto_usuario = input("Introduce una frase: ")

mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

n_mayusculas = 0

for mayuscula in texto_usuario:
    if mayuscula in mayusculas:
        n_mayusculas += 1

print("Hay {} mayusculas".format(n_mayusculas))
