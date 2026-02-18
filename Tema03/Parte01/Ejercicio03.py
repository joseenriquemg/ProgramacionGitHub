import threading
import random
import time

# Variables compartidas ("de clase")
numero_oculto = 0
juego_terminado = False

class HiloAdivino(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def run(self):
        global juego_terminado
        
        while not juego_terminado:
            propuesta = random.randint(0, 100)
            
            if propuesta == numero_oculto:
                if not juego_terminado: # Doble comprobación
                    juego_terminado = True
                    print(f"¡{self.nombre} HA ACERTADO! El número era {numero_oculto}")
            else:
                if juego_terminado:
                    # Si ya acabó, terminamos silenciosamente o avisamos
                    return

if __name__ == "__main__":
    # Generamos el número oculto
    numero_oculto = random.randint(0, 100)
    print("--- El número secreto se ha generado ---")

    hilos = []
    for i in range(10):
        t = HiloAdivino(f"Hilo-{i+1}")
        hilos.append(t)
        t.start()