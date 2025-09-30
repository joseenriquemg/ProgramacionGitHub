def maximo(n1, n2):

    if(n1 != n2 and (number2 % number1 != 0 and number1 % number2 != 0)):

        MCD = n1 * n2

    else: 

        MCD = max(n1, n2) * 1

    return MCD

number1 = int(input("Introduzca su primer numero:"))
number2 = int(input("Introduzca su segundo numero:"))

print("El MCD de sus numeros es:" , maximo(number1, number2))