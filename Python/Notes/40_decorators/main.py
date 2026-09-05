# Decorators
# A decorator is a function that extends the behavior of another function w/o modifying the base function. Pass the base function as an argument to the decorator.
# Ex. @add_sprinkles get_icecream("vanilla")

import decorator

def main():
    ice_cream = decorator.Topping(flavor="vanilla", cone_or_cup=True, is_topping=True)
    
    print(icecream)           # Prints "<decorator.Topping object at 0x000001D34F43C6E0>"
    
    ice_cream.describe()      # Prints "Here is your vanilla icecream in a cone.
                              #         You have added a topping."

    ice_cream.get_ice_cream() # Prints "You add sprinkles 🧁
                              #         You add fudge 🍫
                              #         You add caramel 🍮
                              #         Here is your vanilla icecream!🍦"

if __name__ == "__main__":
    main()