import multiprocessing
import time

def sumar_hasta_n(n):
    """Calcula la suma desde 1 hasta n y muestra el resultado."""
    suma = sum(range(1, n + 1))
    print(f"[Proceso {multiprocessing.current_process().name}] La suma de 1 hasta {n} es: {suma}")

if __name__ == "__main__":
    # Lista de valores hasta los que queremos sumar
    valores = [100, 500, 1000, 5000]
    
    # Lista para guardar las instancias de los procesos
    procesos = []

    # Creación e inicio de los procesos
    for v in valores:
        p = multiprocessing.Process(target=sumar_hasta_n, args=(v,))
        procesos.append(p)
        p.start()

    # Esperar a que todos los procesos terminen (Sincronización)
    for p in procesos:
        p.join()

    print("Todos los procesos han terminado satisfactoriamente.")