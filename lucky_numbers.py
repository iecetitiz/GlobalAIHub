import random


while True:
    random_numbers = random.randrange(1000)
    print(random_numbers)
    if random_numbers == 777:
        print("Founded!")
        break;