numbers = []

sum = 0

numbers_user = int(input("Introduce a number:"))

while(numbers_user >= 0):

    numbers.append(numbers_user)

    numbers_user = int(input("Introduce a number:"))

for number in numbers:

    sum += number

print("La suma de sus numeros resulta:" , sum)