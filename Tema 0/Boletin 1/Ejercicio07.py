# Solicitamos un numero al usuario
number = int(input("Introduce a number:"))

contador = 2

esPrimo = False

while (contador < number and esPrimo == False):

    if (number % contador == 0):

        print("No es primo.")

        esPrimo = True

    contador += 1

if (esPrimo == False):

    print("Es primo.")

    