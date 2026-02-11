import multiprocessing
import os

# --- PROCESO 1 ---
def proceso_1(nombre_depto, cola_salida):
    if not os.path.exists("salarios.txt"):
        return # El error se gestiona en el Main
    
    with open("salarios.txt", "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(";")
            if len(partes) == 4:
                nombre, apellido, salario, depto = partes
                if depto.strip().lower() == nombre_depto.strip().lower():
                    cola_salida.put(f"{nombre};{apellido};{salario}")
    cola_salida.put(None)

# --- PROCESO 2 ---
def proceso_2(salario_min, cola_entrada, cola_salida):
    while True:
        datos = cola_entrada.get()
        if datos is None: break
        
        salario_actual = float(datos.split(";")[2])
        if salario_actual >= salario_min:
            cola_salida.put(datos)
    cola_salida.put(None)

# --- PROCESO 3 ---
def proceso_3(cola_entrada):
    with open("empleados.txt", "w", encoding="utf-8") as f:
        while True:
            datos = cola_entrada.get()
            if datos is None: break
            nombre, apellido, salario = datos.split(";")
            f.write(f"{apellido} {nombre}, {salario}\n")

# --- MAIN (Orquestador) ---
if __name__ == "__main__":
    # 1. Pedir datos ANTES de lanzar procesos (Evita errores en consola)
    depto_input = input("Introduce departamento (ej. Desarrollo): ").strip()
    try:
        salario_input = float(input("Introduce salario mínimo: "))
    except:
        salario_input = 0.0

    # 2. Crear colas
    q1 = multiprocessing.Queue()
    q2 = multiprocessing.Queue()

    # 3. Configurar procesos
    p1 = multiprocessing.Process(target=proceso_1, args=(depto_input, q1))
    p2 = multiprocessing.Process(target=proceso_2, args=(salario_input, q1, q2))
    p3 = multiprocessing.Process(target=proceso_3, args=(q2,))

    # 4. Arrancar
    p1.start()
    p2.start()
    p3.start()

    # 5. Esperar a que terminen
    p1.join()
    p2.join()
    p3.join()

    print("\n>>> Operación terminada. Revisa 'empleados.txt'.")