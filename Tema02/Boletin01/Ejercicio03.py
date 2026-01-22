import multiprocessing
import time

# --- Función 1: El Productor ---
# Lee el fichero y mete los datos en la cola
def lector_fichero(ruta_archivo, cola_tareas, num_consumidores):
    try:
        with open(ruta_archivo, 'r') as f:
            for linea in f:
                numero = linea.strip()
                if numero:
                    cola_tareas.put(int(numero))
    except FileNotFoundError:
        print("Error: El archivo no existe.")
    
    # Al terminar, añade un None por cada consumidor para que todos cierren
    for _ in range(num_consumidores):
        cola_tareas.put(None)

# --- Función 2: El Consumidor (Trabajador) ---
# Toma números de la cola y realiza la suma de cuadrados
def trabajador_suma(id_trabajador, cola_tareas, lista_resultados):
    print(f"Trabajador-{id_trabajador} iniciado.")
    suma_local = 0
    while True:
        numero = cola_tareas.get()
        if numero is None: # Señal de fin
            break
        
        # Simulación de tarea intensiva (suma de cuadrados hasta n)
        res = 0
        for i in range(numero):
            res += i * i
        suma_local += res
        
    lista_resultados.append(suma_local)
    print(f"Trabajador-{id_trabajador} finalizado.")

def ejecutar_prueba(num_trabajadores, archivo):
    cola = multiprocessing.Queue()
    # Usamos Manager para tener una lista compartida donde guardar resultados parciales
    manager = multiprocessing.Manager()
    resultados_parciales = manager.list()
    
    start_time = time.perf_counter()
    
    # Creamos el proceso lector (Productor)
    p_lector = multiprocessing.Process(target=lector_fichero, args=(archivo, cola, num_trabajadores))
    
    # Creamos los procesos trabajadores (Consumidores)
    procesos_trabajadores = []
    for i in range(num_trabajadores):
        p = multiprocessing.Process(target=trabajador_suma, args=(i, cola, resultados_parciales))
        procesos_trabajadores.append(p)
    
    # Arrancamos todos
    p_lector.start()
    for p in procesos_trabajadores:
        p.start()
        
    # Esperamos a que todos terminen
    p_lector.join()
    for p in procesos_trabajadores:
        p.join()
        
    tiempo_total = time.perf_counter() - start_time
    suma_final = sum(resultados_parciales)
    return tiempo_total, suma_final

if __name__ == "__main__":
    # 1. Preparación: Crear un archivo de prueba 'datos.txt'
    nombre_archivo = "datos.txt"
    with open(nombre_archivo, "w") as f:
        # 12 tareas pesadas (número 2.000.000 por línea)
        for _ in range(12):
            f.write("2000000\n")

    # 2. Comparativa con distinto número de procesos trabajadores
    configuraciones = [1, 2, 4]
    print(f"{'Trabajadores':<15} | {'Tiempo Total (s)':<18} | {'Resultado'}")
    print("-" * 55)

    for n in configuraciones:
        tiempo, resultado = ejecutar_prueba(n, nombre_archivo)
        print(f"{n:<15} | {tiempo:<18.4f} | {resultado}")