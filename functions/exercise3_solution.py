import seaborn as sns
import math

day = [1, 2, 3, 4, 5, 6, 7]
avg_temperature = [14, 9, 3, 11, 18, 27, 6]

birthday = "4 September 1996"
place_of_birth = "London"
current_city = "London"


def greetings(name):
    # Please write a greetings function
    return "Hello " + name

greetings("Sam")


def difference(number1, number2):
    # Write a function that calculates the difference between two numbers
    diff = number1 - number2
    return diff


difference(14.99, 12.49)

print(greetings("Sam"))


def print_introduction(birthday, place_of_birth, current_city):
    print("I was born on " + birthday + " in " + place_of_birth + " and now I live in " + current_city)


print_introduction(birthday, place_of_birth, current_city)

def change_current_city(new_city):
    global current_city
    current_city = new_city

change_current_city("New York")
print_introduction(birthday, place_of_birth, current_city)


def mile2km(mile):
    pass

def km2mile(km):
    pass






