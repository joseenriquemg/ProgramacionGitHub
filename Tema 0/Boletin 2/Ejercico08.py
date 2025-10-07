'''
Diseña un programa que registre las ventas de una tienda en un diccionario, donde las claves
son los nombres de los productos y los valores son las cantidades vendidas. El programa debe 
permitir al usuario agregar nuevas ventas y calcular el total de ventas para un producto 
específico. Implementa un menú con ambas opciones. 

'''

# Creamos nuestro diccionario
ventas = {}

# Funcion para añadir las ventas.
def añadir_ventas():

    # Solicitamos al usuario el nombre del producto
    nombre_producto = input("Introduzca el producto vendido:")

    # Solicitamos als unidades vendidas en formato int para poder operar con ellas
    unidades = int(input("¿Cuantas unidades ha vendido?"))

    # Si el producto esta en la lista:
    if(nombre_producto in ventas):
       
       # Actualizamos las unidades
        ventas[nombre_producto] += unidades
        print("Unidades vendidas actualizadas")

    # Si no esta en la lista:
    else:

        # Creamos la nueva venta
        ventas[nombre_producto] = unidades
        print("Nueva venta añadida.")

# Funcion para imprimir el diccionario
def mostrar_ventas():

    #Imprimimos el diccioanrio
    print(ventas)

# Funcion para imprimir el menu
def menu():

    print()
    print("1. Añadir ventas")
    print("2. Mostrar ventas")
    print("3. Salir")

menu()

# Solicitamos una accion al usuario
opcion = int(input("¿Que deseas hacer?"))

# Mientras no salga del programa, seguiremos preguntando acciones  a hacer
while (opcion != 3):

    if (opcion == 1):

        añadir_ventas()

    elif (opcion == 2):

        mostrar_ventas()

    
    menu()

    opcion = int(input("¿Que deseas hacer?"))

print("Saliendo del sistema...")

