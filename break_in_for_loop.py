names = ["Selin", "Filiz", "Deniz", "Arda", "Lucas", 24, "Sarah"]

for name in names:
    if type(name) != str:
        print("Found", name)
        break
    else:
        print(name, "is a string")