'''
Crea una clase llamada Libro que guarde la información de cada uno de los libros de una biblioteca. La 
clase debe guardar el título del libro, autor, número de ejemplares del libro y número de ejemplares prestados. 
La clase contendrá los siguientes métodos:
Constructor con todos los parámetros (se le indica valores para todos los atributos).
prestamo(): incrementa el atributo correspondiente cada vez que se realice un préstamo. No se pueden prestar 
libros si no quedan ejemplares disponibles para prestar. Devuelve true si se ha podido realizar el préstamo 
y false en caso contrario.
devolucion(): decrementa el atributo correspondiente cada vez que se devuelva un libro. No se podrán devolver 
libros que no se hayan prestado. Devuelve true si se ha podido realizar la operación y false en caso contrario.
Crear también los métodos __str__, __eq__ y __lt__. Se considera que dos  libros son iguales si tienen el mismo 
título y el mismo autor. Los libros se ordenarán de menor a mayor por el nombre del autor.
'''

class Libro:

    def __init__(self, titulo, autor, ejemplares, prestados):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares = ejemplares
        self.prestados = prestados


    def prestamo(self):

        if (self.ejemplares > 0):

            self.ejemplares -= 1

            self.prestados += 1

            print("Prestamo realizado con exito")

        else:

            print("No se puede realizar el prestamo puesto que no quedan ejemplares")

    
    def devolucion(self):

        if (self.prestados > 0):

            self.prestados += 1

            self.ejemplares -= 1

            print("Devolucion realizada con exito")

        else:

            print("La devolucion no es posible ya que no hay libros prestados")

        
    def __str__(self):

        return ("Libro: Titulo -> " + self.titulo + " Autor -> " + self.autor + " Ejemplares -> " + str(self.ejemplares) + " Prestados -> " + str(self.prestados))
        

    def __eq__(self, otro_libro):

        return (self.titulo == otro_libro.titulo and self.autor == otro_libro.titulo)
    

    def __lt__(self, otro_libro):

        return (self.autor > otro_libro.autor)
    

def menu():

    print()
    print("1. Realizar un prestamo")
    print("2. Realizar una devolucion")
    print("3. Comprobar libros")
    print("4. Mostrar libros")
    
Libro1 = Libro('Los secretos de Youtube', 'Davi de gre', 500, 0)
Libro2 = Libro('Los futbolisimos', 'Ivan der grado', 33, 2)

menu()

opcion = int(input("¿Que desea hacer?"))

while (opcion != 5):

    if (opcion == 1):

        Libro1.prestamo()

    elif (opcion == 2):

        Libro1.devolucion()

    elif (opcion == 3):

        print(Libro1.__lt__(Libro2))

    elif (opcion == 4):

        print(Libro1)
        print(Libro2)


    menu()

    opcion = int(input("¿Que desea hacer?"))

        

    

