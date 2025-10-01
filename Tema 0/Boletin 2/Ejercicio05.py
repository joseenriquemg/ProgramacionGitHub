'''
Crea un programa que cree una lista de enteros de tamaño 100 y lo rellene con valores enteros aleatorios
 entre 1 y 10. Luego pedirá un valor N y mostrará cuántas veces aparece N. 

'''
# Importamos el random
import random

count_number = 0

# Asignamos a la lista 10 valores entre 1 y 100
list = [random.randint(1,10) for _ in range (100)]

number = int(input("¿Que numero deseas saber cuantas veces aparece?"))

for numero in list:

    if ( numero == number):

        count_number += 1

# Imprimimos la lista 
print (list)
print("El numero", number, "aparece", count_number, "veces.")