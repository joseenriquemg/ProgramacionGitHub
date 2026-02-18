import threading

class HiloVocal(threading.Thread):
    def __init__(self, vocal, texto):
        super().__init__()
        self.vocal_busqueda = vocal
        self.texto = texto

    def run(self):
        # Convertimos a minúsculas para buscar
        texto_minus = self.texto.lower()
        
        # Método pythonico para contar: texto.count(vocal)
        # Pero lo haremos con bucle para imitar la lógica de algoritmos clásicos
        cuenta = 0
        for letra in texto_minus:
            if letra == self.vocal_busqueda:
                cuenta += 1
                
        print(f"La vocal '{self.vocal_busqueda}' aparece {cuenta} veces.")

if __name__ == "__main__":
    texto = ("Esta es una frase de prueba para contar las vocales "
             "utilizando hilos en Python dentro de VS Code.")

    print(f"Analizando texto: {texto}\n")

    vocales = ['a', 'e', 'i', 'o', 'u']
    
    for v in vocales:
        HiloVocal(v, texto).start()