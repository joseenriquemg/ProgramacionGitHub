import multiprocessing
import time

# --- El Productor: Lee y envía datos por la tubería ---
def lector_fichero(ruta_archivo, conexion_envio):
    try:
        with open(ruta_archivo, 'r') as f:
            for linea in f:
                numero = linea.strip()
                if numero:
                    # Enviamos el número convertido a entero
                    conexion_envio.send(int(numero))
    except FileNotFoundError:
        print("Error: El archivo no existe.")
    
    # Enviamos la señal de parada (sentinel)
    conexion_envio.send(None)
    conexion_envio.close()

# --- El Consumidor: Recibe y procesa ---
def trabajador_suma(conexion_recepcion, lista_compartida):
    suma_total = 0
    while True:
        # Bloquea hasta que haya algo que recibir
        numero = conexion_recepcion.recv()
        
        if numero is None:  # Señal de fin detectada
            break
        
        # Realizamos la tarea (Suma de cuadrados)
        res = 0
        for i in range(numero):
            res += i * i
        suma_total += res
    
    # Guardamos el resultado final de este proceso
    lista_compartida.append(suma_total)
    conexion_recepcion.close()

if __name__ == "__main__":
    # 1. Crear archivo de prueba
    nombre_archivo = "datos_pipe.txt"
    with open(nombre_archivo, "w") as f:
        for _ in range(5):
            f.write("3000000\n")

    # 2. Configurar la comunicación (Pipe)
    # parent_conn recibe, child_conn envía
    receptor, emisor = multiprocessing.Pipe()
    
    # Para recuperar el resultado del proceso hijo
    manager = multiprocessing.Manager()
    resultado_final = manager.list()

    # 3. Crear y lanzar procesos
    proceso_lector = multiprocessing.Process(
        target=lector_fichero, 
        args=(nombre_archivo, emisor)
    )
    proceso_sumador = multiprocessing.Process(
        target=trabajador_suma, 
        args=(receptor, resultado_final)
    )

    print("Iniciando comunicación por Pipe...")
    start_time = time.perf_counter()

    proceso_lector.start()
    proceso_sumador.start()

    # 4. Esperar a que terminen
    proceso_lector.join()
    proceso_sumador.join()

    tiempo_total = time.perf_counter() - start_time

    print("-" * 30)
    print(f"Suma final: {resultado_final[0]}")
    print(f"Tiempo total con Pipe: {tiempo_total:.4f} segundos")