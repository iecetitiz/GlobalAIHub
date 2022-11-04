import seaborn as sns
import math
import matplotlib.pyplot as plt

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

day =[1, 2, 3, 4, 5, 6, 7]
avg_temperature = [14, 9, 3, 11, 18, 27, 6]
sns.barplot(x = day, y = avg_temperature)
plt.show()


def mile2km(miles):
    km = miles * 1.60934
    return km


def km2mile(km):
    miles = km / 1.60934
    return miles

def pound_kilogram(quantity, mode):
    assert mode == "pound2kg" or mode == "kg2pound", "Invalid argument!"

    if mode == "pound2kg":
        conv_quan = quantity * 0.45354

    else:
        conv_quan = quantity / 0.45354
        return conv_quan

pound_kilogram(2, "kg2pound")

assert math.isclose(pound_kilogram(2.20462, "pound2kg"), 1, abs_tol=1e-5), "Test failed for mode \"pound2kg\"!"
assert math.isclose(pound_kilogram(43, "kg2pound"), 94.79926, abs_tol=1e-5), "Test failed for mode \"kg2pound\"!"
print("Test passed!")






