fruits = ["apple", "grape", "cherry", "apple", "banana"]
print(fruits)
print("length of list: " , len(fruits))

# a list can contain different data types

list_different_types = ["apple", 40, True]
print(type(list_different_types))

shopping_list = ["apple", "milk"]
print(shopping_list)
shopping_list.append("cd player")
print(shopping_list)
shopping_list.insert(2, "der kaffee")
shopping_list.append("book")
shopping_list.append("water")
shopping_list.append("paper")
print(shopping_list)
shopping_list.append("water")
shopping_list.append("paper")
print(shopping_list)
shopping_list.remove("paper")
print(shopping_list)
shopping_list[3] = "strawberry"
print(shopping_list)

# lists are iterable objects
number_list = [1, 2, 3, 4, 5, 6]
square_list = []


# lists are mutable tuples are immutable


for num in number_list:
    square_list.append(num**2)

print(square_list)

# list comprehension
number_list2 = [1, 2, 3, 4, 5]
square_list2 = [num**2 for num in number_list2]

print(square_list2)