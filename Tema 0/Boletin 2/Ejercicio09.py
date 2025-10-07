'''
Crea un diccionario donde las claves son las letras del abecedario y los valores, la puntuación
para cada letra, como en el Scrabble. El programa le pedirá una palabra al usuario y se mostrará 
por pantalla la puntuación que tiene la palabra en total.
'''

# Diccionario con todas las letras y puntuaciones
scrabble_puntuacion = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1,
    'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
    'K': 8, 'L': 1, 'M': 3, 'N': 1, 'Ñ': 8,
    'O': 1, 'P': 3, 'Q': 5, 'R': 1, 'S': 1,
    'T': 1, 'U': 1, 'V': 4, 'W': 8, 'X': 8,
    'Y': 4, 'Z': 10
}

# Funcion que recorre las letras de una palabra y suma sus puntuaciones
def puntaje_palabra(palabra):

    # Devuelve la suma de las letras que estan pasandolas a mayusculas y las que no estan les da valor 0
    return sum(scrabble_puntuacion.get(letra.upper(), 0) for letra in palabra)

# Preguntamos la palabra de juego al usuario
palabra = input("¿Cual es su palabra?")

# Imprimimos el resultado
print("Con la palabra", palabra, "su puntuacion es", puntaje_palabra(palabra))