import multiprocessing
import random
import time

def proceso_1(cola_salida):
    """Genera 10 IPs aleatorias y las envía a la cola 1."""
    print("[P1] Generando IPs...")
    for _ in range(10):
        ip = f"{random.randint(1, 254)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        print(f"[P1] Envía: {ip}")
        cola_salida.put(ip)
    # Enviamos una señal de fin (None) para que P2 sepa que no hay más datos
    cola_salida.put(None)

def proceso_2(cola_entrada, cola_salida):
    """Filtra IPs por Clase A, B o C y las envía a la cola 2."""
    while True:
        ip = cola_entrada.get()
        if ip is None: # Si recibe la señal de fin
            cola_salida.put(None)
            break
        
        primer_octeto = int(ip.split('.')[0])
        
        # Filtro de clases A, B y C
        if 1 <= primer_octeto <= 126 or 128 <= primer_octeto <= 191 or 192 <= primer_octeto <= 223:
            print(f"[P2] ✅ IP válida aceptada: {ip}")
            cola_salida.put(ip)
        else:
            print(f"[P2] ❌ IP descartada (fuera de clase A, B o C): {ip}")

def proceso_3(cola_entrada):
    """Lee las IPs filtradas e imprime su clase."""
    while True:
        ip = cola_entrada.get()
        if ip is None:
            break
            
        primer_octeto = int(ip.split('.')[0])
        clase = ""
        
        if 1 <= primer_octeto <= 126: clase = "Clase A"
        elif 128 <= primer_octeto <= 191: clase = "Clase B"
        elif 192 <= primer_octeto <= 223: clase = "Clase C"
        
        print(f"[P3] RESULTADO: IP {ip} -> {clase}")

if __name__ == "__main__":
    # Colas de comunicación (Enlazan P1->P2 y P2->P3)
    cola_p1_a_p2 = multiprocessing.Queue()
    cola_p2_a_p3 = multiprocessing.Queue()

    # Creación de procesos
    p1 = multiprocessing.Process(target=proceso_1, args=(cola_p1_a_p2,))
    p2 = multiprocessing.Process(target=proceso_2, args=(cola_p1_a_p2, cola_p2_a_p3))
    p3 = multiprocessing.Process(target=proceso_3, args=(cola_p2_a_p3,))

    # Lanzamiento en orden
    p1.start()
    p2.start()
    p3.start()

    # Esperar a que terminen
    p1.join()
    p2.join()
    p3.join()

    print("\n--- Todos los procesos han finalizado ---")