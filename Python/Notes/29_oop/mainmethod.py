# Object-Oriented Programming (OOP)

# Objects are "bundles" of related attributes (variables) and methods (functions).
# A class is used to design the structure and layout of an object (like a blueprint)
# Best practice dictates placing classes within their own files for better modularity and readability
from car import Car

def group(bot):
    if (bot.group == True):
        print(f"{bot.name} is an Autobot\n")
    else: # if (bot != True)
        print(f"{bot.name} is a Decepticon\n")

def main():
    # When creating an object initialize a variable and call the class to access the constructor method.
    # Be sure to pass in the correct parameters as you would a function
    car1 = Car("Camero", 2025, "Yellow w/black stripe", "Bumblebee", True)

    # When calling variable w/object it won't print the individual paramters, it will print where the object is stored in memory
    # print(car1)         # Prints "<car.Car object at 0x000001CEE6BD16A0>"

    #To print the individal attributes of the object use the attribute access operator (`.`) followed by the name of the attribute
    print(car1.model)       # Prints "Camero"
    print(car1.year)        # Prints "2025"
    print(car1.color)       # Prints "Yellow w/black stripe"
    print(f"{car1.name}\n") # Prints "Bumblebee"

    car2 = Car("Ford Fusion", 2026, "Red w/silver and gold decals", "Knock Out", False)
    print(car2.model)   # Prints "Ford Fusion"
    print(car2.year)    # Prints "2026"
    print(car2.color)   # Prints "Red w/silver and gold decals"
    print(f"{car2.name}\n") # Prints "Knock Out"

    # You can access methods the same way you do attributes
    car1.drive()        # Prints "You drive."
    car1.park()         # Prints "You park."
    car1.transform()    # Prints "You transform."
    group(car1)

    car2.drive()        # Prints "You drive."
    car2.park()         # Prints "You park."
    car2.transform()    # Prints "You transform."
    group(car2)

if __name__ == "__main__":
    main()