def calculadora (n1, n2, operacion):
    
    if operacion == 1:
        return n1 + n2
    
    elif operacion == 2:
        return n1 - n2
    
    elif operacion == 3:
        return n1 * n2
    
    elif operacion == 4:
        return n1 / n2
    
    else:
        return "Nulo."

number1 = int(input("Introduzca su primer numero:"))
number2 = int(input("Introduzca su segundo numero:"))

operacion = int(input("Seleccione:" \
" 1. Suma" + " 2. Resta" +  " 3. Multiplicacion" + " 4. Division"))

print("El resultado de la operacion es:", calculadora(number1, number2, operacion))




    
