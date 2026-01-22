import multiprocessing

def sumar_rango(inicio, fin):
    """
    Suma todos los números entre inicio y fin (inclusive).
    Maneja el caso donde el primero sea mayor que el segundo.
    """
    real_inicio = min(inicio, fin)
    real_fin = max(inicio, fin)
    
    # Calculamos la suma
    suma = sum(range(real_inicio, real_fin + 1))
    
    # Imprimimos desde el proceso hijo
    print(f"Proceso {multiprocessing.current_process().name}: "
          f"Suma de {inicio} a {fin} = {suma}")
    
    return suma # El Pool permite recolectar los retornos si fuera necesario

if __name__ == "__main__":
    # Definimos la lista de tuplas con los argumentos para cada ejecución
    argumentos = [
        (1, 10),
        (20, 15),
        (100, 50),
        (5, 5),
        (10, 20)
    ]
    
    print(f"Lanzando {len(argumentos)} tareas usando un Pool...\n")

    # Creamos un Pool de procesos
    # Por defecto usa tantos procesos como núcleos tenga la CPU
    with multiprocessing.Pool() as pool:
        # starmap descompone cada tupla y la pasa como argumentos a la función
        resultados = pool.starmap(sumar_rango, argumentos)

    # Una vez fuera del bloque 'with', el pool se ha cerrado y sincronizado (join implícito)
    print("\n[Principal]: Todos los procesos del Pool han terminado.")
    print(f"Resultados obtenidos: {resultados}")