final_number = int(input("Introduce the final number:"))

contador = 0

multiplication = 1

# Buvle para parar de multiplicar cuando llegue a 1
while(contador != final_number):

    # Vamos multiplivanco los numeros
    multiplication *= final_number

    # Imprimimos los factores
    print(final_number, end="x")

    # Vamos restando los numeros a imprimir
    final_number -= 1

# Imprimimos el resultado de la multiplicacion
print(1 , " = " , multiplication)

    