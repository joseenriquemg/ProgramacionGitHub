'''
Crea una clase llamada Articulo con los siguientes atributos: nombre, precio (sin IVA), iva (siempre será 21) y 
cuantosQuedan (representa cuántos quedan en el almacén).
Añade los siguientes métodos:
- Constructor con 3 parámetros que asigne valores a nombre, precio y cuantosQuedan. El IVA siempre lo pondrá a 21.
- Método getPVP que devuelva el precio de venta al público (PVP) con iva incluido. 
- Método getPVPDescuento que devuelva el PVP con un descuento pasado como argumento. 
- Método vender que actualiza los atributos del objeto tras vender una cantidad ‘x’ (si es posible). 
Devolverá true si ha sido posible (false en caso contrario). La cantidad a vender se pasará como argumento al método.
- Método almacenar que actualiza los atributos del objeto tras almacenar una cantidad ‘x’. La cantidad a almacenar se pasará como argumento.
- Crear también los métodos __str__, __eq__ y __lt__. Se considera que dos  artículos son iguales si tienen el mismo nombre. Los artículos se ordenarán de menor a mayor por el nombre.
'''

class Articulo:

    def __init__(self, nombre, precio, cuantosQuedan):
        self.nombre = nombre
        self.precio = precio
        self.IVA = 21
        self.cuantosQuedan = cuantosQuedan

    def getPVP(self):
        return self.precio * (1 + self.IVA / 100)
    
    def getPVPDescuento(self, descuento):
        pvp = self.getPVP()
        precio_final = pvp * (1 - descuento / 100)
        return precio_final 
    
    def vender(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser mayor que 0.")
            return False
        
        if cantidad <= self.cuantosQuedan:
            self.cuantosQuedan -= cantidad
            print("Venta realizada con éxito.")
            return True
        else:
            print("No se dispone de suficiente cantidad.")
            return False 
        
    def almacenar(self, cantidad):
        if cantidad > 0:
            self.cuantosQuedan += cantidad
            print("Se han añadido las unidades con éxito.")
        else:
            print("Cantidad inválida. No se puede añadir.")
    
    def __str__(self):
        return f"Artículo: {self.nombre} | Precio: {self.precio:.2f}€ | Stock: {self.cuantosQuedan}"
    
    def __eq__(self, otroArticulo):
        return self.nombre == otroArticulo.nombre
    
    def __lt__(self, otroArticulo):
        return self.nombre < otroArticulo.nombre

def menu():
    print("\n------ MENÚ DE GESTIÓN DE ARTÍCULOS ------")
    print("1. Vender artículo")
    print("2. Almacenar artículo")
    print("3. Comparar artículos (por nombre)")
    print("4. Mostrar artículos")
    print("5. Salir")
    print("------------------------------------------")

# Crear algunos artículos de ejemplo
articulo1 = Articulo("Camiseta", 25.0, 10)
articulo2 = Articulo("Pantalón", 40.0, 5)

# Mostrar menú inicial
menu()
opcion = int(input("¿Qué desea hacer? "))

while opcion != 5:
    if opcion == 1:
        cantidad = int(input("¿Cuántas unidades desea vender del primer artículo? "))
        articulo1.vender(cantidad)

    elif opcion == 2:
        cantidad = int(input("¿Cuántas unidades desea almacenar en el primer artículo? "))
        articulo1.almacenar(cantidad)

    elif opcion == 3:
        print("¿El primer artículo es menor alfabéticamente que el segundo?")
        print(articulo1.__lt__(articulo2))

    elif opcion == 4:
        print(articulo1)
        print(articulo2)

    else:
        print("Opción no válida. Intente de nuevo.")

    # Volver a mostrar el menú
    menu()
    opcion = int(input("¿Qué desea hacer? "))

print("Programa finalizado.")