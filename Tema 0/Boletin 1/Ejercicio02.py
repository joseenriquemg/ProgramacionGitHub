# Solicitamos los dos numeros al usuario
number1 = int(input("Introduce a number:"))

number2 = int(input("Introduce a number:"))

if (number1 > number2):
    print("The correct order is " +  str(number2) + " and " + str(number1))
else: 
    print("The correct order is " + str(number1) + " and " + str(number2))
    
