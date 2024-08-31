import random

def get_number():
 try:
    result = int(input("Guess the number: "))
    return result
 except ValueError:
     print("That's not an integer.")




#random_number = random.randint(1, 100)
#print (random_number)
