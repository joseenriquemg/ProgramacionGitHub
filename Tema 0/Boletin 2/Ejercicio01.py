'''
Crea una lista de enteros de longitud 10 que se inicializará con números aleatorios comprendidos 
entre 1 y 100. 

'''
# Importamos el random
import random

# Asignamos a la lista 10 valores entre 1 y 100
list = [random.randint(1,100) for _ in range (10)]

# Imprimimos la lista 
print (list)