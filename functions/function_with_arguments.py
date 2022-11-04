def print_cars_and_names(car, name, color):
    print(car, name, color)


print_cars_and_names(name = 'elif', color = 'red', car = 'hyundai')


def childs(*kids):
    print("the youngest child is " + kids[4])


childs("ece", "mert", "selin", "burak", "bora")

def my_function(food):
    for x in food:
        print(x)


my_function("ece")