import random

secret_number = random.randint(1,101)

number_user = int(input("Try to guess the number (1-100):"))

while(number_user != secret_number):

    if (secret_number > number_user):
    
        print("The number is greater.")

    else:

        print("The number is less.")

    number_user = int(input("Try to guess the number:"))

print ("You win!")