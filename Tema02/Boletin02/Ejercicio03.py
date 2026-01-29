import multiprocessing
import random
import os
import time

# --- DEFINICIÓN DE PROCESOS ---

def proceso_1(ruta_fichero):
    """Genera 6 notas aleatorias y las guarda en un fichero."""
    with open(ruta_fichero, 'w', encoding='utf-8') as f:
        for _ in range(6):
            # Generamos nota con decimales entre 1 y 10
            nota = round(random.uniform(1, 10), 2)
            f.write(f"{nota}\n")

def proceso_2(ruta_fichero_notas, nombre_alumno):
    """Lee notas de un alumno, calcula la media y la guarda en medias.txt."""
    try:
        with open(ruta_fichero_notas, 'r', encoding='utf-8') as f:
            notas = [float(linea.strip()) for linea in f if linea.strip()]
        
        media = sum(notas) / len(notas) if notas else 0
        
        # Escribimos en medias.txt (modo 'a' de append para no borrar lo anterior)
        # Nota: En sistemas reales se usarían "Locks", pero para este ejercicio 
        # la concurrencia de escritura simple suele funcionar.
        with open("medias.txt", "a", encoding="utf-8") as f_medias:
            f_medias.write(f"{round(media, 2)} {nombre_alumno}\n")
    except Exception as e:
        print(f"Error en P2 para {nombre_alumno}: {e}")

def proceso_3():
    """Busca la nota máxima en medias.txt e imprime el ganador."""
    max_nota = -1.0
    ganador = ""
    
    if not os.path.exists("medias.txt"):
        print("El archivo medias.txt no existe.")
        return

    with open("medias.txt", "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.split()
            if len(partes) >= 2:
                nota = float(partes[0])
                nombre = partes[1]
                if nota > max_nota:
                    max_nota = nota
                    ganador = nombre
    
    print("\n" + "="*30)
    print(f"🏆 NOTA MÁXIMA: {max_nota}")
    print(f"👤 ALUMNO: {ganador}")
    print("="*30)

# --- BLOQUE PRINCIPAL (MAIN) ---

if __name__ == "__main__":
    # Limpieza inicial de archivos previos
    if os.path.exists("medias.txt"): os.remove("medias.txt")
    
    num_alumnos = 10
    nombres_ficheros = [f"Alumno{i+1}.txt" for i in range(num_alumnos)]
    nombres_alumnos = [f"Alumno{i+1}" for i in range(num_alumnos)]

    # --- FASE 1: PROCESO 1 usando Pool ---
    print("Lanzando Proceso 1 (Generación de notas)...")
    with multiprocessing.Pool(processes=num_alumnos) as pool:
        pool.map(proceso_1, nombres_ficheros)

    # --- FASE 2: PROCESO 2 usando bucle for (Manual) ---
    print("Lanzando Proceso 2 (Cálculo de medias)...")
    procesos_p2 = []
    for i in range(num_alumnos):
        p = multiprocessing.Process(target=proceso_2, args=(nombres_ficheros[i], nombres_alumnos[i]))
        procesos_p2.append(p)
        p.start()

    # Esperamos a que todos los procesos P2 terminen (Sincronización)
    for p in procesos_p2:
        p.join()

    # --- FASE 3: PROCESO 3 ---
    print("Lanzando Proceso 3 (Búsqueda de máximo)...")
    proceso_3()