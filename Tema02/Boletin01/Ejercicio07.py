import multiprocessing
import time

# --- Función Lector (Productor) ---
def lector_fichero(ruta_archivo, cola_tareas):
    """Lee pares de números de un fichero y los pone en la cola."""
    try:
        with open(ruta_archivo, 'r') as f:
            for linea in f:
                partes = linea.split()
                if len(partes) == 2:
                    # Convertimos a int y enviamos la tupla (num1, num2)
                    num1, num2 = int(partes[0]), int(partes[1])
                    cola_tareas.put((num1, num2))
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_archivo}")
    
    # Enviamos la señal de parada (None)
    cola_tareas.put(None)
    print("[Lector] Lectura finalizada y señal de parada enviada.")

# --- Función Sumador (Consumidor) ---
def trabajador_suma(cola_tareas):
    """Recibe tuplas de la cola y realiza la suma del rango."""
    while True:
        datos = cola_tareas.get()
        
        if datos is None: # Señal de terminación
            break
        
        inicio, fin = datos
        real_inicio = min(inicio, fin)
        real_fin = max(inicio, fin)
        
        resultado = sum(range(real_inicio, real_fin + 1))
        
        print(f"Proceso {multiprocessing.current_process().name}: "
              f"Suma de {inicio} a {fin} = {resultado}")

if __name__ == "__main__":
    # 1. Crear un fichero de prueba
    nombre_fichero = "rangos.txt"
    with open(nombre_fichero, "w") as f:
        f.write("1 10\n")
        f.write("20 15\n")
        f.write("100 50\n")
        f.write("5 5\n")

    # 2. Configurar la comunicación
    cola = multiprocessing.Queue()

    # 3. Crear los procesos
    # Uno para leer y otro para sumar
    p_lector = multiprocessing.Process(target=lector_fichero, args=(nombre_fichero, cola))
    p_sumador = multiprocessing.Process(target=trabajador_suma, args=(cola,))

    # 4. Iniciar procesos
    p_lector.start()
    p_sumador.start()

    # 5. Esperar a que terminen
    p_lector.join()
    p_sumador.join()

    print("\n[Principal]: El procesamiento ha terminado.")