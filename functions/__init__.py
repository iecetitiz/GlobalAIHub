def greetings(name, surname, auto_correction):
    if auto_correction == True:
        capitalized_name = name.capitalize()
        capitalized_surname = surname.capitalize()
        print("hello", capitalized_name, capitalized_surname)
    else:
        print("hello", name, surname)


greetings("ece", "titiz", True)


