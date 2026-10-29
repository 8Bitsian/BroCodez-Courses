# Project 09: Concession Stand Program - Create a program to mimick a concession stand menu
# Use 16 Notes
# Create a dictionary array to store values for snacks and associated prices

# Dictionary array syntax is dic_name = {"key":"value"}
# Initialize menu{} with {key} snacks and {value} prices as floats
menu = {"popcorn":  5.00,
        "nachos":   4.00,
        "pizza":    4.45,
        "candy":    2.15,
        "fries":    3.50,
        "chips":    1.15,
        "pretzel":  3.50,
        "fountain": 3.15,
        "water":    3.00}

# Declare a cart 1D list for itemized indices
cart = []

# Initilize a total variable as a floating-point for price total
total = 0.0

# To print the menu to the user for possible choices, use the .items() method
print("--------- MENU ---------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------")

# Ask for user input
while (True):
    # Use the .lower() method for normalization
    food = input("Select an item (Q to Quit): ").lower()
    if food == "q":
        break
    # The .get() method will return None if nothing is found like False for bool
    elif menu.get(food) is not None:
        # Use the .append() method to add food (user input) to cart[] list
        cart.append(food)

print("------ YOUR ORDER -------")
for food in cart:
    total += menu.get(food)
    print(food, end=", ")
print()

print(f"Total is: ${total:.2f}")