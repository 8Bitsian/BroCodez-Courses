# Conditional Expression - A one-line shortcut for the if statement (ternary operator) that prints or assigns one of two values based on a condition, i.e., return X IF condition ELSE return Y

num = 5

# print(X if condition else Y)
print("Positive" if num > 0 else "Negative") # Prints "Positive"

# Can use a variable and print that instead for reability
result = "Even" if num % 2 == 0 else "Odd"
print(result) # Prints "Odd"

a = 6
b = 7

max_num = a if a > b else b
print(max_num) # Prints "7"

min_num = a if a < b else b
print(min_num) # Prints "6"

status = 23

status = "Adult" if age >= 18 else "Child"
print(status) # Prints "Adult"

temp = 30

weather = "Hot" if temp > 20 else "Cold"
print(weather) # Prints "Hot"

user_role = "admin"

access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level) # Prints "Full Access"
