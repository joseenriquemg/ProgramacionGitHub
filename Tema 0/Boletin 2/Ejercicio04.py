'''
Escribe un programa que lea 10 números por teclado y que luego los muestre ordenados de mayor a menor.
'''
list = []

count = 0

while (count < 10):

    numbers = int(input("Introduzca un numero:"))

    list.append(numbers)

    count += 1

print("Lista", list)

list.sort(reverse=True)

print("Lista ordenada",list)