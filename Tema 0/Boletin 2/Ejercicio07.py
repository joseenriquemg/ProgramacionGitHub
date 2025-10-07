'''
Crea un programa que permita al usuario agregar, eliminar y buscar contactos en una libreta de direcciones 
implementada como un diccionario. La clave del diccionario será el nombre del contacto y el valor, su número 
de teléfono. Crea un menú para las distintas opciones e implementa una función para cada opción.
'''

agenda = {}

def añadir_contactos():

    nuevo_nombre = input("Introduce el nombre: ")
    nuevo_numero = input("Introduce el numero: ")

    if (agenda.get(nuevo_nombre) == None): 

        agenda[nuevo_nombre] = nuevo_numero

    else: 

        print("El usuario ya existe")

def eliminar_contactos(usuario):

    if (agenda.get(usuario)):

        agenda.pop(usuario)

        print("Se ha eliminado a", usuario, "correctamente.")

    else:

        print("No existe el contacto.")

def buscar_contactos(usuario):

    if (agenda.get(usuario)):

        print("El numero de", usuario, "es", agenda.get(usuario))
    
    else:

        print("No se ha encontrado al usuario")


def mostrar_contactos():


    print("Listado de contactos: \n", agenda)



def menu():
    print()
    print("1. Añadir contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Mostrar contactos")
    print("5. Salir")

menu()

opcion = int(input("¿Que deseas hacer?"))

while (opcion != 5):

    if (opcion == 1):

        añadir_contactos()

    elif (opcion == 2):

        persona_eliminar = input("¿A quien deseas eliminar?")

        eliminar_contactos(persona_eliminar)
    
    elif (opcion == 3):

        persona_buscar = input("¿A quien deseas buscar?")

        buscar_contactos(persona_buscar)

    elif (opcion == 4):

        mostrar_contactos()

    menu()

    opcion = int(input("¿Que deseas hacer?"))


print("Saliendo del sistema...")
