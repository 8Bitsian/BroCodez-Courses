# Project 07: Shopping Cart Program - Create shopping cart for end users to check out multiple items
# Use 13-14 Notes
# Create a collection with a nested loop

# Use lists[] instead of tuples() since the elements will change according to the user's needs
# Could use a set{}, but we are dependent on the position of the element to print with matching price
foods = []
prices = []
# Initializing with a floating-point number
total = 0.0

while (True):
    food = input("Enter food to buy (q to quit): ")

    # To allow for case-sensitivity, include .lower()
    if food.lower() == "q":
        # We need an exit condition to prevent an infinite loop
        break
    else:
        # Type cast the user input as a floating-point number
        # Use an f-string to specify which food to price
        price = float(input(f"Enter the price of {food}: $"))
        # Add the new values for both the food and price elements to lists[] using .append()
        foods.append(food)
        prices.append(price)

# Outside of the nested loop decision structure, print the output
print("\n--- Shopping Bill ---")

# Use a nested for loop to iterate printing the output
x = 0
for food in foods:
    x += 1
    print(f"Item {x}: {food:>15}")
print("----------")

for price in prices:
    total += price

print(f" Total: ${total:>14.2f}")