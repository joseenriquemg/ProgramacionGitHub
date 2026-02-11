import multiprocessing
import random
import os

# --- PROCESO 1: Generador de archivos diarios ---
def proceso_1(dia):
    nombre_fichero = f"{dia:02d}-12.txt"
    with open(nombre_fichero, "w") as f:
        for _ in range(24):
            # Genera temp entre 0 y 20 con 2 decimales
            temp = round(random.uniform(0, 20), 2)
            f.write(f"{temp}\n")

# --- PROCESO 2: Buscador de Máximas ---
def proceso_2(dia):
    nombre_fichero = f"{dia:02d}-12.txt"
    try:
        with open(nombre_fichero, "r") as f:
            temperaturas = [float(line.strip()) for line in f.readlines()]
        maxima = max(temperaturas)
        # Modo "a" (append) para no sobrescribir los resultados de otros días
        with open("maximas.txt", "a") as f_out:
            f_out.write(f"{dia:02d}-12:{maxima}\n")
    except FileNotFoundError:
        pass

# --- PROCESO 3: Buscador de Mínimas ---
def proceso_3(dia):
    nombre_fichero = f"{dia:02d}-12.txt"
    try:
        with open(nombre_fichero, "r") as f:
            temperaturas = [float(line.strip()) for line in f.readlines()]
        minima = min(temperaturas)
        with open("minimas.txt", "a") as f_out:
            f_out.write(f"{dia:02d}-12:{minima}\n")
    except FileNotFoundError:
        pass

# --- MAIN: Orquestador ---
if __name__ == "__main__":
    # Limpiar archivos de resultados previos si existen
    for f in ["maximas.txt", "minimas.txt"]:
        if os.path.exists(f): os.remove(f)

    # PARTE 1: Lanzar Proceso 1 simultáneamente (31 veces)
    print("Generando archivos de temperaturas...")
    pool1 = []
    for dia in range(1, 32):
        p = multiprocessing.Process(target=proceso_1, args=(dia,))
        pool1.append(p)
        p.start()

    # Esperar a que todos los ficheros se creen antes de pasar al siguiente paso
    for p in pool1:
        p.join()

    # PARTE 2: Lanzar Procesos 2 y 3 simultáneamente (31 veces cada uno)
    print("Calculando máximas y mínimas...")
    pool_analisis = []
    for dia in range(1, 32):
        p2 = multiprocessing.Process(target=proceso_2, args=(dia,))
        p3 = multiprocessing.Process(target=proceso_3, args=(dia,))
        pool_analisis.extend([p2, p3])
        p2.start()
        p3.start()

    for p in pool_analisis:
        p.join()

    print("Proceso finalizado con éxito.")