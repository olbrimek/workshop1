import random

def get_number():
    """
    Get number from user.

    Try until user gives proper number.

    :rtype: int
    :return: given number as int
    """
    while True:
        try:
            result = int(input("Guess the number: "))
            break
        except ValueError:
            print("It's not a number")

    return result


random_number = random.randint(1, 100)
print (random_number)
