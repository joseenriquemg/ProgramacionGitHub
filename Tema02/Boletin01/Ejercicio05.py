import multiprocessing

def sumar_rango(inicio, fin):
    """
    Suma todos los números entre inicio y fin, 
    independientemente de cuál sea mayor.
    """
    # Determinamos el menor y el mayor para el rango
    real_inicio = min(inicio, fin)
    real_fin = max(inicio, fin)
    
    # El rango en Python es exclusivo en el límite superior, sumamos 1
    suma = sum(range(real_inicio, real_fin + 1))
    
    print(f"Proceso {multiprocessing.current_process().name}: "
          f"La suma entre {inicio} y {fin} es {suma}")

if __name__ == "__main__":
    # Definimos los casos de prueba (tuplas de argumentos)
    casos = [
        (1, 10),    # Normal
        (10, 1),    # Primero mayor que el segundo
        (5, 5),     # Iguales
        (20, 15)    # Otro caso invertido
    ]
    
    procesos = []

    # Crear y lanzar los procesos
    for i, args in enumerate(casos):
        p = multiprocessing.Process(
            target=sumar_rango, 
            args=args, 
            name=f"Sumador-{i+1}"
        )
        procesos.append(p)
        p.start()

    # Esperar a que todos los procesos terminen
    for p in procesos:
        p.join()

    print("\n[Principal]: Todos los procesos han terminado con éxito.")