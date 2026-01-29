import multiprocessing
import os
from datetime import datetime

def proceso_filtro(ruta_fichero, año_objetivo, cola_comunicacion):
    """Lee el fichero y filtra películas por año."""
    try:
        # Verificamos si la ruta existe realmente antes de abrir
        if not os.path.exists(ruta_fichero):
            print(f"\n[P1] ❌ ERROR: No se encuentra el archivo en: {ruta_fichero}")
            return

        with open(ruta_fichero, 'r', encoding='utf-8') as f:
            for linea in f:
                linea = linea.strip()
                if not linea or ';' not in linea: continue
                
                try:
                    nombre, año_estreno = linea.split(';')
                    if año_estreno.strip() == str(año_objetivo):
                        print(f"[P1] ✨ Encontrada: {nombre}")
                        cola_comunicacion.put(nombre)
                except ValueError:
                    continue
        
    finally:
        cola_comunicacion.put(None)

def proceso_escritura(año_objetivo, cola_comunicacion, directorio_salida):
    """Guarda las películas filtradas en la misma carpeta que el script."""
    nombre_archivo = f"peliculas{año_objetivo}.txt"
    # Guardamos el resultado en la misma carpeta del script
    ruta_salida = os.path.join(directorio_salida, nombre_archivo)
    
    contador = 0
    with open(ruta_salida, 'w', encoding='utf-8') as f:
        while True:
            pelicula = cola_comunicacion.get()
            if pelicula is None:
                break
            f.write(f"{pelicula}\n")
            contador += 1
            
    print(f"[P2] ✅ Guardadas {contador} películas en: {ruta_salida}")

if __name__ == "__main__":
    # --- OBTENER RUTA AUTOMÁTICA ---
    # Esto detecta la carpeta real donde está este script .py
    dir_del_script = os.path.dirname(os.path.abspath(__file__))
    
    print(f"--- Buscador de Películas ---")
    print(f"La carpeta del script es: {dir_del_script}")
    
    try:
        nombre_fichero = input("Introduce el nombre del fichero (ej: cine.txt): ").strip()
        # Si el usuario solo pone el nombre, le añadimos la ruta de la carpeta del script
        if not os.path.isabs(nombre_fichero):
            ruta_fichero_completa = os.path.join(dir_del_script, nombre_fichero)
        else:
            ruta_fichero_completa = nombre_fichero

        año = int(input("Introduce el año de estreno (Ejemplo: 1999): "))
        
        # Validación de año
        if año >= datetime.now().year:
            print("Error: El año debe ser menor al actual.")
            exit()

        # --- MULTIPROCESSING ---
        cola = multiprocessing.Queue()
        p1 = multiprocessing.Process(target=proceso_filtro, args=(ruta_fichero_completa, año, cola))
        # Pasamos el directorio para que el archivo de salida se cree en el mismo sitio
        p2 = multiprocessing.Process(target=proceso_escritura, args=(año, cola, dir_del_script))
        
        p1.start()
        p2.start()
        p1.join()
        p2.join()

    except ValueError:
        print("Error: El año debe ser un número entero.")