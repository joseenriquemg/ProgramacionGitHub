'''
Crea un diccionario donde las claves sean el conjunto 1 de la siguiente tabla y los valores, el conjunto 2:
conjunto 1:
e i k m p q r s t u v
conjunto 2: 
p v i u m t e r k q s
El programa debe pedir una frase al usuario y debe mostrar la frase encriptada. Para ello, cada vez que encuentre
en la frase una letra del conjunto 1 la sustituirá por su correspondiente en el conjunto 2.
'''

# Añadimos el diccionario de los dos conjuntos de letra
diccionario = {
    'e': 'p',
    'i': 'v',
    'k': 'i',
    'm': 'u',
    'p': 'm',
    'q': 't',
    'r': 'e',
    's': 'r',
    't': 'k',
    'u': 'q',
    'v': 's'
}

frase = input("¿Cual es la frase que desea encriptar?").lower()

frase_encriptada = ""

for letra in frase:

    if letra in diccionario:

        frase_encriptada += diccionario[letra]

    else:

        frase_encriptada += letra

print(frase_encriptada)

    

