import threading
import time

# Variable global compartida (nivel de módulo)
contador = 0

class HiloContador(threading.Thread):
    def run(self):
        global contador
        # Mientras sea menor a 1000 incrementamos
        while contador < 1000:
            # Leemos el valor actual
            valor_actual = contador
            
            # Simula un cambio de contexto para forzar el error (race condition)
            time.sleep(0.001) 
            
            # Incrementamos y guardamos
            contador = valor_actual + 1
            
            # Imprimimos (esto ralentiza y ayuda a ver el caos)
            # print(f"{self.name} cuenta: {contador}")

if __name__ == "__main__":
    hilos = []
    
    # Creamos 10 hilos
    for i in range(10):
        t = HiloContador()
        hilos.append(t)
        t.start()
        
    # Esperamos a que todos terminen para ver el resultado final
    for t in hilos:
        t.join()
        
    print(f"Resultado final del contador: {contador}")
    print("Si el resultado es mayor a 1000, ha ocurrido una condición de carrera.")