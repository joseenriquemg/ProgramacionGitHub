import multiprocessing
import os

# --- PROCESO 1: Filtrar por Departamento ---
def proceso_1(nombre_depto, cola_salida):
    if not os.path.exists("salarios.txt"):
        cola_salida.put(None)
        return

    with open("salarios.txt", "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea: continue
            
            partes = linea.split(";")
            if len(partes) == 4:
                nombre, apellido, salario, depto = partes
                # Enviamos al Proceso 2: Nombre;Apellido;Salario (sin depto)
                if depto.strip().lower() == nombre_depto.strip().lower():
                    cola_salida.put(f"{nombre};{apellido};{salario}")
    
    cola_salida.put(None)

# --- PROCESO 2: Filtrar por Salario Mínimo ---
def proceso_2(salario_min, cola_entrada, cola_salida):
    while True:
        datos = cola_entrada.get()
        if datos is None: 
            break
        
        partes = datos.split(";")
        salario_actual = float(partes[2])
        
        if salario_actual >= salario_min:
            # Enviamos tal cual llega
            cola_salida.put(datos)
            
    cola_salida.put(None)

# --- PROCESO 3: Escritura Final + Usuario Manual ---
def proceso_3(cola_entrada, datos_extra):
    """
    Escribe los empleados filtrados y añade al final el usuario introducido por teclado.
    """
    with open("empleados.txt", "w", encoding="utf-8") as f:
        # 1. Escribir los datos que vienen del flujo de procesos
        while True:
            datos = cola_entrada.get()
            if datos is None:
                break
            
            nombre, apellido, salario = datos.split(";")
            f.write(f"{apellido} {nombre}, {salario}\n")
        
        # 2. Añadir el usuario extra que pidió el Main (si se proporcionó)
        if datos_extra:
            f.write(f"{datos_extra}\n")

# --- MAIN ---
if __name__ == "__main__":
    # Datos para los filtros
    depto_input = input("Departamento a buscar: ").strip()
    salario_min_input = float(input("Salario mínimo: "))
    
    # DATOS EXTRA: Nombre y apellido que se añadirán a empleados.txt
    print("\n--- Registro manual ---")
    nombre_extra = input("Introduce un nombre para añadir a empleados.txt: ")
    apellido_extra = input("Introduce su apellido: ")
    salario_extra = input("Introduce su salario: ")
    
    # Formateamos el registro manual igual que el resto
    registro_manual = f"{apellido_extra} {nombre_extra}, {salario_extra}"

    # Colas de comunicación
    q1_a_2 = multiprocessing.Queue()
    q2_a_3 = multiprocessing.Queue()

    # Lanzar procesos
    p1 = multiprocessing.Process(target=proceso_1, args=(depto_input, q1_a_2))
    p2 = multiprocessing.Process(target=proceso_2, args=(salario_min_input, q1_a_2, q2_a_3))
    # Al proceso 3 le pasamos la cola Y el registro manual
    p3 = multiprocessing.Process(target=proceso_3, args=(q2_a_3, registro_manual))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("\n>>> Archivo 'empleados.txt' actualizado con éxito.")