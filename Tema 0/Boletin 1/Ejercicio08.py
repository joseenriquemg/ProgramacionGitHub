# Solicitamos la base de la priramide al usuario
number = int(input("Introduzca la base de su piramide:"))

# Creamos un bucle for 
for i in range(1 ,number + 1):

    # Imprimimos la piramide con
    print(" " * (number - i) + "* " * i)

