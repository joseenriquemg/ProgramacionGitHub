'''
Escribe un programa que tome una cadena de texto como entrada y genere un diccionario que cuente la
frecuencia de cada palabra en el texto.

'''
cadena = input("Introduzca la frase a analizar:")

palabras = cadena.split()

dictionary = {}

for palabra in palabras:

    if (dictionary.get(palabra)):

        dictionary[palabra] += 1

    else:

        dictionary[palabra] = 1


print(dictionary)