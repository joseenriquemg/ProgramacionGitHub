'''
Diseñar la clase CuentaCorriente, que almacena los datos DNI, nombre y el saldo. 
Añade los siguientes constructores:
Con el DNI del titular de la cuenta y un saldo inicial. El nombre se inicializará a cadena vacía.
Con el DNI, nombre y el saldo inicial.
Las operaciones típicas de una cuenta corriente son:
Sacar dinero: el método debe indicar si ha sido posible llevar a cabo la operación, si existe saldo suficiente. 
Si es posible llevar a cabo la operación se resta la cantidad a sacar al saldo de la cuenta.
Ingresar dinero: se incrementa el saldo.
Crear también los métodos __str__, __eq__ y __lt__. Se considera que dos cuentas corrientes son iguales si tienen 
el mismo DNI. Las cuentas corrientes se ordenarán de menor a mayor por el saldo.
'''

class CuentaCorriente:

    def __init__(self, DNI, saldo, nombre = ''):
        self.DNI = DNI
        self.nombre = nombre
        self.saldo = saldo

    def sacar_dinero(self, cantidad):

        if (cantidad < self.saldo):

            self.saldo -= cantidad

            print("Dinero retirado con exito")

        else:

            print("Saldo insuficiente")

    def ingresar_dinero(self, cantidad):

        if (cantidad > 0):

            self.saldo += cantidad

            print("Dinero añadido con exito")

        else:

            print("No puede ingresar una cantidad inferior a 1")


    def __str__(self):
        
        return ("Cuenta: DNI -> " + self.DNI + " Saldo -> " + str(self.saldo) + " Nombre -> " + self.nombre)


    def __eq__(self, otra_cuenta):

        if (self.DNI == otra_cuenta.DNI):

            return True
        
        else:

            return False
        
    def __lt__(self, otra_cuenta):

        return self.saldo <= otra_cuenta.saldo


def menu():

    print()
    print("1. Ingresar dinero")
    print("2. Retirar dinero")
    print("3. Comprobar cuentas")
    print("4. Mostrar Cuentas")
    
Cuenta1 = CuentaCorriente('296272A', 5000, 'Jenri')
Cuenta2 = CuentaCorriente('123453B', 2000000, 'Juan')

menu()

opcion = int(input("¿Que desea hacer?"))

while (opcion != 5):

    if (opcion == 1):

        ingresos = int(input("¿Cuanto desea añadir?"))

        Cuenta1.ingresar_dinero(ingresos)

    elif (opcion == 2):

        retiradas = int(input("¿Cuanto desea añadir?"))

        Cuenta1.sacar_dinero(retiradas)

    elif (opcion == 3):

        print(Cuenta1.__lt__(Cuenta2))

    elif (opcion == 4):

        print(Cuenta1)


    menu()

    opcion = int(input("¿Que desea hacer?"))

        

    

