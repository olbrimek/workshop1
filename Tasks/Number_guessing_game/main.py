import random

def get_number():
 try:
    result = int(input("Write the number: "))
    return result
 except ValueError:
     print("That's not an integer.")

def guess_the_number():
    """Main function"""
    secret_number = random.randint(1, 100)
    given_number = get_number()
    while given_number != secret_number:
        if given_number < secret_number:
            print("Too small!")
        else:
            print("Too big!")
        given_number = get_number()
    print("You Win!")
guess_the_number()




#random_number = random.randint(1, 100)
#print (random_number)
