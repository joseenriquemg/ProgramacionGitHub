import multiprocessing

# --- El Productor: Lee y envía pares por la tubería ---
def lector_fichero(ruta_archivo, conexion_envio):
    try:
        with open(ruta_archivo, 'r') as f:
            for linea in f:
                partes = linea.split()
                if len(partes) == 2:
                    # Enviamos la tupla (num1, num2) directamente
                    num1, num2 = int(partes[0]), int(partes[1])
                    conexion_envio.send((num1, num2))
    except FileNotFoundError:
        print("Error: El archivo no existe.")
    
    # Enviamos la señal de parada (None)
    conexion_envio.send(None)
    conexion_envio.close()

# --- El Consumidor: Recibe y procesa los pares ---
def trabajador_suma(conexion_recepcion):
    print(f"Proceso {multiprocessing.current_process().name} esperando datos...")
    
    while True:
        # Recibimos el objeto (bloqueante hasta que llegue algo)
        datos = conexion_recepcion.recv()
        
        if datos is None:  # Señal de fin
            break
        
        inicio, fin = datos
        real_inicio = min(inicio, fin)
        real_fin = max(inicio, fin)
        
        resultado = sum(range(real_inicio, real_fin + 1))
        print(f"Resultado suma ({inicio} a {fin}): {resultado}")
    
    conexion_recepcion.close()

if __name__ == "__main__":
    # 1. Crear archivo de prueba
    nombre_archivo = "datos_rango.txt"
    with open(nombre_archivo, "w") as f:
        f.write("1 100\n")
        f.write("50 10\n")
        f.write("5 5\n")
        f.write("10 20\n")

    # 2. Crear la tubería (Pipe)
    # conexion_padre recibe, conexion_hijo envía
    receptor, emisor = multiprocessing.Pipe()

    # 3. Crear los procesos
    p_lector = multiprocessing.Process(
        target=lector_fichero, 
        args=(nombre_archivo, emisor),
        name="Lector"
    )
    p_sumador = multiprocessing.Process(
        target=trabajador_suma, 
        args=(receptor,),
        name="Sumador"
    )

    # 4. Iniciar y esperar
    p_lector.start()
    p_sumador.start()

    p_lector.join()
    p_sumador.join()

    print("\n[Principal]: Procesamiento con Pipe finalizado.")