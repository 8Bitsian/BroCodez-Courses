# Main Method - Functions and classes in this module can be reused without the main block of code executing.

# This script can be imported or run standalone

# Prints out a list of all available attributes for file
# print(dir())

print(f"Called script1.py file is: {__name__}\n") # Prints "Called script1.py file is: __main__"

print("Is in favorite_drink() method.")
drink = input("What is your favorite drink? ")
print(f"Your favorite drink is {drink}.\n")

print("Exiting script1.py file...\n")