# Solicitamos los dos numeros al usuario
number1 = int(input("Introduzca el primer numero:"))
number2 = int(input("Introduzca el segundo numero:"))

def intermedios (number1, number2):

    if (number1 < number2):

        print(number1)

        for i in range( number1, number2 - 1):

           print (i + 1)
    
    print(number2)

    for j in range(number2, number1):

           print (j + 1)


intermedios(number1, number2)