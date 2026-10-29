# Main Method
# Functions and classes in this module can be reused without the main block of code executing.

# The asterisk (*) means all
from script1 import *

def favorite_food(food):
    print("Is in favorite_food() method.")
    print(f"Your favorite food is {food}.\n")
    print("Exiting favorite_food() method...")

# Your program implicitly starts here
def main():
    print("Is in main() method.")
    food = input("What is your favorite food? ")

    # You can call other methods to the main() method
    favorite_food(food)

    # Exit main()
    print("Exiting main() method...")

# The program starts by checking if filename is main
if __name__ == "__main__":
    # `__` is refered to as "dunder"
    print(f"Called mainmethod.py file is: {__name__}\n")
    main()
    # Exit file
    print("Exiting mainmethod.py file...")