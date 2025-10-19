'''
Crea una clase llamada Punto que representará un punto de dos dimensiones en un plano. Solo contendrá dos atributos 
enteros llamados x e y (coordenadas). Debe tener los siguientes métodos:
- Un constructor con parámetros que copie las coordenadas pasadas como argumento a los atributos del objeto.
- __str__(): Devuelve una cadena con el formato “(x, y)”. Ejemplo: “(7, -5)”
- setXY(x,y): Modifica ambas coordenadas.
- desplaza(dx, dy): Desplaza el punto la cantidad (dx,dy) indicada. Ejemplo: Si el punto (1,1) se desplaza (2,5) entonces 
estará en (3,6).
- distancia(punto): Calcula y devuelve la distancia entre el propio objeto (self) y otro objeto (punto) que se pasa como 
parámetro (distancia entre dos coordenadas). 
'''

import math

class Punto:

    def __init__(self, coordenadaX, coordenadaY):
       
        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY


    def __str__(self):
        
        return ("Punto: (", self.coordenadaX, ',', self.coordenadaY, ')')
    

    def setXY(self, dx, dy):

        self.coordenadaX = dx 
        self.coordenadaY = dy

    def desplaza(self, dx, dy):

        self.coordenadaX += dx 
        self.coordenadaY += dy

    def distancia(self, punto):
        """Calcula la distancia entre el propio punto y otro punto dado."""
        dx = punto.x - self.x
        dy = punto.y - self.y
        return math.sqrt(dx**2 + dy**2)
    
    import math

class Punto:
    def __init__(self, coordenadaX, coordenadaY):
        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY

    def __str__(self):
        return f"Punto: ({self.coordenadaX}, {self.coordenadaY})"

    def setXY(self, dx, dy):
        self.coordenadaX = dx 
        self.coordenadaY = dy

    def desplaza(self, dx, dy):
        self.coordenadaX += dx 
        self.coordenadaY += dy

    def distancia(self, punto):
        """Calcula la distancia entre el propio punto y otro punto dado."""
        dx = punto.coordenadaX - self.coordenadaX
        dy = punto.coordenadaY - self.coordenadaY
        return math.sqrt(dx**2 + dy**2)


# ----------- MAIN -----------

def menu():
    print("\n===== MENÚ DE PUNTOS =====")
    print("1. Mostrar puntos")
    print("2. Mover (desplazar) un punto")
    print("3. Cambiar coordenadas de un punto")
    print("4. Calcular distancia entre los puntos")
    print("5. Salir")

# Crear dos puntos de ejemplo
punto1 = Punto(3, 4)
punto2 = Punto(0, 0)

menu()
opcion = int(input("¿Qué desea hacer?: "))

while opcion != 5:
    if opcion == 1:
        print(punto1)
        print(punto2)

    elif opcion == 2:
        dx = int(input("Desplazamiento en X: "))
        dy = int(input("Desplazamiento en Y: "))
        punto1.desplaza(dx, dy)
        print("Punto desplazado correctamente.")

    elif opcion == 3:
        x = int(input("Nueva coordenada X: "))
        y = int(input("Nueva coordenada Y: "))
        punto1.setXY(x, y)
        print("Coordenadas actualizadas.")

    elif opcion == 4:
        distancia = punto1.distancia(punto2)
        print(f"La distancia entre {punto1} y {punto2} es {distancia:.2f}")

    else:
        print("Opción no válida.")

    menu()
    opcion = int(input("¿Qué desea hacer?: "))

print("Programa finalizado.")




