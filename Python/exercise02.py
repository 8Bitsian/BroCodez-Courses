# Exercise 02: Shopping Cart Program

# You don't have to typecast str() since it automatically assumes user is inputting a string
item = input("What item would you like to buy? ")
price = float(input("What is the price of each item? "))
quantity = int(input("How many are you buying? "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")