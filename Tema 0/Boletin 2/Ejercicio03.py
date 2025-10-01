'''
Realiza un programa que pida 8 números enteros y los almacene en una lista. A continuación, recorrerá
 esa tabla y mostrará esos números junto con la palabra “par” o “impar” según proceda.
'''
list = []

count = 0

while(count < 8):

    numbers = int(input("Introduzca los numeros a la lista:"))

    list.append(numbers)

    count += 1

for numero in list:

    tipo = "par" if numero % 2 == 0 else "impar"

    print(list[numero - 1], tipo)

