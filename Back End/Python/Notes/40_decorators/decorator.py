# Decorators
# A decorator is a function that extends the behavior of another function w/o modifying the base function. Pass the base function as an argument to the decorator.
# Ex. @add_sprinkles get_icecream("vanilla")

class Ice_Cream:
    # Constructor/Initialization Method
    def __init__(self, flavor, cone_or_cup):
        self.flavor = flavor
        self.cone_or_cup = cone_or_cup

    # Instance Method
    def describe(self):
        print (f"Here is your {self.flavor} ice cream in a {"cone" if (self.cone_or_cup) else "cup"}.")

class Topping(Ice_Cream):
    # Constructor/Initialization Method
    def __init__(self, flavor, cone_or_cup, is_topping):
        super().__init__(flavor, cone_or_cup)
        self.is_topping = is_topping

    def describe(self):
        super().describe()
        print(f"You have {"added a topping" if (self.is_topping) else "chosen plain"}.\n")

    # We have been returning values, but now we return functions w/decorators
    # The following is the basic formatting for creating a decorator
    def add_sprinkles(func):
        # You have to include the inner wrapper function to call the base function
        # Inner wrapper functions use the keywords `*args` and `*kwargs` to accept any number of any type of arguments
        def wrapper(*args, **kwargs):
            print("You add sprinkles 🧁")
            # You have to do the same for the function that you call
            func(*args, **kwargs)
        return wrapper

    def add_fudge(func):
        def wrapper(*args, **kwargs):
            print("You add fudge 🍫")
            func(*args, **kwargs)
        return wrapper

    def add_caramel(func):
        def wrapper(*args, **kwargs):
            print("You add caramel 🍮")
            func(*args, **kwargs)
        return wrapper

    # To apply a decorator to a base function, use the decorator symbol `@` then the decorator name
    # You can apply more than one decorators to a base function.
    @add_sprinkles
    @add_fudge
    @add_caramel
    # You can pass in arguments to a base function, but be sure to have the wrapper functions be able to accept those arguments
    def get_ice_cream(self):
        print(f"Here is your {self.flavor} ice cream!🍦")