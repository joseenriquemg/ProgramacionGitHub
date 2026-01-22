import multiprocessing
import time

# Función que realiza el trabajo pesado
def tarea_pesada(n):
    suma = 0
    for i in range(n):
        suma += i * i
    return suma

def ejecutar_con_pool(num_procesos, datos):
    start_time = time.perf_counter()
    
    # Creamos el Pool con el número de procesos deseado
    with multiprocessing.Pool(processes=num_procesos) as pool:
        # map reparte la lista 'datos' entre los procesos del pool
        resultados = pool.map(tarea_pesada, datos)
    
    end_time = time.perf_counter()
    return end_time - start_time

if __name__ == "__main__":
    # Configuración del experimento
    # 10 tareas pesadas, cada una calcula hasta 10,000,000
    tareas = [10_000_000] * 10
    
    configuraciones = [1, 2, 4, 8]
    resultados_tiempo = {}

    print(f"Iniciando comparativa con {len(tareas)} tareas...")
    print("-" * 45)

    for n in configuraciones:
        tiempo = ejecutar_con_pool(n, tareas)
        resultados_tiempo[n] = tiempo
        print(f"Procesos: {n} | Tiempo total: {tiempo:.4f} segundos")

    print("-" * 45)
    print("Análisis finalizado.")