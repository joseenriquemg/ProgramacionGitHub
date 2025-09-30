def esVocal (letra: str) -> bool:

    return letra.lower() in "aeiou"

letter = input("Introduzca una letra:")

print(esVocal(letter))