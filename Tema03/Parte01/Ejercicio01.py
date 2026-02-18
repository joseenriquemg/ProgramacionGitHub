import threading
import time
import random

class Trabajador(threading.Thread):
    def __init__(self, nombre):
        # Llamamos al constructor de la clase padre
        super().__init__()
        self.nombre = nombre
        # En Python, si quieres que el programa se cierre aunque los hilos
        # sigan en el bucle infinito, puedes usar self.daemon = True
        
    def run(self):
        while True:
            print(f"Soy {self.nombre} y estoy trabajando.")
            
            # Tiempo aleatorio entre 1 y 10 segundos
            tiempo = random.randint(1, 10)
            time.sleep(tiempo)
            
            print(f"Soy {self.nombre} y he terminado de trabajar.")

# Bloque principal de ejecución
if __name__ == "__main__":
    nombres = ["Ana", "Luis", "Marta", "Carlos", "Elena"]
    
    for nombre in nombres:
        hilo = Trabajador(nombre)
        hilo.start()