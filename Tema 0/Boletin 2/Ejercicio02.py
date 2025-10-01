'''
Crea un programa que pida diez números reales por teclado, los almacene en una lista, y luego
 lo recorra para averiguar el máximo y mínimo y mostrarlos por pantalla.

'''
list = []

count = 0

while(count < 10):

    numbers = int(input("Introduzca los numeros a la lista:"))

    list.append(numbers)

    count += 1

print(list)

print("El maximo es:", max(list))
print("El maximo es:",min(list))