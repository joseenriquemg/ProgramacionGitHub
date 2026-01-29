import multiprocessing
import os

def contar_vocal(vocal, ruta_fichero):
    """
    Función que cuenta cuántas veces aparece una vocal específica en un fichero.
    """
    vocal = vocal.lower()
    contador = 0
    try:
        # Usamos encoding='utf-8' para evitar errores con tildes o la 'ñ'
        with open(ruta_fichero, 'r', encoding='utf-8') as f:
            for linea in f:
                contador += linea.lower().count(vocal)
        return (vocal, contador)
    except FileNotFoundError:
        return (vocal, "Error: Fichero no encontrado")
    except Exception as e:
        return (vocal, f"Error inesperado: {e}")

if __name__ == "__main__":
    # --- SOLUCIÓN PARA LA DETECCIÓN DEL ARCHIVO ---
    # Obtenemos la ruta absoluta de la carpeta donde está este script (.py)
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    
    # Nombre de tu archivo (asegúrate de que se llame así y esté en la misma carpeta)
    nombre_archivo = "mi_texto.txt" 
    
    # Construimos la ruta completa al archivo
    ruta_completa = os.path.join(directorio_actual, nombre_archivo)

    # --- DIAGNÓSTICO (Para que veas qué falla en la consola) ---
    print(f"Directorio de trabajo: {os.getcwd()}")
    print(f"Buscando archivo en: {ruta_completa}")
    
    if not os.path.exists(ruta_completa):
        print(f"❌ ERROR: El archivo '{nombre_archivo}' no existe en esa carpeta.")
        # Creamos un archivo de prueba rápido si no existe para que no falle el ejemplo
        with open(ruta_completa, "w", encoding="utf-8") as f:
            f.write("Hola, este es un archivo de prueba creado automáticamente.")
        print(f"✅ Se ha creado un archivo de prueba: {nombre_archivo}")

    # --- PROCESAMIENTO PARALELO ---
    vocales = ['a', 'e', 'i', 'o', 'u']
    
    # Lanzamos los 5 procesos en paralelo
    with multiprocessing.Pool(processes=5) as pool:
        # Preparamos los argumentos (vocal, ruta_completa)
        argumentos = [(v, ruta_completa) for v in vocales]
        resultados = pool.starmap(contar_vocal, argumentos)

    # --- RESULTADOS ---
    print("\n" + "="*30)
    print(f"RESULTADOS PARA: {nombre_archivo}")
    print("="*30)
    for vocal, cuenta in resultados:
        print(f"Vocal '{vocal.upper()}': {cuenta}")