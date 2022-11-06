# lists are mutable tuples are immutable
# tuples use round brackets instead square brackets

car_list = ("hyundai", "mercedes", "bmw", "toyota")
item1, item2, item3, item4 = car_list
print(item1)

print(car_list[0])    #indexlerle erisebilirim
print(car_list[1:3])    #i can make slice

# car_list[1] = "apple" immutable oldugu icin degistiremem


#just like lists, i can add different type of values
coffee_brands = ("tchibo", "jacops", "starbucks", 12, True)
print(coffee_brands)

inventory = dict()
inventory['bananas'] = 25
inventory['apple'] = 45

for key in inventory:
    inventory[key] += 100

print(inventory)
